# Reverse String
# with slicing
# res = s[::-1]
# return res

class Solution:
    def revStr (self, s : str) -> str :
        S= list(s)
        l = 0
        r = len(S)-1
        while l < r:
            S[l], S[r] =S[r], S[l]
            l +=1
            r -=1
        return "".join(S)

# Count digits

# Reverse a number

# Palindrome number

# Sum of digits

# Check prime

# Print primes (variation of prime logic)
def prime(num):
    if num<=1:
        return False
    
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True
    
num = int(input("Enter the num: ")) 
print(prime(num))  

        
    

# Print Fibonacci

# Sum of Fibonacci

# GCD

# LCM

# Palindrome

# Frequency Count

# Prime Check

# Fibonacci

# Two Sum

# Top K Frequent Words

# Subarray Sum = K

# Sliding Window / Log Simulation

# String Transformation