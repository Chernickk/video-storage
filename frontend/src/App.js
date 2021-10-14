import logo from './logo.svg';
import {Route, BrowserRouter, Switch, Redirect} from "react-router-dom";
import './App.css';

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
      <div>
        <BrowserRouter>

          <Menu/>

          <Switch>

            <Route exact path='/' component={() => <UserList users = {this.state.users} />} />

            <Route component={NotFound404}/>

          </Switch>

          <Footer/>

        </BrowserRouter>
      </div>
    )
  }
}

export default App;
