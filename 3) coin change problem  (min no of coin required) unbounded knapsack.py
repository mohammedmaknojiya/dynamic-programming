#here we have to find min no of coins required to make a target val
#this problem is diff from previous one
#in previous we have to calculate no of ways to acheive target val
#but here we have to find min no of coins required to acheive target val


#NOTE
#here is a some changes in the initialization part
#here we intially consider that to make any target val we require infinite no
#of coins
#but while calculating if we come across some value which  is less than infinite
#val then  we consider that val is min no of coins


#means basically we intialize first row with ( infinite - 1 )
# to understand this we can take example
##    0       1       2        3       4      5
##0  inf-1  inf-1   inf-1   inf-1    inf-1  inf-1
##1   0
##2   0
##3   0
##means if we have 0 coins in our array {} means we have null array
##then if we want to make val 0 then we required infinite no of coins to acheive
##this . same for 1 that if we want to make 1 then we required infinite no of
##coins to acheived that if our set is null
##
##now we want target val to be 0 and we have 1 coin inside it which is [1]
##then we have to select 0 no of coin to acheive target val
##
##now if we have 2 coin inside the bag which are [1,2] and we have to make target
##val 0 then how many coin we have to choose? answer is 0 no of coin
##
##now if we have 3 coin inside the bag which are [1,2,3] and we have to make target
##val 0 then how many coin we have to choose? answer is 0 no of coin
##
##inf-1 the reason behind taking -1 is that we are going to do 1+table[][]
##in our code at that time we need this
##because (1 + inf - 1 = inf)
##so if we does not take -1 then it will become 1+inf
##NOTE here inf means max value of int which is INT_MAX
##so if we add 1 in INT_MAX then it become out of range and produces negative value
##so to avoid that we do this
import sys
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
    
    for j in range(n+1):
        table[j][0]=0
    for i in range(t+1):
        table[0][i]=sys.maxsize-1

    #intializing second row also
    for i in range(1,t+1):
        if i%arr[0]==0:
            table[1][i]=int(i/arr[0])
        else:
            table[1][i]=sys.maxsize-1
    print("second time",table)
    for i in range(2,n+1):
        for j in range(1,t+1):
           
            if arr[i-1] > j:
                table[i][j] = table[i-1][j]

            elif arr[i-1] <= j:
                table[i][j] = min(1+table[i][j-arr[i-1]] , table[i-1][j])

    print(table)        
    return table[n][t]
    
array= [1,2,3]

target_val = 5

min_no_of_ways = unbounded_knapsack(array ,target_val)
print(min_no_of_ways)

































