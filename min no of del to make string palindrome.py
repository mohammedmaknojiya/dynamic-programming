def reverse(string): 
    string = "".join(reversed(string)) 
    return string 

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

def palindromic_seq(x):
    y=reverse(x)
    
    
    len_of_longest_palindromic_seq = lcs( x ,y ,len(x) ,len(y) )
    return len_of_longest_palindromic_seq
    

x="agbcba"
len_of_longest_palindromic_seq = palindromic_seq(x)

min_no_of_del = len(x) - len_of_longest_palindromic_seq

print(min_no_of_del)
