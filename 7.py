"""
7. Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому.
"""
import collections


def list_counter(*arg_1):
    counter = collections.Counter(*arg_1)
    for k, v in counter.items():
        print("result: {0} -> {1} times.".format(k, v))


while True:
    try:
        print("input through ','")
        arg_list_in = list(input("enter any number of characters: ").split(","))
        # arg_list_in = [1,1,1,2,"*","*","k","k"]
        list_counter(arg_list_in)

        print("*" * 57)
        yes = input('if you want to leave the program press "Y" if not then "N": ')
        print("*" * 57)
        if "y" == yes.lower():
            break
        else:
            continue
    except:
        print("error")
