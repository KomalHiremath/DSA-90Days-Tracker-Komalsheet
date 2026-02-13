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

# 7. Take a single digit (0–9) and print its word form (“Zero” to “Nine”). 
num = int(input("enter the digit: "))
word = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
if 0 <=num<=9:
    print(word[num])
else:
    print("Invalid")

# 7: Roman to integer
class Solution:
    def romanToInt(self, s: str) -> int:
        val = {'I': 1, 'V': 5,'X':10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        for i in range(len(s)):
            if i < len(s)-1 and val[s[i]] < val[s[i+1]]:
                total -= val[s[i]]
            else:
                total += val[s[i]]
        return total

# 8. Take a weekday number (1–7) and determine if it is a weekday or weekend. 
w = int(input("enter teh weekday num: "))
if 1 <= w <=5:
    print("its weekday")
elif 5< w <= 7:
    print("Its weekend!!..")
else:
    print("Invalid")
    
# 9. Take electricity units consumed and calculate the bill as per slabs (using if-else).
unit = int(input("enter the units: "))  
if unit<=100:
    bill = unit*5
elif unit <= 200:
    bill = (100*5) + ((unit -100)*7)
else:
    bill = (100*5) + (100*7) + ((unit - 200)* 10)
print("the bill is:", bill)

 
# 10. Take a password string and check basic rules (length ≥ 8 and contains at least one digit, one lowercase letter, one uppercase letter, one special character does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" does not).)
word = input("enter the password: ")
if (len(word) >= 8 and 
    any(ch.isdigit() for ch in word) and
    any(ch.islower() for ch in word) and
    any(ch.isupper() for ch in word) and
    any(not ch.isalnum for ch in word) and  #  any(ch in string.punctuation) -> Only these exact symbols
    all(word[i]!=word[i+1] for i in range(len(word)-1))
    ):
    print("valid")
else:
    print("invalid")
# ch.isalnum() → True for letters + digits

