names = open('StarWars.txt', 'r+')

names_counter = {}


for name in names.read().split():
   

    if name not in names_counter:
        names_counter[name] = 1

    else:
        names_counter[name] += 1


print(names_counter)

names.close();
