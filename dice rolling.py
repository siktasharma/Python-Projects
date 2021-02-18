import numpy as np 
while True:
    df = int(input('Enter the number of dices to be rolled - '))
    df=int(df)
    for x in range(0, df):
        x=np.random.randint(1,7)
        print(x)
    t = input('Do you want to continue the rolling (y/n) - ')
    if t.lower()=='n':
        break
    elif t.lower!='y':
        print('Please type either y or n')



