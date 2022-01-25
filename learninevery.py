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

# cat = []
# while True:
#     print('enter the name' + str(len(cat) + 1) + ' tostop: ')
#     name = input()
#     if name == '':
#         break
#     cat += [name] #list加法:cat + ['a'] 可执行
# print('the cat name is: ')
# for name in cat:
#     print(' ' + name)

# print('hello',cat[2])
# print(cat + ['a'])

# supplies = ['pens','staplers', 'flame-throws', 'binders']
# for i in range(len(supplies)):
#     print(i)
#     print('Index ' + str(i) + ' in spplies is： ' + supplies[i])

#技巧：多重赋值
#比如
# dog = [1,2,3]
# size = dog[0]
# color = dog[1]
# weight = dog[2]
#可以写成
# size,color,weight = dog#但是变量的数目和列表的长度必须严格相等
# print(size, color, weight)

#append 末尾加，insert 指定加
# dog.append(4)
# dog.insert(0, 0) 序列 变量值


import random

messages = ['It is certain',
            'It is decidedly so',
            'Yes definitely',
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again'
            'My reply is no',
            'Outlook not so good',
            'Very doubtful'
            ]
# print(messages[random.randint(0, len(messages) - 1)])

# sentence = '我喜欢睡觉。'
# a = list(sentence)
# b = tuple(sentence)
# print(a,b)
spam =[0,1, 2, 3, 4]
# cheese = spam
# cheese[1] = 'hello'
# print(spam, cheese)
# import copy
# spam =[0,1, 2, 3, 4,[3,4]]
# cheese = copy.deepcopy(spam)
# cheese[1] = 42
print(spam[:2])

# list = []
# for i in range(0,len(sentence)):
#     list += sentence[i]
# a = tuple(list)
# print(list(a))

# for i in range(len(list)):
#     a = random.randint(list)
#     print(a)

# name = 'shuak'
#
# for i in name:
#     print('******{i}*******')





