import {Route, BrowserRouter, Switch, Redirect} from "react-router-dom";
import './App.css';
import react from "react";
import RecordForm from "./components/RecordForm";
import NotFound404 from './components/NotFound404.jsx';

class App extends react.Component {
  constructor(props) {
    super(props)
    this.state = {
      'users': [],
      'todos': [],
      'projects': []
    }
  }

  componentDidMount() {
    // axios.get('http://127.0.0.1:8000/api/users')
    //     .then(response => {
    //       const users = response.data
    //
    //       this.setState(
    //           {
    //             'users': users.results
    //           }
    //       )
    //     }).catch(error => console.log(error))
  }

  render() {
    return (
      <div className={'container'}>
        <BrowserRouter>



          <Switch>

            <Route exact path='/' component={() => <RecordForm/>} />

            <Route component={NotFound404}/>

          </Switch>



        </BrowserRouter>
      </div>
    )
  }
}

export default App;
