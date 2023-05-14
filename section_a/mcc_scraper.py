from datetime import datetime
import json
from pathlib import Path
import time

from bs4 import BeautifulSoup
import requests


class MCCScraper:
    def __init__(self):
        self.session = requests.Session()
        self.update_headers()
        self.SLEEP_SEC = 3

    def update_headers(self):
        self.session.headers.update(
            {
                'authority': 'www.mcc-mnc.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
            })

    def fetch_homepage(self):
        url = "https://www.mcc-mnc.com/"
        response = self.session.get(url)
        print('Proessing Homepage data..')
        data = self.parse_response(response)
        time.sleep(self.SLEEP_SEC)
        return data

    def parse_response(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')

        table = soup.find(id='mncmccTable')
        headers = table.find('thead')
        headers_list = [i.get_text().strip() for i in headers.find_all('th')]

        data = []

        body = table.find('tbody')
        rows = body.find_all('tr')
        len_rows = len(rows)
        for count, row in enumerate(rows):
            row_data = {}
            for idx, val in enumerate(row.find_all('td')):
                row_data[headers_list[idx]] = val.get_text().strip()
            data.append(row_data)
            print('Processed row {} of {}..'.format(count+1, len_rows))

        return data

    def export_json(self, data):
        print('Exporting data to JSON..')
        folder_friendly_time = datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")
        filepath = 'section_a/output_data/output_{}.json'.format(folder_friendly_time)
        with open(self.get_file_path(filepath), 'w') as f:
            json.dump(data, f)
        print('Export complete. File Location: {}'.format(filepath))


    def get_file_path(self, fileName):
        broken_filename = fileName.split("/")

        path = Path.cwd()

        while len(broken_filename) > 0:
            path = path.joinpath(broken_filename[0])
            broken_filename = broken_filename[1:]

        return path
    
    def run(self):
        data = self.fetch_homepage()
        self.export_json(data)
        self.close_up()

    def close_up(self):
        print('Scrape complete.')


if __name__ == '__main__':
    scraper = MCCScraper()
    scraper.run()
