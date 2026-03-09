# 1. Print the squares of numbers from 1 to n. 
def squaresNum(n):
    l = []
    for i in range(1, n+1):
        sq = i*i
        l.append(sq)
    return l
n = int(input("NUM: "))
print(squaresNum(n))
    
# 2. Print cubes of numbers from 1 to n. 
def CubeNum(n):
    l = []
    for i in range(1, n+1):
        cube = i*i*i # i*3
        l.append(cube)
    return l
n = int(input("NUM: "))
print(CubeNum(n))

# 3. Print all numbers between a and b divisible by 7. 
def numbers(a, b):
    divs = []
    for i in range(a, b+1):
        if  i%7 == 0:
            divs.append(i)    
    return divs
a = int(input("NUM: "))
b = int(input("NUM: "))
print(numbers(a,b))

# 4. Find HCF (GCD) of two numbers using loops. 
def hcf(a,b):
    h = 1
    for i in range(1,min(a,b)+1):
        if a%i == 0 and b%i==0:
            h = i
    return h
a = int(input("NUM: "))
b = int(input("NUM: "))
print(hcf(a,b))

#     while b!=0:
#         a, b = b,a%b
#     return a
# a = int(input("NUM: "))
# b = int(input("NUM: "))
# print(hcf(a,b))

# 5. Find LCM of two numbers using loops. 
def hcf(a,b):
    h = 1
    for i in range(1,min(a,b)+1):
        if a%i == 0 and b%i==0:
            h = i
    return h
def lcm(a,b):
    return (a*b) // hcf(a,b)
    
a = int(input("NUM: "))
b = int(input("NUM: "))
print(lcm(a,b))
    
# 6. Print all factors of a given number. 
def factors(n):
    f = []
    for i in range(1, n+1):
        if n%i == 0:
            f.append(i)
    return f
n = int(input("NUM: "))
print(factors(n))

# 7. Find the sum of all factors of a number. 
def Sum_factors(n):
    f = []
    for i in range(1, n+1):
        if n%i == 0:
            f.append(i)
    return sum(f)
n = int(input("NUM: "))
print(Sum_factors(n))

# 8. Check if a number is a strong number (sum of factorials of digits = number).
#GFG: https://www.geeksforgeeks.org/problems/strong-numbers4336/1
def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *=i
    return fact
def strong(n):
    ori = n
    total = 0
    while ori > 0:
        dig = ori%10
        total += fact(dig)
        ori = ori//10
    if total == n:
        return True
    else:
        return False
 
n = int(input("NUM: "))
print(strong(n))
# 9. Print first n terms of an arithmetic progression (a, d). 
# 10. Print first n terms of a geometric progression (a, r). 
