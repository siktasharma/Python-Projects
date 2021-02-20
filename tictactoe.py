import numpy as np 
import pandas as pd 
matrix=np.zeros((3,3))
print(matrix)
def row_match():
    player_won=0
    for i in matrix:
        if i[0]==i[1]==i[2]:
            player_won=i[0]
            break
    return player_won

def col_match():
    mat=matrix.transpose()
    player_won=0
    for i in mat:
        if i[0]==i[1]==i[2]:
            player_won=i[0]
            break
    return player_won

def dia_match():
    player_won=0
    if matrix[0,0]==matrix[1,1]==matrix[2,2]:
        player_won=matrix[0,0]
    elif matrix[0,2]==matrix[1,1]==matrix[2,0]
    return player_won
   
player_num=1
i=0
while True: 
    print('Player {}s turn'.format(player_num))
    x = int(input('Enter the x Coordinate - '))
    y= int(input('Enter the y Coordinate - '))
    x= x-1
    y= y-1
    if matrix[x,y]==player_num:
        print('ERROR: Please put another coordinates')
        continue
    else:
        matrix[x,y]=player_num
        print(matrix)
        i=i+1
    r=row_match()
    c=col_match()
    d=dia_match()
    if r!=0:
        print('Player {} has won!'.format(r))
        break
    elif c!=0:
        print('Player {} has won!'.format(r))
        break
    elif d!=0:
        print('Player {} has won!'.format(r))
        break
    if player_num==1:
        player_num=2
    else:
        player_num=1
    if i==9:
        break




