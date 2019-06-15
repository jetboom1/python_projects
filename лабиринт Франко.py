'''
4 4
. . x .
k . x m
. . x .
. . . .
'''

import copy
def printmassive(c):
    for i in range(n+2):
        for j in range(m+2):
            print(c[i][j],end=' ')
        print()
n,m=map(int, input().split())
b=[list(map(str,input().split())) for i in range(n)]
a=[['x']*(m+2) for i in range(n+2)]
                      #Создаем ничего, полный ничем, чтобы внутрь него вставить ничего
queue=[]
for i in range(1,n+1):
    for j in range(1,m+1):
        a[i][j]=b[i-1][j-1]
                      #Лабиринт вставляется внутрь списка из Х
print("Ваш лабиринт: ")
printmassive(a)
for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i][j]=='k':
            a[i][j]=1
            queue.append([i,j])
        elif a[i][j]=='m':
            x1=i
            x2=j
print(' ')
                                             

print("Конечный вариант: ",end='\n')
                                            #Поиск пути:
while queue!=[] and (queue[0][0]!=x1 or queue [0][1]!=x2):
    i=queue[0][0]
    j=queue[0][1]
    k=a[i][j]
    if a[i-1][j]=='.':
        a[i-1][j]=k+1
        queue.append([i-1,j])
    if a[i+1][j]=='.':
        a[i+1][j]=k+1
        queue.append([i+1,j])
    if a[i][j-1]=='.':
        a[i][j-1]=k+1
        queue.append([i,j-1])
    if a[i][j+1]=='.':
        a[i][j+1]=k+1
        queue.append([i,j+1])
    if a[i][j+1]=='m' or a[i][j-1]=='m' or a[i-1][j]=='m' or a[i+1][j]=='m':
        break
    else:
        queue.pop(0)
if queue==[]:
    print("Выхода нет!")
    printmassive(a)
else:
    print()
    printmassive(a)
    print()
    print("Шагов выполнено: ",k)
    print()
    print()
    i=queue[0][0]
    j=queue[0][1]
                                            #Строю путь
                                            #Копирую список для построения пути
    c=copy.deepcopy(a)
    while True:
        i=queue[0][0]
        j=queue[0][1]
        if a[i-1][j]==a[i][j]-1:
            c[i][j]="|"
            queue.append([i-1,j])
            queue.pop(0)
        elif a[i+1][j]==a[i][j]-1:
            c[i][j]="|"
            queue.append([i+1,j])
            queue.pop(0)
        elif a[i][j-1]==a[i][j]-1:
            c[i][j]="|"
            queue.append([i,j-1])
            queue.pop(0)
        elif a[i][j+1]==a[i][j]-1:
            c[i][j]="|"
            queue.append([i,j+1])
            queue.pop(0)
        if a[i][j+1]==1 or a[i][j-1]==1 or a[i-1][j]==1 or a[i+1][j]==1:
            print('Пройденный путь:')
            printmassive(c)
            break
        
