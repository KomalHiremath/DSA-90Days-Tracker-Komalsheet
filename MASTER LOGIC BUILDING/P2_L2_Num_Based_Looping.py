# 1. Count the number of digits in a given number. 
def countDigits(num):
    cnt = 0
    while num > 0:
        num = num//10
        cnt+=1
    return cnt
num = int(input("NUm : "))
print(countDigits(num))

## Count the Digits That Divide a Number   
 #LC: https://leetcode.com/problems/count-the-digits-that-divide-a-number/description/
def countDigits(self, num):
        ori = num
        cnt = 0
        while num > 0:
            digit = num% 10
            if ori % digit == 0:
                cnt +=1
            num = num//10
        return cnt
# num = 121 op : 2 # 121 is divisible by 1, but not 2. Since 1 occurs twice as a digit, we return 2.


# 2. Print the reverse of a given number. 
def revNum(n):
    ori = n
    rev = 0
    while n > 0:
        dig = n % 10
        rev = rev * 10 + dig
        n = n // 10
    return rev
n = int(input("NUM: "))
print(revNum(n))


# 3. Check if a number is a palindrome.
# LC: https://leetcode.com/problems/palindrome-number/submissions/1940482467/
# GFG: https://www.geeksforgeeks.org/problems/palindrome0746/1
def Palindrome(n):
    ori = n
    rev = 0
    while n > 0:
        dig = n % 10
        rev = rev * 10 + dig
        n = n // 10
        if rev == ori:
            return True
    return False
n = int(input("NUM: "))
print(Palindrome(n)) 

# 4. Find the sum of digits of a number. 
def sumOfDigits(self, n):
    if n == 0:
        return 0        
    last = n%10
    rem = n //10
    return last + self.sumOfDigits(rem)
        
# 5. Check if a number is an Armstrong number. 
def armstrong(n):
    ori = n
    pow = len(str(n))
    total =  0
    while n>0:
        dig = n%10
        total = total + dig **pow
        n = n//10
    if total == ori:
        return True
    return False
n = int(input("NUMs: "))
print(armstrong(n)) 

# 6. Check if a number is a perfect number. 
# LC: https://leetcode.com/problems/perfect-number/description/
# GFG: https://www.geeksforgeeks.org/problems/perfect-numbers3207/1
def checkPerfectNumber(self, num: int) -> bool:
    if num<=1:
        return False
    s= 1
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            s+=i
            if i!=num//i:
                s+=num//i
    return s==num
# num = 28  op: 28 = 1 + 2 + 4 + 7 + 14 --> 1, 2, 4, 7, and 14 are all divisors of 28.


# 7. Print all prime numbers between 1 and 100.
#GFG: https://www.geeksforgeeks.org/problems/prime-number2314/1 
def prime(a, b):
    primes = []
    for num in range(a, b):
        if num > 1:
            for i in range (2, int(num **0.5)+1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes
a = int(input("NUMs: "))
b = int(input("NUMs: "))
print(prime(a, b)) 
        
# 8. Check if a number is prime or not. 
def prime(n):
    if n <=1:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n% i == 0:
            return False
    return True
n = int(input("NUMs: "))
print(prime(n)) 
    
# 9. Print Fibonacci series up to n terms. 
def fib(n):
    a = 0
    b = 1
    c = 0
    for i in range(n):
        a = b
        b = c
        c = a+b
    return c
n = int(input("NUMs: "))
print(fib(n)) 
# NUMs: 6 op: 8 --> 1 1 2 3 5 8 
    
# # 10. Print sum of first n terms of Fibonacci series. 
def fib(n):
    a = 0
    b = 1
    c = 0
    total = 0
    for i in range(n):
        total = total + c
        a = b
        b = c
        c = a+b 
    return total 
n = int(input("NUMs: "))
print(fib(n)) 
# NUMs: 5 op:7(0+1+1+2+3) --> n = 5 iterations