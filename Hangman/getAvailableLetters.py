def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
    yet been guessed
    '''
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    a2 = a[:]
    
    def remove(X1, X2):
        X1Start = X1[:]
        for b in X1:
            if b in X1Start:
                X2.remove(b)
        return ''.join(str(b) for b in X2)

    return remove(lettersGuessed, a2)