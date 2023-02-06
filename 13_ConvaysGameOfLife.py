"""Игра "Жизнь Конвея, (с) Эл Свейгарт
Клеточный автомат для имитационного моделирования. Нажмите Ctrl+C для останова"""

import copy, random, sys, time


WIDTH = 79
HEIGHT = 20

ALIVE = 'O'
DEAD = ' '
nextCells ={}

for x in range(WIDTH):
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            nextCells[(x, y)] = ALIVE
        else:
            nextCells[(x, y)] = DEAD

while True:
    print('\n' * 50)
    cells = copy.deepcopy(nextCells)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x,y)], end='')
        print()
    print('Press Ctrl+C to quit')

    for x in range(WIDTH):
        for y in range(HEIGHT):
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT
            
            numNeighbours = 0 
            if cells[(left, above)] == ALIVE:
                numNeighbours += 1
            if cells[(x, above)] == ALIVE:
                numNeighbours += 1
            if cells[(right, above)] == ALIVE:
                numNeighbours += 1
            if cells[(left, y)] == ALIVE:
                numNeighbours += 1
            if cells[(right, y)] == ALIVE:
                numNeighbours += 1
            if cells[(left, below)] == ALIVE:
                numNeighbours += 1
            if cells[(x, below)] == ALIVE:
                numNeighbours += 1
            if cells[(right, below)] == ALIVE:
                numNeighbours += 1
            if cells[(x, y)] == ALIVE and (numNeighbours == 2 or numNeighbours
                                           == 3):
                nextCells[(x, y)] = ALIVE
            elif cells[(x, y)] == DEAD and numNeighbours == 3:
                nextCells[(x, y)] = ALIVE
            else:
                nextCells[(x, y)] = DEAD
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print("Conway's game of life")
        sys.exit()
