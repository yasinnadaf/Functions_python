# dictionary comprehension

# without using dict comprehension
square_dict = dict()
for num in range(1, 11):
    square_dict[num] = num*num
print(square_dict)

# using dict comp we write this code in single line
d = {num: num * num for num in range(1, 11)}
print('using dict comp', d)
print()

# creating dict comprehension on 2lists
list2 = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat']
list1 = [1, 2, 3, 4, 5, 6, 7]
print(list1)
print(list2)

weeks = {k : v for (k, v) in zip(list1, list2)}
print(weeks)

dictionary = {x: x.upper() for x in "upper"}
print("lower letters in upper letters", dictionary)

dictionary1 = {x: x.lower() for x in "LOWER"}
print("upper letters in lower letters", dictionary1)