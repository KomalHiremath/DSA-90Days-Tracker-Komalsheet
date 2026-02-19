# Reverse String
# with slicing
# res = s[::-1]
# return res

# class Solution:
#     def revStr (self, s : str) -> str :
#         S= list(s)
#         l = 0
#         r = len(S)-1
#         while l < r:
#             S[l], S[r] =S[r], S[l]
#             l +=1
#             r -=1
#         return "".join(S)
    
# # ------ 1. PRIME CHECK (OPTIMIZED √N VERSION)  -----
# # ------ 1. PRINT PRIMES (VARIATION OF PRIME LOGIC) ----

# # def prime(num):
# #     if num<=1:
# #         return False
    
# #     for i in range(2, int(num**0.5)+1):
# #         if num%i == 0:
# #             return False
# #     return True
    
# # num = int(input("Enter the num: ")) 
# # print(prime(num))  

# # ---- 2. COUNT DIGITS ----------

# def count(n):
#     return(len(str(abs(n))))

# #     n = abs(n) 
# #     if n == 0:
# #         return 1
# #     count = 0
# #     while n > 0:
# #         count +=1
# #         n = n//10
# #     return count

# n = int(input("Enter the num: ")) 
# print(count(n))

# # --- 2. COUNT THE NUMBER OF DIGITS IN N THAT DIVIDE N EVENLY ------

# # Input: n = 2446 Output: 1
# # Explanation: Here among 2, 4, 6 only 2 divides 2446 evenly while 4 and 6 do not.

# # Input: n = 23  Output: 0
# # Explanation: 2 and 3, none of them divide 23 evenly.

# # Input: n = 12 Output: 2
# # Explanation: 1, 2 when both divide 12 leaves remainder 0.


# def evenlyDivides(self, n):
#     original = abs(n)
#     count = 0
    
#     while n > 0:
#         digit = n % 10
        
#         if digit != 0 and original % digit == 0:
#             count += 1
        
#         n //= 10
    
#     return count

# # --- 1. REVERSE NUMBER ----
# def reverseDigits(self, n):
#     rev = 0
       
#     while n > 0:
#         digit = n % 10
#         rev = rev * 10 + digit
#         n = n // 10

# #     return rev

# # --- 2. PALINDROME NUMBER ----
# def pal(n):
#     rev = 0
#     original = n
    
#     while n > 0:
#         digit = n % 10
#         rev = rev*10 + digit
#         n = n//10
#     return rev == original
# n = int(input("enter the num: "))
# if pal(n):
#     print("true")
# else:
#     print("False")
        
#  # --- 2. PALINDROME STRING ----       
# def pal(s):
#     return(s[::-1]) == s
# s =input("ENter the string: ")
# print(pal(s))

# # --- 3. SUM OF DIGITS ----
# def num(n):
#     if n == 0:
#         return 0
#     last = n % 10
#     rem = n // 10
#     return last + num(rem)
    
# n = int(input("NUm : "))
# print(num(n))

# # --- 4. GCD (EUCLIDEAN METHOD) ----
# def gcd(a,b):
#     while b!= 0:
#         a, b = b , a%b
#     return a
# a = int(input("NUm : "))
# b = int(input("NUm : "))
# print(gcd(a, b))

###### OR ###########

# import math
# a = int(input("Num : "))
# b = int(input("NUm : "))
# print(math.gcd(a,b))

#  # --- 5. LCM ----
# def gcd(a,b):
#     while b!= 0:
#         a, b = b , a%b
#     return a
# def lcm(a,b):
#     return (a*b) // gcd(a,b)
# a = int(input("Num : "))
# b = int(input("NUm : "))
# print(lcm(a,b))
 
# # --- 6. FIBONACCI (LOOP VERSION) ---

# n = int(input("NUm : "))
# a = 0
# b = 1
# c = 0
# for i in range( n):
#     print(c)
#     a = b
#     b =c
#     c = a+b

# # --- 7. SUM OF FIBONACCI (LOOP VERSION)  ----
# n = int(input("Num: "))
# a = 0 
# b = 1
# c = 0
# total = 0
# for i in range(n):
#     print(c)
#     total +=c
    
#     a = b 
#     b = c 
#     c = a+b 
# print("sum: ", total)

# # --- 6. FIBONACCI (Recursion)------------
# def fib(n):
#     if n <= 1: return n
#     return fib(n-2) +fib(n-1)

# # --- 7. SUM OF FIBONACCI  (Recursion)----
# def fib(n):
#     if n <=1:
#         return n
#     return fib(n-1)+fib(n-2)
# def sum_fib(n):
#     if n == 0:
#         return 0
#     return fib(n) + sum_fib(n-1)
# n = int(input("Enter the num: "))
# print(sum_fib(n))
 

# # --- 8. PRINT PRIMES IN RANGE ----
# def prime(start, end):
#     primes = []
#     for num in range(start, end+1):
#         if num > 1:
#             for i in range(2, int(num**0.5)+1):
#                 if num% i == 0:
#                     break
#             else:
#                 primes.append(num)
#     return primes
            
                    
# print(prime(10, 20))

# --- 9. PRINT FACTORS ----
# --- 10. PERFECT NUMBER ---
# # --- 11. ARMSTRONG NUMBER ----
# def arm(n):
#     original = n
#     total = 0
#     power = len(str(n))
#     while n > 0:
#         dig = n % 10
#         total += dig**power
#         n = n// 10
#     return total == original
# print(arm(15))

# --13. MISSING ELEMENT IN ARRAY -- 
# def miss(arr):
#     n = len(arr) + 1
    
#     xor_all = 0
#     xor_given = 0
    
#     # XOR of all 1 to n
#     for i in range(1, n+1):
#         xor_all = xor_all ^ i
        
#     # XOR of missing elem in arr
#     for num in arr:
#         xor_given = xor_given ^ num
#     return xor_all ^ xor_given
# print(miss([1, 2,3,5]))

def miss(arr):
    n = len(arr)+1
    ori = n * (n+1) // 2
    missing = sum(arr)
    return ori - missing
print(miss([1,2,3,5]))

        
    
# --- 12. TWO SUM (O(N) HASHMAP) ----
# --- 13. FREQUENCY COUNT USING DICTIONARY ----
# --- 14. TOP K FREQUENT (BASIC VERSION) ----
# --- 15. SUB ARRAY SUM = K (PREFIX SUM IDEA) ----

# --- 10. Count num of vowels ----
# vowels = ['a', 'e', 'i', 'o', 'u']
# word = input("Enter any word: ")
# count = 0
# for i in range(len(word)):
#     if word[i] in vowels:
#         count += 1
# if count == 0:
#     print("no vowels")
# else:
#     print("Num of vowels:", count)

# --- 16. STRING PALINDROME ----
# --- 17. REVERSE WORDS ----
# --- 18. CHARACTER FREQUENCY ----
# --- 19. BASIC SLIDING WINDOW (MAX SUM SUB ARRAY) ----
