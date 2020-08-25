
def subset_sum_problem(array_of_val,target_sum,len_of_array):

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
        table[0][i]=False

    print(table)

    for j in range(n+1):
        table[j][0]=True
    print(table)

    #now we start indexing from 1 because we we have already set values
    for i in range(1,n+1):
        for j in range(1,s+1):

            if arr[i-1]>j:
                table[i][j]=table[i-1][j]
            elif arr[i-1]<=j:
                table[i][j]= table[i-1][j-arr[i-1]] or table[i-1][j]
    print(table)           
    return table[n][s]    



        
    
array=[1,2,3]
s=3
status=subset_sum_problem(array,s,len(array))
print(status)
