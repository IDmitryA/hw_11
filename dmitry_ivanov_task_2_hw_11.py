"""
This function takes 3 arguments: 'func' (def f(): ... or lambda ...), 'iterable' (any iterable object)
and 'initializer' (optional argument, if the 'initializer' is present, is placed before the items of
the 'iterable') and return accumulated value according to 'func'.
"""


def my_reduce(func, iterable, initializer=None):
    current_iterable = iterable[::]

    # Next conditions are necessary for correct 'initializer' adding
    if '__iter__' in dir(initializer):  # if 'initializer' is iterable object
        position = 0
        for i in initializer:
            current_iterable.insert(position, i)
            position += 1
    elif not (initializer is None):  # if 'initializer' isn't 'None' and not iterable object
        current_iterable.insert(0, initializer)
    # if- and elif- branches don't make any computation, but raise/return fixed values
    if len(current_iterable) == 0:
        raise TypeError('reduce() of empty sequence with no initial value')
    elif len(current_iterable) == 1:
        answer = current_iterable
        return answer
    # else- branch return accumulated value according to 'func'
    else:
        accumulated_value = current_iterable[0]
        for i in range(1, len(current_iterable)):
            accumulated_value = func(accumulated_value, current_iterable[i])
            if i == (len(current_iterable)-1):
                answer = accumulated_value
    return answer


def my_sum(a, b):
    return a + b


def factorial(a, b):
    return a * b


def biggest(a, b):
    if a > b:
        return a
    else:
        return b


python_list = ['P', 'y', 't', 'h', 'o', 'n']
my_list = [1, 2, 9, 4, 5, 3]
my_tuple_list = (1, 2, 3, 10, 4, 5)
jast_a = 'A'
blanc_list = []

"""-----------------------------------------------------------------------"""

print(my_reduce(my_sum, my_list, 5))  # 29
print('-' * 100)
print(my_reduce(factorial, my_list))  # 1080
print('-' * 100)
print(my_reduce(biggest, my_list))  # 9
print('-' * 100)
print(my_reduce(my_sum, python_list, 'I study '))  # I study Python
print('-' * 100)
print(my_reduce(lambda a, b: a + b, python_list))  # Python
print('-' * 100)
print(my_reduce(lambda a, b: a if a > b else b, my_list, 18))  # 18
print('-' * 100)
print(my_reduce(lambda a, b: a if a > b else b, my_tuple_list))  # 10
print('-' * 100)
print(my_reduce(lambda a, b: a + b, jast_a))  # A
print('-' * 100)
print(my_reduce(lambda a, b: a if a > b else b, blanc_list))  # TypeError: reduce() of empty sequence with no
                                                              # initial value









