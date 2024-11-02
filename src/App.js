import logo from './logo.svg';
import './App.css';
import React, { useState } from "react";
import Login from "./login";


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
          {/* <li><a href="#login">User Login</a></li> */}
          <li><button onClick={<Login/>}>User Login</button></li>
        </ul>
      </nav>
      {/* <Login onLogin={}/> */}
      {/* <Login/> */}
      {/* <button onClick={<Login/>}>User Login</button> */}
      {/*
      first click on the login button in header to redirect to login (or just do a popup window)
      after that, you just need your onLogin function so that it'll do something once you login
      pass the onlogin function to the <Login /> component when called
      */}
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
// function HandleLogin(){
// const handleLogin = (username, password) => {
//   // Here, you can add validation or connect to a backend for verification
//   if (username === "testuser" && password === "testpassword") {
//     setUserData({ username });
//     setIsLoggedIn(true);
//   } else {
//     alert("Incorrect username or password");
//   }
// };

// const handleLogout = () => {
//   setIsLoggedIn(false);
//   setUserData(null);
//   return (
//     <div className="App">
//       {isLoggedIn ? (
//         <div>
//           <h2>Welcome, {userData.username}</h2>
//           <button onClick={handleLogout}>Logout</button>
//         </div>
//       ) : (
//         <Login onLogin={handleLogin} />
//       )}
//     </div>
//   );
// };

// }


  


export default App;


