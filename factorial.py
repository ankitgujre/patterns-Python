# factorial
# num = int(input("Enter a number: "))
# fact  = 1
# if num < 0:
#     print("Factorial does not exist for negative numbers")
# elif num == 0:
#     print("The factorial of 0 is 1")
# else:
#     for i in range(1, num + 1):
#         fact *= i
#     print("The factorial of", num, "is", fact)

# factorial using function:

# def factorial(n):
#     fact = 1
#     if n < 0:
#         print("Factorial does not exist for negative numbers")
#     elif n == 0:
#         print("The factorial of 0 is 1")
#     else:
#         for i in range(1, n + 1):
#             fact *= i
#         print("The factorial of", n, "is", fact)
# n = int(input("Enter a number: "))
# factorial(n)

# factorial using recursion:

# def facto(n):
#     if n < 0:
#         print("Factorial does not exist for negative numbers")
#     elif n == 0:
#         return 1
#     else:
#         return n * facto(n - 1)
# n = int(input("Enter a number: "))
# print(facto(n))

# factorial using while loop:
num = int(input("Enter a number: "))
fact = 1
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    while num > 0:
        fact *= num
        print(num)
        num -= 1
    print("The factorial is", fact)