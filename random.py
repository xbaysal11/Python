f = open('random-numbers.txt','r')

for i in f:
    print(i)
    x = i.split(' ')
    print(x)
    
for i in range(len(x)):
    x[i] = int(x[i])
    
average = float(sum(x))/len(x)
print(average)  

f = open('out.txt','a')
f.write('\n'+str(average))
f.close()  
