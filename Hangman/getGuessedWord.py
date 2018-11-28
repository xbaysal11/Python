def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    count = 0
    blank = ['_ '] * len(secretWord)

    for i, g in enumerate(secretWord):
        if g in lettersGuessed:
            count += 1
            blank.insert(count-1,g)
            blank.pop(count)
            if count == len(secretWord):
                return ''.join(str(b) for b in blank)
        else:
            count += 1
            blank.insert(count-1,'_')
            blank.pop(count)
            if count == len(secretWord):
                return ''.join(str(b) for b in blank)