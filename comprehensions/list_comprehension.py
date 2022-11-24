# List comprehension is a way to compress our code in one single line rather than multiple lines present in there

# without using list comprehension
a = []
for i in range(5):
    f = i * i
    a.append(f)
print(a)

# using list comprehension we compress our code in single line
sq = [i * i for i in range(5)]
print('using list comprehension', sq)

# if condition
d = [i for i in range(1, 50) if i % 7 == 0]
print(d)
print()

# if else
number = [num if num < 5 else num * 2 for num in range(2, 9)]
print(number)
print()

values = [23, 44, 54, 67, 30, 60, 36]
a = [val for val in values if val % 3 == 0]
print(a)

# nested for loop
result = [x*y for x in [10, 5, 2] for y in [2, 3, 4]]
print(result)
