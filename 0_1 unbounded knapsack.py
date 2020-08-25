#unbounded knapsack is where we can have infinte supply for each ele
#we can retake any element many times

def unbounded_knapsack(weight_array,value__array,capacity):
    c=capacity
    w_arr=weight_array
    v_arr=value_array
    n=len(weight_array)

    table=[]

    for i in range(n+1):
        rows=[]
        for j in range(c+1):
            rows.append(0)
        table.append(rows)

    print(table)
    
    #initialization
    for i in range(c+1):
        table[0][i]=0
    for j in range(n+1):
        table[j][0]=0

    
    
    for i in range(1,n+1):
        for j in range(1,c+1):
            if i==0 or j==0:
                table[i][j]=0


            elif w_arr[i-1] > j:
                table[i][j] = table[i-1][j]

            elif w_arr[i-1] <= j:
                table[i][j] = max(v_arr[i-1] + table[i][j-w_arr[i-1]] ,table[i-1][j])

            
    return table[n][c]
    

weight_array= [1,3,2,4] #kg
value_array= [10,20,30,40] #rupees

capacity = 7 #kg

max_profit = unbounded_knapsack(weight_array, value_array ,capacity)
print(max_profit)
