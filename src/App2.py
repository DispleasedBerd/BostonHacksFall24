import pandas as pd
import sqlite3
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time 
import json
from flask import Flask

app = Flask()

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

    return variables

@app.route('/getCoordinates')
def get_json_coordinates():
    return {"The Immigrant Learning Center": [42.4271186, -71.0671071], "Immigrant Family Services Institute ": [42.286217, -71.0906896], "Rian Immigrant Center": [42.3527552, -71.0584604224359], "International Institute of New England": [null, null], "Action for Boston Community Development": [42.3520191, -71.0629688], "East Boston Community Council": [42.376546950000005, -71.03944463124805], "Catholic Charities Boston": [42.338818849999996, -71.05135479834671], "Jewish Vocational Service": [null, null], "MassHire Downtown Boston Career Center": [null, null], "East Boston Community Soup Kitchen": [42.37005765, -71.04019203482005], "Roslindale Food Collective": [null, null], "Fair Foods: First Parish Church": [42.30819395, -71.06204429421979], "Project Citizenship": [null, null], "Refugee & Immigrant Assistance Center (RIAC)": [42.3304191, -71.0934607062716], "Mass Office for Refugees and Immigrants (ORI)": [null, null], "Kids in Need of Defense (KIND)": [null, null], "Boston Healthcare for the Homeless": [42.333645250000004, -71.07279114401811], "Centro Presente": [null, null], "Boston Center for Refugee Health & Human Rights (program of Immigrant and Refugee Health Center at Boston Medical Center)": [null, null], "U.S. Committee for Refugees and Immigrants": [46.3144754, 11.0480288], "Massachusetts Alliance of Portuguese Speakers (MAPS)": [null, null], "Greater Boston Food Bank": [42.334405149999995, -71.06583269114233], "Brazillian Worker Center (BWC)": [42.3552369, -71.1324104], "NeighborHealth (formerly East Boston Community Health Center)": [null, null], "MIRA (Massachusetts Immigrant and Refugee Advocacy Coalition)": [null, null], "Center to Support Immigrant Organizing": [null, null], "Greater Boston Legal Services": [42.3638865390222, -71.06021109003544], "YMCA Mobile Markets": [null, null], "Waldo Immigration and Refugee Services Inc": [42.3304191, -71.0934607062716], "African Community Economic Development of New England (ACEDONE)": [null, null], "Political Asylum Immigration Representation Project (PAIR) ": [null, null]}

def get_coordinates(address):
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

def wrapper_coordinates(file_path):
    data = load_excel_data(file_path)
    coordinates = {}

    for key, value in data.items():
        address = value[5]  # Assuming the address is at index 5
        if address:
            latitude, longitude = get_coordinates(address)
            coordinates[key] = (latitude, longitude)
    return coordinates
    



def save_data_to_csv(data, output_file_path):
    """
    Save the data dictionary to a CSV file.
    
    Parameters:
    - data (dict): The data dictionary.
    - output_file_path (str): The path for the output CSV file.
    """
    # Convert the dictionary into a DataFrame
    df = pd.DataFrame.from_dict(data, orient='index')
    
    # Set column names if needed (adjust based on data structure)
    df.columns = [f'Column_{i+1}' for i in range(df.shape[1])]

    # Save DataFrame to CSV
    df.to_csv(output_file_path, index_label="Variable")

if __name__ == "__main__":

    excel_file_path = r"C:\Boston Hacks Fall 24\BostonHacksFall24\src\Urban Refuge Aid Services.xlsx"
    output_csv_path = r"Updated_Urban_Refuge_Aid_Services.csv"

    key = 'The Immigrant Learning Center'
    coords = wrapper_coordinates(excel_file_path)
    
    with open("src/coordinates.json", "w") as outfile: 
        json.dump(coords, outfile)


    
    # Step 3: Save the updated data to a CSV file
    #save_data_to_csv(data, output_csv_path)

    #print(f"Data with coordinates has been saved to {output_csv_path}")

    