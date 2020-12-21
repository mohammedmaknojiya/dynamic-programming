#https://www.geeksforgeeks.org/convert-an-array-to-reduced-form-set-1-simple-and-hashing/


#link for explaination

a=[10,40,20,30,50]

temp=a.copy()

temp.sort()

h={}
replace_val=1
for i in range(len(temp)):
    h[temp[i]]=replace_val
    replace_val+=1

print(h)

for i in range(len(a)):
    if a[i] in h:
        a[i]=h[a[i]]

print(a)
