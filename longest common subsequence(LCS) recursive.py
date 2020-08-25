
def lcs(x,y,n,m):
    #base case
    if m==0 or n==0:
        return 0
    elif x[n-1]==y[m-1]:
        return 1+lcs(x,y,n-1,m-1) #1+search in remaining string
    elif x[n-1]!=y[m-1]:
        return max( lcs(x,y,n-1,m) , lcs(x,y,n,m-1) )
    

x="abcdfg"
y="abfce"

len_of_common_seq=lcs(x,y,len(x),len(y))
print(len_of_common_seq)

#here we have to find longest common sub sequence
#the diff bet sub_string and sub sequence is that here in sub sequence it should not be continuous
#but in sub string it should be continuous

#base case
#when any one of the string has len 0 then we return 0 means common string len is 0 and it is not present
# eg x="abcd" y="" then because y==0 hence return 0

##second condition
# here we check last char of both the string
#if they get match then we add 1 and search other common strings in remaining part

#third condition
#here if we do not find last char equal in both the strings then we have two choices
# 1) reduce the len of first string and second string as it is
# 2) or reduce the len of second string and first string as it is

# we try both of them and return max one out of them

#we have not added 1 in seocnd condition with lcs because we have not founded common in them
