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

# 6. Take two numbers and print the larger one.  Your task is to print 1 if a < b, print 2 if a > b and print 3 if a = b. 
    def check(self, a,b):
        if a < b:
            return 1
        elif a > b:
            return 2
        else:
            return 3

# 7. Take three numbers and print the largest. 
    def greatestOfThree(self, a, b, c):
        if a >= b and a >= c:
            return a
        elif b >= a and b >= c:
            return b
        else:
            return c
        
# 8. Take a temperature value and print “Cold”, “Warm”, or “Hot” using range conditions.
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = celsius + 273.15 
        fahrenheit = celsius * 1.80 + 32.00
        ans = [kelvin, fahrenheit]
        return ans   

# 9. Take a character and check if it’s a vowel or consonant./ Write a program to check whether a character is a vowel or not. 
    def isVowel (ob,c):
        vow = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        if c in vow:
            
            return "YES"
        
        else:
            return "NO"
# 10. Take a character and check whether it’s uppercase, lowercase, a digit, or a special character. 
ch = input("enter a char:")
if ch.isupper():
    print("is upper char")
elif ch.islower():
    print("is lower char")
elif ch.isdigit():
    print("is digit")
else:
    print("is special char")
    
# 8. Take an alphabet character and check if it lies between ‘a’ and ‘m’ or ‘n’ and ‘z’.
ch = input("Enter the char: ") 

if 'a' <= ch <= 'm':
    print("ch is between a - m")
elif 'n' <= ch <= 'z':
    print("ch is between n - z")
else:
    print("Invalid")
    