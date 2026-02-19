### FUNCTION ####################################################################################################
# AVerage of 3 numbers using function

def cal_avg(a, b, c):
    avg =(a+b+c)/3
    print(avg)
cal_avg(111, 278, 3567)

def prod(a=1,b= 8):
    print(a*b)  
    return a *b   
prod(8)

###   RECURSION ######################################

def show(n):
    # BASE CASE
    if n==0:
        return 
    print(n, end = " ")
    show(n-1) # Recursive call  
show(5) # 5 4 3 2 1

## factorial#############
def fact(n):
    if n==0 or n==1:
        return 1
    return fact(n-1)*n
print(fact(5))

