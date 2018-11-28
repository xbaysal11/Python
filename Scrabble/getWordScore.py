def getWordScore(word, n):

    score = 0
    bonus = 50
    for letter in word:
        try:
            score += SCRABBLE_LETTER_VALUES[letter]
        except KeyError:
            return 0      
    word_len = len(word)
    score *= word_len
    if (word_len == n):
        score += bonus
    return score