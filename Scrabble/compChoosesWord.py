def compChooseWord(hand, wordList, n):

    max_score = 0
    best_word = None
    for word in wordList:
        if(isValidWord(word, hand, wordList)):
            score = getWordScore(word, n)      
            if(score > max_score):
                max_score = score
                best_word = word
    return best_word