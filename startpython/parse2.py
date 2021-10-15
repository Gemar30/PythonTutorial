# Python read and display from JSON FILE
import json

with open('player.json') as f:
    data = json.load(f)

# Displaying output
print(data)