# # 1. Print a Single Star (*)
# print("*")

# # 2. Print Four Stars (****)
# print("****")

# # 3.Print n Stars on Same Line
# n = int(input("Enter the stars:"))
# print("*" * n)

# #      ------ OR -----
# n = int(input("Enter the stars:"))
# for i in range(n):
#     print("*", end="")


## 4. Print Square of Stars (n x n Stars)
# n = int(input("Enter the num of stars:"))
# for i in range(n):
#     print("*" * n)

n = int(input("Enter the num of stars:"))

# # 5. Print an Increasing Triangle of Stars
# # *
# # **
# # ***
# # ****
# for i in range(1, n+1):
#     print("*" * i)

# # 6. Print a Right-Aligned Triangle of Stars
# #   *
# #  **
# # ***
# for i in range(1, n+1):
#     print(" " * (n-i) + "*" * i)


# # 7. Print Stars in Even Numbers (2, 4, 6, 8, 10)
# # **
# # ****
# # ******
# # ********
# for i in range(1, n+1):
#     print("*" * (i+i))

# 8. Print Stars in Odd Numbers (1, 3, 5, 7, 9)
# $
# $$$
# $$$$$
# $$$$$$$
# $$$$$$$$$
# for i in range(1, n+1):
#     print("$" * (i+(i-1)))

# 9. Print a Centered Pyramid of Stars
#    &   
#   &&&  
#  &&&&& 
# &&&&&&&

# for i in range(1, n+1):
#     print(" " * (n-i) + "&" * (i+(i-1)) + " " * (n-i))

# 10. Print Stars and Spaces Alternating (Stars and Blank Spaces)
# ---*
# --* *
# -* * *
# * * * *

# for i in range(1, n+1):
#     print("-" * (n-i) + "* " * (i-1) + "*")

# 11. Print Numbers in an Increasing Sequence (1, 12, 123, 1234, 12345)
# 1
# 12
# 123
# 1234

# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end="")
#     print()

# 12. Print Repeated Numbers per Row (Same Number Repeated)  
# 1
# 22
# 333
# 4444
# 55555

# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(i, end="")
#     print()

# 13.

# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15 

# num =1
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(num, end=" ")
#         num += 1
#     print()
        
# 14. 

# 1 
# 2 3 
# 4 5 6 
# 7 8 9 0 
# 1 2 3 4 5 
# 6 7 8 9 0 1 
# 2 3 4 5 6 7 8 
# 9 0 1 2 3 4 5 6 

# num = 1
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(num%10, end = " ")
#         num=num+1
#     print()

# 15. 

# 0 
# 1 0 
# 0 1 0 
# 1 0 1 0 
# 0 1 0 1 0 

# for i in range(1, n+1):
#     for j in range(1, i+1):
#         val = (i+j) % 2
#         print(val, end =" ")
#     print()

# 16.

# A 
# B C 
# D E F 
# G H I J 
# K L M N O 

# ch = ord('A')
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(chr(ch), end=" ")
#         ch += 1
#     print()

# 17. 
# A 
# B B 
# C C C 
# D D D D 
# E E E E E 

# ch = ord('A')
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(chr(ch), end=" ")
#     ch += 1
#     print()

# 18. 
# A 
# A B 
# A B C 
# A B C D 
# A B C D E 

# for i in range(1, n+1):
#     ch = ord('A')
#     for j in range(1, i+1):
#         print(chr(ch), end= " ")
#         ch += 1
#     print()

# 19.
# ----A 
# ---B C D 
# --E F G H I 
# -J K L M N O P 
# Q R S T U V W X Y

# ch = ord('A')
# for i in range(1, n+1):
#     print("-" * (n-i), end ="")
#     for j in range(1, i*2):  # -- this line ---
#         print(chr(ch), end = " ")
#         ch += 1
#     print()
    
# ----A 
# ---B C 
# --D E F 
# -G H I J 
# K L M N O 

# ch = ord('A')
# for i in range(1, n+1):
#     print("-" * (n-i), end ="")
#     for j in range(1, i+1):  # -- this line ---
#         print(chr(ch), end = " ")
#         ch += 1
#     print()  

# 20. 
# ----1
# ---21
# --321
# -4321
# 54321

# for i in range(1, n+1): 
#     print("-"*(n-i), end="") 
#     for j in range(i, 0, -1):
#         print(j, end="")
#     print()
    
# 21.
# ----1
# ---121
# --12321
# -1234321
# 123454321

# for i in range(1, n+1):
#     #  FORWARD
#     print("-" * (n-i), end="")
#     for j in range(1, i+1):
#         print(j, end="")
        
#     # BACKWARD 
    # for j in range(i, 1, -1):
    #     print(j-1, end="")   
    # print()
    
# 22. 
# ----5
# ---545
# --54345
# -5432345
# 543212345

# ----5
# ---54
# --543
# -5432
# 54321
# for i in range(1, n+1):
#     print("-"*(n-i), end="")
#     for j in range(5, 5-i, -1):
#         print(j, end="")
        
# BLANK      
# 5
# 45
# 345
# 2345 
    # for j in range(6-i, 5):
    #     print(j+1, end="")
    # print()
    
# 23.

# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
      
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print("*", end="")
#     print() 

#       INVERTED
# for i in range(1, n+1):
#     for j in range(1, (n-i)+1):
#         print("*", end="")  
#     print() 
    
# 24. 

# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

# for i in range(1, n+1):
#     for j in range(1,i+1):
#         print("*", end="")
#     print()
    
#       INVERTED
# for i in range(1, n+1):
#     for j in range(1, (n-i)+2):
#         print("*", end="")
#     print()


23.

#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
    
# for i in range(1, n+1):
#     print(" " * ((n-i)), end="")
#     for j in range(1, i*2):  
#         print("*", end="")
#     print()

# #      INVERTED
# for i in range(1, n+1):
#     print(" " * i, end="" )
#     for j in range(1, ((n*2)-(i*2))):
#         print("*", end="" )
#     print()