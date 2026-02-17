# # 1. Print numbers from 1 to 10. 
# for i in range(1,11):
#     print(i)

# # 2. Print all even numbers between 1 and 50. 
# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)
# # 3. Print all odd numbers between 1 and 100. 
# for i in range(1, 21):
#     if i % 2 != 0:
#         print(i)
# # 4. Print numbers from 10 down to 1. 
# for num in range(10, 0, -1):
#     print("Down are: ", num)
# # 5. Print the table of a given number (n × 1 to n × 10). 
# n = int(input("Enter the number:"))
# for i in range(1, 11):
#     print(n* i)   
# # 6. Print the sum of first n natural numbers.
# n = int(input("Enter the number:"))
# if n >= 1:
#     sum = (n*(n+1))//2
#     print(sum)
# else:
#     print("Invalid")
    
# # 7. Print the sum of all even numbers up to n. 
# n = int(input("Enter the num: "))
# if n > 0:
#     k = n //2
#     sum = k*(k+1)
#     print(sum)
# else:
#     print("Invalid")
# # 8. Print the sum of all odd numbers up to n. 
# n = int(input("Enter the num: "))
# if n > 0:
#     k = (n+1) //2
#     sum = k*k
#     print(sum)
# else:
#     print("Invalid")

# # 9. Print the factorial of a given number.
# n = int(input("Enter the num: "))
# if n < 0:
#     print("Invalid")
# else:
#     fact = 1
#     for i in range(1, n+1):
#         fact = fact*i
#     print(fact)
    
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)
     
# n = int(input("Enter the num: "))
# print(factorial(n))

# 10. Print the product of digits of a given number.
n = input("Enter the num: ")
if n == 0:
    print(0)
else:
    prod = 1
    for digit in n:
        prod = prod * int(digit)
    print(prod)
    

