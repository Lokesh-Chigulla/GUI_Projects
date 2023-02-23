#importing Modules
import random
from tkinter import * 
from tkinter import messagebox  
  
root = Tk()
root.configure(bg='white')
root.title('Rock, Paper, Scissor')
root.iconbitmap('rps game.ico')

#Defining Button Functions
def Rock_click(text1):
    
    global user_action
    user_action=text1
    return user_action

def Paper_click(text2):
    global user_action
    user_action=text2
    return user_action

def Scissor_click(text3):
    global user_action
    user_action=text3
    return user_action

def computer_click():
    
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    if user_action == computer_action:
       messagebox.showinfo('Bot Pick', computer_action)
       messagebox.showinfo('Result', f"Both players selected {user_action}. It's a tie!")
      
    elif user_action == "rock":
       if computer_action == "scissors":
          messagebox.showinfo('Bot Pick', computer_action)
          messagebox.showinfo('Result',"Rock smashes scissors! You win!")
          
       else:
          messagebox.showinfo('Bot Pick', computer_action)
          messagebox.showinfo('Result',"Paper covers rock! You lose.")
    elif user_action == "paper":
       if computer_action == "rock":
          messagebox.showinfo('Bot Pick', computer_action)
          messagebox.showinfo('Result',"Paper covers rock! You win!")
       else:
          messagebox.showinfo('Bot Pick', computer_action)
          messagebox.showinfo('Result',"Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
          messagebox.showinfo('Bot Pick', computer_action)
          messagebox.showinfo('Result',"Scissors cuts paper! You win!")
        else:
          messagebox.showinfo('Bot Pick', computer_action)
          messagebox.showinfo('Result',"Rock smashes scissors! You lose.")
    


#defining Things in tkinter root

Label1=Label(root, text='Welcome to Rock, Paper, Scissor Game "\U0001f600" ', bg='red', fg='white', font=('cambria 20 bold'))
Label2=Label(root, text='', bg='white')
Label3=Label(root, text='', bg='white')
Label5=Label(root, text='', bg='white')
Label6=Label(root, text='', bg='white')
Label4=Label(root, text='Please Click Your Choice "\U0001F609"', font=('cambria 12 bold'))
Button_Rock=Button(root, text='Rock', width=30,pady=10, bd=5, font=('cambria 12 bold'), bg='#0A2369', fg='white', command=lambda: Rock_click('rock'))
Button_Paper=Button(root, text='Paper', width=30,pady=10,bd=5, font=('cambria 12 bold'), bg='#06C8F3', fg='white', command=lambda: Paper_click('paper'))
Button_Scissor=Button(root, text='Scissor', width=30,pady=10,bd=5, font=('cambria 12 bold'), bg='#2455DD', fg='white', command=lambda: Scissor_click('scissors'))
Button_computer=Button(root, text='Click Here to Computer Play', width=30,pady=10,bd=5, font=('cambria 12 bold'), bg='#25B8BD', fg='white', command=computer_click)



#Getting Things on Screen 
Label1.grid(row=0,column=0, columnspan=3)
Label2.grid(row=1,column=0)
Label3.grid(row=3,column=1)
Label4.grid(row=2,column=0)
Label5.grid(row=5,column=0)
Label6.grid(row=7,column=0)
Button_Rock.grid(row=4,column=0)
Button_Paper.grid(row=4, column=2)
Button_Scissor.grid(row=6,column=1)
Button_computer.grid(row=8,column=1)

root.mainloop()
