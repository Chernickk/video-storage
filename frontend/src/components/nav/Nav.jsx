import React from 'react';
import classes from './Nav.module.css';
import {NavLink} from "react-router-dom";

const Nav = () => {
    return (
        <div className={'Nav'}>
            <div className={classes.links}>
                <div className={classes.link}>
                    <NavLink to="/" className={isActive => "nav-link" + (!isActive ? " unselected" : "")}>
                        Получение записей выгрузки по времени
                    </NavLink>
                </div>
                <div className={classes.link}>
                    <NavLink to="/action" className={isActive => "nav-link" + (!isActive ? " unselected" : "")}>
                        Получение записей по ID
                    </NavLink>
                </div>
                <div className={classes.link}>
                    <NavLink to="/request" className={isActive => "nav-link" + (!isActive ? " unselected" : "")}>
                        Запросы с остальных камер
                    </NavLink>
                </div>
            </div>
        </div>
    );
};

export default Nav;