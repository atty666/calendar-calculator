import tkinter as tk
from tkinter import *
import calendar


app = Tk()
app.geometry("800x500")
app.resizable(False, False)
app.title('Holidays Calendar')
app.configure(background='#272427')


def show_calendar(year, month):
    pass

def previous_button():
    prev_button = Button(borderwidth=1, relief='solid', width=12, height=1, bg='#25CFFC', text='Prev', font=("Arial", 12))
    prev_button.pack(side=tk.LEFT, padx=10,)


def next_button():
    next_btn = Button(borderwidth=1, relief='solid', width=12, height=1, bg="#25CFFC", text='Next', font=("Arial", 12))
    next_btn.pack(side=tk.RIGHT, padx=10)


previous_button()
next_button()

if __name__ == '__main__':
    app.mainloop()
