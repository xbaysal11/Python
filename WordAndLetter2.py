def avoids(words, list):
    if list[2] in words:
        return False
    else:
        return True
words = str(input())
list = str(input())
print(avoids(words,list))
