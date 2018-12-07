"""currency.py: To convert one currency into another at an exchange rate.
__author__ = "Zhang Tianyu"
__pkuid__  = "1800011759"
__email__  = "1800011759@pku.edu.cn"
"""

import turtle

def tile(m,n,a,b,alls=[],l=0,i=0,lst=[],ans=[]):
    '''Cover a given size wall with a given size brick.
    m,n are int:size of wall
    a,b are int:size of brick
    l is a int:current row
    i is a int:current colume
    lst is a list:stores the laying of wall
    ans is a list:stores the coordinates of existing bricks
    return alls is a list:solution of this question
    '''
    if lst==[]:
        lst=[0]*(m*n)
    if i==m:
        l+=1
        i=0
    if (0 not in lst) and (ans not in alls):
        alls.append(ans[:])
    if ((l*m)+i)<(m*n) and lst[l*m+i]==1:
        tile(m,n,a,b,alls,l,i+1,lst,ans)
    else:
        if query(m,n,a,b,l,i,lst):
            ls=lst[:]
            an=ans[:]
            record(m,a,b,l,i,ls,an)
            tile(m,n,a,b,alls,l,i+1,ls,an)
        if query(m,n,b,a,l,i,lst):
            ls=lst[:]
            an=ans[:]
            record(m,b,a,l,i,ls,an)
            tile(m,n,a,b,alls,l,i+1,ls,an)
            
def record(m,a,b,l,i,ls,an):
    '''Record the coordinates of the bricks and the laying of wall
    m is a int:width of the wall
    a,b are int:size of brick
    l is a int:current row
    i is a int:current colume
    ls is a list:stores the laying of wall
    an is a list:stores the coordinates of existing bricks
    return an is a list:add a coordinates of newly laid bricks to an
    '''
    re=()
    for j in range(l,l+b):
        for k in range(i,i+a):
            z=j*m+k
            ls[z]=1
            re=re+(z,)
    an.append(re)

def query(m,n,a,b,l,i,lst):
    '''Query whether the target location is occupied.
    m,n are int:size of wall
    a,b are int:size of brick
    l is a int:current row
    i is a int:current colume
    lst is a list:stores the laying of wall
    return a bool:False for occupy,True for vacancy
    '''
    if (i+a)>m or (l+b)>n:
        return False
    for j in range(l,l+b):
        for k in range(i,i+a):
            if lst[j*m+k]==1:
                return False
    return True

def visualization(m,n,solution,z):
    '''Visualize the solution selected by the user.
    m,n are int:size of wall
    solution in a list:all of the solution
    z is a int:the solution chosen by the user
    return a screen:displays the graph of the solution
    '''
    alex = turtle.Turtle()
    ms=m*30
    ns=n*30
    sol=solution[z] 
    for v in sol:
        first=v[0]
        last=v[-1]
        y0=int(first//m)
        x0=int(first%m)
        y1=int(last//m)+1
        x1=int(last%m)+1
        alex.up()
        alex.goto((x0*10),(y0*10))
        alex.down()
        alex.goto((x0*10),(y1*10))
        alex.goto((x1*10),(y1*10))
        alex.goto((x1*10),(y0*10))
        alex.goto((x0*10),(y0*10))
    

def main():    
    '''the main modle
    '''
    wall=input('请输入墙的尺寸(形如3*2)：',).split('*')
    brick=input('请输入砖的尺寸(形如2*1)：',).split('*')
    m=int(wall[0])
    n=int(wall[1])
    a=int(brick[0])
    b=int(brick[1])
    solution=[]
    tile(m,n,a,b,solution)
    print('有{0}种解法，分别为:\n{1}'.format(len(solution),solution))
    if solution!=[]:
        x=int(input('请输入您想使用的解法编号(第一种解法记为0):',))
        visualization(m,n,solution,x)
    
if __name__ == '__main__':
    main()
