# List Tasks
# Create a list of 10 random numbers and sort it in ascending and descending order.
# Remove all even numbers from a given list.
# Find the second_largest number in a list.
# Reverse a list without using the reverse() method.
# Remove duplicates from a list.

# Dictionary Tasks
# Create a dictionary of 5 students with their marks and find the student with the highest marks.
# Merge two dictionaries and sum values of common keys.
# Count the occurrences of each word in a given sentence using a dictionary.
# Convert two lists into a dictionary (one as keys, the other as values).
# Create a nested dictionary to store employee details (name, age, salary) and display them.


# 01:Create a list of 10 random numbers and sort it in ascending and descending order.
# def order(l):
#     l.sort()
#     print("ascending order:",l)
#     reverse=l.reverse()
#     return l
# l=[1,2,5,6,3,9,4,7,43,1]
# print("descending order :",order(l))

# 02:Remove all even numbers from a given list.
# def remove_even(l):
#     for i in l:
#         if i%2==0:
#             l.remove(i)
#         else:
#             pass
#     return l
# l=[1,2,3,4,5,6,7,8,9,10]
# print(remove_even(l))

# 03:Find the second_largest number in a list.
# def sec_maxi(l):
#     maximum=max(l)
#     sec_max= 0
#     for i in l:
#         if  sec_max < i < maximum:
#             sec_max = i
#     return sec_max,maximum
# l=[1,2,3,4,5,6,7,8,9,10]
# sec_max,maximum=sec_maxi(l)
# print("Maximum number is :",maximum)
# print("Second maximum number is :",sec_max)

# 04:Reverse a list without using the reverse() method.
# def revers(l):
#     list=[]
#     for i in range(len(l)):
#         list.append(l.pop())
#     return list
#
# l=[1,2,3,4,5,6]
# print(revers(l))

#05: write code of reverse list:
# def revers(l):
#     return l[::-1]  # Slicing method to reverse

# l = [1, 2, 3, 4, 5, 6]
# print(revers(l))
