from tkinter import Button, Label, Tk, mainloop, Pack, Grid, Toplevel, Checkbutton
import winsound
from threading import Thread
global g
g = 0
def al():
    global g
    for i in range(100):
        if g == 5:
            break
        else:
            print(i, g)
            winsound.PlaySound('Alarm08',winsound.SND_FILENAME)
            if g == 5:
                break
    return
def t():
    def d():
        global g
        g = 5
        alarm_window.destroy()
    alarm_window = Tk()
    break_button = Button(alarm_window, text='Stop', bg='#16334d', activeforeground='darkblue', fg='#9ac8f5',command=d)
    break_button.pack(pady=10, padx=10)
    conue = Checkbutton(alarm_window, onvalue=1, offvalue=0, text='Check to keep alarms active, leave unchecked to stop alarms.')
    conue.pack()
    alarm_window.mainloop()

Thread(target= al).start()
Thread(target= t).start()



