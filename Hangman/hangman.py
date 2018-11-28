
import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print ("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

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


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
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
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many
    letters the secretWord contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess
    about whether their guess appears in the computers word.
    * After each round, you should also display to the user the
    partially guessed word so far, as well as letters that the
    user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''
    introduction = str(len(secretWord))
    lettersGuessed = []
    letter = str()
    mistakesMade = 8
    wordGuessed = False
    
    print ('Welcome to the game, Hangman!')
    print ('I am thinking of a word that is ' + str(introduction) + ' letters long.')
    print ('------------')

    while mistakesMade > 0 and mistakesMade <= 8 and wordGuessed is False:
        if secretWord == getGuessedWord(secretWord, lettersGuessed):
            wordGuessed = True
            break
        print ('You have ' + str(mistakesMade) + ' guesses left.')
        print ('Available letters: ' + getAvailableLetters(lettersGuessed))
        letter = raw_input('Please guess a letter: ').lower()
        if letter in secretWord:
            if letter in lettersGuessed:
                print ("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
            else:
                lettersGuessed.append(letter)
                print ('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
        else:
            if letter in lettersGuessed:
                print ("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
            else:
                lettersGuessed.append(letter)
                mistakesMade -= 1
                print ('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
                print ('------------')

    if wordGuessed == True:
        return 'Congratulations, you won!'
    elif mistakesMade == 0:
        print ('Sorry, you ran out of guesses. The word was ' + secretWord)

secretWord = chooseWord(wordlist).lower()
print(chooseWord(wordlist))
hangman(secretWord)	 	  	 	  	   	  	     	     	 	
