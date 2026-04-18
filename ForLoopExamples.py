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

'''
print list items
'''

# arr = [1,2,300,45]

# for i in arr:
#     print(i)

''' find sum of list '''

# arr = list([1,2,3,4])
# # print(type(arr))
# sum = 0
# for i in arr:
#     sum += i

# print(sum)

''' count even numbers in a list '''

# arr = [10,20,50,55,77]
# arr = list(map(int, input("Enter numbers (comma separated): ").split(",")))
# e_count = 0
# o_count = 0

# for i in arr:
#     if i%2 == 0:
#         e_count += 1
#     else:
#         o_count += 1
# print("Even = ",e_count)
# print("Odd = ",o_count)

# # 33. Multiply all elements
# arr = [1, 2, 3, 4]
# m = 1

# for i in arr:
#     m *= i

# print(m)

# print dictionary key

d = {"a":1,"b":2}
# for key in d:
#     print(key)

# print dictionary values

# for val in d.values():
#     print(val)

# print keys and value pair

# for k,v in d.items():
#     print(k,v)

''' print ascii values '''

# for ch in "ABC":
#     print(ord(ch))

''' convert ascii to character '''

# for i in range(65,70):
#     print(chr(i), end=',')


#  45. Count words in string
# s = "hello world python"
# print(len(s.split()))

# find max in list

# arr = [1,2,11,55,0]
# m = arr[0]
# for i in arr:
#     if i > m:
#         m = i
# print(m)

#  49. Print index and value
# arr = [10, 20, 30]

# for i in range(len(arr)):
#     print(i, arr[i])

# for i in range(5):
#     for j in range(5):
#         print("*", end=" ")
#     print()


# palindrome check

# n = int(input("Enter any number: "))
# if str(n) == str(n)[::-1]:
# a = input("Enter anything: ")
# if a == a[::-1]:
#     print(a, "is palindrome")
# else:
#     print("Not palindrome")

# check prime

n = int(input("Enter any number: "))

if n > 0:
    for i in range(2,n):
        if n%i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")