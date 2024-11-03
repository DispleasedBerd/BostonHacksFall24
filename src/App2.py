import pandas as pd
import sqlite3
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time 

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

if __name__ == "__main__":
    # Step 1: Load the Excel file
    excel_file_path = r"C:\Users\tiaro\OneDrive\BostonHacks 2024\BostonHacksFall24\src\Urban Refuge Aid Services.xlsx"

    # Load data from the Excel file
    data = load_excel_data(excel_file_path)

    # Step 2: Add latitude and longitude to each address in the data dictionary
    for key, value in data.items():
        address = value[5]  # Assuming the address is at index 5
        if address:
            latitude, longitude = get_coordinates(address)
            value.extend([latitude, longitude])

    # Print updated data with coordinates
    print(data)
