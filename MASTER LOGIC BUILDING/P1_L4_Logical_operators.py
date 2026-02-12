# 1. Take a character and check if it is a letter, a digit, or neither. 
s = input("Enter the char: ")
if "a" <= s <= "z" or "A" <= s <= "Z":
    print("Its a letter")
elif "0" <= s <= "9":
    print("Its a digit")
else:
    print("neither")
    
# 2. Take a number and print “Fizz” if divisible by 3, “Buzz” if divisible by 5, and “FizzBuzz” if divisible by both. 
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz") 
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0 :
                answer.append("Buzz") 
            else:
                answer.append(str(i))
        return answer
  # “Return an array/list of size N” 
#✅ Create empty list
# ✅ Loop
# ✅ Append inside loop
# ❌ Never return inside loop  

# 3. Take three numbers and print the median value (neither maximum nor minimum). 
num = list(map(int, input("Enter the number: ").split()))
if len(num) == 3:
    num.sort()
    print("The median val is: ", num[1])
else:
    print("none")
   
# 4. Take 24-hour time (hours and minutes) and print whether it is AM or PM. 
hour= int(input("ENter the hour(0-23): "))
min = int(input("enter the minutes (0-59)"))

if 0 <= hour <=23 and 0<=min<=59:
    if hour <12:
        print("Its AM")
    else:
        print("Its PM")
else:
    print("Invalid input")

#5. Take income and age, and check if eligible for tax (age > 18 and income > 5 L). 
income = int(input("Enter the income: "))
age = int(input("Enter the age: "))
if age > 18 and income > 500000:
    print("Eligible")
else:
    print("Not eligible") 
    
# 6. Take two numbers and check if both are positive and their sum is less than 100.
a = int(input("Enter the num: "))
b = int(input("Enter the num: "))

if (a > 0 or b > 0) and a+b < 100:
    print("positive")
else:
    print("Not satisfied")
  

# and  → higher precedence
# # or   → lower precedence

# a > 0 or b > 0 and a + b < 100
# Python reads it as: a > 0 or (b > 0 and a + b < 100)
 
# (a > 0 or b > 0) and a + b < 100
# Here parentheses force:
# Check first (a > 0 or b > 0) 
# Then check and a + b < 100




    
