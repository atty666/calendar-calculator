from tkinter import *
import calendar
import datetime
import time

app = Tk()
app.geometry('700x380')
app.resizable(False, False)
app.title('Holidays Calendar')

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
        lblb.grid(row=row + 2, column=col, sticky=NSEW)
        days.append(lblb)

def fill():
    info_label['text'] = calendar.month_name[month] + " " + str(year)
    month_days = calendar.monthrange(year, month)[1]
    if month == 1:
        back_month_days = calendar.monthrange(year - 1, 12)[1]
    else:
        back_month_days = calendar.monthrange(year, month - 1)[1]

    week_day = calendar.monthrange(year, month)[0]
    for n in range(month_days):
        day_number = n + 1
        days[n + week_day]['text'] = day_number

    for n in range(week_day):
        days[week_day - n - 1]["text"] = (back_month_days - n)

    for n in range(6 * 7 - month_days - week_day):
        days[week_day + month_days + n]["text"] = n + 1

def previous_button():
    prev_button = Button(borderwidth=1, relief='solid', width=12, height=1, bg='#25CFFC', text='<-- Previous',
                         font="Arial 12 bold", command=prev)
    prev_button.grid(row=0, column=6, sticky=NSEW)


def next_button():
    next_btn = Button(borderwidth=1, relief='solid', width=12, height=1, bg="#25CFFC", text='Next -->',
                      font="Arial 12 bold", command=next)
    next_btn.grid(row=0, column=9, sticky=NSEW)

def calculate_button():
    calc_button = Button(borderwidth=1, relief='solid', width=12, height=1, bg='#DB83F3', text='Calculate',
                         font='Arial 12 bold', command=calculate)
    calc_button.grid(row=0, column=0, sticky=NSEW)

def prev():
    global month, year
    month -= 1
    if month == 0:
        month = 12
        year -= 1
    fill()


def next():
    global month, year
    month += 1
    if month == 13:
        month = 1
        year += 1
    fill()
def calculate(start_day):
    red = '#EB3E26'
    yellow = '#F08E27'
    green = '#43EC0D'
    day_count = 0
    holi_count = 0
    night_count = 0
    month_days = calendar.monthrange(year, month)[1]
    week_day = calendar.monthrange(year, month)[0]

    for n in range(week_day, month_days + week_day):
        day_lb = days[n]
        day_number = n - week_day + 1

        if day_number < start_day:
            continue

        if day_count < 4:
            day_lb['bg'] = yellow
            day_count += 1
        elif holi_count < 2:
            day_lb['bg'] = green
            holi_count += 1
        elif night_count < 4:
            day_lb['bg'] = red
            night_count += 1


        if day_count == 4 and holi_count == 2 and night_count == 4:
            day_count = 0
            holi_count = 0
            night_count = 0

        if day_number == month_days:
            day_count = holi_count = night_count = 0

        day_lb['text'] = day_number

start_day = 1
calculate(start_day)
previous_button()
next_button()
calculate_button()
fill()
app.mainloop()
