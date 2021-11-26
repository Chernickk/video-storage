import React from 'react';
import classes from './Requests.module.css'

function record_status(status) {
    if (status === '') {
        return 'Неизвестен'
    } else if (status) {
        return ''
    } else {
        return ''
    }
}

const RequestsTable = ({requests}) => {
    return (
        <div>
            <h4>Запросы:</h4>
            <table className={classes.table}>
                <th className={classes.tableHeader}>Машина</th>
                <th className={classes.tableHeader}>Время начала</th>
                <th className={classes.tableHeader}>Время конца</th>
                <th className={classes.tableHeader}>Доставлен</th>
                <th className={classes.tableHeader}>Статус</th>
                {
                    requests.map((request) =>
                        <tr>

                            <td>{request.car}</td>
                            <td>{new Date(request.start_time).toLocaleString('ru-RU')}</td>
                            <td>{new Date(request.finish_time).toLocaleString('ru-RU')}</td>
                            <td>{request.delivered ? "Да": "Нет"}</td>
                            <td>{request.record_status ? "Да": "Нет"}</td>
                        </tr>)
                }
            </table>
        </div>
    );
};

export default RequestsTable;