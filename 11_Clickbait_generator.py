"""Генератор заголовок-приманок, (с) Эл Свейгарт
Генератор заголовков-приманок для сайта со скучным контентом"""

import random

OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
POSESSIVE_PRONOUNS = ['Her', 'His', 'Their']
PERSONAL_PRONOUNS = ['She', 'He', 'They']
STATES = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania',
          'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']
NOUNS = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent',
         'Cat', 'Dos', 'Chicken', 'Robot', 'Video Game', 'Avocado',
         'Plastic Straw', 'Serial Killer', 'Telephone Psychic']
PLACES = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement',
          'Workplace', 'Donut Shop', 'Apocalypse Bunker']
WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']


def generateAreMillenialsKillingHeadline():
    noun = random.choice(NOUNS)
    return f'Are Milleneals Killing the {noun} Industry?'


def generateWhatYouDontKnowHeadline():
    noun = random.choice(NOUNS)
    pluralNoun = random.choice(NOUNS) + 's'
    when = random.choice(WHEN)
    return f'Without This {noun}, {pluralNoun} Could Kill You {when}'


def generateBigCompaniesHateHerHeadline():
    pronoun = random.choice(OBJECT_PRONOUNS)
    state = random.choice(STATES)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return f'Big Companies Hate {pronoun}! See How This {state} {noun1} Invented a Cheaper {noun2}'


def generateYouWontBelieveHeadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    pronoun = random.choice(OBJECT_PRONOUNS)
    place = random.choice(PLACES)
    return f'You Won\'t Believe What This {state} {noun} Found in {pronoun} {place}'


def generateDontWantYouToKnowHeadline():
    pluralNoun1 = random.choice(NOUNS) + 's'
    pluralNoun2 = random.choice(NOUNS) + 's'
    return f'What {pluralNoun1} Don\'t Want You To Know About {pluralNoun2}'


def generateGiftIdeaHeadline():
    number = random.randint(7, 15)
    noun = random.choice(NOUNS)
    state = random.choice(STATES)
    return f'{number} Gift Ideas to Give Your {noun} From {state}'


def generateReasonsWhyHeadline():
    number1 = random.randint(7, 15)
    pluralNoun = random.choice(NOUNS) + 's'
    number2 = random.randint(1, number1)
    return f'{number1} Reasons Why {pluralNoun} Are More Interesting Than You' \
           f' Think (Number {number2} Will Surprise You!)'


def generateJobAutomatedHeadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)

    i = random.randint(0, 2)
    pronoun1 = POSESSIVE_PRONOUNS[i]
    pronoun2 = PERSONAL_PRONOUNS[i]
    if pronoun1 == 'Their':
        return f'This {state} {noun} Didn\'t Think Robots Would Take {pronoun1} Job.' \
               f'{pronoun2} Were Wrong.'
    else:
        return f'This {state} {noun} Didn\'t Think Robots Would Take {pronoun1} Job.' \
               f'{pronoun2} Was Wrong.'


def main():
    print('Clickbait Headline Generator')
    print('By Al Sweigart')
    print()
    print('Our website needs to trick people into looking at ads!')
    while True:
        print('Enter the number of clickbait headlines to generate:')
        response = input('> ')
        if not response.isdecimal():
            print('Please enter a number.')
        else:
            numberOfHeadlines: int = int(response)
            break
    for i in range(numberOfHeadlines):
        clickbaitType: int = random.randint(1, 8)
        if clickbaitType == 1:
            headline = generateAreMillenialsKillingHeadline()
        elif clickbaitType == 2:
            headline = generateWhatYouDontKnowHeadline()
        elif clickbaitType == 3:
            headline = generateBigCompaniesHateHerHeadline()
        elif clickbaitType == 4:
            headline = generateYouWontBelieveHeadline()
        elif clickbaitType == 5:
            headline = generateDontWantYouToKnowHeadline()
        elif clickbaitType == 6:
            headline = generateGiftIdeaHeadline()
        elif clickbaitType == 7:
            headline = generateReasonsWhyHeadline()
        elif clickbaitType == 8:
            headline = generateJobAutomatedHeadline()

        print(headline)
    print()

    website = random.choice(['wobsite', 'blag', 'Facebuuk', 'Googles',
                             'Facesbook', 'Tweedie', 'Pastagram'])
    when = random.choice(WHEN).lower()
    print(f'Post these to our {website} {when} or you\'re fired')

if __name__ == '__main__':
    main()
