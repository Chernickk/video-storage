import React, {Component} from 'react';
import DateTimePicker from 'react-datetime-picker/dist/entry.nostyle';
import 'react-calendar/dist/Calendar.css';
import 'react-clock/dist/Clock.css';
import 'react-datetime-picker/dist/DateTimePicker.css';
import "react-loader-spinner/dist/loader/css/react-spinner-loader.css";
import RecordInfo from "./RecordInfo";
import Loader from "react-loader-spinner";
import Select from "react-select";
import axios from "axios";

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

const url = '127.0.0.1:8000'

class RecordForm extends Component {
    constructor(props) {
        super(props)
        this.state = {
            from_datetime: '',
            to_datetime: '',
            show_loader: false,
            show_message: false,
            show_coordinates: false,
            message_text: '',
            select_value: '',
            cars: [],
            filenames: [],
            coordinates: []
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
                    'filenames': response.data['filename'],
                    'show_loader': false,
                    'show_message': false,
                    'show_coordinates': true,
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
        const time_diff = (this.state.to_datetime - this.state.from_datetime) / 1000;
        if (time_diff <= 300 && time_diff >= 10) {
            axios.get(`http://${url}/api/get_record_link`,
                {
                    params:
                        {
                            'from_time': this.state.from_datetime.toLocaleString('ru-Ru'),
                            'to_time': this.state.to_datetime.toLocaleString('ru-Ru'),
                            'car_id': this.state.select_value.value,

                        }
                })
                .then(response => {
                    this.handleResponse(response)
                }).catch(error => this.handleError(error))

            axios.get(`http://${url}/api/get_gps`,
                {
                    params:
                        {
                            'from_datetime': this.state.from_datetime.toISOString(),
                            'to_datetime': this.state.to_datetime.toISOString(),
                            'car_id': this.state.select_value.value
                        }
                })
                .then(response => {
                    console.log(response)
                    this.setState({
                        'coordinates': response.data
                    })
                }).catch(error => console.log(error))

        } else {
            this.setState(
                {
                    'message_text': 'Clip must be more then 10 seconds and less then 5 minutes',
                    'show_loader': false
                }
            );
        }
        event.preventDefault();
    }

    render() {
        return (
            <div className={'Content'}>

                <form onSubmit={(event) => this.handleSubmit(event)}>

                    <div className={'date_form'}>

                        <Select
                            className={"select"}
                            options={this.state.cars.map(car => {
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
                            className={"datetime-picker"}
                            onChange={(event) => this.handleChange(event, 'from_datetime')}
                            format="y-MM-dd HH:mm:ss"
                            value={ this.state.from_datetime }
                            disableClock={ true }
                            maxDate={ new Date() }
                            required={ true }
                        />

                        <DateTimePicker
                            className={"datetime-picker"}
                            onChange={(event) => this.handleChange(event, 'to_datetime')}
                            format="y-MM-dd HH:mm:ss"
                            value={ this.state.to_datetime }
                            disableClock={ true }
                            minDate={ this.state.from_datetime }
                            maxDate={ new Date() }
                            required={ true }
                        />

                        <input type="submit" value="Submit" className={"submit-button"}/>
                            {this.state.show_message && <h3>{ this.state.message_text }</h3>}
                            {this.state.show_loader && <div className={'loader-spinner'}>
                                    <Loader
                                        type="TailSpin"
                                        color="#000000"
                                        height={100}
                                        width={100}
                                        timeout={0}
                                    />
                                </div>
                            }
                    </div>

                    {this.state.show_coordinates && <RecordInfo coordinates={this.state.coordinates}
                                                                        filenames={this.state.filenames}/>
                            }

                </form>
            </div>
        );
    }
}

export default RecordForm;