list=['A', 'B', 'C', 'D', 'E']
lowList=['a', 'b', 'c', 'd','e']
n=[]
dict={}
d=1
user=input()
if user in list:
    for  k in list:
        dict[k]=lowList[d]
        d+=1
        print(dict)