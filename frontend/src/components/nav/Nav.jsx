import React from 'react';
import classes from './Nav.module.css';
import {NavLink} from "react-router-dom";

const Nav = () => {
    return (
        <div className={'Nav'}>
            <div className={classes.links}>
                <div className={classes.link}>
                    <NavLink to="/" className={isActive => "nav-link" + (!isActive ? " unselected" : "")}>
                        <p>
                            Запросы с камер
                        </p>
                    </NavLink>
                    <NavLink to="/cars" className={isActive => "nav-link" + (!isActive ? " unselected" : "")}>
                        <p>
                            Статус машин
                        </p>
                    </NavLink>
                </div>
            </div>
        </div>
    );
};

export default Nav;