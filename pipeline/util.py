import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    data_list = []
    target_list = []
    
    # Open the CSV file and read its contents
    with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        
        # Iterate through each row and append the values to the respective lists
        for row in csv_reader:
            data_list.append(row['Textos_espanol'])
            target_list.append(int(row['sdg']))  # Convert 'sdg' to integer
    
    # Create the dictionary with the desired format
    output_dict = {
        "data": data_list,
        "target": target_list
    }
    
    # Write the dictionary to the JSON file
    with open(json_file_path, mode='w', encoding='utf-8') as jsonfile:
        json.dump(output_dict, jsonfile, ensure_ascii=False, indent=4)

# Example usage:
csv_file_path = 'pipeline/ODScat_345.csv'  # Replace with your CSV file path
json_file_path = 'pipeline/training.json'  # Replace with the output JSON file path

csv_to_json(csv_file_path, json_file_path)

print(f"CSV has been converted to JSON and saved to {json_file_path}")
