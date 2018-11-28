def isVowel(char):

    '''

    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.

    '''

    if char in 'AaIiEeUuOo':
       return ("True")
    else:
        return("False")


char = input()
print(isVowel(char))