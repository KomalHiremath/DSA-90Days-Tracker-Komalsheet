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
    
# ------ 1. PRIME CHECK (OPTIMIZED √N VERSION)  -----
# ------ 1. PRINT PRIMES (VARIATION OF PRIME LOGIC) ----

# def prime(num):
#     if num<=1:
#         return False
    
#     for i in range(2, int(num**0.5)+1):
#         if num%i == 0:
#             return False
#     return True
    
# num = int(input("Enter the num: ")) 
# print(prime(num))  

# ---- 2. COUNT DIGITS ----------

def count(n):
    return(len(str(abs(n))))

#     n = abs(n) 
#     if n == 0:
#         return 1
#     count = 0
#     while n > 0:
#         count +=1
#         n = n//10
#     return count

n = int(input("Enter the num: ")) 
print(count(n))

# --- 2. COUNT THE NUMBER OF DIGITS IN N THAT DIVIDE N EVENLY ------

# Input: n = 2446 Output: 1
# Explanation: Here among 2, 4, 6 only 2 divides 2446 evenly while 4 and 6 do not.

# Input: n = 23  Output: 0
# Explanation: 2 and 3, none of them divide 23 evenly.

# Input: n = 12 Output: 2
# Explanation: 1, 2 when both divide 12 leaves remainder 0.



def evenlyDivides(self, n):
    original = abs(n)
    count = 0
    
    while n > 0:
        digit = n % 10
        
        if digit != 0 and original % digit == 0:
            count += 1
        
        n //= 10
    
    return count

# --- 1. REVERSE NUMBER ----
def reverseDigits(self, n):
    rev = 0
       
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    
    return rev

# --- 2. PALINDROME NUMBER ----
# --- 3. SUM OF DIGITS ----
# --- 4. GCD (EUCLIDEAN METHOD) ----
# --- 5. LCM ----
# --- 6. FIBONACCI (LOOP VERSION) ----
# --- 7. SUM OF FIBONACCI ----
# --- 8. PRINT PRIMES IN RANGE ----
# --- 9. PRINT FACTORS ----
# --- 10. PERFECT NUMBER ----
# --- 11. ARMSTRONG NUMBER ----

# --- 12. TWO SUM (O(N) HASHMAP) ----
# --- 13. FREQUENCY COUNT USING DICTIONARY ----
# --- 14. TOP K FREQUENT (BASIC VERSION) ----

# --- 15. SUBARRAY SUM = K (PREFIX SUM IDEA) ----

# --- 16. STRING PALINDROME ----
# --- 17. REVERSE WORDS ----
# --- 18. CHARACTER FREQUENCY ----
# --- 19. BASIC SLIDING WINDOW (MAX SUM SUBARRAY) ----
