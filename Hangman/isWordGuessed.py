def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count = 0
    for i, g in enumerate(secretWord):
    	if g in lettersGuessed:
    		count += 1
    if count == len(secretWord):
    	return True
    else:
    	return False