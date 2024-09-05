
"""
01_bulls_and_cows.py: druhý projekt do Engeto Online Python Akademie
author: Artur Boyko
email: boykoartur@gmail.com
discord: bavdisbagc
"""

import random
import time
import sys


interesting_facts = [
    """
    Difficulty of Guessing:

     There are 5040 possible combinations of four-digit
    numbers with no repeating digits. This makes the task
    challenging!
    """,
    """
    Mathematical Probability:

     The probability of guessing the number on the first
    attempt is 1/5040, which is very low—about 0.02%!
    """,
    """
    Game History:

     The game, based on "bulls and cows," has roots in
    ancient logic puzzles long before computers existed.
    """,
    """
    Numerical Intuition:

     Our brains tend to seek patterns, even in randomness.
    Players often look for "patterns" in their guesses.
    """,
    """
    Winning Strategies:

     Strategies like "divide and conquer" can significantly
    reduce the number of attempts. This involves testing
    different digits in various positions.
    """,
    """
    Average Number of Attempts:

     On average, it takes about 7-8 attempts to guess the
    four-digit number if using an optimal strategy.
    """,
    """
    Cognitive Skills:

     Guessing numbers and analyzing feedback improves logical
    thinking, strategic planning, and decision-making under
    uncertainty.
    """,
    """
    Color Psychology:

     In versions with colors, players tend to memorize
    sequences faster. Colors activate different brain areas,
    enhancing memory and perception.
    """,
    """
    Cultural Variations:

     In some countries, there are popular versions of this
    game using letters instead of numbers, like "Mastermind."
    """,
    """
    Popularity in IT:

     The game is often used by programmers to teach and test
    algorithmic thinking, as it requires logical algorithms.
    """
]


def line_func(string='-', how_many=79) -> None:
    print(string * how_many)


def welcome_func() -> None:
    line_func('X')
    print(
        f'C====[= $ == WELCOME TO === {{BULLS & COWS] GAME ==> $'
        f'{"I==IO{ python 3.12 ]":>{26}}'
    )
    line_func('x')


def game_description_func() -> None:
    print(
        """
    DESCRIPTION:

      The journey through the shadows of the digital realm is a quest
    for truth. The computer conceals a secret 4-digit number, and the
    player's mission is to uncover this hidden truth.

      Each guess brings the player closer to revealing the mysterious
    number, with every bull{ and cow[ serving as a clue. Only by
    deciphering these clues can the player unveil the secret, earning
    victory by unearthing the complete truth hidden within the code.
    """
    )


def game_rules_func() -> None:
    line_func()
    print(
        """
    THE RULES OF THE GAME:

      In the shadows of the digital world, the computer conceals a
    secret 4-digit number, challenging the player to uncover its mystery.

      When the player guesses a digit and its position correctly, it’s a
    BULL{. If the player guesses a digit that is in the number but
    in the wrong position, it’s a COW[.

      For example, if the hidden number is 1234 and the player guesses
    9321, there will be 3 cows[.

      The game continues its mystery until the player reveals all digits
    in their correct order, earning 4 bulls{ and achieving victory.
    """
    )


def trick_func() -> None:
    line_func('x')
    input(' <-- ARE YOU READY?: ')
    line_func()
    sarcasm_text = (
        f' -> HA Ha ha! Srsly??? \n'
        f' -> Your words mean nothing to me.'
        f' I only understand zeros and ones. \n'
        f' -> You are in game adventurer! \n'
    )
    for elem in sarcasm_text:
        print(elem, end='', flush=True)
        time.sleep(0.10)


def secret_number_func() -> list[int]:
    digits = list(range(10))
    random.shuffle(digits)
    if digits[0] != 0:
        digs = digits[:4]
    else:
        digs = digits[1:5]
    return digs


def user_number_func() -> list[int]:
    while True:
        line_func('x')
        use_num = input(f' <-- En__er--yor___nbr A!D@V#E$T%U^R*E(R): ')

        errs = [f' -> THE NUMBER: {"-" * 63}']
        if not use_num.isdigit():
            errs.append('  * contains NON-DIGIT characters. ')

        if len(use_num) != 4:
            errs.append('  * has MORE or LESS than 4 symbols. ')

        if len(use_num) != len(set(use_num)):
            errs.append('  * contains REPEATING symbols. ')

        if len(use_num) > 0 and use_num[0] == '0':
            errs.append('  * starts with ZER0. ')

        if len(errs) > 1:
            line_func('x')
            print(' ---> WE HAVE SOME PROBLEMS !!! ')
            line_func('!', 31)
            for err in errs:
                print(err)
            continue
        else:
            user_number = [int(num) for num in use_num]
            return user_number


def the_equalizer_func(sec_num_list, use_num_list) -> str | list[int]:
    bulls = 0
    cows = 0
    for num_from_sec, num_from_use in zip(sec_num_list, use_num_list):
        if num_from_sec == num_from_use:
            bulls += 1
        elif num_from_use in sec_num_list:
            cows += 1

    if bulls == 4:
        return 'victory'
    else:
        return [bulls, cows]


def main():
    welcome_func()
    game_description_func()
    game_rules_func()

    secret_number = secret_number_func()
    secret_number_str = ''.join(map(str, secret_number))

    trick_func()

    # processing
    start_time = time.time()
    attempts_counter = 0
    fact_index = 0
    while True:
        attempts_counter += 1

        user_number = user_number_func()
        user_number_str = ''.join(map(str, user_number))

        result = the_equalizer_func(secret_number, user_number)
        if result != 'victory':
            line_func('x')
            print(
                f'===>  *-BULLS{{ |{result[0]}|:|{result[1]}| ]COWS-*  <==='
                f'{f"ATTEMPT |{attempts_counter}|":>{43}}'
                f'\n{"=" * 36} {f"NUMBER |{user_number_str}|":>{42}}'
            )
            if fact_index < 10:
                print(' -> INTERESTING FACT:', '-' * 57)
                print(interesting_facts[fact_index])
                fact_index += 1
            continue
        else:
            end_time = time.time()
            proc_time = end_time - start_time
            line_func('x')
            print(
                f'''
        Congratulations, brave adventurer!

          After a long and arduous quest through the digital realm,
          you have successfully unveiled the hidden truth!

          The Epic Journey Is Over!
            -> The secret number was: {secret_number_str}
            -> Attempts taken: {attempts_counter}
            -> Time taken: {int(proc_time // 60)}:{int(proc_time % 60):02} seconds

          May this victory inspire new quests and adventures.         

        Thank you for playing. Farewell, until the next challenge!
        '''
            )
            line_func('X')
            break
    sys.exit()


if __name__ == "__main__":
    main()
