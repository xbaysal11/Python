#daniyarovbaysal
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    if x == "":
        return True
    elif word == "" and x != "":
        return False
    elif x[0] in word:
        return True and x_ian(x[1:], word[word.find(x[0]):])
    else:
        return False