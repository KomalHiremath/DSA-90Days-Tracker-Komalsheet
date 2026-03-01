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
    
# # # num = int(input("Enter the num: ")) 
# # # print(prime(num))  

# # # ---- 2. COUNT DIGITS ----------

# # def count(n):
# #     return(len(str(abs(n))))

# # #     n = abs(n) 
# # #     if n == 0:
# # #         return 1
# # #     count = 0
# # #     while n > 0:
# # #         count +=1
# # #         n = n//10
# # #     return count

# # n = int(input("Enter the num: ")) 
# # print(count(n))

# # # --- 2. COUNT THE NUMBER OF DIGITS IN N THAT DIVIDE N EVENLY ------

# # # Input: n = 2446 Output: 1
# # # Explanation: Here among 2, 4, 6 only 2 divides 2446 evenly while 4 and 6 do not.

# # # Input: n = 23  Output: 0
# # # Explanation: 2 and 3, none of them divide 23 evenly.

# # # Input: n = 12 Output: 2
# # # Explanation: 1, 2 when both divide 12 leaves remainder 0.


# # def evenlyDivides(self, n):
# #     original = abs(n)
# #     count = 0
    
# #     while n > 0:
# #         digit = n % 10
        
# #         if digit != 0 and original % digit == 0:
# #             count += 1
        
# #         n //= 10
    
# #     return count

# # # --- 1. REVERSE NUMBER ----
# # def reverseDigits(self, n):
# #     rev = 0
       
# #     while n > 0:
# #         digit = n % 10
# #         rev = rev * 10 + digit
# #         n = n // 10

# # #     return rev

# # # --- 2. PALINDROME NUMBER ----
# # def pal(n):
# #     rev = 0
# #     original = n
    
# #     while n > 0:
# #         digit = n % 10
# #         rev = rev*10 + digit
# #         n = n//10
# #     return rev == original
# # n = int(input("enter the num: "))
# # if pal(n):
# #     print("true")
# # else:
# #     print("False")
        
# #  # --- 2. PALINDROME STRING ----       
# # def pal(s):
# #     return(s[::-1]) == s
# # s =input("ENter the string: ")
# # print(pal(s))

# # # --- 3. SUM OF DIGITS ----
# # def num(n):
# #     if n == 0:
# #         return 0
# #     last = n % 10
# #     rem = n // 10
# #     return last + num(rem)
    
# # n = int(input("NUm : "))
# # print(num(n))

# # # --- 4. GCD (EUCLIDEAN METHOD) ----
# # def gcd(a,b):
# #     while b!= 0:
# #         a, b = b , a%b
# #     return a
# # a = int(input("NUm : "))
# # b = int(input("NUm : "))
# # print(gcd(a, b))

# ###### OR ###########

# # import math
# # a = int(input("Num : "))
# # b = int(input("NUm : "))
# # print(math.gcd(a,b))

# #  # --- 5. LCM ----
# # def gcd(a,b):
# #     while b!= 0:
# #         a, b = b , a%b
# #     return a
# # def lcm(a,b):
# #     return (a*b) // gcd(a,b)
# # a = int(input("Num : "))
# # b = int(input("NUm : "))
# # print(lcm(a,b))
 
# # # --- 6. FIBONACCI (LOOP VERSION) ---

# # n = int(input("NUm : "))
# # a = 0
# # b = 1
# # c = 0
# # for i in range( n):
# #     print(c)
# #     a = b
# #     b =c
# #     c = a+b

# # # --- 7. SUM OF FIBONACCI (LOOP VERSION)  ----
# # n = int(input("Num: "))
# # a = 0 
# # b = 1
# # c = 0
# # total = 0
# # for i in range(n):
# #     print(c)
# #     total +=c
    
# #     a = b 
# #     b = c 
# #     c = a+b 
# # print("sum: ", total)

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
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for key in range(len(nums)):
            val = target - nums[key]

            if val in hash:
                return [hash[val], key]
            hash[nums[key]] = key
            
### brute force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

  
# --- 13. FREQUENCY COUNT  ----
def findFrequency(self, arr, x):
    t = tuple(arr)
    return t.count(x)

# --- 13. FREQUENCY COUNT USING DICTIONARY ----
def findFrequency(self, arr, x):
    freq = {}
    for elem in arr:
        if elem in freq:
            freq[elem] += 1 # {3:2}
        else:                   # or
            freq[elem] = 1 # {3:1}
                
        # if x in freq:
        #     return freq[x]
        # else:
        #     return 0
        
    # or
        return freq.get(x,0)
 
### ----  LC 540. SINGLE ELEMENT IN A SORTED ARRAY ------------
    
def singleNonDuplicate(self, nums):
    freq = {}

    for elem in nums:
        if elem in freq:
            freq[elem] += 1
        else:
            freq[elem] = 1

    for elem in freq:
        if freq[elem] == 1:
            return elem
        
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

# =========================
# HASHMAP (FREQUENCY PATTERN)
# =========================

# --- 14. TOP K FREQUENT (BASIC VERSION) ---
def topk(nums):
    freq = {}
    for elem in nums:
    # count freq of each elem
        if elem in freq:
            freq[elem] +=1
        else:
            freq[elem] = 1
            
        result = []
        for i in range(k): 
            max_freq = 0
            max_num = 0
            for elem in freq:
                if freq[elem] > max_freq:
                    max_freq=freq[elem]
                    max_elem=elem
            result.append(max_elem)
        
        del freq[max_elem]
    return result
    
# --- 15. FIRST NON-REPEATING CHARACTER ---
class Solution:
    def nonRepeatingChar(self,s):
        freq = {}
        
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
            
        for ch in s:
            if freq[ch] == 1:
                return ch 
        else:
            return "$"
                
