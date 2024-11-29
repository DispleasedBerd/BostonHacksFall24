/* installs
1. npm install react react-dom leaflet
2. npm install react-leaflet
3. npm install -D @types/leaflet
*/
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css"
import Papa from 'papaparse';
import logo from './logo.svg'; // Adjust path as necessary
import logo from './logo.png';
import './App.css';
import React, { useEffect, useState } from "react";
import Login from "./login";
import { Icon, divIcon, point } from "leaflet";
import coordinates from "./coordinates.json"



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

// create custom icon
const customIcon = new Icon({
    // iconUrl: "https://cdn-icons-png.flaticon.com/512/447/447031.png",
    iconUrl: require("./icons/placeholder.png"),
    iconSize: [38, 38] // size of the icon
});

// custom cluster icon
const createClusterCustomIcon = function (cluster) {
    return new divIcon({
        html: `<span class="cluster-icon">${cluster.getChildCount()}</span>`,
        className: "custom-marker-cluster",
        iconSize: point(33, 33, true)
    });
};

function App() {
    const [markers, setMarkers] = useState([]);

    useEffect(() => {
        async function fetchData() {
            try {
                const response = await fetch('http://127.0.0.1:5000/getCoordinates');
                const data = await response.json();
                console.log('Fetched data:', data); // Log the data to see its structure
                setMarkers(data);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
            
    }

    fetchData();
    //console.log('Markers:', markers);
  }, []);

  return (
    <div className="App">
    <Header />
      <MapContainer center={[42.3601, -71.0589]} zoom={13} scrollWheelZoom={false}>
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        {markers.length > 0 && markers.map((marker, index) => (
          <Marker
            key={index}
            position={marker.coordinates}
            icon={customIcon}
          >
            <Popup>{marker.label}</Popup> 
          </Marker>
        ))}
      </MapContainer>
      <h1 id="#login"><Login /></h1>
    </div>
  );
}

export default App;

