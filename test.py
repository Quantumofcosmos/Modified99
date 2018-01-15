import itertools
import random
import indianshuffle

def initialize():
    values = range(2, 11) + "Ace Jack Queen King".split()
    suits = "Diamonds Clubs Hearts Spades".split()
    deck_of_cards = ["%s of %s" % (v, s) for v in values for s in suits]
    return deck_of_cards


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


fulldeck = initialize()
# print(fulldeck)

shufdeck = indianshuffle.indianshuffle(fulldeck, 10)
##print(shufdeck)
# print(riffle(fulldeck))
ncard = input("Enter number of cards: ")
if int(ncard) > 13:
    ncard = input("Enter number of cards 13 or less: ")
else:
    pass
mydeck, remaining = distribute(shufdeck, int(ncard))

print(mydeck)
