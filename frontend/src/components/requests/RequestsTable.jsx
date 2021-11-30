import React from 'react';
import classes from './Requests.module.css'

function record_status(status, records, car_license_table) {
    if (status === null) {
        return 'Неизвестен'
    } else if (status) {
        return <table>{records.map((record) => <tr><td><a href={`/request/${car_license_table}/${record.file_name}`}>{record.file_name}</a></td></tr>)}</table>
    } else if (status === false) {
        return 'Отсутствует'
    }
}

function get_car_name(car_id, cars) {
    let result = cars.filter(car => car.id === car_id)
    return result[0].license_table
}

const RequestsTable = ({requests, cars, deleteRequest}) => {
    return (
        <div>
            <h4>Запросы:</h4>
            <table className={classes.table}>
                <th className={classes.tableHeader}>Машина</th>
                <th className={classes.tableHeader}>Время начала</th>
                <th className={classes.tableHeader}>Время конца</th>
                <th className={classes.tableHeader}>Доставлен</th>
                <th className={classes.tableHeader}>Статус</th>
                <th className={classes.tableHeader}>Удалить</th>
                {
                    requests.map((request) =>
                        <tr>

                            <td>{get_car_name(request.car, cars)}</td>
                            <td>{new Date(request.start_time).toLocaleString('ru-RU')}</td>
                            <td>{new Date(request.finish_time).toLocaleString('ru-RU')}</td>
                            <td>{request.delivered ? "Да": "Нет"}</td>
                            <td>{record_status(request.record_status, request.records, get_car_name(request.car, cars))}</td>
                            <td><button onClick={() => deleteRequest(request.id)}>Удалить</button></td>
                        </tr>)
                }
            </table>
        </div>
    );
};

export default RequestsTable;