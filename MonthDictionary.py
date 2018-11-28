list = ['January','February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
dict = {}
k = 1
for month in list:
    dict[month] = k
    k += 1
print(dict)