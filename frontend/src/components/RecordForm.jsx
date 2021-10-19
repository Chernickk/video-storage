import React, {Component, useState} from 'react';
import DateTimePicker from 'react-datetime-picker/dist/entry.nostyle';
import 'react-calendar/dist/Calendar.css';
import 'react-clock/dist/Clock.css';
import 'react-datetime-picker/dist/DateTimePicker.css';
import "react-loader-spinner/dist/loader/css/react-spinner-loader.css";
import Loader from "react-loader-spinner";
import Select from "react-select";
import axios from "axios";

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

const url = '192.168.203.48:8000'

class RecordForm extends Component {
    constructor(props) {
        super(props)
        this.state = {
            from_datetime: '',
            to_datetime: '',
            show_loader: false,
            show_message: false,
            message_text: '',
            select_value: '',
            cars: [],
        }
    }

    componentDidMount() {
        axios.get(`http://${url}/api/get_cars`)
        .then(response => {
            const cars = response.data
            this.setState(
              {
                'cars': cars
              }
          )
        }).catch(error => console.log(error))
  }

    handleChange(event, name) {
        this.setState(
            {
                [`${name}`]: event
            }
        );
    }



    handleError(error) {
        console.log(error)
        this.setState(
            {
                'message_text': 'Some error occured, please try again later',
                'show_loader': false
            }
        );
    }


    handleResponse(response) {
        if (response.data['status'] === 'OK') {
            this.setState(
                {
                    'message_text': response.data['filename'].map((file) => {
                        return <p><a href={`/media/${file}`}>{file}</a></p>
                    }),
                    'show_loader': false
                }
            );
        } else {
            this.setState(
                {
                    'message_text': response.data['status'],
                    'show_loader': false
                }
            );
        }
    }

    handleSubmit(event) {
        this.setState(
            {
                'show_loader': true,
                'show_message': true,
                'message_text': 'Please, wait for your link'
            }
        );
        axios.get(`http://${url}/api/get_record_link`,
            {params:
                    {'from_time': this.state.from_datetime.toLocaleString('ru-Ru'),
                        'to_time': this.state.to_datetime.toLocaleString('ru-Ru'),
                        'car_id': this.state.select_value.value}})
        .then(response => {
            this.handleResponse(response)
        }).catch(error => this.handleError(error))

        event.preventDefault();
    }

    render() {
        return (
            <div>

                <form onSubmit={(event) => this.handleSubmit(event)}>



                <div className={'date_form'}>
                    <h1>Get video</h1>
                    <Select options={this.state.cars.map(car => {
                                return {
                                    value: `${car.id}`,
                                    label: `${car.name}`
                                }
                            }
                        )}
                            value={this.state.select_value}
                            onChange={(event) => this.handleChange(event, 'select_value')}
                    />

                    <DateTimePicker
                    onChange={(event) => this.handleChange(event, 'from_datetime')}
                    format="y-MM-dd HH:mm:ss"
                    value={ this.state.from_datetime }
                    disableClock={ true }
                    maxDate={ new Date() }
                    required={ true }
                />

                <DateTimePicker
                    onChange={(event) => this.handleChange(event, 'to_datetime')}
                    format="y-MM-dd HH:mm:ss"
                    value={ this.state.to_datetime }
                    disableClock={ true }
                    minDate={ this.state.from_datetime }
                    maxDate={ new Date() }
                    required={ true }
                />

                <input type="submit" value="Submit"/>
                    {this.state.show_message && <h3>{ this.state.message_text }</h3>}
                    {this.state.show_loader && <div className={'loader-spinner'}>

                        <Loader
                            type="TailSpin"
                            color="#000000"
                            height={100}
                            width={100}
                            timeout={0} //3 secs
                        />

                    </div>
                    }
                </div>
                </form>
            </div>
        );
    }
}

export default RecordForm;