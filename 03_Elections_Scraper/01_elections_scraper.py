
"""
01_elections_scraper.py: třetí projekt do Engeto Online Python Akademie
author: Artur Boyko
email: boykoartur@gmail.com
discord: bavdisbagc
"""


import logging
import sys
from requests import get
from bs4 import BeautifulSoup
from collections import defaultdict
from time import sleep
from csv import writer


logging.basicConfig(
    level=logging.INFO,
    format='|> SCRAPER |> %(asctime)s |> %(levelname)s |> ( %(message)s )'
)

# This is the main function that controls the script
def main():
    logging.info('## IN - "main()"')
    try:
        validate_args_ps2017nssps32_f()
        scraper = PS2017nssPS32(sys.argv[1], sys.argv[2])
        scraper.run_cf()
    except Exception as ex:
        logging.error(ex)
        sys.exit(logging.warning('The script ended with an ERROR!'))
    logging.info('## END - "main()"')

# This function validates the command-line arguments
def validate_args_ps2017nssps32_f():
    logging.info('### IN - "validate_args_f()"')
    if len(sys.argv) != 3:
        sys.exit(logging.error('Enter pls: "url-address" _space_ "file name"'))
    elif not sys.argv[1].startswith("https://www.volby.cz/pls/ps2017nss/ps32"):
        sys.exit(logging.error('Check pls: "url-address"'))
    else:
        logging.info('---> [ARGUMENTS = OK]')
    logging.info('### END - "validate_args_f()"')

# This class scrapes data from a given URL and saves it into a CSV file
class PS2017nssPS32:
    # This is the class constructor, initializing the URL, CSV file name,
    # defaultdict to store scraped data and a list for result URLs.
    def __init__(self, url_argv, csv_file_name):
        self.url_argv = url_argv
        self.csv_file_name = csv_file_name
        self.scrap_data = defaultdict(list)
        self.urls_vysledky = list()

    # This function runs the main scraping process
    def run_cf(self):
        logging.info('#### IN - "run_cf()"')
        self.scrap_okres_cf()
        self.scrap_obec_cf()
        self.data_recording_cf()
        logging.info('#### END - "run_cf()"')

    # This static method sends an HTTP request to the provided URL
    @staticmethod
    def html_req_cf(url: str) -> BeautifulSoup:
        req = get(url)
        return BeautifulSoup(req.text, 'html.parser')

    # This function scrapes district data (numbers, names, and result URLs)
    def scrap_okres_cf(self):
        logging.info('##### IN - "scrap_okres_cf()"')
        object_bs = self.html_req_cf(self.url_argv)
        self.scrap_data['Číslo:'] = [
            cislo.text for cislo in object_bs.select('.cislo')
        ]
        self.scrap_data['Název:'] = [
            nazev.text for nazev in object_bs.select('.overflow_name')
        ]
        self.urls_vysledky = [
            "https://www.volby.cz/pls/ps2017nss/" + url[
                'href'] for url in object_bs.select('.cislo a')
        ]
        logging.info('---> [OKRES = OK]')
        logging.info('##### END - "scrap_okres_cf()"')

    # This function scrapes data for each municipality
    def scrap_obec_cf(self):
        logging.info('##### IN - "scrap_obec_cf()"')
        strany = [
            strana.text for strana in self.html_req_cf(
                self.urls_vysledky[0]).select('.overflow_name')
        ]
        for num, url in enumerate(self.urls_vysledky, 1):
            sleep(0.5)
            object_bs = self.html_req_cf(url)
            self.scrap_data['Voliči v seznamu:'].append(
                object_bs.select_one('.cislo[headers="sa2"]').text.replace(
                    '\xa0', '')
            )
            self.scrap_data['Vydané obálky:'].append(
                object_bs.select_one('.cislo[headers="sa3"]').text.replace(
                    '\xa0', '')
            )
            self.scrap_data['Platné hlasy:'].append(
                object_bs.select_one('.cislo[headers="sa6"]').text.replace(
                    '\xa0', '')
            )
            strany_hlasy = [
                hlasy.text.replace('\xa0', '') for hlasy in object_bs.select(
                    '.cislo[headers="t1sa2 t1sb3"]') + object_bs.select(
                    '.cislo[headers="t2sa2 t2sb3"]')
            ]
            for strana, hlasy in zip(strany, strany_hlasy):
                self.scrap_data[strana + ':'].append(hlasy)
            print(f'\r|> [{num}/{len(self.urls_vysledky)}] |> ', end='')
        logging.info('---> [OBEC = OK]')
        logging.info('##### END - "scrap_obec_cf()"')

    # This function writes the scraped data into a CSV file
    def data_recording_cf(self):
        logging.info('##### IN - "data_recording_cf()"')
        with open(
                f'{self.csv_file_name}.csv', 'w', encoding='UTF-8', newline=''
        ) as csv_file:
            burner = writer(csv_file)
            burner.writerow(self.scrap_data.keys())
            rows = zip(*self.scrap_data.values())
            burner.writerows(rows)
        logging.info('---> [RECORDING = OK]')
        logging.info('##### END - "data_recording_cf()"')

# This block runs the main function if the script is executed directly
if __name__ == "__main__":
    logging.info('# IN - "__name__"')
    main()
    logging.info('# END - "__name__"')
    sys.exit(logging.info('The script ended successfully!'))
