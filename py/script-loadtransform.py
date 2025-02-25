import os
import requests
from bs4 import BeautifulSoup
import re
import json

def download_transform_save_json():
    try:
        # Step 1: Ask for the URL
        url = input("Enter the URL to download HTML from: ").strip()
        
        # Step 2: Fetch the HTML content
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        html_content = response.text
        
        # Step 3: Extract filename from URL
        file_name = re.search(r"scripts/([^/]+)\.html", url)
        if file_name:
            safe_file_name = file_name.group(1)
        else:
            print("URL format is invalid or missing 'scripts/' path.")
            return
        
        # Step 4: Save the HTML to the "Loaded" directory
        loaded_directory = "/Users/gilosbo/Documents/1Documents/*Personal/iOSdev/Grammarless/Scripts/Loaded"
        os.makedirs(loaded_directory, exist_ok=True)  # Ensure the directory exists
        loaded_file_path = os.path.join(loaded_directory, f"{safe_file_name}.html")
        
        with open(loaded_file_path, 'w', encoding='utf-8') as loaded_file:
            loaded_file.write(html_content)
        
        print(f"HTML successfully downloaded and saved to: {loaded_file_path}")
        
        # Step 5: Extract and transform the content within the <pre> tag
        soup = BeautifulSoup(html_content, 'html.parser')
        pre_tag = soup.find('pre')
        if not pre_tag:
            print("No <pre> tag found in the HTML.")
            return
        
        # Transform: Add new lines after <b>, before </b>, and after </b> followed by text
        transformed_content = pre_tag.encode_contents().decode("utf-8")
        transformed_content = re.sub(r"(<b>)\s+", r"\1\n", transformed_content)  # After <b>
        transformed_content = re.sub(r"\s+(</b>)", r"\n\1", transformed_content)  # Before </b>
        transformed_content = re.sub(r"(</b>)\s+", r"\1\n", transformed_content)  # After </b> and text
        transformed_content = "\n".join(line.lstrip() for line in transformed_content.splitlines())  # Remove leading spaces
        
        # Step 6: Save the transformed content to the "Transformed" directory
        transformed_directory = "/Users/gilosbo/Documents/1Documents/*Personal/iOSdev/Grammarless/Scripts/Transformed"
        transformed_directory2 = "/Users/gilosbo/Documents/1Documents/*Personal/iOSdev/Grammarless/Scripts"
        os.makedirs(transformed_directory, exist_ok=True)  # Ensure the directory exists
        transformed_file_path = os.path.join(transformed_directory, f"{safe_file_name}_transformed.html")
        
        with open(transformed_file_path, 'w', encoding='utf-8') as transformed_file:
            transformed_file.write(transformed_content)
        
        print(f"Transformed script saved to: {transformed_file_path}")
        
        # Step 7: Convert transformed content to JSON
        lines = transformed_content.splitlines()
        json_data = []
        in_bold_block = False  # State tracker for bold block

        for i, line in enumerate(lines, start=1):
            # Check if entering or exiting a bold block
            if "<b>" in line:
                in_bold_block = True
                line_type = "h2"
                clean_content = line.replace("<b>", "").strip()
            elif "</b>" in line:
                line_type = "h2"
                clean_content = line.replace("</b>", "").strip()
                in_bold_block = False
            else:
                line_type = "h2" if in_bold_block else "body"
                clean_content = line.strip()
            
            json_data.append({"row": i, "type": line_type, "content": clean_content})
        
        # Save the JSON to the "Transformed" directory
        json_file_path = os.path.join(transformed_directory2, f"{safe_file_name}_transformed.json")
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file, indent=2)
        
        print(f"JSON file saved to: {json_file_path}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
download_transform_save_json()
