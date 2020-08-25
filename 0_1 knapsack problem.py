# 0/1 knapsack problem

# choose items such that profit is max

# solve using top down approach matrix

def knapsack(weight_array,value_array,max_capacity,length_of_array):
    w_a=weight_array # 1kg  3kg  4kg  it is nothing but how much kg item is available
    v_a=value_array  # it is nothing but profit 10rs 30rs 50rs so on
    W=max_capacity  #capacity of knapsack
    n=length_of_array #length f weight array


    table=[]
    #i represent no of items in the list of weights
    #j represent weights in the list
    

    for i in range(n+1):
        rows=[]
        for j in range(W+1):
            rows.append(0)
        table.append(rows)
    print("intial table",table)        
    
    #now initialization of rows is done
    for i in range(n+1):
        for j in range(W+1):

            #if there is no ele present in list means weight is 0 no item is there
            #then {} profit is also 0 hence intialize 0 col and 0 row with 0
            if i==0 or j==0:
                table[i][j]=0

            elif w_a[i-1] <= j:
                table[i][j] =max( v_a[i-1] + table[i-1][j-w_a[i-1]] , table[i-1][j] )
            else:
                table[i][j]=table[i-1][j]

  

                
    print(table)            
    return table[n][W]
            
            


    

weight_array=[1,2,3]
value_array=[10,15,40]
capcity_of_knapsack=6

s=knapsack(weight_array,value_array,capcity_of_knapsack,len(weight_array))
print(s)




