import React from 'react';
import axios from "axios";

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';


const RecordInfo = ({coordinates, filenames}) => {
    return (<div>
            <h4>files:</h4>
            <table className={'files-table'}>
                <th className={'table-header'}>files</th>
                {
                    filenames.map((file) => {
                        return <tr><td><a href={`/media/${file}`}>{file}</a></td></tr>
                    })
                }
            </table>
            <h4>gps coordinates:</h4>
            <table className={'files-table'}>
                <th colSpan="2" className={'table-header'}>coordinates</th>
                <th className={'table-header'}>date time</th>
                {
                coordinates.map((coordinate) =>
                    <tr>
                            <td>
                                <a href={`https://yandex.ru/maps/?text=${coordinate.latitude}%2C${coordinate.longitude}`} target="blank">{coordinate.latitude}</a>
                            </td>
                            <td>
                                <a href={`https://yandex.ru/maps/?text=${coordinate.latitude}%2C${coordinate.longitude}`} target="blank">{coordinate.longitude}</a>
                            </td>
                        <td>{new Date(coordinate.datetime).toLocaleString('ru-Ru', {timeZone: 'UTC'})}</td>
                    </tr>)
                }
            </table>
        </div>
    )
}

export default RecordInfo;