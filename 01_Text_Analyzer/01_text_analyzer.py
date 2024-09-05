
"""
01_text_analyzer.py: první projekt do Engeto Online Python Akademie
author: Artur Boyko
email: boykoartur@gmail.com
discord: bavdisbagc
"""


from sys import exit


# USERS
user_database = {
    'bob': '123',
    'ann': 'pass123',
}


# TEXTS
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
    '''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]


def line(what='-', much=79) -> None:
    print(what * much)


# < WELCOME BLOCK >
line('X')
print(' ---> $ Welcome to TextAnalyzer (python 3.12) $ <--- ')


# < SCRIPT_INFO BLOCK >
line('x')
print(
    ' -> This script analyzes the text, for example: ',
    '  *  determining the number of words, ',
    '  *  showing the length and quantity of words. ',
    ' -> You can insert """text""" into "TEXTS variable" and get it parsed. ',
    sep='\n')


# < LOG-IN BLOCK >
line()
print(' -> Please log-in before you start. ')

line()
login = input(' <-- Enter your login: ')
password = input(' <-- Enter your password: ')
if user_database.get(login) != password:
    line('x')
    print(
        ' !!! Attention !!! ',
        '  -> username <- ',
        ' (or) ',
        '  -> password <- ',
        ' !!> isn\'t True !! ',
        sep='\n'
    )
    line('X')
    exit(1)


# < !!! "TADA!" BLOCK !!! >
line()
print(f' ---> !!! Welcome {login.title()} !!! ')


# < TEXTS_PRESENT. BLOCK >
line()
print(f' -> Today, we have {len(TEXTS)} texts to be analyzed: ')
line()
for num, txt in enumerate(TEXTS, 1):
    print(f' {num}. """ {txt[:30]}... """ ')


# < TEXT_USER_CHOICE BLOCK >
line()
text_num = input(f' <-- Enter your text number (1-{len(TEXTS)}): ')
if not text_num.isdigit():
    line('x')
    print(f' -> The number.isdigit(FALSE) ')
    line('X')
    exit(1)
if int(text_num) < 1 or int(text_num) > len(TEXTS):
    line('x')
    print(f' -> The number is out of len(TEXTS) ')
    line('X')
    exit(1)


# < TEXT BLOCK >
text = TEXTS[int(text_num) - 1]
text_split = text.split()


# < TEXT_ANALYZE BLOCK >
# len(text)
words_lentxt = len(text_split)
# .istitle
words_title = 0
# .isaplha and .isupper
words_alpha_upper = 0
# .islower
words_lower = 0
# .isdigit
words_digit = 0
# sum(.isdigit)
words_sum_digit = 0
# lenth and quantity of words
lenth_quantity = dict()

# processing...
for word in text_split:
    if word.istitle():
        words_title += 1
    if word.isalpha() and word.isupper():
        words_alpha_upper += 1
    if word.islower():
        words_lower += 1
    if word.isdigit():
        words_digit += 1
        words_sum_digit += int(word)

    quantity = 0
    for element in word:
        if element.isalpha() or element.isdigit():
            quantity += 1
    if quantity not in lenth_quantity:
        lenth_quantity[quantity] = 1
    else:
        lenth_quantity[quantity] += 1

line('x')
print(
    f' -> There are {words_lentxt} words in the selected text. ',
    f' -> There are {words_title} titlecase words. ',
    f' -> There are {words_alpha_upper} uppercase words. ',
    f' -> There are {words_lower} lowercase words. ',
    f' -> There are {words_digit} numeric strings. ',
    f' -> The sum of all the numbers {words_sum_digit}. ',
    sep='\n')


# < GRAF BLOCK >
keys = sorted(lenth_quantity)
keys_values = sorted(lenth_quantity.values())

line('X')
print(f' -> LEN| {'OCCURENCES':^{keys_values[-1]}} |NR. ')
line('x')
for key in keys:
    stars = '*' * lenth_quantity[key]
    print(f'{key:>{7}}| {stars:<{keys_values[-1]}} |{lenth_quantity[key]}')
line('X')
