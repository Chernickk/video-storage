import React from 'react';

const NotFound404 = ({location}) => {
    return (
        <div>
            <h2>Page with address { location.pathname } not found</h2>
        </div>
    );
};

export default NotFound404;