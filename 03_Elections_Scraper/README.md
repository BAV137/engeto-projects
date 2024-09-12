# Elections Scraper

    ->  THIS SCRIPT COLLECTS RESULTS FROM: the elections to the Chamber 
        of Deputies of the Parliament of the Czech Republic held 
        on October 20-21, 2017.

`https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ`

    ->  BASED ON: district Brno Venkov

`https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6203`
    
    ->  RUN WITH ARGUMENTS: two

`01_elections_scraper.py 'district_url' 'results_file_name'`


### Collects DATA:

    ('Číslo:', ['582794', '582808', '581321', '582824', '582832', '582841', '58...]) 
    ('Název:', ['Babice nad Svitavou', 'Babice u Rosic', 'Běleč', 'Bílovice nad...]) 
    ('Voliči v seznamu:', ['925', '553', '160', '2676', '145', '924', '1749', '...]) 
    ('Volební účast v %:', ['71,35', '63,83', '81,88', '75,41', '59,31', '78,4,...]) 
    ('Platné hlasy:', ['655', '351', '130', '2004', '85', '724', '1091', '218',...]) 
    ('Občanská demokratická strana:', ['109', '32', '13', '316', '6', '64', '12...]) 
    ('Řád národa - Vlastenecká unie:', ['1', '0', '0', '0', '0', '0', '2', '0',...])
    ...


### Saves results to .CSV:

    XXX (Elections Scraper -> VOLBY.cz) XXXXXXXXXXXXXXXXXXXXXX (python 3.9.6.+) XXX
     -> Processing... [187/187] -> Data successfully downloaded!
     -> Writing... [.csv, "utf-8"] -> Data successfully saved!
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

    Číslo:,Název:,Voliči v seznamu:,Volební účast v %:,Platné hlasy:,Občanská de...
    582794,Babice nad Svitavou,925,"71,35",655,109,1,2,43,0,53,31,7,3,10,0,0,93,...
    582808,Babice u Rosic,553,"63,83",351,32,0,0,18,1,27,30,5,1,6,0,2,37,0,13,93...
    ...


## Requirements:
    
    ->  Python 3.9.6.+ (tested)

    ->  Libraries:

        - requirements.txt