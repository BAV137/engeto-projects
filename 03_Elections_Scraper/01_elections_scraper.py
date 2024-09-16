
"""
01_elections_scraper.py: třetí projekt do Engeto Online Python Akademie
author: Artur Boyko
email: boykoartur@gmail.com
discord: bavdisbagc
"""


from requests import get
from bs4 import BeautifulSoup
from collections import defaultdict
from time import sleep
from csv import writer
import sys


def gdi_func(string='=', how_many=79) -> None:
    print(string * how_many)


def arguments_func() -> None:
    if len(sys.argv) != 3 or 'volby.cz/pls/ps2017nss/ps32' not in sys.argv[1]:
        gdi_func()
        print(f' Error! -> Check arguments.')
        gdi_func()
        sys.exit(1)


def request_bs4_func(url: str) -> BeautifulSoup:
    req = get(url)
    return BeautifulSoup(req.text, 'html.parser')


def main():

    arguments_func()
    url_arg = sys.argv[1]
    name_csv_arg = sys.argv[2]

    print(f'XXX (Elections Scraper -> VOLBY.cz) {"X" * 23} (python 3.9.6+) XXX')
    # ('key:', ['value-1', 'value-2'...])
    scrap_data = defaultdict(list)
    try:
    # ===STAGE(1)=> //'OKRES'_PAGE >
        okres_bs4 = request_bs4_func(url_arg)

        scrap_data['Číslo:'] = [cislo.text for cislo in okres_bs4.find_all(
            'td', class_='cislo')]
        scrap_data['Název:'] = [nazev.text for nazev in okres_bs4.find_all(
            'td', class_='overflow_name')]
        okrsek_urls = ['https://volby.cz/pls/ps2017nss/' + url.find('a')['href']
                       for url in okres_bs4.find_all('td', class_='cislo')]

    # ===STAGE(2)=> //'VYSLEDKY OKRSKU'_PAGE >
        strany = [strana.text for strana in request_bs4_func(okrsek_urls[0]).find_all(
            'td', class_='overflow_name')]
        # processing...
        for num, url in enumerate(okrsek_urls, 1):
            sleep(0.3)
            okrsek_bs4 = request_bs4_func(url)

            scrap_data['Voliči v seznamu:'].append(okrsek_bs4.find(
                'td', headers='sa2').text.replace('\xa0', ''))
            scrap_data['Volební účast v %:'].append(okrsek_bs4.find(
                'td', headers='sa4').text.replace('\xa0', ''))
            scrap_data['Platné hlasy:'].append(okrsek_bs4.find(
                'td', headers='sa6').text.replace('\xa0', ''))
            strany_hlasy = [hlasy.text.replace('\u00A0', '') for hlasy
                            in okrsek_bs4.find_all('td', headers='t1sa2 t1sb3')
                            + okrsek_bs4.find_all('td', headers='t2sa2 t2sb3')]
            for strana, hlasy in zip(strany, strany_hlasy):
                scrap_data[strana + ':'].append(hlasy)

            print(f'\r -> Processing... [{num}/{len(okrsek_urls)}]', end='')
        print(f' -> Data successfully downloaded!')

    # ===STAGE(3)=> BURNING >>>
        print(f' -> Writing... [.csv, "utf-8"]', end='')
        with open(f'{name_csv_arg}.csv', 'w', encoding='utf-8', newline='') as csv_file:
            burner = writer(csv_file)
            burner.writerow(scrap_data.keys())
            rows = zip(*scrap_data.values())
            burner.writerows(rows)
        print(f' -> Data successfully saved!')
        gdi_func('X')
    except Exception as ex:
        print(f' -> We have some error: {ex}')
        gdi_func()
        sys.exit(1)
    sys.exit()


if __name__ == "__main__":
    main()
