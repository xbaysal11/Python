def has_duplicates(listt):
    for i in listt:
        if len(listt) != len(set(listt)):
            print('False')
        else:
            print('True')
listt=input()
has_duplicates(listt)