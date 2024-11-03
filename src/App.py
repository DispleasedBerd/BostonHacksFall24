import pandas as pd
import sqlite3
import requests
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


if __name__ == "__main__":
    # Step 1: Load the Excel file
    excel_file_path = r"C:\Users\tiaro\AppData\Roaming\Microsoft\Windows\Network Shortcuts\urban refuge data_copy.xlsx"

    # Load data from the Excel file
    data = load_excel_data(excel_file_path)
print(data)


