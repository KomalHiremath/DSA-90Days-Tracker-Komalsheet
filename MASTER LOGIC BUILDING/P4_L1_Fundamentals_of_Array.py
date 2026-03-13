# # 1. Input n and take n integers into an array; print them. 
# # 2. Find the sum of all elements in an array. 
# # 3. Find the average of the array elements. 
# # 4. Find the maximum element in an array. 
# # 5. Find the minimum element in an array. 
# # 6. Count how many elements are positive, negative, or zero. 
# # 7. Count how many elements are even and odd. 
# # 8. Find the index of the maximum element. 
# # 9. Find the index of the minimum element. 
# # 10. Take n elements and print only those greater than a given value k.
#             ############################
            
# # 1. Input n and take n integers into an array; print them. 
# def array(n):
#     arr = []
#     for i in range(n):
#         num = int(input("Enter the num: "))
#         arr.append(num)
#     print("array elms are: ")
#     for i in arr:
#         print(i, end= " ")
# n = int(input("enter the size: "))
# array(n)

# ## OR ####
# def arr(n):
#     arr = []
#     for i in range(n):
#         arr.append(int(input()))
#     return arr
# n = int(input("Enter the size: "))
# print(arr(n))

# # 2. Find the sum of all elements in an array. 
# def SumOfNum(n):
#     arr = []
#     for i in range(n):
#         arr.append(int(input()))
#     return sum(arr)
# n = int(input("Enter the size: "))
# print( "The sum is:",SumOfNum(n))

# # 2. calculate sum without storing the array.
# def SumOfNum(n):
#     total = 0
#     for i in range(n):
#         num= int(input())
#         total += num
#     return total
# n = int(input("Enter the size: "))
# print( "The sum is:",SumOfNum(n))

# # 3. Find the average of the array elements. 
# def AvgOfNum(n):
#     arr = []
#     for i in range(n):
#         arr.append(int(input()))
#     total = sum(arr)/n
#     return total
# n = int(input("Enter the size: "))
# print( "The avg is:",AvgOfNum(n))

# #3. calculate average without storing the array.
# def AvgOfNum(n):
#     total = 0
#     for i in range(n):
#         num= int(input())
#         total += num
#     return total/n
# n = int(input("Enter the size: "))
# print( "The sum is:",AvgOfNum(n))

# # 4. Find the maximum element in an array. 
# def MaxOfNum(n):
#     arr = []
#     for i in range(n):
#         arr.append(int(input()))
#     total = max(arr)
#     return total
# n = int(input("Enter the size: "))
# print( "The max is:",MaxOfNum(n))

# #4. calculate max without storing the array.
# def MaxOfNum(n):
#     arr = []
#     for i in range(n):
#         arr.append(int(input()))
#     return max(arr)
# n = int(input("Enter the size: "))
# print( "The min is:",MaxOfNum(n))

# # 5. Find the minimum element in an array. 
# def MinOfNum(n):
#     arr = []
#     for i in range(n):
#         arr.append(int(input()))
#     total = min(arr)
#     return total
# n = int(input("Enter the size: "))
# print( "The min is:",MinOfNum(n))

# # 5. calculate min without storing the array.
# def MinOfNum(n):
#     arr = []
#     for i in range(n):
#         arr.append(int(input()))
#     return min(arr)
# n = int(input("Enter the size: "))
# print( "The min is:",MinOfNum(n))


# # 6. Count how many elements are positive, negative, or zero.
# def elem(n):
#     arr = []
#     for i in range(n):
#         arr.append(int(input()))
#     return arr
# def find(arr):
#     pos = 0
#     neg = 0
#     zero = 0
#     for i in arr :
#         if i>0:
#             pos += 1
#         elif i<0:
#            neg += 1
#         else:
#             zero += 1
#     print("Positive", pos)
#     print("negative", neg)
#     print("zero", zero)
            
# n = int(input("Enter the size: "))
# arr = elem(n)
# find(arr)
         
 
# # 7. Count how many elements are even and odd. 
def elem(n):
    arr = []
    for i in range(n):
        arr.append(int(input()))
    return arr
def find(n):
    even = odd = 0
    for i in arr:
        if i%2 ==0:
            even +=1
        else:
            odd +=1
    print("Even", even)
    print("odd", odd)
n = int(input("enter the size: "))
arr = elem(n)
find(arr)
            
# # 8. Find the index of the maximum element. 
# # 9. Find the index of the minimum element. 
# # 10. Take n elements and print only those greater than a given value k.