if __name__ == '__main__':
    def cube(number):
        return number ** 3


    iter = [2, 4, 5]
    result = map(cube, iter)
    print(list(result))

#     ----->  using lambda function   <------
result1 = map(lambda x: x ** 3, [2, 4, 5])
print('using lambda func lambda->', list(result1))