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




array=[1,3,5,8]
range_of_array=int(sum(array))
possible_ele=[]#these are the ele which can be made from given array

for i in range(range_of_array):
    #if subset which sum is equal to target val is possible then append
    #else discard
    if subset_sum_problem(array,i,len(array)):
        possible_ele.append(i)
import math
h=math.ceil(len(possible_ele)/2)
#we do this because after half way range-2s1 comes -ve val which is similar to +ve val
#and we want +ve min val

half_of_possible_ele=possible_ele[: h]

min_subset_val_array=[]
for i in half_of_possible_ele:
    min_subset_val_array.append(range_of_array-2*i)
    

min_val=min(min_subset_val_array)
print(min_val)

# find s1 and s2 such that s1-s2 or s2-s1 is min
#range=sum(array ele)
#min_diff=s2-s1
#range=s1+s2
#hence s2=range-s1
#hence min_diff=range-s1-s1=range-2s1
#min_diff=range-2s1




