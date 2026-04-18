# wap to interchange first and last element of a list
# lst = [1, 2, 3, 4, 5]
# lst[0], lst[-1] = lst[-1], lst[0]
# print(lst)

# using function

# def swap(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
# lst = [1, 2, 3, 4, 5]
# print(swap(lst))

# using recursion
def swap(lst, start, end):
    if start >= end:
        return lst
    lst[start], lst[end] = lst[end], lst[start]
    return swap(lst, start + 1, end - 1)
lst = [1, 2, 3, 4, 5]
print(swap(lst, 0, len(lst) - 1))