#suppose hamara pass ek array hai [1,2,5,3,4]
#or ham ko find karna hai aisa kitna subset hai jinka sum 5 ho
#idhar hamko allow hai ele ko repeat karna ka

#ham idhar subset sum problem ka hi use kara ga
#but initialization me False ko 0 sa end True ko 1 sa start karega
#kyuki hamko no of count return karna hai
#or hamlog OR ko plus sa replace kardega



def count_subset_problem(array_of_val,target_sum,len_of_array):

    arr=array_of_val
    s=target_sum
    n=len_of_array

    table=[]

    for i in range(n+1):
        rows=[]
        for j in range(s+1):
            rows.append(0)

        table.append(rows)

    print(table)

    for i in range(s+1):
        table[0][i]=0

    print(table)

    for j in range(n+1):
        table[j][0]=1
    print(table)

    #now we start indexing from 1 because we we have already set values
    for i in range(1,n+1):
        for j in range(1,s+1):

            if arr[i-1]>j:
                table[i][j]=table[i-1][j]
            elif arr[i-1]<=j:
                table[i][j]= table[i-1][j-arr[i-1]] + table[i-1][j]
    print(table)           
    return table[n][s]    



        
    
array=[1,2,2]
s=3
count=count_subset_problem(array,s,len(array))
print(count)
