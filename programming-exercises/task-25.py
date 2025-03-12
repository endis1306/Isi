
import requests
from bs4 import BeautifulSoup

url = 'https://www.w3schools.com'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    links = soup.find_all('a', href=True)

    href_links = [link['href'] for link in links]

    print(href_links)
else:
    print(f"Nie udało się pobrać strony. Status: {response.status_code}")



