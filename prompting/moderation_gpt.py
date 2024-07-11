import os
import pandas as pd

# Define the path to the output folder
def read_excel_files_from_folder(folder_path):
    """
    Reads all Excel files in the specified folder and creates a variable for each DataFrame with the same name.

    Parameters:
    folder_path (str): The path to the folder containing the Excel files.
    """
    excel_files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]

    # Read each Excel file into a DataFrame and create a variable with the file name (without extension)
    for file in excel_files:
        file_path = os.path.join(folder_path, file)
        df_name = os.path.splitext(file)[0]  # Get the file name without extension
        globals()[df_name] = pd.read_excel(file_path)

output_folder = os.path.join(os.path.dirname(__file__), '../output')

# Read the Excel files from the folder
read_excel_files_from_folder(output_folder)


