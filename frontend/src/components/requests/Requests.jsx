import React, {Component} from 'react';
import DateTimePicker from 'react-datetime-picker/dist/entry.nostyle';
import 'react-calendar/dist/Calendar.css';
import 'react-clock/dist/Clock.css';
import 'react-datetime-picker/dist/DateTimePicker.css';
import "react-loader-spinner/dist/loader/css/react-spinner-loader.css";
import Loader from "react-loader-spinner";
import Select from "react-select";
import axios from "axios";
import RequestsTable from "./RequestsTable";


class Requests extends Component {
    constructor(props) {
        super(props)
        this.state = {
            select_value: '',
            from_datetime: '',
            to_datetime: '',
            cars: props.cars,
            requests: props.requests,

        }
    }

    componentDidMount() {

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
    }

    deleteRequest(id) {
        axios.delete(`/api/requests/${id}`)
            .then(response => {
                console.log(response)
            }).catch(error => this.handleError(error))
        const request = this.state.requests.filter(request => request.id === id)[0]
        const index = this.state.requests.indexOf(request)
        let requests = this.state.requests
        requests.splice(index, 1)
        if (index > -1) {
            this.setState({
                requests: requests
            })
        }
    }


    addRequest(request) {
        this.setState(
            {
                'requests': [request, ...this.state.requests]
            })
    }


    handleSubmit(event) {
        const tzoffset = (new Date()).getTimezoneOffset() * 60000; //offset in milliseconds
        const start_time = (new Date(this.state.from_datetime - tzoffset)).toISOString().slice(0, -1);
        const finish_time = (new Date(this.state.to_datetime - tzoffset)).toISOString().slice(0, -1);

        axios.post(`/api/requests`,
            {
                'car': this.state.select_value.value,
                'start_time': start_time,
                'finish_time': finish_time,
            })
            .then(response => {
                this.addRequest(response.data)
            }).catch(error => this.handleError(error))

        this.setState({
            select_value: '',
            from_datetime: '',
            to_datetime: '',
        })
        event.preventDefault()
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
                                        label: `${car.license_table}`
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
                            value={this.state.from_datetime}
                            disableClock={true}
                            maxDate={new Date()}
                            required={true}
                        />

                        <DateTimePicker
                            className={"datetime-picker"}
                            onChange={(event) => this.handleChange(event, 'to_datetime')}
                            format="y-MM-dd HH:mm:ss"
                            value={this.state.to_datetime}
                            disableClock={true}
                            minDate={this.state.from_datetime}
                            maxDate={new Date()}
                            required={true}
                        />

                        <input type="submit" value="Submit" className={"submit-button"}/>
                        {this.state.show_message && <h3>{this.state.message_text}</h3>}
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


                </form>
                <RequestsTable requests={this.state.requests}
                               cars={this.state.cars}
                               deleteRequest={(id) => this.deleteRequest(id)}/>
            </div>
        );
    }
}

export default Requests;