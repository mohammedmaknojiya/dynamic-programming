#here we have given set of coins and the target value
#we have to find no of ways by which we can acheive target value
#means if array is [1,2,3] and target value is 5
#then we can form 5 by
#  2,3    1,1,1,1,1     1,2,2    1,3,1    2,1,1,1
#means answer is 5


#we require code of unbounded knapsack only
#but remeber one thing
#whenever there is question where they ask for total no of possible ways
#at that time replace max and OR with + sign
#because here we have to find count of all ways which are possible

def unbounded_knapsack(array,target_val):
    t=target_val
    arr=array 
    n=len(array)

    table=[]

    for i in range(n+1):
        rows=[]
        for j in range(t+1):
            rows.append(0)
        table.append(rows)

    print(table)
    
    #initialization have some changes as compare to unbounded knapsack
    for i in range(t+1):
        table[0][i]=0
    for j in range(n+1):
        table[j][0]=1

    
    
    for i in range(1,n+1):
        for j in range(1,t+1):
           
            if arr[i-1] > j:
                table[i][j] = table[i-1][j]

            elif arr[i-1] <= j:
                table[i][j] = table[i][j-arr[i-1]] + table[i-1][j]

    print(table)        
    return table[n][t]
    
array= [1,2,3]

target_val = 5

no_of_ways = unbounded_knapsack(array ,target_val)
print(no_of_ways)
