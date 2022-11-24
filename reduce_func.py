from functools import reduce


if __name__ == '__main__':
    def calculate(a, b):
        return a + b

    result = reduce(calculate, [1, 2, 3, 4, 5])
    print(result)

    # using lambda function
    l = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
    print("using lambda function-> ", l)

    list1 = [1, 2, 3, 4, 2]
    num = reduce(lambda x, y: x * y, list1)
    print(num)

