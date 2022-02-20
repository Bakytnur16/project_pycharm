# # 4.10.1
def Tostr(list):
    for i in range(0,len(list)):
        if list[i] == list[-1]:
            print('and',list[i])
        else:
            print(list[i],end=', ')

spam = ['apples', 'bananas', 'tofu', 'cats','bear']
# print(Tostr(spam))
Tostr(spam)

#4.10.2

grid = [['.', '.', '.', '.', '.', '.'],  
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
for x in range(len(grid) - 3):
    for y in range(len(grid[x]) + 2):
        print(grid[y][x],end=' ')
    print(grid[8][x])
 

# 计算文本的每个字符的出现次数
from sys import argv
script, filename = argv
def countTxt(message):
    count = {}
    for character in message:
        count.setdefault(character, 0)
        count[character] = count[character] + 1
    print(count)

a = open(filename)
countTxt(a.read())
