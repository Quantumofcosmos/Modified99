import itertools
import random


def initialize():
    a = ['Diamond', 'Spade', 'Clover', 'Hearts']
    b = ['K', 'Q', 'J', 'A']
    for i in range(2, 11):
        b.append(str(i))
    superset = list(itertools.product(a, b, repeat=1))
    # print(superset)
    large = []
    for each in superset:
        large.append(each[1] + 'of' + each[0])
        # print each
    return large


def sattolocycle(items):
    i = len(items)
    while i > 1:
        i = i - 1
        j = random.randrange(i)  # 0 <= j <= i-1
        items[j], items[i] = items[i], items[j]
    return items


def distribute(shufleddeck, n):
    deck = shufleddeck[0:n]
    remainingdeck = shufleddeck[n:]
    return deck, remainingdeck


def hindushuffle(deck, n):
    decklength = len(deck)
    i = 0
    while i < n:
        finger = round(random.random() * 52)
        position = round(random.random() * (decklength - finger))
        decktop = deck[int(min(finger, position)):int(max(position, finger) + 1)]
        deckbottom = deck
        for each in decktop:
            deckbottom.remove(each)
            # print(each)
        # print(decktop)
        # print(deckbottom)
        deck = decktop
        deck.extend(deckbottom)
        i = i + 1
    return deck


fulldeck = initialize()
# print(fulldeck)

shufdeck = hindushuffle(fulldeck, 10)
##print(shufdeck)
# print(riffle(fulldeck))
ncard = input("Enter number of cards: ")
if int(ncard) > 13:
    ncard = input("Enter number of cards 13 or less: ")
else:
    pass
mydeck, remaining = distribute(shufdeck, int(ncard))

print(mydeck)
