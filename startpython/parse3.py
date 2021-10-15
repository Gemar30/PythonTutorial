# Writing json to a file
import json
player1 = {
    "name": "Gemar",
    "age": 35,
    "languages": ["English", "Filipino"],
    "city": "Manila"
}

# open the file in write mode
with open("player1.txt","w") as json_file:
    json.dump(player1, json_file)

