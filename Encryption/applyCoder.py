#daniyarovbaysal
def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    final = ''
    for x in text:

        if not (x in string.punctuation or x == '' or x in str(range(10)) ):
            final += coder[x]

        else:
            final += x

    return final
text = str(raw_input())
print applyCoder(text, buildCoder(1))
print applyCoder("Hello world! ", buildCoder(25))