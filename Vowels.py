def isVowel(char):

    '''

    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.

    '''

    if char == "i" or char == "e" or char == "a" or char == "o" or char == "u" or char == "I" or char == "E" or char == "A" or char == "O" or char == "U":
       return ("True")
    else:
        return("False")


char = input()
print(isVowel(char))