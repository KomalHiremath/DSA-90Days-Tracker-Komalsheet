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
   
 
