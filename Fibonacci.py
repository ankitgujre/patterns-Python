# wap to get the Fibonacci series up to n terms
# n = int(input("Enter the number of terms: "))
# a, b = 0, 1
# count = 0
# while count < n:
#     print(a)
#     c = a + b
#     a = b
#     b = c
#     count += 1
    # count = count + 1

# n = 10
# a = 0
# b = 1
# count = 0
# while count < n:
#     print(a)
#     a = b
#     b = a + b
#     count += 1

# using function

# def fibo(n):
#     a = 0
#     b = 1
#     count = 0
#     while count < n:
#         print(a)
#         a, b = b, a + b
#         count += 1

# n = int(input("Enter the number of terms: "))
# fibo(n)
    
# n = int(input("Enter the number of terms: "))      
# fibo(n)

# using recursion
# def fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)
# n = int(input("Enter the number of terms: "))
# for i in range(n):
#     print(fibo(i))

# def fibo(n):
#     if n <= 1:
#         print(n)
#     else:
#         print(fibo(n-1) + fibo(n-2))
# n = int(input("Enter the number of terms: "))
# for i in range(n):
#     fibo(i)

