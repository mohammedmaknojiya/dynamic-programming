#here we have to return no of insertion and deletion
#integer values



#here 2 string x and y are given
#to convert them from x to y we first remove h and then p means 2 del
#then we insert p at the begining means 1 insert


def lcs(x,y,n,m):

    #make table
    table=[]
    for i in range(n+1):
        rows=[]
        for j in range(m+1):
            rows.append(0)
        table.append(rows)
    
    for i in range(n+1):
        for j in range(m+1):
        #base case
            if i==0 or j==0:
                table[i][j]=0
            
            elif x[i-1]==y[j-1]:
                table[i][j]= 1+table[i-1][j-1]#1+previous 
            elif x[i-1]!=y[j-1]:
                table[i][j] = max( table[i-1][j] , table[i][j-1] )
    return table[n][m]  

def min_ins_del(x,y):
    

    len_of_lcs=lcs(x,y,len(x),len(y))

    delete=len(x) - len_of_lcs
    insert=len(y) - len_of_lcs  
    
    
    return insert,delete

x="heap"
y="pea"
insert,delete=min_ins_del(x,y)
print("insert {} delete {}".format(insert,delete))

