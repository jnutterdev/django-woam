import logo from './logo.svg';
import './App.css';
import axios from 'axios';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1 className="text-3xl text-teal-300 font-bold underline">
      Hello world!
    </h1>
      </header>
    </div>
  );
}

export default App;
