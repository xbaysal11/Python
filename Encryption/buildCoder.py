#daniyarovbaysal
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    
    
    dict ={}
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    for l in range(len(upper)):
        dict[upper[l]] = upper[(l+shift) % len(upper)]
    for l in range(len(lower)):
        dict[lower[l]] = lower[(l+shift) % len(lower)]
    return dict
print(buildCoder(2))