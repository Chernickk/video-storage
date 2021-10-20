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
