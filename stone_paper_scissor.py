from tkinter import *
import random
from tkinter import messagebox

win = Tk()
win.title('Rock Paper Scissors')
win.geometry('500x365')
win.config(bg = 'black')
win.resizable(0,0)

def info():
    messagebox.showinfo('Info','rock<paper<scissor\nCreator: Sahil Rajwar')

def rock():
    obj = ['rock','paper','scissor']
    view = random.choice(obj)
    your_label.config(text = 'rock')
    computer_label.config(text = view)
    if view == 'rock':
        outcomes_label.config(text = 'Tie', fg = 'grey')
    elif view == 'paper':
        outcomes_label.config(text = 'You Lose', fg = 'red')
    elif view == 'scissor':
        outcomes_label.config(text = 'You Win', fg = 'green')
    else:
        outcomes_label.config(text = 'Error', fg = 'purple')

def paper():
    obj = ['rock','paper','scissor']
    view = random.choice(obj)
    your_label.config(text = 'paper')
    computer_label.config(text = view)
    if view == 'rock':
        outcomes_label.config(text = 'You Win', fg = 'green')
    elif view == 'paper':
        outcomes_label.config(text = 'Tie', fg = 'grey')
    elif view == 'scissor':
        outcomes_label.config(text = 'You Lose', fg = 'red')
    else:
        outcomes_label.config(text = 'Error', fg = 'purple')

def scissor():
    obj = ['rock','paper','scissor']
    view = random.choice(obj)
    your_label.config(text = 'scissor')
    computer_label.config(text = view)
    if view == 'rock':
        outcomes_label.config(text = 'You Lose', fg = 'red')
    elif view == 'paper':
        outcomes_label.config(text = 'You Win', fg = 'green')
    elif view == 'scissor':
        outcomes_label.config(text = 'Tie', fg = 'grey')
    else:
        outcomes_label.config(text = 'Error', fg = 'purple')

heading_frame = Frame(win, bd = 6, relief = SUNKEN)
heading_frame.pack(fill = BOTH, padx = 10, pady = 10)

heading_label = Label(heading_frame, font = ('Comic sans ms',20,'bold','italic'), text = 'Rock Paper Scissor')
heading_label.pack(fill = BOTH, padx = 10, pady = 10)

main_frame = Frame(win, bd = 6, relief = SUNKEN)
main_frame.pack(fill = BOTH, padx = 10, pady = 10)

you_label = Label(main_frame, font = ('Comic sans ms',12,'bold','italic'), text = ':Your Decision:',fg = 'green')
you_label.grid(row = 0, column = 0, padx = 10, pady = 10)
your_label = Label(main_frame, font = ('Comic sans ms',12,'bold','italic'))
your_label.grid(row = 0, column = 1, padx = 10, pady = 10)

comp_label = Label(main_frame, font = ('Comic sans ms',12,'bold','italic'), text = ':Computer Decicsion:',fg = 'red')
comp_label.grid(row = 1, column = 0, padx = 10, pady = 10)
computer_label = Label(main_frame, font = ('Comic sans ms',12,'bold','italic'))
computer_label.grid(row = 1, column = 1, padx = 10, pady = 10)

result_label = Label(main_frame, font = ('Comic sans ms',12,'bold','italic'), text = ':Results:',fg = 'black')
result_label.grid(row = 2, column = 0, padx = 10, pady = 10)
outcomes_label = Label(main_frame, font = ('Comic sans ms',12,'bold','italic'))
outcomes_label.grid(row = 2, column = 1, padx = 10, pady = 10)

btn_frame = Frame(win, bd = 6, relief = SUNKEN)
btn_frame.pack(fill = BOTH, padx = 10, pady = 10)
rock_btn = Button(btn_frame, font = ('Comic sans ms',12), text = 'Rock', command = rock)
rock_btn.grid(row = 0, column = 0, padx = 10, pady = 10, ipadx = 10)
paper_btn = Button(btn_frame, font = ('Comic sans ms',12), text = 'Paper', command = paper)
paper_btn.grid(row = 0, column = 1, padx = 10, pady = 10, ipadx = 10)
scissor_btn = Button(btn_frame, font = ('Comic sans ms',12), text = 'Scissor', command = scissor)
scissor_btn.grid(row = 0, column = 2, padx = 10, pady = 10, ipadx = 10)
info_btn = Button(btn_frame, font = ('Comic sans ms',12), text = 'Info', command = info)
info_btn.grid(row = 0, column = 3, padx = 10, pady = 10, ipadx = 10)


mainloop()
