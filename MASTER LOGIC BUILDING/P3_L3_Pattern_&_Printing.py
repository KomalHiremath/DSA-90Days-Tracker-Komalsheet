## 1. Print a line of n stars recursively. 
# def stars(n):
#     return n*"*"
# n = int(input("Enter the num:"))
# print(stars(n))

# # 2. Print a square of stars(n×n). 
# def stars(n):
#     for i in range(n):
#         for j in range(n):
#             print("*", end =" ")
#         print()       
# n = int(input("Enter the num:"))
# stars(n)

#3. Print a triangle of stars (top-down).  
def stars(n):
    for i in range(n):
        for j in range(n-i):
            print("*", end =" ")
        print()       
n = int(input("Enter the num:"))
stars(n)

# 4. Print a triangle of stars  (bottom-up).
def stars(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end =" ")
        print()       
n = int(input("Enter the num:"))
stars(n)
 
