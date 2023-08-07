import time
from datetime import datetime
from mwi import intnumchk
import winsound
from tkinter import Tk, IntVar, Pack, Grid, Toplevel, mainloop, Button, Label, Checkbutton
from threading import Thread

global contiu
contiu = 0
def old_check_ext( red_):
        x = datetime(int(red_[:4]),int(red_[5:7]),int(red_[8:10]),int(red_[11:13]),int(red_[14:16]))
        if x == datetime.today():
            return('present')
        elif x < datetime.today():
            return('past')
        else:
            return('future')

def old_remove_ext():
        t_f = open('event_save_new.txt','a')
        t_f = open('event_save_new.txt','r')
        cont = t_f.readlines()
        if len(cont) == 0:
            return(0)
        for i in range(0,len(cont),2):
            if old_check_ext(cont[i]) != 'future':
                #print(i, len(cont), cont[i], M_W.old_check(M_W, cont[i]))
                cont.pop(i)
                cont.pop(i)
                t_f = open('event_save_new.txt', 'w')
                t_f.writelines(cont)
                t_f.close()
                return(old_remove_ext())
            else:
                pass
        return(0)

    
def formatted_events(filename, soul):
    days = []
    c = open(str(filename), 'r')
    redd = c.readlines()
    for i in range(len(redd)):
        if intnumchk(redd[i][0]) == 1:
            #print(redd[i][:len(redd[i])-1])
            x = datetime(int(redd[i][:4]),int(redd[i][5:7]),int(redd[i][8:10]),int(redd[i][11:13]),int(redd[i][14:16]))
            days.append(x)
            #print(x,'\n')
        else:
            pass
            #print('Supposed to be not, or wrong format\n')  
    days_str = []
    for x in range(len(days)):
        days_str.append(days[x].strftime('%Y-%m-%d %H:%M'))

    if soul == 'str':
        return(days_str)
    elif soul == 'datetime':
        return(days)

def current_time_formated(soul):
    #print(datetime.today().strftime('%Y-%m-%d %H:%M'))
    current_time_str = datetime.today().strftime('%Y-%m-%d %H:%M')
    current_time_lst_date = current_time_str[:10].split("-")
    current_time_lst_time = current_time_str[-5:].split(":")
    current_time_formated = datetime(int(current_time_lst_date[0]),int(current_time_lst_date[1]),int(current_time_lst_date[2]),int(current_time_lst_time[0]),int(current_time_lst_time[1]))
    #print(current_time_formated)
    if soul == 'str':
        return(current_time_str)
    elif soul == 'datetime':
        return(current_time_formated)
    elif soul == 'default':
        return(datetime.today())
    elif soul == 'list':
        return[int(current_time_lst_date[0]),int(current_time_lst_date[1]),int(current_time_lst_date[2]),int(current_time_lst_time[0]),int(current_time_lst_time[1])]

def exce(inp):
    global tog
    tog = 0
    def al():
        global tog
        for i in range(100):
            if tog == 5:
                break
            else:
                #print(i, tog)
                winsound.PlaySound('Alarm08',winsound.SND_FILENAME)
                if tog == 5:
                    break
        return
    def t():

        def d():
            global tog
            tog = 5
            alarm_window.destroy()
        
        alarm_window = Tk()
        
        break_button = Button(alarm_window, text='Stop', bg='#16334d', activeforeground='darkblue', fg='#9ac8f5',command=d)
        break_button.pack(pady=10, padx=10)

        vart = IntVar()
        conue = Checkbutton(alarm_window, variable=vart, text='Check to keep alarms active, leave unchecked to stop alarms.')
        conue.pack()
        global contiu
        contiu = 0
        if vart.get() == 0:
            contiu = 1
        alarm_window.mainloop()
    
    def t_s():
        Thread(target= al).start()
        Thread(target= t).start()
    
    if inp == 1:
        t_s()

def reminder():
    i=0
    g=0
    b=1
    while b==1:
        if current_time_formated('str') in formatted_events('event_save_new.txt', 'str'):
            g = 3
        if g == 3:
            exce(1)
            old_remove_ext()
            b=0
            print("are we out?")
            break
        else:
            #print(current_time_formated(str), formatted_events('event_save_new.txt','str'))
            #print('muda muda',str(i))
            time.sleep(8)
            
        i+=1

def alarm_count(filename):
    r = open(filename, 'r')
    d = r.readlines()
    r.close
    return(len(d))

def go():
    global contiu
    valid = 0
    #i = 0
    while valid == 0:
        #print(i)
        time.sleep(20)
        if contiu == 1:
            valid = 1
            print('return')
            return(0)
        else:
            valid = 0
            print('-')
            reminder()
            print("we're out")
            
        
        #i=i+1
            


if __name__ == '__main__':
    print('name = main ----------------------------------------------------------------')
    go()