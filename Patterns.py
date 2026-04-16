# # n = 5
# n = int(input("Enter number: "))
# for i in range(5):
#     print("*" * n)

# right angle triangle
'''
n = 5
for i in range(1, n+1):
    print("*" * i)
    '''

# Reverse right triangle
'''
n = 5
for i in range(n, 0, -1):
    print("*" * i)
'''

# 4. Pyramid Pattern
'''
n = 5
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
    
'''

# inverted Pyramid
'''
n = 5
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
'''

# 6. Left Triangle Pattern
'''
n = 5
for i in range(1, n+1):
    print(" " * (n - i) + "*" * i)
'''

# 7 . reverse left triangle
'''
n = 5
for i in range(n, 0, -1):
    print(" " * (n-i) + "*" * (i-1))
'''

# 8. diamond pattern
'''
n = 50
for i in range(n):
    print(" " * (n-i-1) + "*" * (2*i+1))

for i in range(n-2,-1,-1):
    print(" " * (n-i) +  "*" * (2*i-1))
'''

# Binary Right triangle

n = 5
for i in range(1,n+1):
    for j in range(i):
        print((i+j)%2, end='')
    print()

