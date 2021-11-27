"""
4. Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона,
    і вертатиме список простих чисел всередині цього діапазона
"""
from math import sqrt

def is_prime(arg_1, arg_2):
    list_prime = []
    for i in range(arg_1, arg_2 + 1):
        prime_number = True
        for j in range(2, i):
            if (i % j == 0):
                prime_number = False
        if prime_number:
            list_prime.append(int(i))
            # print(i)
    return list_prime


while True:
    try:
        arg_1 = int(input("enter the first number of the range: "))
        arg_2 = int(input("enter the second number of the range: "))
        if arg_1 >= 2 and arg_2 >= 2:
            print(is_prime(arg_1, arg_2))
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
