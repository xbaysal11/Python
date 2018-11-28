def calculateHandlen(hand):

    length = 0
    for letter in hand:
        if hand[letter] != 0:
            length += hand[letter]
    return length