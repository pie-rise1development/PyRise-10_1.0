from tkinter import *
from tkinter import messagebox
from random import *

clicks = 0


def randomize():
    global clicks
    btnClick.place(x=randint(70, 1000), y=randint(70, 650))
    clicks += 1
    labelClick['text'] = str(clicks)
    labelClick.pack()


root = Tk()
root.title('Pie-Rise The Sound - [Playing Clicker]')
root.geometry('1200x720')
root.resizable(width=False, height=False)
root['bg'] = 'black'

labelClick = Label(root, text='0', font=('Comic Sans MS', 30, 'bold'), bg='black', fg='red')
labelClick.pack()

btnClick = Button(root,
                  text='Репутация ( + )',
                  bg='Blue',
                  fg='black',
                  padx='20',
                  pady='8',
                  font=('Times New Roman', 14, 'bold'),
                  command=randomize
                  )
btnClick.place(x=randint(70, 1000), y=randint(70, 650))



root.mainloop()