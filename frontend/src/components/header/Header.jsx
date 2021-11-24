import React from 'react';
import classes from './Header.module.css'

const Header = () => {
    return (
        <div className={'Header'}>
            <h2 className={classes.HeaderText}>Получение видеозаписей с камер</h2>
        </div>
    );
};

export default Header;