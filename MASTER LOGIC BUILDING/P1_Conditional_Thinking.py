# Level 1: Simple Conditions 
# 1. Take a number and print whether it’s positive, negative, or zero. 
num = int(input("enter the number:"))
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("Zero")
    
# 2. Check if a number is even or odd. 
    def isEven (self, n):
        if n % 2 == 0:
            return True
        else: 
            return False

#  3. Given a number N in the form of string, the task is to check if the number is divisible by 5. 
def divisibleBy5 (ob,N):
        if N[-1] == '0' or N[-1] =='5': # num = int(N)   # ❌ crashes for very large numbers

            return 1
        else:
            return 0
     
# 4 Check if a number is divisible by both 3 and 5. 
num = int(input("ENter:"))
if num%5 == 0 and num%3 ==0:
    print("1") 
else:
    print("0")

# 5 You are given an Integer n. Return true if It is a Leap Year otherwise return false

    def checkYear (self, n):
        if n%4 ==0 and n%100 !=0 or n%400 == 0:
            return True
        else:
            return False