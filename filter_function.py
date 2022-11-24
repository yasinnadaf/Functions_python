if __name__ == '__main__':
    def check_condition(a):
        if a >= 3:
            return a


    f = filter(check_condition, [1, 2, 3, 4, 5])
    print(tuple(f))


# using lambda function
l = filter(lambda x: (x >= 3), [1, 2, 3, 4, 5])
print('using lambda function', tuple(l))


# result contains odd numbers of the list
seq = [0, 1, 2, 3, 5, 8, 13]

result = filter(lambda x: x % 2 != 0, seq)
print("odd numbers are: ", list(result))