
/* installs
1. npm install react react-dom leaflet
2. npm install react-leaflet
3. npm install -D @types/leaflet
*/
import './App.css'
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css"

function App() {
    return (
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

    );
}

export default App;

