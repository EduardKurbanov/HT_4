"""
1. Написати функцію < square > , яка прийматиме один аргумент - сторону квадрата,
    і вертатиме 3 значення (кортеж): периметр квадрата, площа квадрата та його діагональ.
"""


def square(arg_1):
    if float(arg_1) > 0:
        per_s = arg_1 * 4
        area_s = arg_1 ** 2
        diagonal_s = (arg_1 ** 2 + arg_1 ** 2) ** 0.5
        square_list = [per_s, area_s, diagonal_s]
        return tuple(square_list)
    else:
        print("side of a square cannot be negative ")


while True:
    try:
        square_arg = float(input("enter the side of the square : "))
        print(square(square_arg))

        print("*" * 57)
        yes = input('if you want to leave the program press "Y" if not then "N": ')
        print("*" * 57)
        if "y" == yes.lower():
            break
        else:
            continue
    except:
        print("error")
