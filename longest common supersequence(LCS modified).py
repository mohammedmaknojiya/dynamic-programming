
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



def super_sequence(x,y):
    
    len_of_super_sequence=len(x)+len(y)-lcs(x,y,len(x),len(y))
    return len_of_super_sequence




x="aggtab"
y="gxtxayb"

len_of_super_sequence=super_sequence(x,y)
print(len_of_super_sequence)
