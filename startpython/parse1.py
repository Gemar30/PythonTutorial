# Convert from JSON to Python

import json

'''# Adding some JSON
player1 = ' {"name":"Gemar", "age":24, "city":"Makati"}'

#Parse
x = json.loads(player1)

#Display output
print(x["name"])'''

# Convert from Python to JSON

#Create python dictionary
''' player1 = {"name": "Gemar",
            "age": 25,
            "city": "Taguig"

}

# converting into JSON
x = json.dumps(player1)

# Display output
print(x)'''

# Convert Python Object to JSON

''' print(json.dumps({"name": "Gemar", "age": 26, "city": "Manila"})) # Dictionary to JSON
print(json.dumps(["orange","lemon"])) # List to JSON
print(json.dumps(("apple", "fig"))) # Tuple to JSON
print(json.dumps("Hi There")) # String to JSON
print(json.dumps(55)) # Int to JSON
print(json.dumps(12.1)) # Floating number to JSON
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))'''

