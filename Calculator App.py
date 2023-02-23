#importing Tkinter Module
from tkinter import *

root =Tk()
root.title("Loki's Calculator")
root.iconbitmap('calc1.ico')

e=Entry(root, width=50, borderwidth=5)
e.grid(row=0,column=0,columnspan=4, padx=10, pady=10)

#defining Button's function

def button_click(number):#Button click
    current=e.get()
    e.delete(0,END)
    e.insert(0, str(current)+str(number))

def button_clear():#clear button
    e.delete(0,END)
    
def button_add():#Add button
    first_num=e.get()
    global f_num, math
    f_num=int(first_num)
    e.delete(0,END)
    math='add'
    
def button_Sub():#Sub button
    first_num=e.get()
    global f_num, math
    f_num=int(first_num)
    e.delete(0,END)
    math='sub'

def button_Mul():#Mul button
    first_num=e.get()
    global f_num, math
    f_num=int(first_num)
    e.delete(0,END)
    math='Mul'

def button_div():#divide button
    first_num=e.get()
    global f_num, math
    f_num=int(first_num)
    e.delete(0,END)
    math='div'

def button_equal():#Equal button with operations
    second_num=int(e.get())
    e.delete(0,END)
    
    if math=='add':
       e.insert(0, f_num + second_num)
    if math=='sub':
       e.insert(0, f_num - second_num)
    if math=='Mul':
       e.insert(0, f_num * second_num)
    if math=='div':
       (e.insert(0, f_num // second_num))

# defining buttons in tkinter root
button_1=Button(root, text='1', padx=40, pady=20,bg='white', command=lambda: button_click(1))
button_2=Button(root, text='2', padx=40, pady=20, bg='white', command=lambda: button_click(2))
button_3=Button(root, text='3', padx=40, pady=20, bg='white', command=lambda: button_click(3))
button_4=Button(root, text='4', padx=40, pady=20, bg='white', command=lambda: button_click(4))
button_5=Button(root, text='5', padx=40, pady=20, bg='white', command=lambda: button_click(5))
button_6=Button(root, text='6', padx=40, pady=20, bg='white', command=lambda: button_click(6))
button_7=Button(root, text='7', padx=40, pady=20, bg='white', command=lambda: button_click(7))
button_8=Button(root, text='8', padx=40, pady=20, bg='white', command=lambda: button_click(8))
button_9=Button(root, text='9', padx=40, pady=20, bg='white', command=lambda: button_click(9))
button_0=Button(root, text='0', padx=40, pady=20, bg='white', command=lambda: button_click(0))
button_add=Button(root, text='+', padx=20, pady=20, bd=5, font=('cambria 11 bold'), command=button_add)
button_Sub=Button(root, text='-', padx=20, pady=20, bd=5, font=('cambria 11 bold'), command=button_Sub)
button_Mul=Button(root, text='x', padx=20, pady=20, bd=5, font=('cambria 11 bold'), command=button_Mul)
button_div=Button(root, text='÷', padx=20, pady=20, bd=5, font=('cambria 11 bold'), command=button_div)
button_equal=Button(root, text='=', padx=40, pady=20,bg='#2A76F0', fg='white',relief=RAISED, bd=3, command=button_equal)
button_clear=Button(root, text='Clear', padx=23, pady=17, font=('cambria 11 bold'), command=button_clear)



# getting buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_clear.grid(row=4,column=0)

button_add.grid(row=1, column=3)
button_Sub.grid(row=2, column=3)
button_Mul.grid(row=3, column=3)
button_div.grid(row=4, column=3)


root.mainloop()
