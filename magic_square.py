'''This program returns a magic square table whose sum is same by adding through columns, rows as well as diagonals'''

#Defining an array with 9 elements
square=[[0,0,0],[0,0,0],[0,0,0]]
#Defining a function for printing the square
def print_sq(arr):
    for i in range(3):
        for j in range(3):
            print(arr[i][j],end=' ')
        print('\n')

#Defining a function for position changing
def pos_change(x,y):
    if x!=0:
        x1=x-1
    else:
        x1=2
    if y!=2:
        y1=y+1
    else:
        y1=0
    if square[x1][y1]!=0:
        x,y=down(x,y)
        return x,y
    else:
        return x1,y1

#Defining a function if the current position is occupied
def down(x,y):
    if x==2:
        x=0
    else:
        x=x+1
    return x,y

#Setting x and y as position
x=0
y=1

#For loop for inserting elements in the square
for i in range(9):
    square[x][y] = i + 1
    x, y= pos_change(x, y)
    print_sq(square)
    print('\n')
print_sq(square)