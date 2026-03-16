# 1. Input an element x — check if it exists in the array. 
# 2. Count how many times a given element appears. 
# 3. Find the first occurrence of a given number. 
# 4. Find the last occurrence of a given number. 
# 5. Check if all elements in an array are unique. 
# 6. Find the sum of even elements only. 
# 7. Find the sum of odd elements only. 
# 8. Find the count of prime numbers in the array. 
# 9. Count how many numbers are divisible by 3 and 5 both. 
# 10. Count how many elements are perfect squares. 

##### -----------------------------------------------###############

# # 1. Input an element x — check if it exists in the array. 
# # GFG: https://www.geeksforgeeks.org/problems/search-an-element-in-an-array-1587115621/1
# def element(n):
#     arr =[]
#     for i in range(n):
#         arr.append(int(input()))
#     return arr

# def find(arr):
#     for i in arr:
#         if i == k:
#             return True
#         return False

# n = int(input("Enter the size: "))
# arr = element(n)
# k = int(input("Enter the num to search: "))
# print(find(arr))

# 2. Count how many times a given element appears. 
def element(n):
    arr =[]
    for i in range(n):
        arr.append(int(input()))
    return arr

def appear(arr):
    cnt = 0
    for i in arr:
        if i == k:
            cnt +=1
    return cnt
n = int(input("Enter the size: "))
arr = element(n)
k = int(input("Enter the num to search: "))
print(appear(arr))
        
    
    
    
    
    
    
# 3. Find the first occurrence of a given number. 
# 4. Find the last occurrence of a given number. 
# 5. Check if all elements in an array are unique. 
# 6. Find the sum of even elements only. 
# 7. Find the sum of odd elements only. 
# 8. Find the count of prime numbers in the array. 
# 9. Count how many numbers are divisible by 3 and 5 both. 
# 10. Count how many elements are perfect squares. 
