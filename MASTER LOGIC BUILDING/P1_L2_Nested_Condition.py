# 1. Take three sides and check if they form a valid triangle.
def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        a, b , c = nums
        # check validity
        if a+b <= c :
            return "none"
        
# 2. If the sides form a valid triangle, determine whether it is equilateral, isosceles, or scalene. 
def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        a, b , c = nums
        # check validity
        if a+b <= c :
            return "none"
        
        #Check type of triangle
        if a==b==c:
            return "equilateral"
        elif a ==b or a == c or b ==c:
            return "isosceles"
        else:
            return "scalene"
 
# 3. Take marks (0–100) and print the corresponding grade (A/B/C/D/F).   
mark = int(input("Enter the marks"))
if 0 <= mark <= 20:
    print("F")
elif 21 <= mark <= 40:
    print("D")
elif 41 <= mark <= 60:
    print("C")
elif 61 <= mark <= 80:
    print("B")
elif 81<= mark <=100:
    print("A")
else:
    print("invalid")
    
# 4. Check if one of two given numbers is a multiple of the other.
# 5. Take the hour of the day (0–23) and print “Good Morning”, “Good Afternoon”, “Good Evening”, or “Good Night”
hr = int(input("Enter the hour: ")) 
if 5 <= hr <= 11:
    print("Good morning")
elif 12 <= hr <= 16:
    print("Good afternoon")
elif 17 <= hr <= 20:
    print("Good evening")
elif 21 <= hr <= 4:
    print("good night")   
else:
    print("invalid hr")

# 6. Check voting eligibility for a given age (18+). 
age = int(input("enter the age: "))
if age < 0 or age > 120:
    print("Invalid age")
elif age >= 18:
    print("Eligible")
else:
    print("Not eligible")

# 7. Take two numbers and determine whether both are even, both are odd, or one is even and one is odd. 
a, b = map(int, input("Enter a and b").split())
if a % 2 == 0 and  b % 2 == 0 :
    print("Both even")
elif a % 2 != 0 and b % 2 != 0:
    print("Both are odd")
elif a % 2 == 0 and  b % 2 != 0:
    print("a  is even and b is odd")
else:
    print("b  is even and a is odd")
    