# --- 16. CHARACTER FREQUENCY ---
class Solution:
    def charFrequency(self, s: str):
        freq = {}

        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        return freq
    
# --- 17. SUB ARRAY SUM EQUALS K ---
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_freq= {0:1}
        run_sum = 0
        result = 0

        for elem in nums:
            run_sum += elem
            prev = run_sum - k

            if prev in pre_freq:
                result = result+pre_freq[prev]

            if run_sum in pre_freq:
                pre_freq[run_sum] +=1
            else:
                pre_freq[run_sum] = 1
        return result


# =========================
# TWO POINTER PATTERN
# =========================

# --- 18. STRING PALINDROME ---
class Solution:
    def isPalindrome(self, s):
        return s[::-1] == s
    
# --- 19. REVERSE WORDS IN A STRING ---
class Solution:
    def reverseWords(self, s):
        words = s.split(".")
        
        clean = []
        for w in words:
            if w!="":
                clean.append(w)
        clean.reverse()
        return ".".join(clean)


# =========================
# SLIDING WINDOW (FIXED SIZE)
# =========================

# --- 20. MAXIMUM SUB ARRAY OF SIZE K ---


# --- 21. MAX Average SUB ARRAY ---
class Solution:
    def findMaxAverage(self, arr, n, k):
        curr = sum(arr[:k])
        max_sum = curr ## gives max sum among all sub arraay
        start_index = 0 # gives max sum sub array

        for i in range(1, n - k + 1):
            curr = curr - arr[i - 1] + arr[i + k - 1]

            if curr > max_sum:
                max_sum = curr
                start_index = i

        return start_index

# =========================
# SLIDING WINDOW (VARIABLE SIZE)
# =========================

# --- 22. LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS ---
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        left = 0 # index
        max_len = 0

        for right in range(len(s)):
            ch = s[right]
            if ch in freq:
                freq[ch] +=1
            else:
                freq[ch] =1

            while freq[ch] >1:
                left_char=s[left]
                freq[left_char] -=1
                left +=1
            max_len = max(max_len, right - left +1)
        return max_len


# --- 23. SMALLEST SUB ARRAY >= TARGET ---
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0                    # left pointer of window
        curr_sum = 0                # sum of current window
        min_len = float("inf")      # store minimum length found
        
        # Expand the window using right pointer
        for right in range(len(nums)):
            
            curr_sum += nums[right]     # add current element to window
            
            # Shrink window while condition is satisfied
            while curr_sum >= target:
                
                # Update minimum length
                min_len = min(min_len, right - left + 1)
                
                # Remove left element from window
                curr_sum -= nums[left]
                
                # Move left pointer forward
                left += 1
        
        # If no valid window found, return 0
        if min_len == float("inf"):
            return 0
        else:
            return min_len
# =========================
# KADANE / GREEDY PATTERN
# =========================

# --- 24. MAXIMUM SUB ARRAY ---
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        max_sum =nums[0]

        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)
        return max_sum
# --- 25. BEST TIME TO BUY AND SELL STOCK ---
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for day_price in prices:
            profit = max(profit , day_price - buy)
            buy = min(buy, day_price)
        return profit
        


###  ------------------------    PYQS ------------------------------####

# 1. STRING COMPRESSION 
def compress_string(s):
    freq ={}
    i = 0
    while i < len(s):
        ch = s[i]
        i+=1
        num =""
        while i <len(s) and s[i].isdigit():
            num += s[i]
            i+=1
            
        if ch in freq:
            freq[ch] += int(num)
        else:
            freq[ch] = int(num)
        
        result = ""
        for ch in sorted(freq):
            result = ch + str(freq[ch])
        return ch
            
        
def ans(hours, minutes, seconds):
    return hours + ":" + minutes + ":" + seconds


def solveClock(input_time):
    seconds = input_time[6:8]
    minutes = input_time[3:5]
    hours = input_time[0:2]

    minAns = ""
    maxAns = ""

    # seconds second digit
    if seconds[1] == '@':
        sec = list(seconds)

        sec[1] = '0'
        minAns = ans(hours, minutes, "".join(sec))

        sec[1] = '9'
        maxAns = ans(hours, minutes, "".join(sec))

    # seconds first digit
    if seconds[0] == '@':
        sec = list(seconds)

        sec[0] = '0'
        minAns = ans(hours, minutes, "".join(sec))

        sec[0] = '5'
        maxAns = ans(hours, minutes, "".join(sec))

    # minutes first digit
    if minutes[0] == '@':
        mins = list(minutes)

        mins[0] = '0'
        minAns = ans(hours, "".join(mins), seconds)

        mins[0] = '5'
        maxAns = ans(hours, "".join(mins), seconds)

    # ✅ minutes second digit (THIS WAS MISSING)
    if minutes[1] == '@':
        mins = list(minutes)

        mins[1] = '0'
        minAns = ans(hours, "".join(mins), seconds)

        mins[1] = '9'
        maxAns = ans(hours, "".join(mins), seconds)

    # hour second digit
    if hours[1] == '@':
        hrs = list(hours)

        hrs[1] = '0'
        minAns = ans("".join(hrs), minutes, seconds)

        if hours[0] == '2':
            hrs[1] = '3'
        else:
            hrs[1] = '9'

        maxAns = ans("".join(hrs), minutes, seconds)

    # hour first digit
    if hours[0] == '@':
        hrs = list(hours)

        hrs[0] = '0'
        minAns = ans("".join(hrs), minutes, seconds)

        hrs[0] = '2'
        maxAns = ans("".join(hrs), minutes, seconds)

    return minAns, maxAns


# Example
print(solveClock("10:1@:40"))
        
    
