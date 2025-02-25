import pandas as pd
import json
import os

def excel_to_json():
    """
    Convert an Excel file on the desktop to a JSON file on the desktop.
    """
    # Get the user's desktop path
    desktop_path = os.path.expanduser("~/Desktop")
    
    # Ask for the Excel file name
    excel_file_name = input("Enter the Excel file name (with extension, e.g., 'example.xlsx') on your desktop: ").strip()
    excel_file_path = os.path.join(desktop_path, excel_file_name)
    
    # Check if the file exists
    if not os.path.isfile(excel_file_path):
        print(f"File not found: {excel_file_path}")
        return
    
    try:
        # Read the Excel file
        data = pd.read_excel(excel_file_path, sheet_name=None)  # Load all sheets
        
        # Convert to JSON format
        json_data = {}
        for sheet_name, df in data.items():
            json_data[sheet_name] = df.to_dict(orient='records')  # Convert each sheet to a list of dictionaries
        
        # Define the output JSON file path
        output_file_name = os.path.splitext(excel_file_name)[0] + '.json'
        output_file_path = os.path.join(desktop_path, output_file_name)
        
        # Save JSON data to the file
        with open(output_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file, indent=4, ensure_ascii=False)
        
        print(f"JSON file successfully created: {output_file_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
if __name__ == "__main__":
    excel_to_json()
