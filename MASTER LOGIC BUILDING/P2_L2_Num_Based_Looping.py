# # 1. Count the number of digits in a given number. 
# def countDigits(num):
#     cnt = 0
#     while num > 0:
#         num = num//10
#         cnt+=1
#     return cnt
# num = int(input("NUm : "))
# print(countDigits(num))

 # Count the Digits That Divide a Number   
 # LC: https://leetcode.com/problems/count-the-digits-that-divide-a-number/description/
# def countDigits(self, num: int) -> int:
#         ori = num
#         cnt = 0
#         while num > 0:
#             digit = num% 10
#             if ori % digit == 0:
#                 cnt +=1
#             num = num//10
#         return cnt
## num = 121 op : 2 # 121 is divisible by 1, but not 2. Since 1 occurs twice as a digit, we return 2.


# # 2. Print the reverse of a given number. 
# def revNum(n):
#     ori = n
#     rev = 0
#     while n > 0:
#         dig = n % 10
#         rev = rev * 10 + dig
#         n = n // 10
#     return rev
# n = int(input("NUM: "))
# print(revNum(n))


# 3. Check if a number is a palindrome.
# LC: https://leetcode.com/problems/palindrome-number/submissions/1940482467/
# GFG: https://www.geeksforgeeks.org/problems/palindrome0746/1
def Palindrome(n):
    ori = n
    rev = 0
    while n > 0:
        dig = n % 10
        rev = rev * 10 + dig
        n = n // 10
        if rev == ori:
            return True
    return False
n = int(input("NUM: "))
print(Palindrome(n)) 


# 4. Find the sum of digits of a number. 
# 5. Check if a number is an Armstrong number. 
# 6. Check if a number is a perfect number. 
# 7. Print all prime numbers between 1 and 100. 
# 8. Check if a number is prime or not. 
# 9. Print Fibonacci series up to n terms. 
# 10. Print sum of first n terms of Fibonacci series. 
