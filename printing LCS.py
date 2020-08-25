
def print_lcs(x,y,n,m):

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
    #return table[n][m]
    #now start from back and traverse untill we reach first col or first row
    i=n
    j=m
    string=""
    while( i>0 and j>0 ):
        if table[i-1]==table[j-1]:
            string=string+x[i-1]
            i-=1
            j-=1
        elif table[i-1]!=table[j-1]:
            if table[i-1][j] > table [i][j-1] :
                i-=1
            elif table[i-1][j] < table [i][j-1] :
                j-=1
            
    return string

x="abcdfe"
y="abe"

s=list(reversed(print_lcs(x,y,len(x),len(y))))

st=""
for i in range(len(s)):
    st=st+s[i]

print(st)
    

