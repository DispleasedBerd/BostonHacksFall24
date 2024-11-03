/* installs
1. npm install react react-dom leaflet
2. npm install react-leaflet
3. npm install -D @types/leaflet
*/
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css"
import logo from './logo.svg'; // Adjust path as necessary
import logo2 from './logo2.png'; // Your second logo if needed
import './App.css';
import React, { useState } from "react";
import Login from "./login";
import { Icon, divIcon, point } from "leaflet";



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
  
  //locations
  const locations = new Array({lat: 42.26861281372227, long: -71.09347770697872}, {lat: 42.26861281372227, long: -71.19347770697872}); //read the excel for the data
  const markers = new Array();
  for (let i =0; i < locations.length; i++){
    markers.push({
        geocode:[locations[i].lat,locations[i].long], 
        popUp: i
    });
  } 
  // markers
//   const markers = [
//     {
//       geocode: [42.26861281372227, -71.09347770697872],
//       popUp: "Hello, I am pop up 1"
//     },
//     {
//       geocode: [42.26861281372227, -71.19347770697872],
//       popUp: "Hello, I am pop up 2"
//     },
//     {
//       geocode: [42.26861281372227, -71.29347770697872],
//       popUp: "Hello, I am pop up 3"
//     }
//   ];

function App() {
    return (
        <div className="App">
            <Header />
           
            <MapContainer center={[42.3601, -71.0589]} zoom={13} scrollWheelZoom={false}>
                <TileLayer
                    attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                />
                {/* <Marker position={[42.26861281372227, -71.09347770697872]} icon={new Icon({iconUrl: markerIconPng, iconSize: [25, 41], iconAnchor: [12, 41]})}>
                    <Popup>
                        A pretty CSS3 popup. <br /> Easily customizable.
                    </Popup>-
                </Marker> */}
                {/* Mapping through the markers */}
                {markers.map((marker) => (
                <Marker position={marker.geocode} icon={customIcon}>
                    <Popup>{marker.popUp}</Popup>
                </Marker>
                ))}
            </MapContainer>
            <h1 id="#login"><Login /></h1>
        </div>
    );
}
function OnLoginClick() {
    return (
        <p>
            youve logged in :)
        </p>
    );
}

// function HandleLogin(username, password){
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

