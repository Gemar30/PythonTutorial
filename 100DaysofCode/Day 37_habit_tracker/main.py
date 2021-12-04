import requests
from datetime import datetime

USERNAME = "gemar123"
TOKEN = "dsadsadas123sdas"
GRAPH_ID = "graph123"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_endpoint = f"/{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Read book",
    "unit": "Km",
    "type": "float",
    "color": "shibafu",
}


headers = {
    "X-USER-TOKEN": TOKEN,
}

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many km did you cycle today?"),

}
response = requests.post(url = pixel_creation_endpoint, json = pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "5.4",
}
# response = requests.put(url = update_endpoint, json = new_pixel_data, headers= headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

delete_pixel_data = {
    "date": today.strftime("%Y%m%d"),
}
# response = requests.delete(url = delete_endpoint, headers= headers)
# print(response.text)