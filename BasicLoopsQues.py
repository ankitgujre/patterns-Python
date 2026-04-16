# Wap to print sum of n natural numbers

# n = int(input("enter any no. : "))
# sum = 0
# for i in range(1,n+1):
#     sum += i
#     print(i)
# print("the sum of n natural numbers is : ", sum)

# sum = 0

# if n < 0:
#     print("enter a positive number")
# else:
#     for i in range(1, n+1):
#         sum += i
#         print(i)
#     print("the sum of n natural numbers is : ", sum)

# using functions

# def sum_natural(n):
#     sum = 0
#     if n < 0:
#         print("enter a positive number")
#     else:
#         for i in range(1,n+1):
#             sum += i
#             print(i)
#         print(sum)
# n = int(input("enter any no. : "))
# sum_natural(n)

# using recursion

# def sum_natural(n):
#     if n < 0:
#         print("enter a positive number")
#     else:
#         if n == 0:
#             return 0
#         else:
#             return n + sum_natural(n-1)
# n = int(input("enter any no. : "))
# print(sum_natural(n))

# using while loop

n = int(input("enter any no. : "))
sum = 0
if n < 0:
    print("enter a positive number")
else:
    while n > 0:
        sum += n
        print(n)
        n -= 1
    print("the sum of n natural numbers is : ", sum)