"""Обратный отсчет, (С) Эл Свейгарт"""

import sys, time
import sevseg

secondsLeft = 30
try:
    while True:
        print('\n' * 60)
        hours = str(secondsLeft//60)
        minutes = str((secondsLeft % 3600) // 60)
        seconds = str(secondsLeft % 60)

        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBotomRow = hDigits.splitlines()


        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBotomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBotomRow = sDigits.splitlines()

        print(hTopRow + '   ' + mTopRow + '   ' + sTopRow)
        print(hMiddleRow + ' * ' + mMiddleRow + ' * ' + sMiddleRow)
        print(hBotomRow + ' * ' + mBotomRow + ' * ' + sBotomRow)

        if secondsLeft == 0:
            print()
            print('   * * * * BOOM * * * *')
            break

        print()
        print('Press Ctrl+C to quit')
        time.sleep(1)
        secondsLeft -= 1
except KeyboardInterrupt:
    print('Countdown, by Al Sweigart')
    sys.exit
