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





    

