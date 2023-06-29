n=[1,2,2,3,2,4,5,6,6]
i=0
list=[]
while i<len(n):
    j=i+1
    while j<len(n):
        if n[i]==n[j] and n[i] not in list:
            list.append(n[i])
        j=j+1
    i=i+1
print(list)        