import csv
import json
import os

def csv_to_json(csv_file, json_file):
    # Check if the JSON file already exists
    if os.path.isfile(json_file):
        # If it does, ask the user if they want to overwrite it
        overwrite = input(f"The file {json_file} already exists. Do you want to overwrite it? (y/n) ")
        if overwrite.lower() != 'y':
            # If they don't want to overwrite it, create a new filename
            base, ext = os.path.splitext(json_file)
            i = 1
            while os.path.isfile(f"{base}{i:02d}{ext}"):
                i += 1
            json_file = f"{base}{i:02d}{ext}"
            print(f"{json_file} created in the current folder.")

    # Open the CSV file in binary mode
    with open(csv_file, 'rb') as file:
        # Decode the file using the utf-8-sig codec to remove the BOM
        decoded_file = file.read().decode('utf-8-sig')
        # Read the CSV file
        reader = csv.DictReader(decoded_file.splitlines())
        # Skip the first line
        next(reader)
        # Convert the CSV data into a list of dictionaries
        data = [row for row in reader]

    # Open the JSON file
    with open(json_file, 'w') as file:
        # Write the JSON data to the file
        json.dump(data, file, indent=4)

    # Print a message indicating that the conversion was successful
    print(f"Style file '{csv_file}' converted successfully into '{json_file}'.")

def json_to_csv(json_file, csv_file):
    # Check if the CSV file already exists
    if os.path.isfile(csv_file):
        # If it does, ask the user if they want to overwrite it
        overwrite = input(f"The file {csv_file} already exists. Do you want to overwrite it? (y/n) ")
        if overwrite.lower() != 'y':
            # If they don't want to overwrite it, create a new filename
            base, ext = os.path.splitext(csv_file)
            i = 1
            while os.path.isfile(f"{base}{i:02d}{ext}"):
                i += 1
            csv_file = f"{base}{i:02d}{ext}"
            print(f"{csv_file} created in the current folder.")

    # Open the JSON file
    with open(json_file, 'r') as file:
        # Read the JSON data
        data = json.load(file)

    # Open the CSV file
    with open(csv_file, 'w', newline='') as file:
        # Write the CSV data
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    # Print a message indicating that the conversion was successful
    print(f"Style file '{json_file}' converted successfully into '{csv_file}'.")

# Print the name of the script with an ASCII frame
script_name = "sandner.art | Style Convertor: Convert Forge/A1111 .csv styles to ComfyUI .json styles (or the other way around)"
frame_width = len(script_name) + 4
print("+" + "-" * frame_width + "+")
print("|" + " " * ((frame_width - len(script_name)) // 2) + script_name + " " * ((frame_width - len(script_name) + 1) // 2) + "|")
print("+" + "-" * frame_width + "+")

# Ask the user which conversion they want to perform
conversion = input("Convert .csv styles (Forge) to .json or .json to .csv (Forge)? (csv/json) ")

# Get the name of the input file from the user
input_file = input("Enter the name of the input file: ")

# Determine the name of the output file based on the conversion type
if conversion.lower() == 'csv':
    # Add the .csv extension if it's not already there
    if not input_file.endswith('.csv'):
        input_file += '.csv'
    output_file = os.path.splitext(input_file)[0] + '.json'
    # Convert the CSV file to JSON
    csv_to_json(input_file, output_file)
elif conversion.lower() == 'json':
    # Add the .json extension if it's not already there
    if not input_file.endswith('.json'):
        input_file += '.json'
    output_file = os.path.splitext(input_file)[0] + '.csv'
    # Convert the JSON file to CSV
    json_to_csv(input_file, output_file)
else:
    print("Invalid conversion type. Please enter 'csv' or 'json'.")
