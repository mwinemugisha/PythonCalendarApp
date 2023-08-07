import time
from playsound import playsound
from datetime import datetime
from mwi import intnumchk

def formatted_events(filename, soul):
    days = []
    c = open('event_save_new.txt', 'r')
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

def reminder():
    i=0
    while True:
        if current_time_formated(str) in formatted_events('event_save_new.txt','str'):
            playsound('ZA WARUDO _ TOKI WO TOMARE _(MP3_160K).mp3')
            return('done')
        else:
            print(current_time_formated(str), formatted_events('event_save_new.txt','str'))
            print('not - yet',str(i))
            time.sleep(50)
        i+=1

def alarm_count(filename):
    r = open(filename, 'r')
    d = r.readlines()
    r.close
    return(len(d))

def go():
    while True:
        if alarm_count('event_save_new.txt') == 0:
            break
        else:
            reminder()

go()