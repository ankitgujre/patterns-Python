# Print 1 to 10
'''
for i in range(1, 11):
    print(i) '''

# without range function
# n = int(input("Enter a number: "))
# for i in range(1, n + 1):
#     print(i)

'''
wap to print even numbers from 1 to 20
'''
# for i in range(1,21):
#     if i % 2 == 0:
#         print(i)

# for i in range(2, 21, 2):
#     print(i)

# n = int(input("Enter a number: "))
# for i in range(2, n+1, 2):
#     print(i)

# wap to print odd numbers from 1 to 20
# for i in range(1, 21):
#     if i % 2 != 0:
#         print(i)

'''
wap to print reverse of a number using for loop
'''
# n  = int(input("Enter number: "))
# for i in range(n, -1, -1):
#     print(i)

'''
print multiplication table of a number
'''
# n = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(n, "x", i, "=", n * i)

''' 
square of 1 to 10
'''
# for i in range(1,11):
#     print("the square of", i, "is", i**2)

'''
cube of 1 to 10
'''
# for i in range(1,11):
#     print("the cube of", i, "is", i**3)

'''
count digits in a number
'''
# n = int(input("Enter a number: "))
# count = 0
# while n > 0:
#     count += 1
#     n //= 10
# print("the number of digits in the number is", count)

'''
sum of digits in a number
'''
# n = int(input("Enter a number: "))
# sum = 0
# while n > 0:
#     digit = n % 10
#     sum += digit
#     n //= 10
# print("the sum of digits in the number is", sum)

'''
reverse of a number
'''
# n = int(input("Enter a number: "))
# reverse = 0
# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n //= 10
# print("the reverse of the number is", reverse)
'''
triangles patters 

for i in range(1,6):
    print("*"*i)

for i in range(6,0,-1):
    print("*"*i)

'''
# 26. Nested loop table
# for i in range(1, 6):
#     for j in range(1, 11):
#         print(i * j, end=" ")
#     print()

