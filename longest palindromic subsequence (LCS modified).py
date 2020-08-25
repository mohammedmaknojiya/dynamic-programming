#here we have given one string
#we have to del some ele from that such that string remain is palindromic in
#nature
#so for that we take one example and we we solve that using LCS
#example is x="agbcba"
#initially this string is not palindrome
#but when we delete g it becomes palindrome
# x="agbcba" reverse of that is y="abcbga"
#now we find lcs of both which will come as lcs = "abcba" which is palindrome
#in nature
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
print(len_of_longest_palindromic_seq)





