"""Глубокая пешера, (с) Эл Свейгарт"""


import random, sys, time

WIDTH = 70
PAUSE_AMOUNT = 0.5

print('Deep Cave, by Al Sweigart')
print('Press CTRL+C to stop')
time.sleep(1)

leftWidth = 20
gapWidth = 10

while True:
    rightWidth = WIDTH - gapWidth - leftWidth
    print(('#' * leftWidth) + (' ' * gapWidth) + ('#' * rightWidth))

    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        sys.exit()

    diceRoll = random.randint(1, 6)
    if diceRoll == 1 and leftWidth > 1:
        leftWidth = leftWidth - 1
    elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
        leftWidth = leftWidth + 1
    else:
        pass