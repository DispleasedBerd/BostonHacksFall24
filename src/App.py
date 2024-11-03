import pandas as pd
import sqlite3
import requests
import time
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

geolocator = Nominatim(user_agent="abcd")

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


def extract_addresses(data, address_index):
    """
    Extract addresses from the data dictionary based on the specified index.

    Parameters:
    - data (dict): The data dictionary with addresses.
    - address_index (int): The index in the list that corresponds to the address.

    Returns:
    - list: A list of addresses.
    """
    addresses = []
    for values in data.values():
        if len(values) > address_index:  # Ensure the index exists in the values
            addresses.append(values[address_index])  # Append the address
    return addresses


def get_coordinates(address, retries=3, delay=2):
    """
    Get the latitude and longitude of an address using geopy (Nominatim).

    Parameters:
    - address (str): The address to geocode.

    Returns:
    - tuple: A tuple of (latitude, longitude), or (None, None) if the address could not be found.
    """
    for attempt in range(retries):
        try:
            location = geolocator.geocode(address, timeout=10)
            if location:
                return (location.latitude, location.longitude)
            else:
                print(f"Coordinates not found for address: {address}")
                return (None, None)
        except GeocoderTimedOut:
            print(f"Geocoding timed out for address: {address} - retrying in {delay} seconds")
            time.sleep(delay)
            delay *= 2  # Exponential backoff: double the delay
        except Exception as e:
            print(f"An error occurred: {e}")
            return (None, None)

    print(f"Failed to get coordinates for address: {address} after {retries} attempts")
    return (None, None)


def add_coordinates_to_addresses(addresses):
    """
    Add coordinates (latitude and longitude) to each address in the address list.

    Parameters:
    - addresses (list): A list of addresses.

    Returns:
    - list: A list of tuples containing (address, latitude, longitude).
    """
    coordinates_list = []
    for address in addresses:
        #print(f"Getting coordinates for: {address}")
        lat, lon = get_coordinates(address)
        coordinates_list.append((address, lat, lon))
        #print(f"Latitude: {lat}, Longitude: {lon}")
    return coordinates_list


if __name__ == "__main__":
    # Step 1: Load the Excel file
    excel_file_path = r"C:\Users\tiaro\AppData\Roaming\Microsoft\Windows\Network Shortcuts\urban refuge data_copy.xlsx"

    # Load data from the Excel file
    data = load_excel_data(excel_file_path)

    # Step 2: Extract addresses (assuming addresses are located at index 5)
    address_index = 5  # Set this to the appropriate index for addresses
    addresses = extract_addresses(data, address_index)

    # Step 3: Add coordinates to addresses
    coordinates = add_coordinates_to_addresses(addresses)


