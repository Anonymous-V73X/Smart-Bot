import json

def remove_duplicate_ids():
    # Load file data from JSON
    file_data = load_file_data()

    # Iterate over each file in the file data
    for file_name, file_ids in file_data.items():
        if len(file_ids) == 2:
            # Remove one of the duplicate IDs
            file_ids = [file_ids[0]]

        # Update the file IDs in the file data
        file_data[file_name] = file_ids

    # Save the modified file data back to JSON
    save_file_data(file_data)

def load_file_data():
    try:
        with open("file_data.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
    return data

def save_file_data(file_data):
    with open("file_data.json", "w") as file:
        json.dump(file_data, file)

# Call the function to remove duplicate IDs
remove_duplicate_ids()

import json

# Read the file_data.json file
with open('file_data.json', 'r') as file:
    file_data = json.load(file)

import re

# Custom sorting function
def custom_sort_key(key):
    # Remove special characters you want to ignore
    cleaned_key = re.sub(r'[\/!_.,:;\'"+&%$#!)(\^<>?|]', '', key)
    
    # Check if the key starts with a number
    if cleaned_key[0].isdigit():
        # Return a tuple with (0, cleaned_key) to make keys starting with numbers come first
        return (0, cleaned_key)
    else:
        # Return a tuple with (1, cleaned_key) for other keys
        return (1, cleaned_key)

# Sort the keys alphabetically, ignoring special characters and considering numbers first
sorted_file_data = {k: v for k, v in sorted(file_data.items(), key=lambda item: custom_sort_key(item[0]))}



# Write the sorted data back to file_data.json
with open('file_data.json', 'w') as file:
    json.dump(sorted_file_data, file, indent=4)

print("File_data.json has been sorted alphabetically.")



