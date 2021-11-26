"""
8. Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку.
    Тобто, функція приймає два аргументи: список і величину зсуву (якщо ця величина додатня - пересуваємо з кінця на початок,
    якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).

       Наприклад:

           fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]

           fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]
"""


def array_shift(args, shift=1):
    list_int = []
    if len(args) - 1 >= shift >= 0:
        list_len = len(args)
        new_list = args[list_len - shift:] + args[:-list_len - shift + list_len]
        for i in new_list:
            list_int.append(int(i))
        print(list_int)

    elif (-len(args) + 1) <= shift <= 0:
        list_len = len(args)
        new_list = args[-(shift + list_len):] + args[:-(shift + list_len)]
        for i in new_list:
            list_int.append(int(i))
        print(list_int)

    else:
        print("the shift is greater than the length of the array:")


while True:
    try:
        arg_list = list(input("enter the side of the square : ").split(","))
        arg_shiht = int(input("enter the side of the square_1: "))
        array_shift(arg_list, arg_shiht)

        print("*" * 57)
        yes = input('if you want to leave the program press "Y" if not then "N": ')
        print("*" * 57)
        if "y" == yes.lower():
            break
        else:
            continue
    except:
        print("error")
