# wap to print 1 to 10 using while loop

# n = int(input("Enter a number: "))
# i = 1
# while i <= n:
#     print(i)
#     i += 1

'''
wap to print even numbers from 1 to 20 using while loop
'''

# n = int(input("Enter a number: "))
# i = 2
# while i <= n:
#     print(i)
#     i += 2

'''
wap to print reverse of a number using while loop
'''
n = int(input("Enter a number: "))
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10
print(reverse)