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
# 3. Take a 4-digit number and check if the first and last digits are equal.
# 4. Check whether a given integer is single-digit, double-digit, or multi-digit. 
# 5. Check if a number isa multiple of 7 or ends with 7. 
# 6. Take coordinates (x, y) and determine which quadrant the point lies in.
# 7. Check if an amount can be evenly divided into 2000, 500, and 100 currency notes. 
# 8. Check if a number lies within the range [100, 999]. 
# 9. Take two angles of a triangle and compute the third angle. 
# 10. Check whether a number is a perfect square (without using the square root function). 
