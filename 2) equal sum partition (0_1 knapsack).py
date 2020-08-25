#here we have to find whether we can find two subset with equal sum from
#the given matrix

#suppose matrix is given as [1,11,5,5] then we can find two subset s1 and s2

#with the sum 11 and 11

#if element at 0 index is involved in subset s1 then it should not involved in
#subset s2
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

    #print(table)

    for i in range(s+1):
        table[0][i]=False

    #print(table)

    for j in range(n+1):
        table[j][0]=True
    #print(table)

    #now we start indexing from 1 because we we have already set values
    for i in range(1,n+1):
        for j in range(1,s+1):

            if arr[i-1]>j:
                table[i][j]=table[i-1][j]
            elif arr[i-1]<=j:
                table[i][j]= table[i-1][j-arr[i-1]] or table[i-1][j]
    #print(table)           
    return table[n][s]    




#now if we consider two subset with equal sum means s1=s2 4
# then  s=s1=s2

# S = s+s = 2s

#hence it is possible to divide two subset in equal sum only if the whole sum of
#the main set is even
#means [1,11,5,5] it should be even totally 

# the whole sum of the set is 22 here
#hence it is possible to divide set into two equal subset

#now we check sum%2==0 if not then we return can not be possible to divide
#else sum%2==0 then  we take half of it subset=sum/2
#now we check whether subset(11) is present in the set or not
#if one subset is present then second subset is automatically present


def subset_partition(array):
    array=array
    sum_of_ele=sum(array) #sum of all element

    if sum_of_ele % 2 != 0:
        return False #means we can not form partition
    
    elif sum_of_ele % 2 == 0:

        subset = int(sum_of_ele/2)

        status=subset_sum_problem(array,subset,len(array))

        return status

array=[1,5,11]
s=subset_partition(array)
print(s)
        
    
        
        






