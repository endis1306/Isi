import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


class Home:
    def __init__(self, header_name, price, price_for_m2):
        self.header_name = header_name
        self.price = price
        self.price_for_m2 = price_for_m2


def fetch_homes(url):
    homes = []

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        listings = soup.find_all('article', class_='css-136g1q2 eg92do40')
        for listing in listings:
            header_name = listing.find('p', class_='css-u3orbr e1g5xnx10').get_text(strip=True) if listing.find('p',class_='css-u3orbr e1g5xnx10') else 'Brak nagłówka'
            price = listing.find('span', class_='css-2bt9f1 evk7nst0').get_text(strip=True) if listing.find('span',class_='css-2bt9f1 evk7nst0') else 'Brak ceny'
            dl = listing.find('dl', class_='css-9q2yy4 e1nke57n1')
            price_for_m2 = dl.find_all('span')[2].get_text(strip=True) if dl and len(dl.find_all('span')) > 2 else 'Brak ceny za m2'

            home = Home(header_name, price, price_for_m2)
            homes.append(home)

    else:
        print(f"Nie udało się pobrać strony. Status: {response.status_code}")

    return homes


def save_to_csv(homes, filename='home.csv'):

    def clean_text(text):
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'[^\w\s,.ąćęłńóśżźĄĆĘŁŃÓŚŻŹ-]', '', text)
        return text.strip()

    data = [
        {
            'header_name': clean_text(home.header_name),
            'price': clean_text(home.price),
            'price_for_m2': clean_text(home.price_for_m2)
        }
        for home in homes
    ]


if __name__ == "__main__":
    url = 'https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/pomorskie/gdynia/gdynia/gdynia?priceMax=600000&viewType=listing'
    homes = fetch_homes(url)

    homes_dict = {home.header_name: home for home in homes}

    save_to_csv(homes)

    for home in homes:
        print(f"Nagłówek: {home.header_name}, Cena: {home.price}, Cena za m2: {home.price_for_m2}")
