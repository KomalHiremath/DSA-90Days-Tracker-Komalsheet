# Reverse String
res = s[::-1]
return res

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

# Palindrome

# Frequency Count

# Prime Check

# Fibonacci

# Two Sum

# Top K Frequent Words

# Subarray Sum = K

# Sliding Window / Log Simulation

# String Transformation