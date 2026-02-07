# 1. Take three sides and check if they form a valid triangle.
 def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        a, b , c = nums
        # check validity
        if a+b <= c :
            return "none"
        
        if a==b==c:
            return "equilateral"
        elif a ==b or a == c or b ==c:
            return "isosceles"
        else:
            return "scalene"