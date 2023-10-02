from tkinter import *
import calendar
import datetime
import time

app = Tk()
#app.geometry("800x500")
app.resizable(False, False)
app.title('Holidays Calendar')
#app.configure(background='#272427')


def show_calendar():
    days = []
    now = datetime.datetime.now()
    year = now.year
    month = now.month

    info_label = Label(app, text=year, width=1, height=1, font='Arial 16 bold', fg='#9B43E8')
    info_label.grid(row=0, column=1, columnspan=5, sticky=NSEW)

    for n in range(7):
        lblb = Label(app, text=calendar.day_abbr[n], width=1, height=1, font='Arial 10 bold', fg='#9B43E8')
        lblb.grid(row=1, column=n, sticky=NSEW)

    for row in range(6):
        for col in range(7):
            lblb = Label(app, text='0', width=4, height=2, font='Arial 16 bold')
            lblb.grid(row=row+2, column=col, sticky=NSEW)
            days.append(lblb)

    info_label['text'] = calendar.month_name[month] + " " + str(year)
    month_days = calendar.monthrange(year, month)[1]
    if month == 1:
        back_month_days = calendar.monthrange(year-1, 12) #[1]
    else:
        back_month_days = calendar.monthrange(year, month-1) #[1]

    week_day = calendar.monthrange(year, month)[0]

    for n in range(month_days):
        days[n + week_day]['text'] = n + 1
        days[n + week_day]['fg'] = 'black'
        if year == now.year and month == now.month and n == now.day:
            days[week_day]['bg'] = 'green'
            days[n + week_day]['bg'] = 'green'
        else:
            days[n + week_day]['bg'] = 'green'



def previous_button():
    prev_button = Button(borderwidth=1, relief='solid', width=12, height=1, bg='#25CFFC', text='Previous', font="Arial 12 bold")
    prev_button.grid(row=0, column=0, sticky=NSEW)


def next_button():
    next_btn = Button(borderwidth=1, relief='solid', width=12, height=1, bg="#25CFFC", text='Next', font="Arial 12 bold")
    next_btn.grid(row=0, column=6, sticky=NSEW)


previous_button()
next_button()
show_calendar()
app.mainloop()
