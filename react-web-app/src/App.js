import React, { Component }  from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';

class App extends Component {

  constructor() {
    super()
    this.state = {
      words: '',
      animate: false
    }
  }

  getIt = () => {
    this.setState({ animate: true })
    axios.get(`/api/hello`)
      .then(res => {
        const words = res.data;
        this.setState({ words });
      })
  }

  render() {
    let { words, animate } = this.state

    return (
      <div className="App">
        <header className="App-header">
          <button onClick={() => this.getIt()} className="Logo-button">
            <img onClick={() => this.getIt()} src={logo} className={animate ? "App-logo-spin" : "App-logo"} alt="logo" />
          </button>
          {words &&
            <p>
              Here are some words: {words}
            </p>
          }
        </header>
      </div>
    );
  }
}

export default App;
