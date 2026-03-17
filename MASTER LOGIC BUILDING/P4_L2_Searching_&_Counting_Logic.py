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

# # 2. Count how many times a given element appears. 
# def element(n):
#     arr =[]
#     for i in range(n):
#         arr.append(int(input()))
#     return arr

# def appear(arr):
#     cnt = 0
#     for i in arr:
#         if i == k:
#             cnt +=1
#     return cnt
# n = int(input("Enter the size: "))
# arr = element(n)
# k = int(input("Enter the num to search: "))
# print(appear(arr))
    
# 3. Find the first occurrence of a given number.
# arr = [5, 3, 7, 3, 9] # k = 3
# output: 1 --> Because the first 3 appears at index 1.
# def element(n):
#     arr =[]
#     for i in range(n):
#         arr.append(int(input()))
#     return arr

# def occ(arr):
#     for i in range (len(arr)):
#         if arr[i] == k:
#             return i
#     return -1
        
# n = int(input("Enter the size: "))
# arr = element(n)
# k = int(input("Enter the num to search: "))
# print(occ(arr))

# # 4. Find the last occurrence of a given number. 
# def element(n):
#     arr =[]
#     for i in range(n):
#         arr.append(int(input()))
#     return arr

# def occ(arr):
#     index = -1
#     for i in range (len(arr)):
#         if arr[i] == k:
#             index = i
#     return index

##### ---- OR ----- #####

# def occ(arr):
#     for i in range (len(arr)-1, -1, -1): # range(start, stop, step)
#         if arr[i] == k:
#             return i
#     return -1

# n = int(input("Enter the size: "))
# arr = element(n)
# k = int(input("Enter the num to search: "))
# print(occ(arr))


# # 5. Find the first and last occurrence of a given number. 
# def element(n):
#     arr =[]
#     for i in range(n):
#         arr.append(int(input()))
#     return arr

# def first_occ(arr, k):
#     for i in range (len(arr)):
#         if arr[i] == k:
#             return i
#     return -1

# def last_occ(arr, k):
#     for i in range (len(arr)-1, -1, -1): # range(start, stop, step)
#         if arr[i] == k:
#             return i
#     return -1

# n = int(input("Enter the size: "))
# arr = element(n)
# k = int(input("Enter the num to search: "))
# print(first_occ(arr, k), last_occ(arr, k))


# # 6. Find the sum of even elements only. 

# def element(n):
#     arr =[]
#     for i in range(n):
#         arr.append(int(input()))
#     return arr

# def even(arr):
#     total = 0
#     for i in arr:
#         if i%2 == 0:
#             total += i
#     return total
        
# n = int(input("Enter the size: "))
# arr = element(n)
# print("The sum is:", even(arr))

# # 7. Find the sum of odd elements only. 
# def element(n):
#     arr =[]
#     for i in range(n):
#         arr.append(int(input()))
#     return arr

# def odd(arr):
#     total = 0
#     for i in arr:
#         if i%2 != 0:
#             total += i
#     return total
        
# n = int(input("Enter the size: "))
# arr = element(n)
# print("The sum is:", odd(arr))

# 8. Check if all elements in an array are unique. 
def element(n):
    arr =[]
    for i in range(n):
        arr.append(int(input()))
    return arr
def unique(arr):
    j = arr[i] +1
    for i in range(len(arr)+1):
        if j==i:
            return False
    return True
n = int(input("Enter the size: "))
arr = element(n)
print(unique(arr))

        


# 8. Find the count of prime numbers in the array. 
# 9. Count how many numbers are divisible by 3 and 5 both. 
# 10. Count how many elements are perfect squares. 
