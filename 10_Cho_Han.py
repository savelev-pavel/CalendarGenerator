"""Чо-Хан, (С) Эл Свейгарт
Традиционная японская игра в кости типа чет-нечет."""

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI',3: 'SAN',
                   4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, by Al Sweigart

In tnis traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the flor. The player must guess if the
dice total to an even (cho) or odd (han) number.
''')

purse = 5000
while True:
    print(f'You have {purse} mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('> ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You don\'t have enough to make that bet.')
        else:
            pot = int(pot)
            break
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('''The dealer swirls the cup and you hear the rattle of dice
the dealer slams the cup on the floor, still covering the
dice and asks for your bet

CHO (even) or HAN (odd)?''')

    while True:
        bet = input('> ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    print(f"""The dealer lifts the cup to reveal:
{JAPANESE_NUMBERS[dice1]} - {JAPANESE_NUMBERS[dice2]}
{dice1} - {dice2}""")

    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    if playerWon:
        print(f'You won! You take {pot} mon')
        purse = purse + pot
        print(f'The house collects a {pot//10} mon fee')
        purse = purse - pot//10
    else:
        print('You lost')
        purse = purse - pot
        if purse <= 0:
            print('''You have run out of money!
Thanks for playing!''')
            sys.exit()
