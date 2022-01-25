# def collatz(number):
#     if number % 2 == 0:
#         return number // 2
#     elif number % 2 == 1: #计算奇数的方法
#         return 3 * number + 1
#     else:
#         return
#
# a = 0
#
# while a != 1:
#     try:
#         a = int(input("请输入一个整数： "))
#         print(collatz(a))
#     except ValueError:
#         print('请输入一个整数')

# spam = ['cat', 'bat', 'rat', 'elephant']
# print(spam[0])
# print([1, 2, 3, None, 5][3])

cat = []
while True:
    print('enter the name' + str(len(cat) + 1) + ' tostop: ')
    name = input()
    if name == '':
        break
    cat += [name] #list加法:cat + ['a'] 可执行
print('the cat name is: ')
for name in cat:
    print(' ' + name)

# print('hello',cat[2])
# print(cat + ['a'])





