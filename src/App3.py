import pandas as pd
import sqlite3
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time 
import json
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def load_excel_data(file_path):
    """
    Load data from an Excel file and return it as a dictionary of variables.
    
    Parameters:
    - file_path (str): The path to the Excel file.
    
    Returns:
    - dict: A dictionary with variable names as keys and their respective values.
    """
    # Read the Excel file
    df = pd.read_excel(file_path)

    # Create a dictionary to hold the variables
    variables = {}

    # Iterate over rows in the DataFrame and assign values to respective variable names
    for index, row in df.iterrows():
        key = row.iloc[0]  # Get the first column value as the variable name
        value = row.iloc[1:]  # Get the rest of the row as the variable value
        variables[key] = value.tolist()  # Store as a list in the dictionary
    #print(variables)
    return variables

#@app.route('/getCoordinates')
def get_json_coordinates():
    return [{"label": "The Immigrant Learning Center", "coordinates": [42.4271186, -71.0671071]}, {"label": "Immigrant Family Services Institute ", "coordinates": [42.286217, -71.0906896]}]
                           #"Rian Immigrant Center": [42.3527552, -71.0584604224359], "International Institute of New England": [None, None], "Action for Boston Community Development": [42.3520191, -71.0629688], "East Boston Community Council": [42.376546950000005, -71.03944463124805], "Catholic Charities Boston": [42.338818849999996, -71.05135479834671], "Jewish Vocational Service": [None, None], "MassHire Downtown Boston Career Center": [None, None], "East Boston Community Soup Kitchen": [42.37005765, -71.04019203482005], "Roslindale Food Collective": [None, None], "Fair Foods: First Parish Church": [42.30819395, -71.06204429421979], "Project Citizenship": [None, None], "Refugee & Immigrant Assistance Center (RIAC)": [42.3304191, -71.0934607062716], "Mass Office for Refugees and Immigrants (ORI)": [None, None], "Kids in Need of Defense (KIND)": [None, None], "Boston Healthcare for the Homeless": [42.333645250000004, -71.07279114401811], "Centro Presente": [None, None], "Boston Center for Refugee Health & Human Rights (program of Immigrant and Refugee Health Center at Boston Medical Center)": [None, None], "U.S. Committee for Refugees and Immigrants": [46.3144754, 11.0480288], "Massachusetts Alliance of Portuguese Speakers (MAPS)": [None, None], "Greater Boston Food Bank": [42.334405149999995, -71.06583269114233], "Brazillian Worker Center (BWC)": [42.3552369, -71.1324104], "NeighborHealth (formerly East Boston Community Health Center)": [None, None], "MIRA (Massachusetts Immigrant and Refugee Advocacy Coalition)": [None, None], "Center to Support Immigrant Organizing": [None, None], "Greater Boston Legal Services": [42.3638865390222, -71.06021109003544], "YMCA Mobile Markets": [None, None], "Waldo Immigration and Refugee Services Inc": [42.3304191, -71.0934607062716], "African Community Economic Development of New England (ACEDONE)": [None, None], "Political Asylum Immigration Representation Project (PAIR) ": [None, None]}]}

@app.route('/getCoordinates')
def get_coordinates():
    file_path = r".\src\Urban Refuge Aid Services.xlsx"
    #print("here")
    coordinates = wrapper_coordinates(file_path)
    #print(coordinates)
    return coordinates

def wrapper_coordinates(file_path):
    data = load_excel_data(file_path)
    services = []

    for key, value in data.items():
        #print(key)
        address = value[5]  # Assuming the address is at index 5
        if address:
            coordinates = find_coordinates(address)
            if coordinates[0] != None:
                services.append({"label": key, "coordinates": coordinates})
            else:
                print(key)
    return services

def find_coordinates(address):
    """
    Get the latitude and longitude for a given address.
    
    Parameters:
    - address (str): The address to geocode.
    
    Returns:
    - tuple: A tuple (latitude, longitude) if successful, else (None, None).
    """
    geolocator = Nominatim(user_agent="abcd")
    try:
        location = geolocator.geocode(address, timeout=10)
        if location:
            return (location.latitude, location.longitude)
    except GeocoderTimedOut:
        time.sleep(1)
        return get_coordinates(address)  # Retry in case of timeout
    return (None, None)



if __name__ == "__main__":
    app.run(debug=True)