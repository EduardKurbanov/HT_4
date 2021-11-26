"""
6. Вводиться число. Якщо це число додатне, знайти його квадрат, якщо від'ємне, збільшити його на 100, якщо дорівнює 0, не змінювати.
"""


def variable_value_function(arg_1):
    if float(arg_1) > 0:
        print("squaring a number {0}^2 -> {1}".format(arg_1, arg_1 ** 2))
    elif float(arg_1) < 0:
        print("increase the number {0} by 100 -> {1}".format(arg_1, arg_1 - 100))
    elif float(arg_1) == 0:
        print("you entered {0} will remain {0}".format(arg_1))
    else:
        print("you entered not a number.")


while True:
    try:
        num_arg = float(input("enter any number: "))
        variable_value_function(num_arg)

        print("*" * 57)
        yes = input('if you want to leave the program press "Y" if not then "N": ')
        print("*" * 57)
        if "y" == yes.lower():
            break
        else:
            continue
    except:
        print("error")