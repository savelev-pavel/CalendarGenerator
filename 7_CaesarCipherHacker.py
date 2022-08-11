'''
Caesar Cipher Hacker, by Al Sweigart al@inventwithpython.com
'''

print('Caesar Cipher Hacker, by Al Sweigart al@inventwithpython.com')
print('Enter the encrypted Caesar cipher message to hack.')
message = input('> ')

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)):
    translated = ''
    for symbol in message:
        if symbol.capitalize() in SYMBOLS:
            num = SYMBOLS.find(symbol.capitalize())
            num = num - key
            if num < 0:
                num = num + len(SYMBOLS)
            translated = translated + SYMBOLS[num]
        else:
            translated = translated + symbol
    print('Key #{}: {}'.format(key +1, translated))