from time import sleep

"""
So, 'tester()' is decorator, which takes 'my_reduce' as argument. 'tester()' includes 'test_dict', which items 
are 'expected meaning': ('func', iterable', 'initializer'). 'my_reduce()' takes values of test_dict and if
execution result == corresponding keys we can see congratulatory text - 'Wow, my_reduce() works great!!!'.
"""


def tester(func_reduce):
    def wrapper():
        # next lists and dict just for testing
        python_list = ['P', 'y', 't', 'h', 'o', 'n']
        my_list = [1, 2, 9, 4, 5, 3]
        # test_dict = {'expected meaning': ('func', iterable', 'initializer'), ... }
        test_dict = {
            29: (lambda a, b: a + b, my_list, 5),
            1080: (lambda a, b: a * b, my_list),
            9: (lambda a, b: a if a > b else b, my_list),
            'I study Python': (lambda a, b: a + b, python_list, 'I study '),
            'Python': (lambda a, b: a + b, python_list),
            18: (lambda a, b: a if a > b else b, my_list, 18)
        }

        print('test starting')
        sleep(3)
        result_and_reduce_arguments = test_dict.items()

        for i in result_and_reduce_arguments:
            assert func_reduce(*i[1]) == i[0], 'no-no-no, something going wrong'

        print('test finished')
        sleep(1)
        print(f'Wow, my_reduce() works great!!!')

    return wrapper


@tester
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


my_reduce()










