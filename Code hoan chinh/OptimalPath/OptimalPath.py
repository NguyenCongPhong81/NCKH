from cProfile import label
from cgitb import reset, text
from tkinter import *
from tkinter.ttk import Frame, Button
from tkinter.ttk import Entry
from dijkstra import *
import math


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Optimal Path")

        lable_title = Label(self, text="Find the optimal path:",
                            font=("Arial Bold", 11), fg="blue")
        lable_title.grid(columnspan=2, row=0, pady=10)

        startLabel = Label(self, text='Start:', font=("Arial Bold", 10))
        startLabel.grid(column=0, row=1, pady=10)
        startEntry = Entry(self, width=60)
        startEntry.grid(column=1, row=1, padx=10)

        endLabel = Label(self, text='End:', font=("Arial Bold", 10))
        endLabel.grid(column=0, row=2, pady=10)
        endEntry = Entry(self, width=60)
        endEntry.grid(column=1, row=2)

        dayLabel = Label(self, text='Day:', font=("Arial Bold", 10))
        dayLabel.grid(column=0, row=3, pady=10)
        dayEntry = Entry(self, width=60)
        dayEntry.grid(column=1, row=3)

        monthLabel = Label(self, text='Month:', font=("Arial Bold", 10))
        monthLabel.grid(column=0, row=4, pady=10)
        monthEntry = Entry(self, width=60)
        monthEntry.grid(column=1, row=4)

        yearLabel = Label(self, text='Year:', font=("Arial Bold", 10))
        yearLabel.grid(column=0, row=5, pady=10)
        yearEntry = Entry(self, width=60)
        yearEntry.grid(column=1, row=5)

        hourLabel = Label(self, text='Hour:', font=("Arial Bold", 10))
        hourLabel.grid(column=0, row=6, pady=10)
        hourEntry = Entry(self, width=60)
        hourEntry.grid(column=1, row=6)

        minuteLabel = Label(self, text='Minute:', font=("Arial Bold", 10))
        minuteLabel.grid(column=0, row=7, pady=10)
        minuteEntry = Entry(self, width=60)
        minuteEntry.grid(column=1, row=7)

        def submit():
            startNode = startEntry.get()
            endNode = endEntry.get()
            d = dayEntry.get()
            m = monthEntry.get()
            y = yearEntry.get()
            h = hourEntry.get()
            mn = minuteEntry.get()

            title = (startNode.upper(), endNode.upper())

            Time, path = dijkstra(startNode, endNode, d, m, y, h, mn)
            path = '\n'.join(path)
            title = ' → '.join(title)

            if Time == timeStrInfinity:
                notificationPath.configure(text=path)
            else:
                notificationtitle.configure(text=title)
                notificationPath.configure(text="Optimal path: " + path)
                notificationTime.configure(text="Time: " + str(Time))

        def reset():
            startEntry.delete(0, END)
            endEntry.delete(0, END)
            dayEntry.delete(0, END)
            monthEntry.delete(0, END)
            yearEntry.delete(0, END)
            hourEntry.delete(0, END)
            minuteEntry.delete(0, END)
            notificationPath.configure(text="")
            notificationtitle.configure(text="")
            notificationTime.configure(text="")

        button_Frame = Frame(self)
        button_Frame.grid(column=1, row=8, pady=15)
        submit_button = Button(button_Frame, text='Submit', command=submit)
        submit_button.grid(column=1, row=0, padx=5)
        reset_button = Button(button_Frame, text='Reset', command=reset)
        reset_button.grid(column=0, row=0, padx=5)

        notificationtitle = Label(self)
        notificationtitle.grid(columnspan=2, row=9)

        notificationPath = Label(self)
        notificationPath.grid(columnspan=2, row=10)

        notificationTime = Label(self)
        notificationTime.grid(columnspan=2, row=11)

        self.pack()

def main():
    win = Tk()
    win.geometry("700x700")
    app = Example(win)
    win.mainloop()

if __name__ == "__main__":
    main()