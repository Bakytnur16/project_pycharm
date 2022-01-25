def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1: #计算奇数的方法
        return 3 * number + 1
    else:
        return

a = 0

while a != 1:
    try:
        a = int(input("请输入一个整数： "))
        print(collatz(a))
    except ValueError:
        print('请输入一个整数')



