"""Printing even numbers from 0 to max_number"""


def only_even(max_number: int):
    for i in range(max_number):
        if i % 2 == 0:
            yield print(i)


""" for checking """

even_numbers = only_even(10)

next(even_numbers)
next(even_numbers)
next(even_numbers)
next(even_numbers)
next(even_numbers)



"""Printing New Year tree with given width"""


def new_year_tree(width: int):
    now_width = 1
    while now_width <= width:
        branch = '*' * now_width
        yield print(branch.center(width))  # printing branch (current length line)
        now_width += 2


""" for checking """

my_tree = new_year_tree(20)

next(my_tree)
next(my_tree)
next(my_tree)
next(my_tree)
next(my_tree)
next(my_tree)
next(my_tree)
next(my_tree)
next(my_tree)
next(my_tree)


"""Printing stairs with given stairs width"""


def stairs(stairs_width: int):
    current_step_number = 1
    while current_step_number <= stairs_width:
        yield print('_' * (current_step_number + 1) + '\n' + ' ' * current_step_number + '|')
        current_step_number += 3


""" for checking """

my_stairs = stairs(20)

next(my_stairs)
next(my_stairs)
next(my_stairs)
next(my_stairs)
next(my_stairs)
next(my_stairs)
next(my_stairs)


