import random
def indianshuffle(deck, n):
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
