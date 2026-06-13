def arr(n):
    a=[]
    b = []
    print("ENter the 1st arr: ")
    for i in range(n):
        a.append(int(input()))
        
    print("ENter the 2nd arr: ")
    for i in range(n):
        b.append(int(input()))
        
    return a , b
n = int(input("Enter the size of arr: "))
a, b= arr(n)
print(a)
print(b)

# # 1. Compare two arrays — check if they contain the same elements (ignore order).
# https://www.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/1
# def checkEqual(a, b):
#     if len(a) != len(b):
#         return False
    
#     freq = {}    
#     for elem in a:
#         if elem in freq:
#             freq[elem] += 1
#         else:
#             freq[elem] = 1
            
#     for elem in b:
#         if elem in freq:
#             freq[elem] -= 1
#         else:
#             return False
        
#         if freq[elem] == 0:
#             del freq[elem]
            
#     return len(freq) == 0
# print("", checkEqual(a, b))


# # 2. Compare two arrays — check if they are equal (same elements & order)
# def checkEqual(a, b):
#     if len(a) != len(b):
#         return False
    
# # why only a? Because we already checked that both arrays have the same length:
# # we can also write: for i in range(len(b)) and it would work exactly the same because: len(a) == len(b)
#     for i in range(len(a)):
#         if a[i] != b[i]:
#             return False

#     freq = {}
#     for elem in a:
#         if elem in freq:
#             freq[elem] += 1
#         else:
#             freq[elem] = 1
            
#     for elem in b:
#         if elem in freq:
#             freq[elem] -= 1
#         else:
#             return False
        
#         if freq[elem] == 0:
#             del freq[elem]       
#     return len(freq) == 0

# print("", checkEqual(a, b))

# # 3. Merge two arrays into a third array. 
# # https://www.geeksforgeeks.org/problems/merging-two-unsorted-arrays-in-sorted-order1020/1
# def mergeElem(a,b):
#     c = []
#     c= a + b
#     return c
# print("", mergeElem(a, b))

# 4. Find the common elements between two arrays. 
# 5. Find elements that are in one array but not in the other. 
# 6. Count how many elements are common between two arrays. 
# 7. Find element-wise sum of two arrays (A[i] + B[i]). 
# 8. Find the element-wise product of two arrays. 
# 9. Create a frequency array of numbers (count the occurrence of each number). 
# 10. Print all elements that appear more than once.
