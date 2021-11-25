import React, {Component} from 'react';
import DateTimePicker from 'react-datetime-picker/dist/entry.nostyle';
import 'react-calendar/dist/Calendar.css';
import 'react-clock/dist/Clock.css';
import 'react-datetime-picker/dist/DateTimePicker.css';
import "react-loader-spinner/dist/loader/css/react-spinner-loader.css";
import Loader from "react-loader-spinner";
import Select from "react-select";
import axios from "axios";
import classes from './ActionForm.module.css';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

const url = '127.0.0.1:8000'

class ActionForm extends Component {
    constructor(props) {
        super(props)
        this.state = {
            actions: [],
            show_loader: false,
            show_message: false,
            message_text: '',
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

        event.preventDefault();
    }

    render() {
        return (
            <div className={'Content'}>

                <Select
                    className={classes.Select}
                    options={this.state.actions.map(action => {
                            return {
                                value: `${action.id}`,
                                label: `${action.uid}`
                            }
                        }
                    )}
                    value={this.state.select_value}
                    onChange={(event) => this.handleChange(event, 'select_value')}
                />

                <button
                    value="Submit"
                    className={"submit-button"}
                    onClick={(event) => this.handleSubmit(event)}/>
            </div>
        );
    }
}

export default ActionForm;