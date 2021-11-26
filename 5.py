"""
5. Написати функцію < fibonacci >, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.
"""


def fibonacci(arg_1):
    if int(arg_1) > 0:
        fibo_list = []
        num_fibo_1 = num_fibo_2 = 1
        for i in range(1, arg_1 + 1):
            if i == 1:
                fibo_list.append(i)
                if i == 1:
                    fibo_list.append(i)
            num_fibo_1, num_fibo_2 = num_fibo_2, num_fibo_1 + num_fibo_2
            fibo_list.append(num_fibo_2)
        print(fibo_list)
    else:
        print("you entered an invalid value.")


while True:
    try:
        num_fibo = int(input("enter a number to get fibonacci numbers : "))
        fibonacci(num_fibo)

        print("*" * 57)
        yes = input('if you want to leave the program press "Y" if not then "N": ')
        print("*" * 57)
        if "y" == yes.lower():
            break
        else:
            continue
    except:
        print("error")
