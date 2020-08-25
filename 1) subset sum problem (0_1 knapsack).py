#check whether any subset present in the given array with the given target sum

#it is similar to 0/1 knapsack

#here our array look like weight array

#target sum value looks like capacity of the knapsack

# if any subset present in the array then we return True else False



def knapsack(weight_array,max_capacity,length_of_array):
    w_a=weight_array # 1kg  3kg  4kg  it is nothing but how much kg item is available
    #nothing but value present inside the array
    
    #v_a=value_array  # it is nothing but profit 10rs 30rs 50rs so on
    
    W=max_capacity  #capacity of knapsack #nothing but target sum
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


      #if there is no ele present in list means weight is 0 no item is there
    #then it is not possible to make subset
    for j in range(W+1):
        table[0][j]=False
    

    #if there we want to find a sub set which has no val means weight=0
    #that sub set we can find at every stage means we simply just return True
    for i in range(n+1):
        table[i][0]=True

    #now initialization of rows is done
    for i in range(n+1):
        for j in range(W+1):

            #because in the table we are storing True and False hence we converd MAX
            #into OR
            #val array is not present hence we ignore it into the formula
                
            if w_a[i-1] <= j:
                table[i][j] = table[i-1][j-w_a[i-1]] or table[i-1][j] 
            elif w_a[i-1]> j:
                table[i][j]=table[i-1][j]

  

                
    print(table)            
    return table[n][W]
            
            


    

weight_array=[1,2,3]
#value_array=[10,15,40]
capcity_of_knapsack=5

s=knapsack(weight_array,capcity_of_knapsack,len(weight_array))
print(s)




