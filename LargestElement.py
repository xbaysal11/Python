def great(list):
   if len(list) == 1:
        return list[0]
   else:
       if list[0] < great(list[1:]):
           return great(list[1:])
       elif list[0] > great(list[1:]):
           return list[0]
x = input()
print(great(x))