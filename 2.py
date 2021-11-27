"""
2. Написати функцію < bank > , яка працює за наступною логікою:
    користувач робить вклад у розмірі < a > одиниць строком на < years > років під < percents >
    відсотків (кожен рік сума вкладу збільшується на цей відсоток,
    ці гроші додаються до суми вкладу і в наступному році на них також нараховуються відсотки).
    Параметр < percents > є необов'язковим і має значення по замовчуванню < 10 > (10%).
    Функція повинна принтануть і вернуть суму, яка буде на рахунку.
"""


def bank(arg_money, arg_years, arg_percent):
    if (arg_money > 0) and (arg_years > 0) and (100 >= float(arg_percent) >= 10):
        arg_percent_p = float(arg_percent) / 100.0
        for i in range(1, arg_years + 1):
            arg_money_d = arg_money * arg_percent_p
            arg_money += arg_money_d
            print(f"{i} years to {arg_percent}% -> {arg_money:.2f} $")
    else:
        print("<<error>>")


while True:
    # try:
        print("deposit account:")
        arg_money = float(input("enter funds: "))
        arg_years = int(input("enter the deposit for how many full years: "))
        arg_percent = input("enter a percentage rate of at least 10%: ")
        print(type(arg_percent))
        if arg_percent in (0, 0.0, "", " ", None) or float(arg_percent) <= 10.0:
            arg_percent = 10.0

        bank(arg_money, arg_years, arg_percent)

        print("*" * 57)
        yes = input('if you want to leave the program press "Y" if not then "N": ')
        print("*" * 57)
        if "y" == yes.lower():
            break
        else:
            continue
    # except:
    #     print("error")
