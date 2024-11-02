/* installs
1. npm install react react-dom leaflet
2. npm install react-leaflet
3. npm install -D @types/leaflet
*/
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css"
import React from 'react';
import logo from './logo.svg'; // Adjust path as necessary
import logo2 from './logo2.png'; // Your second logo if needed
import './App.css';

function Header() {
  return (
    <div className="Header">
       <img src={logo2} alt="Urban Refuge Logo" className="Logo" /> {/* Add the logo */}
      <h1>Urban Refuge</h1> {/* Name of Website */}
      <nav>
        <ul>
          <li><a href="#home">Home</a></li>
          <li><a href="#about">About</a></li>
          <li><a href="#contact">Contact</a></li>
          <li><a href="#login">User Login</a></li>
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
       {/*} <img src={logo2} className="App-logo" alt="logo" /> */}
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
      <MapContainer center={[42.3601, -71.0589]} zoom={13} scrollWheelZoom={false}>
        <TileLayer
            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        <Marker position={[42.26861281372227, -71.09347770697872]}>
            <Popup>
                A pretty CSS3 popup. <br /> Easily customizable.
            </Popup>
        </Marker>
    </MapContainer>
    </div>
  );
}



// function App() {
//     return (
//     <MapContainer center={[42.3601, -71.0589]} zoom={13} scrollWheelZoom={false}>
//         <TileLayer
//             attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
//             url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
//         />
//         <Marker position={[42.26861281372227, -71.09347770697872]}>
//             <Popup>
//                 A pretty CSS3 popup. <br /> Easily customizable.
//             </Popup>
//         </Marker>
//     </MapContainer>

//     );
// }

export default App;
