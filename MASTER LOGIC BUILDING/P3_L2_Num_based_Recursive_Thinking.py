# # # 1. Count the number of digits in a number recursively. 
# # def cnt(n):
# #     return len(str(n))
# # n = input("NUM: ")
# # print(cnt(n))
# ## --- OR--- recursive ##


# #     if n == 0:
# #         return 0
# #     return 1+cnt(n//10)
# # n = input("NUM: ")
# # print(cnt(n))

# # # 2. Reverse a number recursively  
# def revNum(n, rev=0):
#     if n == 0:
#         return rev
#     return revNum(n//10, rev*10+n%10)
  
# n = int(input("NUM: "))
# print(revNum(n))

# # 3. Check if a number is a palindrome using recursion. 
# def revNum(n, rev=0):
#     if n==0:
#         return rev
#     return revNum(n//10, rev*10 + n%10)
# def palindrome(n):
#     return n == revNum(n)
# n = int(input("NUM: "))
# print(palindrome(n))

# # 4. Find the product of the digits of a number recursively. 
# def prod(n):
#     if n == 0:
#         return 1
#     return  (n%10) * prod(n//10)
# n = int(input("NUM: "))
# print(prod(n))

# # 5. Find the GCD (HCF) of two numbers using Euclid’s algorithm recursively.
# import math
# def gcd(a,b):
#     return math.gcd(a,b)
# a = int(input("NUM: "))
# b = int(input("NUM: "))
# print(gcd(a,b))

# # 6. Convert a number to binary    
# def bin(n):
#     b = ""
#     if n == 0:
#         return n
#     else:
#         while n > 0:
#             rem = n%2
#             b = str(rem) + b
#             n =n//2
#         return b
# n = int(input("NUM: "))
# print(bin(n))    

# # 6. Convert a number to binary recursively. 
# def bin(n):
#     if n==0:
#         return ""
#     return bin(n//2) + str(n%2)
# n = int(input("NUM: "))
# print(bin(n))

# # 6. Convert a number to binary(BUILT-IN)
# def binary(n):
#     return bin(n)
# n = int(input("NUM: "))
# print(binary(n))

# 7. Print digits of a number in words recursively (e.g., 123 → “one two three”).
# def read(n):
#     word= ["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
#     res = ""
#     for i in n:
#         res +=  word[int(i)] + " "
#     return res
# n = input("NUM: ")
# print(read(n))

# def read(n):
#     word= ["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
#     if n =="":
#         return ""
#     return word[int(n[0])] + " " +read(n[1:])
# n = input("NUM: ")
# print(read(n))
        
## 8. Calculate the sum of the first n even numbers recursively. 
# def even(n):
#     if n == 0:
#         return 0
#     return 2*n + even(n-1)
# n = int(input("NUM: "))
# print(even(n))

# 9. Calculate the sum of the first n odd numbers recursively.
def odd(n):
    if n == 0:
        return 0
    return (2*n -1)+ odd(n-1)
n = int(input("NUM: "))
print(odd(n))
 

# 10. Find nCr (Combination formula) recursively using Pascal’s relation.
