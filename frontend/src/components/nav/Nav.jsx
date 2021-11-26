import React from 'react';
import classes from './Nav.module.css';
import {NavLink} from "react-router-dom";

const Nav = () => {
    return (
        <div className={'Nav'}>
            <div className={classes.links}>
                <div className={classes.link}>
                    <NavLink to="/" className={isActive => "nav-link" + (!isActive ? " unselected" : "")}>
                        Запросы с камер
                    </NavLink>
                </div>
            </div>
        </div>
    );
};

export default Nav;