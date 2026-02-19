# 1. Print numbers from 1 to n using recursion. 
def rec(n):
    if n ==0:
        return "Invalid"
    
    # print(n) -> 5 4 3 2 1
    rec(n-1)
    print(n) # 1 2 3 4 5
num = int(input("enter the num:"))
rec(num)

# 2. Print numbers from n down to 1 using recursion. 
def rec(n):
    if n ==0:
        return
    
    print(n)
    rec(n-1)
    
num = int(input("Enter the num"))
rec(num)


# 3. Print only even numbers from 1 to n recursively. 
def even(n):
    if n == 0:
        return 
    even(n-1)
    if n%2 == 0:
        print(n)
num =  int(input("Enter the num"))
even(num)

# 4. Print only odd numbers from 1 to n recursively. 
def odd(n):
    if n == 0:
        return
    odd(n-1)
    if n%2 != 0:
        print(n)
        
num =  int(input("Enter the num"))
odd(num)

# 5. Print sum of first n natural numbers recursively. 
def first(n):
    if n == 0:
        return 0
    
    sum = n + first(n-1)
    print(sum)
    return sum

num =  int(input("Enter the num"))
first(num)

# 6. Print factorial of a number recursively. 
def fact(n):
    if n < 0:
        return "INVALID"
    if n ==0 or n ==1:
        return 1
    
    return n * fact(n-1)
num =  int(input("Enter the num"))
print(fact(num))

# # 7. Calculate power of a number (xⁿ) using recursion. 
# # 8. Find nth Fibonacci number recursively. 
# # 9. Print Fibonacci series up to n terms recursively. 
# 10. Find sum of digits of a number recursively.

def rec(digit):
    if digit == 0:
        return 0
    last = digit % 10
    remaining = digit // 10
    return last + rec(remaining)


digit=  int(input("Enter the num"))
print(rec(digit))   


    

