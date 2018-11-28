#daniyarovbaysal
def findBestShift(wordList, text):
     """
     Finds a shift key that can decrypt the encoded text.

     text: string
     returns: 0 <= int < 26
     """
    total = 0
    real = 0

    for i in range(26):
        current = 0
        converted = applyShift(text, i)
        lista = converted.split(' ')

        for m in lista:
            if isWord(wordList, m):
                current += 1

        if current > real:
            total = i
            real = current

    return total