import React from 'react';
import classes from "./CarStatus.module.css";

const CarStatus = ({cars, getCarsData}) => {
    return (
        <div>
            <h4>Машины:</h4>
            <button onClick={getCarsData} className={`submit-button ${classes.button}`}>Обновить </button>
            <table className={classes.table}>
                <th className={classes.tableHeader}>Номер</th>
                <th className={classes.tableHeader}>IP адрес</th>
                <th className={classes.tableHeader}>Последнее появление в сети</th>
                <th className={classes.tableHeader}>Статус</th>
                {
                    cars.map((car) =>
                        <tr>

                            <td>{car.license_table}</td>
                            <td>{car.ip_address}</td>
                            <td>{new Date(car.last_seen).toLocaleString('ru-RU')}</td>
                            <td>{car.online ? "в сети" : "не в сети"}</td>
                        </tr>)
                }
            </table>
        </div>
    );
};

export default CarStatus;