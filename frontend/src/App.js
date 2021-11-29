import {Route, Routes, BrowserRouter} from "react-router-dom";
import './App.css';
import react from "react";
import NotFound404 from './components/NotFound404.jsx';
import Header from "./components/header/Header";
import Nav from "./components/nav/Nav";
import Footer from "./components/footer/footer";
import Requests from "./components/requests/Requests";
import axios from "axios";


axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

class App extends react.Component {
    constructor(props) {
        super(props)
        this.state = {
            'cars': [],
            'requests': [],
            'cars_status': false,
            'request_status': false,
        }
    }

    componentDidMount() {
        axios.get(`/api/cars`)
            .then(response => {
                const cars = response.data
                console.log(cars)
                this.setState(
                    {
                        'cars': cars,
                        'cars_status': true
                    }
                )
            }).catch(error => console.log(error))

        axios.get(`/api/requests`)
            .then(response => {
                let requests = response.data
                requests.sort((request) => request.id)
                requests.reverse()
                this.setState(
                    {
                        'requests': requests,
                        'request_status': true
                    }
                )
            }).catch(error => console.log(error))
    }


    render() {
        return (
            <div className={'container'}>
                <BrowserRouter>
                    <Header/>
                    <Nav/>
                    <Routes>
                        <Route exact path='/' element={this.state.request_status &&
                        this.state.cars_status &&
                        <Requests
                            cars={this.state.cars}
                            requests={this.state.requests}
                        />}/>
                        <Route element={NotFound404}/>
                    </Routes>
                    <Footer/>
                </BrowserRouter>
            </div>
        )
    }
}

export default App;
