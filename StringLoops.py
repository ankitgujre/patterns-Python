# print each characters of string

# str = input("Enter a string: ")
# # count = 0
# for char in str:
#     # count += 1
#     print(char)
# # print("the length of the string is : ", count)
# print("the length of the string is : ", len(str))

# print each characters of string using while loop
# str = input("Enter a string: ")
# i = 0
# while i < len(str):
#     print(str[i])
#     i += 1

# print each characters of string using function

# def printChar(str):
#     for char in str:
#         print(char)
#     print("the length of the string is : ", len(str))
# str = input("Enter a string: ")
# printChar(str)

# print each characters of string using recursion

# def printChar(str, index):
#     if index < len(str):
#         print(str[index])
#         printChar(str, index + 1)
# str = input("Enter a string: ")
# printChar(str, 0)

# print count vowels in a string

# s = input("Enter a string: ")
# vowels = 'aeiouAEIOU'
# count = 0
# for char in s:
#     if char in vowels:
#         count += 1
#     elif char not in  vowels:
#         print("the character is not a vowel : ", char)
# print("The number of vowels in the string is: ", count)

'''
Reverse string
'''

# s = input("Enter a string: ")
# reverse = ""
# for char in s:
#     reverse = char + reverse
# print("original string: ", s)
# print(reverse)

# print(s[::-1])

'''
Count uppercase and lowercase characters in a string
'''

# s = input("Enter a string: ")
# upper_count = 0
# lower_count = 0
# for char in s:
#     if char.isupper():
#         upper_count += 1
#     elif char.islower():
#         lower_count += 1
# print("Number of uppercase characters: ", upper_count)
# print("Number of lowercase characters: ", lower_count)

'''
check if a string is palindrome or not
'''
# s = input("Enter a string: ").lower()
# reverse = s[::-1]
# if s == reverse:
#     print("The string is a palindrome")
# else:
#     print("The string is not a palindrome")

'''
WAP TO REMOVE SPACES FROM A STRING
'''
# s = input("Enter a string: ")
# new_s = ""
# for char in s:
#     if char != " ":
#         new_s += char
# print(new_s)

'''
character frequency in a string
'''
# s = input("Enter a string: ")
# freq = {}
# for char in s:
#     if char in freq:
#         freq[char] += 1
#     else:
#         freq[char] = 1
# print(freq)

'''
non repeating characters in a string
'''
# s = input("Enter a string: ")
# for char in s:
#     if s.count(char) == 1:
#         print("the non repeating character is : ", char)
#         break
# else:
#     print("no non repeating character found")

'''
count words in a string
'''

# s = input("Enter a string: ")
# words = s.split()
# print(words)
# print("the number of words in the string is : ", len(words))

''' Remove duplicate characters from a string '''
# s = input("Enter a string: ")
# new_s = ""
# for char in s:
#     if char not in new_s:
#         new_s += char
# print(new_s)


''' Count the occurrence of a specific character in a string '''
# s = input("Enter a string: ")
# char = input("Enter a character: ")
# count = 0
# for c in s:
#     if c == char:
#         count += 1
# print("the number of occurrences of the character is : ", count)

''' Check if a string contains only digits '''
# s = input("Enter a string: ")
# if s.isdigit():
#     print("The string contains only digits")
# else:
#     print("The string does not contain only digits")

'''
compress a string
'''
s = input("Enter a string: ")
compressed = ""
count = 1
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        compressed += s[i - 1] + str(count)
        count = 1
compressed += s[-1] + str(count)
print(compressed)

