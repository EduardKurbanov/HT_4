"""
3. Написати функцию < is_prime >, яка прийматиме 1 аргумент - число від 0 до 1000,
    и яка вертатиме True, якщо це число просте, и False - якщо ні.
"""
from math import sqrt

def is_prime(arg_1):
    if arg_1 < 2:
        return False
    if arg_1 == 2:
        return True
    limit = sqrt(arg_1)
    i = 2
    while i <= limit:
        if arg_1 % i == 0:
            return False
        i += 1
    return True


while True:
    try:
        arg_1 = int(input("enter the number: "))
        if arg_1 >= 2:
          print(is_prime(arg_1))
        else:
            print("<<error_input>>")
            continue

        print("*" * 57)
        yes = input('if you want to leave the program press "Y" if not then "N": ')
        print("*" * 57)
        if "y" == yes.lower():
            break
        else:
            continue
    except:
        print("error")
