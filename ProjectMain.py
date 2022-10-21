import time
import sys
from random import randint
from tkinter import *
from tkinter import messagebox   

def Welcome():
    delay_print('Welcome to the maze.\n')
    time.sleep(1)
    delay_print('Click START to begin! (Or QUIT to close the program)\n')

    top = Tk()  
    
    top.geometry("200x100")  
    
    def fun():  
        print('START')
        top.destroy()
        J1()
        
    def fun2():
        print('QUIT')
        top.destroy()
        quit()
    
    b1 = Button(top,text = "START",command = fun,activeforeground = "red",activebackground = "pink",pady=10)  
    b2 = Button(top,text = "QUIT",command = fun2,activeforeground = "red",activebackground = "pink",pady=10) 
    
    b1.pack(side = TOP)  
    b2.pack(side = BOTTOM)

    top.mainloop()

def Win():
    delay_print('Congratulations, you made it to the centre of the maze!\n')
    delay_print('Click AGAIN to start again or EXIT to quit the program \n')
    top = Tk()  
    
    top.geometry("200x100")  
    
    def fun():
        top.destroy()
        print('AGAIN')
        delay_print('Restarting game...\n')
        J1()
        
    def fun2():
        print('EXIT')
        top.destroy()
        delay_print('Thanks for playing!')
        time.sleep(1)
        quit()
    
    b1 = Button(top,text = "AGAIN",command = fun,activeforeground = "red",activebackground = "pink",pady=10)  
    b2 = Button(top,text = "EXIT",command = fun2,activeforeground = "red",activebackground = "pink",pady=10) 
    
    b1.pack(side = TOP)  
    b2.pack(side = BOTTOM)

    top.mainloop()

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)
        
def Verify(options):
    while True:
        x = input()
        if x in options:
            break
        print('Try again with a valid input')
    return x

def Junction_Text():
    verbs = ['arrive at','stumble upon','turn the corner to find','make it to']
    x = verbs[randint(0,3)]
    Sentence = 'You {} the next junction\n'.format(x)
    delay_print(Sentence)
    
def Walking():
    time.sleep(1)
    delay_print('Walking...\n')
    time.sleep(1)

def Back(x):
    delay_print('Retracing steps...\n')
    Walking()
    x()

def Dead_End(x):
    print('You have reached a dead end!')
    time.sleep(2)
    print('You can go back to the previous junction by typing BACK')
    Verify(['BACK'])
    Back(x)

def Junction(Options, Parent):
    Junction_Text()
    if len(Options) > 2:
        print('You can go ' + str(Options[0]) + ', ' + str(Options[1]) + ' or ' + str(Options[2]))
        print('Choose your direction by typing ' + str(Options[0]).upper() + ', ' + str(Options[1]).upper() + ' or ' + str(Options[2].upper()))
    else:
        print('You can go ' + str(Options[0]) + ' or ' + str((Options[1])))
        print('Choose your direction by typing ' + str(Options[0]).upper() + ' or ' + str(Options[1]).upper())
    a = Verify(Options)
    if a == 'LEFT':
        print('Going left...')
        Walking()
    elif a == 'RIGHT':
        print('Going right...')
        Walking()
    elif a == 'STRAIGHT':
        print('Going straight...')
        Walking()
    else:
        Back(Parent)
    return a
        

def J1():
    delay_print('You arrive at the first junction\n')
    print('You can go left or right.')
    print('Choose your direction by typing LEFT or RIGHT')
    a = Verify(['LEFT','RIGHT'])
    if a == 'LEFT':
        print('Going left...')
        Walking()
        J3()
    else:
        print('Going right...')
        Walking()
        J2()

def J3():
    x = Junction(['LEFT','STRAIGHT'],J1)
    if x == 'LEFT':
        Dead_End(J3)
    elif x == 'STRAIGHT':
        Dead_End(J3)

def J3_():
    Junction_Text()
    print('You can go left or straight')
    print('Choose your direction by typing LEFT or STRAIGHT (or BACK)')
    direction = Verify(['LEFT','STRAIGHT','BACK'])
    if direction == 'LEFT':
        print('Going left...')
        Walking()
        Dead_End(J3)
    elif direction == 'STRAIGHT':
        print('Going straight...')
        Walking()
        Dead_End(J3)
    else:
       Back(J1)
    
def J2():
    Junction_Text()
    print('You can go left or straight')
    print('Choose your direction by typing LEFT or STRAIGHT')
    direction = Verify(['LEFT','STRAIGHT','BACK'])
    if direction == 'LEFT':
        print('Going left...')
        Walking()
        J4()
    elif direction == 'STRAIGHT':
        print('Going straight...')
        Walking()
        Dead_End(J2)
    else:
        Back(J1)
        
def J4():
    Junction_Text()
    print('You can go left,straight or right.')
    print('Choose your direction by typing LEFT or STRAIGHT or RIGHT')
    direction = Verify(['LEFT','STRAIGHT','RIGHT','BACK'])
    if direction == 'LEFT':
        print('Going left...')
        Walking()
        Dead_End(J4)
    elif direction == 'STRAIGHT':
        print('Going straight...')
        Walking()
        J6()
    elif direction == 'RIGHT':
        print('Going right...')
        Walking()
        Dead_End(J4)
    else:
        Back(J1)
        
def J5():
    Junction_Text()
    print('You can go left or right.')
    print('Choose your direction by typing LEFT or RIGHT')
    direction = Verify(['LEFT','RIGHT','BACK'])
    if direction == 'LEFT':
        print('Going left...')
        Walking()
        Dead_End(J5)
    elif direction == 'RIGHT':
        print('Going right...')
        Walking()
        Dead_End(J5)
    else:
        Back(J4)

def J6():
    Junction_Text()
    print('You can go straight or right.')
    print('Choose your direction by typing STRAIGHT or RIGHT')
    direction = Verify(['STRAIGHT','RIGHT','BACK'])
    if direction == 'STRAIGHT':
        print('Going straight...')
        Walking()
        Dead_End(J6)
    elif direction == 'RIGHT':
        print('Going right...')
        Walking()
        Win()
    elif direction == 'BACK':
        Back(J4)
    else:
        print('Invalid input. Please enter a valid direction')

Welcome()