def lettersIndex(x,y):
    while y  in x:
        return ("Index: ",x.index(y))
        break
word=str(input())
letter=str(input())
print(lettersIndex(word,letter))
