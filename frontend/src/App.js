import {Route, Routes, BrowserRouter} from "react-router-dom";
import './App.css';
import react from "react";
import RecordForm from "./components/record/RecordForm";
import NotFound404 from './components/NotFound404.jsx';
import Header from "./components/header/Header";
import Nav from "./components/nav/Nav";
import Footer from "./components/footer/footer";
import ActionForm from "./components/action/ActionForm";
import RequestForm from "./components/requests/RequestForm";

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
          <Header/>
          <Nav/>
          <Routes>

            <Route exact path='/' element={<RecordForm/>} />
            <Route exact path='/action' element={<ActionForm/>} />
            <Route exact path='/request' element={<RequestForm/>} />
            <Route element={NotFound404}/>

          </Routes>
          <Footer/>
        </BrowserRouter>
      </div>
    )
  }
}

export default App;
