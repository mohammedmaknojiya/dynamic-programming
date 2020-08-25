
def longest_substring(x,y,n,m):

    #make table
    table=[]
    for i in range(n+1):
        rows=[]
        for j in range(m+1):
            rows.append(0)
        table.append(rows)
    length=0
    for i in range(n+1):
        for j in range(m+1):
        #base case
            if i==0 or j==0:
                table[i][j]=0
            
            elif x[i-1]==y[j-1]:
                table[i][j]= 1+table[i-1][j-1]#1+previous
                length= max(length , table[i][j]) #above calculated table[i][j]
            elif x[i-1]!=y[j-1]:
                table[i][j] = 0
    print(table)    
    return length  

x="abcdfe"
y="abcde"

len_of_common_seq=longest_substring(x,y,len(x),len(y))
print(len_of_common_seq)

#elif x[i-1]!=y[j-1]:
#    table[i][j] = max( table[i-1][j] , table[i][j-1] )
##in lcs this statement was there but in longest common sub STRING we wont allow
##discontinuation . So thats why we assing 0 len means we initialize length again
##if condition is false
