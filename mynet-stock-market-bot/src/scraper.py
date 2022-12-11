import json
import requests
import datetime
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, url):
        self.url = url
        self.soup = BeautifulSoup(requests.get(url).content, "lxml")

    def start(self):
        """
        Scraper start method
        """
        companies = []
        for i in self.soup.find_all('strong', attrs={'class': 'mr-4'}):
            companies.append(i.find('a', href=True)['href'])

        company_list = {}
        for company in companies:
            soup = BeautifulSoup(requests.get(company).content, "lxml")
            dict_title = soup.find('div', attrs={'class': 'flex-list-heading'}).text
            company_attr = {}
            for i in soup.find_all('li', attrs={'class': 'flex align-items-center justify-content-between'}):
                parsed_text = i.text.split("\n")
                key = parsed_text[1]
                value = parsed_text[2]
                company_attr[key] = value
            company_list[dict_title] = company_attr
        return self.__json_encoder(company_list)

    @staticmethod
    def __json_encoder(company_list):
        """
            Encode json data
        """
        encoded_json = json.dumps(company_list, ensure_ascii=False)
        return encoded_json.replace("\\n", "")

    def save_file(self, data):
        """
            It saves data to the file system
        """
        current_date = datetime.datetime.now()
        with open(f'data_{current_date}.json', 'w', encoding='utf-8') as f:
            json.dump(json.loads(data), f, ensure_ascii=False, indent=4)





