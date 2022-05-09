def decorative_function(func):
    def cont1(values1):
        return [func(value[0], value[1]) for value in values1]
    return cont1


@decorative_function
def num1(a, b):
    print(a * b)

print(num1([(50, 2), (45, 3), (30, 5)]))    