import React from 'react';
import classes from './Nav.module.css';
import {NavLink} from "react-router-dom";

const Nav = () => {
    return (
        <div className={'Nav'}>
            <div className={classes.links}>
                <div className={classes.link}>
                    <NavLink
                        to="/"
                        className={(navData) => "nav-link" + (!navData.isActive ? ` ${classes.unselected}` : ` ${classes.active}`)}>
                        <p>
                            Запросы с камер
                        </p>
                    </NavLink>
                    <NavLink
                        to="/cars"
                        className={(navData) => "nav-link" + (!navData.isActive ? ` ${classes.unselected}` : ` ${classes.active}`)}>
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