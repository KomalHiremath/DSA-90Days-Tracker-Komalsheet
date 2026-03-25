# 1. Create a new array containing squares of all numbers. 
# 2. Create a new array containing only even elements. 
# 3. Replace every negative number with 0. 
# 4. Replace all even numbers with 1 and all odd with 0. 
# 5. Swap the first and last elements of the array. 
# 6. Reverse an array (without using built-in reverse). 
# 7. Rotate an array by one position to the left. 
# 8. Rotate an array by one position to the right. 
# 9. Swap alternate elements (1st ↔ 2nd, 3rd ↔ 4th, etc.). 
# 10. Copy one array to another manually. 

 ###########----------------#########################
 
# 1. Create a new array containing squares of all numbers. 
# def element(n):
#     arr = []
#     for i in range(1, n+1):
#         arr.append(i*i)
#     return arr

# n = int(input("Enter the size of arr:"))
# print(element(n))

##      OR        ###

# def element(n):
#     return [i*i for i in range(1, n+1)]

# n = int(input("Enter the size of arr:"))
# print(element(n))


# 2. Create a new array containing only even elements. 
# def even(n):
    # arr = []
    # for i in range(1, n+1):
    #     if i%2 == 0:
    #         arr.append(i)
    # return arr
    
# n = int(input("Enter the size of arr:"))
# print(even(n))

###     OR  #############
# def even(n):
#     return [i for i in range(n1, +1) if i%2 == 0 ]

# n = int(input("Enter the size of arr:"))
# print(even(n))
  
## 3. Replace every negative number with 0. 
# def element(n):
#     arr = []
#     for i in range(n):
#         num = int(input())
#         if num<0:
#             arr.append(0)
#         else:
#             arr.append(num)
#     return arr

# n = int(input("Enter the size of arr:"))
# print(element(n))
              
# # 4. Replace all even numbers with 1 and all odd with 0. 
# def element(n):
#     arr = []
#     for i in range(n):
#         num = int(input())
#         if num%2 == 0:
#             arr.append(1)
#         else:
#             arr.append(0)
#     return arr

# n = int(input("Enter the size of arr:"))
# print(element(n))

# # 5. Swap the first and last elements of the array. 
# def elem(n):
#     arr = []
#     for i in range(n):
#         arr.append(int(input()))
#     arr[0], arr[-1] = arr[-1], arr[0]
#     return arr
# n = int(input("Enter the size of arr:"))
# print(elem(n))

# # 6. Reverse an array (without using built-in reverse).
# GFG : https://www.geeksforgeeks.org/problems/reverse-an-array/1
# def elem(n):
#     arr = []
#     for i in range(n):
#         arr.append(int(input()))
#     return arr

# def rev(arr):
#     arr.reverse()
#     return arr

## TWO POINTER     
# def rev(arr):
#     l = 0
#     r = len(arr)-1
#     while l < r: 
#         arr[l], arr[r] = arr[r], arr[l]
#         l += 1
#         r -= 1
#     return arr


# #   RECURSION 
# def rev(arr):
#     n = len(arr)
#     for i in range(n//2):      # no +1, loop handles stopping
#         arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
#     return arr

# n = int(input("Enter the size of arr:"))
# arr = elem(n)
# print("Reverse", rev(arr))
    

# 7. Rotate an array by one position to the left. 
def elem(n):
    arr = []
    for i in range(n):
        arr.append(int(input()))
    return arr

# def rotate(arr, k):
#     n = len(arr)
#     k = k%n
#     arr1 = arr[0:k]
#     arr2 = arr[k:]
    
#     arr1.reverse()
#     arr2.reverse()
    
#     result = arr1[:] + arr2[:]
#     arr[:] = result
#     arr.reverse()
#     return arr

def rotate(arr):
    n = len(arr)
    temp = arr[0]
    # shift to the left
    for i in range(1, n):
        arr[i-1] = arr[i]
    arr[n-1] = temp
    return arr
    
n = int(input("Enter the size of array:"))
arr = elem(n)
# k= int(input("Enter the no. of position to rotate:"))
print(rotate(arr))
    
    
# 8. Rotate an array by one position to the right. 
# 9. Swap alternate elements (1st ↔ 2nd, 3rd ↔ 4th, etc.). 
# 10. Copy one array to another manually. 

