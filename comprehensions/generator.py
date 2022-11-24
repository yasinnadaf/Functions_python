# Generator Comprehension
if __name__ == '__main__':
    even_list = [x for x in range(0, 11, 2)]
    print("Even numbers", even_list)
    odd_set = (var + 1 for var in even_list)
    for var1 in odd_set:
        print(var1, end=" ")