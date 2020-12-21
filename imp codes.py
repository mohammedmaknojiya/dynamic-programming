############################## CHECK PRIME OR NOT #######################
### check whether number is prime or not
###it returns true if number is prime else false


##Prime numbers:

##A prime number is a natural number greater than 1 and having no positive
##divisor other than 1 and itself.

# 1 (one) is neither prime nor composite hence number should be greater than 1
# we start dividing num with 2 beacause all number get divisible by 1 and it returns True always
# IF NUM IS PRIME THEN IT IS ONLY DIVISIBLE BY 1 AND SELF
# IF ANY OTHER NUMBER CAN DIVIDE IT THEN OUR NUMBER IS NOT PRIME


def check_prime(number):
    num=number
    if num > 1:
        for i in range(2,num):
            if( num%i ) == 0:
                return False
            #means our number get divided with another number other than 1 and self
            
        return True
        #means num is divisible by self only

    else:
        return False
        #because number is less than 1

#driver code

status=check_prime(4)
print(status)

################################# CHECK PRIME OR NOT #######################


################## FIND PRIME NUMBER BETWEEN GIVEN RANGE ####################

def find_prime_in_range(start,end):
    number1=start
    number2=end
    #list of prime numbers in the given range
    final_prime_list=[]

    #we add number2+1 because we also want to check is number2 is prime or not
    
    for i in range(number1,number2+1):
        #we call check prime function here
        status=check_prime(i)
        #if it returns True then we append it
        #else we ignore
        if status==True:
            final_prime_list.append(i)

    #at the end we return our list 
    return final_prime_list


#driver code

list_of_num = find_prime_in_range(2,11)
print(list_of_num)

################## FIND PRIME NUMBER BETWEEN GIVEN RANGE ####################

#################### PRINT N FIBONACCI NUMBERS ##########################
def fibonacci(number):
    count=number
    first=0
    second=1
    list_of_fibo=[]
    if count>0:
        #if only one number
        if count==1:
            list_of_fibo.append(first)
            return list_of_fibo
        
        #if first 2 numbers
        elif count==2:
            list_of_fibo.append(first)
            list_of_fibo.append(second)
            return list_of_fibo

        #if more than 2 numbers
        elif count>2:
            list_of_fibo.append(first)
            list_of_fibo.append(second)

            for i in range(count-2):
                c=first+second
                list_of_fibo.append(c)
                first=second
                second=c
                
            return list_of_fibo

#driver code
list_of_fibo=fibonacci(2)
print(list_of_fibo)



#################### PRINT N FIBONACCI NUMBERS ##########################
  


##################### PRINT N FIBONACCI NUMBERS WITH FIRST ELEMNET = 5 AND
####################   SECOND ELEMENT = 6 ##################################

def fibonacci(count,first,second):
    count=count
    first=first
    second=second
    list_of_fibo=[]
    if count>0:
        #if only one number
        if count==1:
            list_of_fibo.append(first)
            return list_of_fibo
        
        #if first 2 numbers
        elif count==2:
            list_of_fibo.append(first)
            list_of_fibo.append(second)
            return list_of_fibo

        #if more than 2 numbers
        elif count>2:
            list_of_fibo.append(first)
            list_of_fibo.append(second)

            for i in range(count-2):
                c=first+second
                list_of_fibo.append(c)
                first=second
                second=c
                
            return list_of_fibo

#driver code
list_of_fibo=fibonacci(2,2,3)
print(list_of_fibo)



##################### PRINT N FIBONACCI NUMBERS WITH FIRST ELEMNET = 5 AND
####################   SECOND ELEMENT = 6 ###############################














