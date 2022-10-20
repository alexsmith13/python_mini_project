import time

Maze_Level = []
length = len(Maze_Level)

def Walking():
    time.sleep(1)
    print('Walking...')
    time.sleep(1)

def Back():
    print('Retracing steps...')
    Walking()
    if Maze_Level[-1] == Maze_Level[-2]:
        x = Maze_Level[-3]
#    elif Maze_Level[-1] == Maze_Level[len-2]:
#        x = Maze_Level[-4]
    else:
        x = Maze_Level[-1]
    x()

def Dead_End():
    print('You have reached a dead end!')
    print('You can go back to the previous junction by typing BACK')
    back = input()
    if back == 'BACK':
        Back()
    else:
        print('Invalid input. Please enter a valid command.')
        
def J1():
    Maze_Level.append(J1)
    print('You arrive at the first junction 1, you can go left or right.')
    print('Choose your direction by typing LEFT or RIGHT')
    direction = input()
    if direction == 'LEFT':
        print('Going left...')
        Walking()
        J3()
    elif direction == 'RIGHT':
        print('Going right...')
        Walking()
        J2()
    else:
        print('Invalid input. Please enter a valid direction')

def J3():
    Maze_Level.append(J3)
    print('You arrive at another junction 3, you can go left or straight')
    print('Choose your direction by typing LEFT or STRAIGHT')
    direction = input()
    if direction == 'LEFT':
        print('Going left...')
        Walking()
        Dead_End()
    elif direction == 'STRAIGHT':
        print('Going straight...')
        Walking()
        Dead_End()
    elif direction == 'BACK':
        Back()
    else:
        print('Invalid input. Please enter a valid direction')
    
def J2():
    Maze_Level.append(J2)
    print('You arrive at another junction 2, you can go left or straight')
    print('Choose your direction by typing LEFT or STRAIGHT')
    direction = input()
    if direction == 'LEFT':
        print('Going left...')
        Walking()
    elif direction == 'STRAIGHT':
        print('Going straight...')
        Walking()
        Dead_End
    elif direction == 'BACK':
        Back()
    else:
        print('Invalid input. Please enter a valid direction')


print('Welcome to the maze')
print('Type START to begin')
start = input()
if start == 'START':
    J1()