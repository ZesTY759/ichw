"""currency.py: To convert one currency into another at an exchange rate.
__author__ = "Zhang Tianyu"
__pkuid__  = "1800011759"
__email__  = "1800011759@pku.edu.cn"
"""

import turtle

def tile(m,n,a,b,alls=[],row=0,colume=0,lst=[],ans=[]):
    '''Cover a given size wall with a given size brick.
    m,n are int:size of wall
    a,b are int:size of brick
    row is a int:current row
    colume is a int:current colume
    lst is a list:stores the laying of wall
    ans is a list:stores the coordinates of existing bricks
    return alls is a list:solution of this question'''
    if lst == []:
        lst = [0] * (m*n)
    if colume == m:
        row += 1
        colume = 0
    if 0 not in lst:
        alls.append(ans[:])
    else:
        if ((row*m) + colume) < (m*n) and lst[row*m+colume] == 1:
            tile(m,n,a,b,alls,row,colume+1,lst,ans)
        else:
            if query(m,n,a,b,row,colume,lst):
                ls = lst[:]
                an = ans[:]
                record(m,a,b,row,colume,ls,an)
                tile(m,n,a,b,alls,row,colume+1,ls,an)
            if query(m,n,b,a,row,colume,lst):
                ls = lst[:]
                an = ans[:]
                record(m,b,a,row,colume,ls,an)
                tile(m,n,a,b,alls,row,colume+1,ls,an)
            
def record(m,a,b,row,colume,ls,an):
    '''Record the coordinates of the bricks and the laying of wall
    m is a int:width of the wall
    a,b are int:size of brick
    row is a int:current row
    colume is a int:current colume
    ls is a list:stores the laying of wall
    an is a list:stores the coordinates of existing bricks
    return an is a list:add a coordinates of newly laid bricks to an'''
    re=()
    for j in range(row,row+b):
        for k in range(colume,colume+a):
            serial_number = j*m + k
            ls[serial_number] = 1
            re = re + (serial_number,)
    an.append(re)

def query(m,n,a,b,row,colume,lst):
    '''Query whether the target location is occupied.
    m,n are int:size of wall
    a,b are int:size of brick
    row is a int:current row
    colume is a int:current colume
    lst is a list:stores the laying of wall
    return a bool:False for occupy,True for vacancy'''
    if (colume+a) > m or (row+b) > n:
        return False
    for j in range(row,row+b):
        for k in range(colume,colume+a):
            serial_number = j*m + k
            if lst[serial_number] == 1:
                return False
    return True

def visualization_wall(m,n,alex0):
    '''Visualize the wall.
    m,n are int:size of wall
    alex0 is a turtle for wall
    return a screen:displays the wall
    '''
    serial=0
    for row in range(n):
        for colume in range(m):
            alex0.up()
            alex0.goto(20*colume+10,-(20*row+17))
            alex0.write(serial,False,align="center")
            serial+=1
    alex0.hideturtle()
            
def visualization(m,n,solution,choice,alex):
    '''Visualize the solution selected by the user.
    m,n are int:size of wall
    solution in a list:all of the solution
    choice is a int:the solution chosen by the user
    alex is a turtle for bricks
    return a screen:displays the graph of the solution'''
    sol = solution[choice]
    for v in sol:
        first = v[0]
        last = v[-1]
        y0 = first//m
        x0 = first%m
        y1 = (last//m)+1
        x1 = (last%m)+1
        alex.up()
        alex.goto((x0*20),-(y0*20))
        alex.down()
        alex.goto((x0*20),-(y1*20))
        alex.goto((x1*20),-(y1*20))
        alex.goto((x1*20),-(y0*20))
        alex.goto((x0*20),-(y0*20))

def main():    
    '''the main modle'''
    wall = input('请输入墙的尺寸(形如3*2)：',).split('*')
    brick = input('请输入砖的尺寸(形如2*1)：',).split('*')
    m,n = int(wall[0]),int(wall[1])
    a,b = int(brick[0]),int(brick[1])
    solution = []
    tile(m,n,a,b,solution)
    print('有{0}种解法，分别为:'.format(len(solution)))
    for (num,sol) in enumerate(solution):
        print('解法{0}：{1}'.format(num,sol))
    if  solution != []:
        alex = turtle.Turtle()
        alex0 = turtle.Turtle()
        visualization_wall(m,n,alex0)
        while True:
            choice_str = input('请输入您想使用的解法编号:',)
            if choice_str == '':
                print('Good bye!')
                break
            if not choice_str.isdigit():
                print('请用正整数表示编号，请重新输入编号')
                continue
            elif int(choice_str) >= len(solution) or int(choice_str) < 0:
                print('编号超出了种类总数，请重新输入编号（0<=x<={0}）'.format(len(solution)-1))
                continue
            else:
                choice_int = int(choice_str)
                alex.clear()
                visualization(m,n,solution,choice_int,alex)   
        turtle.done()
    
if __name__ == '__main__':
    main()
