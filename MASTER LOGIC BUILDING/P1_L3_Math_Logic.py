#1. Take a 3-digit number and check if all digits are distinct.
# Input: nums = [131, 11, 48]   Output: 1 3 4 8
def common_digits(self, nums):
    s = set()
    for val in nums:
        num_str = str(val)
    for digit in num_str:
        s.add(int(digit))
    return sorted(list(s))
	   
# 2. Take a 3-digit number and determine if the middle digit is the largest, smallest, or neither. 
val = int(input("Enter the number:"))
s = str(val)

if len(s)!=3:
    print("Enter a valid 3 -digit number")
else:
    f = int(s[0])
    m = int(s[1])
    l = int(s[2])
    if m > f and m >l:
        print("Biggest")
    elif m < f  and m < l:
        print("Smallest")
    else:
        print("Neither")
        
# 3. Take a 4-digit number and check if the first and last digits are equal.
val = int(input("enter the number:"))
s = str(abs(val)) # handles -ve value
if len(s)!= 4:
    print("Invalid")
else:
    first = s[0]
    # sec = s[1]
    # third = s[2]
    fourth = s[3] 
    if first == fourth:
        print("first and last digits are equal")
    else:
        print("NOT")
        
# 4. Check whether a given integer is single-digit, double-digit, or multi-digit. 
val = int(input("Enter the number: "))
s = str(abs(val))
if len(s) == 1:
    print("Single digit")
elif len(s) == 2:
    print("Double digit")
else:
    print("Multi-digit")
    
# 5. Check if a number is a multiple of 7 or ends with 7.
val = int(input("enter the number:"))
if val%7 == 0:
    print("Multiple of 7")
elif abs(val) % 10 == 7:
    print("ends with 7") 
else:
    print("None")
    
# 6. Take coordinates (x, y) and determine which quadrant the point lies in.
x = int(input("Enter the num"))
y = int(input("Enter the num"))

if x ==0 and y== 0:
    print("origin")
elif x == 0:
    print("Y axis")
elif y == 0:
    print("X axis")
elif x > 0 and y > 0:
    print("1st quadrant")
elif x < 0 and y > 0:
    print("2nd quadrant")
elif x < 0 and y < 0:
    print("3rd quadrant")
else:
    print("4th quadrant")
    
# 7. Check if an amount can be evenly divided into 2000, 500, and 100 currency notes. 
val = int(input("Enter the num"))
if val%100 == 0:
    print(" amount can be evenly divided")
else:
    print("Its not")

# 8. Check if a number lies within the range [100, 999].
val = int(input("Enter the num"))
if 100 <= val <= 999:
    print("In the range")
else:
    print("Not")
    
 
# 9. Take two angles of a triangle and compute the third angle. 
a = int(input("Enter the angle"))
b = int(input("Enter the angle"))
if a > 0 or b > 0 or a + b < 180 :
    c = 180 - (a+b)
    print("The angle is: ", c)
else:
    print("invalid")

# 10. Check whether a number is a perfect square (without using the square root function).
val = int(input("Enter the num")) 
if val < 0:
    print("Invalid: ")
else:
    i = 0
    while i*i <= val:
        if i*i == val:
            print("perfect square")
            break
        i += 1
    else:
        print("Not a perfect square") 
