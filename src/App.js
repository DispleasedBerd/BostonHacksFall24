import logo from './logo.svg';
import './App.css';

function Header() {
  return (
    <div className="Header">
      <h1>Urban Refuge</h1> {/* Name of Website */}
      <nav>
        <ul>
          {/* Used for the headings of the header bar */}
          <li><a href="#home">Home</a></li>
          <li><a href="#about">About</a></li>
          <li><a href="#contact">Contact</a></li>
          <li><a href="#contact">User Login</a></li>
        </ul>
      </nav>
    </div>
  );
}


function App() {
  return (
    <div className="App">
      <Header />
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;

