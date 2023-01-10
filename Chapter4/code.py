#Comma Code

def fn(*list):
    for i in range(len(list)):
        if i<(len(list)-1):
            print(list[i], end= ",")
        else:
            print("and", list[i])
fn(*['apples', 'bananas', 'tofu', 'cats'])

#Coin Flip Streaks

import random
numberOfStreaks = 0
list=[]
count=1
freq=[]
ele=[]
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    a= random.randint(0,1)
    
    if a==0:
        list.append('H')
    else:
        list.append('T')
# print(list)
    # Code that checks if there is a streak of 6 heads or tails in a row.
for i in range(len(list)-1):
    if list[i]== list[i+1]:
        count+=1
    else:
        freq.append(count)
        ele.append(list[i])
        count=1
freq.append(count)
ele.append(list[i+1])
# print(ele, freq)
numberOfStreaks= freq.count(6)
print('Chance of streak: %s%%' % (numberOfStreaks / 100))


#Character Picture Grid

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for i in range(len(grid[0])):
    for j in range(len(grid)):
        print(grid[j][i], end="")
    print()

