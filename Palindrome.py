def ispalindrome(word):
    if word == word[::-1]:
      return word[::-1]
word = str(input())
print(ispalindrome(word))