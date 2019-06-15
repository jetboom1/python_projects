data,height = input().split()
height = int(height)
spacenum = height-1
num = 1
counter = 0
array = [0]*height
for i in range(height):
    array[i]=' '*spacenum+data*num
    counter +=spacenum+num
    num+=2
    spacenum-=1
print(counter)
for i in array:
    print(i)