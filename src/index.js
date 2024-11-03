import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
//import {GoogleGenerativeAI} from "@google/generative-ai"

//const genAI = new Google GenerativeAI(process.env.API_KEY)
//const model = genAI.getGenerativeModel({model: "gemini-1.5-flash",
//systemInstruction: 

//})

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
