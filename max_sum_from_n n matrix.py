l=[
    [-9, -9, -9, 1 ,1, 1],
    [0 ,-9, 0, 4 ,3 ,2],
    [-9, -9, -9, 1, 2 ,3],
    [0 ,0, 8, 6, 6 ,0],
    [0, 0 ,0, -2, 0 ,0],
    [0, 0, 1, 2, 4, 0]

]
n=6
max_sum=[]

for i in range(n-2):
    first=l[i]

    second=l[i+1]

    third=l[i+2]

    for j in range(len(first)-2):
        #for k in range(1,len(second)-1):
        #print(first[j] , first[j+1] , first[j+2])
        #print(second[j+1])
       # print(third[j] , third[j+1] , third[j+2])

        s = first[j] + first[j+1] + first[j+2] + second[j+1] + third[j] + third[j+1] + third[j+2]

        max_sum.append(s)
       # break

print(max(max_sum))
#print(max_sum)