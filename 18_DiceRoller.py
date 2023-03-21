"""Выбрасыватель игральных костей, (с) Эл Свейгарт"""

import random, sys

print('''Dice Roller, by Al Sweigart

Enter what kind and how many dice to roll. The format is the number of
dice, folowed by "d", followed by the number of sidesthe dice have.
You can also add a plus or minus adjustment.
  
Examples:
  3d6 rolls three 6-sided dice
  1d10+2 rolls one 10-sided die, and adds 2
  2d38-1 rolls two 38-sided die, and subtracts 1
  QUIT quits the program''')

while True:
    try:
        diceStr = input('>  ')
        if diceStr.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        diceStr = diceStr.lower().replace(' ', '')
        dIndex = diceStr.find('d')
        if dIndex == -1:
            raise Exception('Missing the "d" character.')

        numberOfDice = diceStr[:dIndex]
        if not numberOfDice.isdecimal():
            raise Exception('Missing the number of dice.')
        numberOfDice = int(numberOfDice)

        modIndex = diceStr.find('+')
        if modIndex == -1:
            modIndex = diceStr.find('-')

        if modIndex == -1:

            numberOfSides = diceStr[dIndex + 1:]
        else:
            numberOfSides = diceStr[dIndex + 1: modIndex]
        if not numberOfSides.isdecimal():
            raise Exception('Missing the number of sides.')
        numberOfSides = int(numberOfSides)

        if modIndex == -1:
            modAmount = 0
        else:
            modAmount = int(diceStr[modIndex + 1:])
            if diceStr[modIndex] == '-':
                modAmount = -modAmount


        rolls = []
        for i in range(numberOfDice):
            rollResult = random.randint(1, numberOfSides)
            rolls.append(rollResult)

        print('Total:', sum(rolls) + modAmount, '(Each die:', end='')

        for i, roll in enumerate(rolls):
            rolls[i] = str(roll)
        print(', '.join(rolls), end = '')

        if modAmount != 0:
            modSign = diceStr[modIndex]
            print(', {}{}'.format(modSign, abs(modAmount)), end='')
        print(')')
    except Exception as exc:
        print('Invalid input. Enter something like "3d6" or "1d10+2".')
        print('Input was invalid because: ' + str(exc))
        continue

