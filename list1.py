list=[50,40,23,70,56,12,5,10,7]
max=0
s_max=0
i=0
while i<len(list):
    if list[i]>max:
        s_max=max
        max=list[i]
    elif list[i]>s_max:
        s_max=list[i]    
    i=i+1
print("second max=",s_max)