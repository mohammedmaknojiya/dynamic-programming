#means here we have given one array and target difference value

#now we have to find s1 and s2 which satisfies the given diff
#and we have to return no of subset which satisfies this
# array=[1,1,2,3] diff=1
#   diff = s1-s2
# now   total = s1 + s2 
#so there are 2 equations
# diff = s1 - s2
# total = s1 + s2
#---------------------  add both
#  diff + total = 2s1
#hence s1 = (diff + total)/2

#hence s1 = ( 1 + 7 )/2 =4

# now after applying these all formulas problem reduces to finding subset s1
#with val 4
# now we have to just return count of s1


def subset_diff_count(array_of_val,target_sum,len_of_array):

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

array=[1,1,2,3]
diff=2

total = int(sum(array))

s1=int((diff+total)/2)

count=subset_diff_count(array,s1,len(array))
print(count)
