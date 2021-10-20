import React, {Component, useState} from 'react';
import axios from "axios";

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';


class RecordInfo extends Component {
    constructor(props) {
        super(props)
        this.state = {
            from_datetime: '',
            to_datetime: '',
            coordinates: {},
            url: this.props.url,
        }
    }

    componentDidMount() {
        axios.get(`http://${this.state.url}/api/get_coordinates`,{
                    params:
                        {
                            'from_time': this.props.from_time.toLocaleString('ru-Ru'),
                            'to_time': this.props.to_time.toLocaleString('ru-Ru'),
                            'car_id': this.props.car_id
                        }
                })
        .then(response => {
            this.setState({
                'coordinates': response.data
            })
        }).catch(error => console.log(error))
    }

    render() {
        return (
            <div>

            </div>
        );
    }
}

const RecordInfo = ({from_time, to_time, car_id, url}) => {


    return (
            coordinates.map((coordinate) => {
                <td>coordinate.latitude</td><td>coordinate.longitude</td><td>coordinate.datetime</td>
                    })
    );
};

export default RecordInfo;