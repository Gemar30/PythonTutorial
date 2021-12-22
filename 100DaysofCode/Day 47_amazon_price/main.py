import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.amazon.com/Duo-Evo-Plus-esterilizadora-vaporizador/dp/B07W55DDFB/ref=sr_1_4?qid=1597660904"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

response = requests.get(url, headers= header)
my_html = response.content
soup = BeautifulSoup(my_html, "lxml")
price = soup.find_all(name="span", class_="a-size-medium a-color-price")[4].getText().split("$")[1]
print(price)