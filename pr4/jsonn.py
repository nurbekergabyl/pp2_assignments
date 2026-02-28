# json.py

import json

# Python dictionary
data = {
    "name": "Nurbek",
    "age": 18,
    "city": "Almaty"
}

# Convert Python to JSON string
json_string = json.dumps(data, indent=4)
print("JSON String:")
print(json_string)

# Write JSON to file
with open("output.json", "w") as file:
    json.dump(data, file, indent=4)

# Read JSON from file
with open("output.json", "r") as file:
    loaded_data = json.load(file)

print("Loaded Data:", loaded_data)
