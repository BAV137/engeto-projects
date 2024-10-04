# Elections Scraper

**THIS SCRIPT COLLECTS RESULTS FROM:**  
The elections to the Chamber of Deputies of the Parliament of the Czech Republic held on 
October 20-21, 2017.

[https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ](
https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ)

- **BASED ON:** District Brno Venkov  

  [https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6203](
  https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6203)

### Collects Data:

    Číslo: ['582794', '582808', '581321', '582824', '582832'] ...
    Název: ['Babice nad Svitavou', 'Babice u Rosic', 'Běleč', 'Bílovice nad Svitavou', 'Biskoupky'] ...
    Voliči v seznamu: ['925', '553', '160', '2676', '145'] ...
    Vydané obálky: ['660', '353', '131', '2018', '86'] ...
    Platné hlasy: ['655', '351', '130', '2004', '85'] ...
    Občanská demokratická strana: ['109', '32', '13', '316', '6'] ...
    Řád národa - Vlastenecká unie: ['1', '0', '0', '0', '0'] ...
    ...


### Saves Results to .CSV:

    Číslo:,Název:,Voliči v seznamu:,Vydané obálky:,Platné hlasy:,Občanská demokratická strana:, ...
    582794,Babice nad Svitavou,925,660,655,109,1,2,43,0,53,31,7,3,10,0,0,93,0,39,129,0,3,69,0,  ...
    582808,Babice u Rosic,553,353,351,32,0,0,18,1,27,30,5,1,6,0,2,37,0,13,93,0,1,25,5,4,1,1,49, ...
    581321,Běleč,160,131,130,13,0,0,25,0,8,14,0,1,0,0,0,11,1,1,30,0,0,14,0,0,0,0,12,0,0, ...
    582824,Bílovice nad Svitavou,2676,2018,2004,316,0,2,103,0,257,78,28,6,44,2,0,205,2,147,432, ...
    ...

## Requirements:

- Python 3.9.6+ (tested)
- Libraries:  
  Install from `requirements.txt`

## How to Run:

1. **Install Python:**  
   Download and install Python from [https://www.python.org/](https://www.python.org/).

2. **Install Required Libraries:**  
   Open your terminal or command prompt, navigate to the directory containing the script 
   and `requirements.txt`, then run:

   `pip install -r requirements.txt`

3. **Run the Script:**  
   In the terminal or command prompt, run:  

   `python 01_elections_scraper.py "district_url" "results_file_name"`

   Example:  

   `python 01_elections_scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2104" "vysl_hlas_Kolin"`

4. **Check Results:**  
   The file `vysl_hlas_Kolin.csv` will be saved in the script folder. Open it with your file explorer.