#in this problem we have given one rod
#we have to cut this rod in such a way that profit is max
# we have given diff len array [1,2,3,4,5] in meters
# and associated profit with each len [10,30,15,20,35] rupees
#and hence total len of rod is 5 meter

#means it is similar to unbounded knapsack
#here weight array = len array
#and value array = profit array
# and capacity = total len of array

#means now if we cut rod into two parts 1 meter and 4 meter then if we sell it
#then profit is 10 rs + 20 rs =30 rs
#in this manner we have to cut the rod such that profit comes max
#this is nothing but similar problem as unbounded knapsack
#we can take one single len of rod as many time as we want

#unbounded knapsack is where we can have infinte supply for each ele
#we can retake any element many times

def unbounded_knapsack(lengths_of_rod,profit_associated,total_len_of_rod):
    c=total_len_of_rod
    w_arr=lengths_of_rod
    v_arr=profit_associated 
    n=len(lengths_of_rod )

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
    

#weight_array= [1,3,2,4] #kg
#value_array= [10,20,30,40] #rupees
len_of_rod=[1,3,2,4]# meter
profit_associated=[10,20,30,40] #rupees

total_len_of_rod = 7 #meter

max_profit = unbounded_knapsack(len_of_rod,profit_associated,total_len_of_rod)
print(max_profit)
