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
        if x == 'QUIT':
            quit()
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
    print('You can go',end = ' ')
    for x in Options:
        print(x, end=' ')
    print('\nChoose your direction by typing',end= ' ')
    for x in Options:
        print(x.upper(), end = ' ')
    print('')
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
    delay_print('Your head feels groggy as you open your eyes\n')
    delay_print('You look around to find yourself surrounded by thick concrete walls\n')
    delay_print('You are in a maze and with only one option, you begin to walk...\n')
    x = Junction(['LEFT','RIGHT'],J1)
    if x == 'LEFT':
        J3()
    else:
        J2()

def J3():
    x = Junction(['LEFT','STRAIGHT','BACK'],J1)
    if x == 'LEFT':
        Dead_End(J3)
    elif x == 'STRAIGHT':
        Dead_End(J3)

def J2():
    x = Junction(['LEFT','STRAIGHT','BACK'],J1)
    if x == 'LEFT':
        J4()
    elif x == 'STRAIGHT':
        Dead_End(J2)

def J4():
    x = Junction(['LEFT','STRAIGHT','RIGHT','BACK'],J2)
    if x == 'LEFT':
        Dead_End(J4)
    elif x == 'STRAIGHT':
        J6()
    elif x == 'RIGHT':
        J5()
 
def J5():
    x = Junction(['LEFT','RIGHT','BACK'],J4)
    if x == 'LEFT':
        Dead_End(J5)
    elif x == 'RIGHT':
        Dead_End(J5)

def J6():
    x = Junction(['STRAIGHT','RIGHT','BACK'],J2)
    if x == 'STRAIGHT':
        Dead_End(J6)
    elif x == 'RIGHT':
        Win()

Welcome()