import event_reminder
from tkinter import *
from tkcalendar import *
import datetime
import calendar
from mwi import intnumchk
from threading import Thread
class M_W():
    def __init__(self, width_, height_, title_):
        Text_Manage.old_remove_g(Text_Manage)
        self.tk = Tk()
        self.tk.title(title_)
        self.tk.geometry('700x500')
        self.tk.iconbitmap('calendar.ico')
        self.tk.resizable(width=False, height=False)
        self.window = Frame(self.tk, width=100, height=500)
        self.window.pack(side='left')

        self.upcoming_events = LabelFrame(self.window, width=150, height=500, text="Upcoming Events", bg='lightgray')
        self.upcoming_events.grid(row=1, column=0, padx=2)
        
        self.lst = Text_Manage.init_read_new(Text_Manage)
        self.upcomint_ev(self.lst)

        self.current_date = [datetime.date.today()]
        self.current_date = str(self.current_date[0]).split("-")
        self.calen = Calendar(self.tk, selectmode="day", year=int(self.current_date[0]), month=int(self.current_date[1]), day=int(self.current_date[2]))
        self.calen.pack(side='right', pady=5, fill='both', expand=True)
        self.date_select = Button(self.window, text="View Information", width=19, command=self.date_info, borderwidth=1,bg='#16334d',fg='white',activebackground='#0380fc')
        self.date_select.grid(row=0, column=0, pady=6)
        
        #self.but = Button(self.tk, text="click", command=self.window_create)
        #self.but.grid(row=0,column=1)
        #self.label_input = Entry(self.tk, width=50)
        #self.label_input.grid(row=1, column=1)

        self.tk.mainloop()
    
    def old_check(self, red_):
        x = datetime.datetime(int(red_[:4]),int(red_[5:7]),int(red_[8:10]),int(red_[11:13]),int(red_[14:16]))
        if x == datetime.datetime.today():
            return('present')
        elif x < datetime.datetime.today():
            return('past')
        else:
            return('future')
    
    def week_check(self, red_):
        x = datetime.datetime(int(red_[:4]),int(red_[5:7]),int(red_[8:10]),int(red_[11:13]),int(red_[14:16]))
        if x > datetime.datetime.today() + datetime.timedelta(days=7):
            #print(datetime.datetime.today() + datetime.timedelta(days=7))
            return('more')
        else:
            #print(datetime.datetime.today() + datetime.timedelta(days=7))
            return('less')

    def upcomint_ev(self,lst):
        les = sorted(lst)
        les = les[:5]
        #print(les)
        #print(les)
        if len(les) == 0:
            no_ev = Label(self.upcoming_events, text='No Events', fg='#525453', width = 15, height=20)
            no_ev.pack(pady=25)
        else:
            for i in range(0,len(les)):
                if self.week_check(les[i][0]) == 'less':
                    labelle = Label(self.upcoming_events, text=str(les[i][0].split(",")[0])+' - '+str(les[i][0].split(",")[1]),bg='lightgray', width=15, bd=0, fg='black', height=2)
                    labelle.pack(pady=5)
                    notes = Button(self.upcoming_events, justify='right',text=str(les[i][1]), fg='#525453', width=15,command=lambda index_=i: self.full_note(index_, les), borderwidth=1,height=2)
                    notes.pack(pady=2)
                else:
                    pass
    
    def full_note(self, index, lst):
        n_w = Toplevel()
        tt = Label(n_w, text=lst[index][1], bg='white')
        tt.pack(fill='both', expand='true', pady=10,padx=7)
        n_w.grab_set()
    
    def full_note_info(self, index, lst):
        n_w = Toplevel()
        tt = Label(n_w, text=lst[index][1], bg='white')
        tt.pack(fill='both', expand='true', pady=10,padx=7)
        n_w.grab_set()
        
    def window_create(self): 
        self.new_win = Toplevel(width=500, height=500)
        self.new_win.title = ("Child")
        self.new_but = Button(self.new_win, borderwidth=5, text="new label", command=self.label_create_test)
        self.new_but.grid(row=0, column=0)
    
    def date_interpret(self, obj):
        lst = str(obj)
        lst = lst.split("-")
        day = lst[2]
        year = lst[0]
        month = calendar.month_name[int(lst[1])]
        return(month + ", "+ day + ", " + year)
    
    def create_event(self, date):
        if len(self.date_minute_entry.get()) == 1:
            min_ent = '0'+str(self.date_minute_entry.get())
        else:
            min_ent = str(self.date_minute_entry.get())
        
        if len(self.date_time_entry.get()) == 1:
            tim_ent = '0'+str(self.date_time_entry.get())
        else:
            tim_ent = str(self.date_time_entry.get())

        #print(self.date_time_entry.get(), self.date_minute_entry.get())
        self.time_selected = tim_ent+':'+min_ent
        self.notes_selected = self.date_note_entry.get()
        Text_Manage.new_event(date, self.time_selected, self.notes_selected)
        self.date_window.destroy()
        self.date_info()

        self.upcoming_events.destroy()
        self.upcoming_events = LabelFrame(self.window, width=150, height=500, text="Upcoming Events", bg='lightgray')
        self.upcoming_events.grid(row=1, column=0, padx=2)
        self.lst = Text_Manage.init_read_new(Text_Manage)
        self.upcomint_ev(self.lst)
    
    def event_display_info(self, bst):
        lst = sorted(bst)
        #print(bst,'\n',lst)
        if len(lst) == 0:
            no_ev = Label(self.date_info_frame, text='No Events', fg='#525453', width = 40, height=20)
            no_ev.pack(pady=5)
        else:
            for i in range(len(lst)):
                labelle = Button(self.date_info_frame, text=str(lst[i][0]),bg='lightgray', width=40, bd=0, fg='black', cursor='tcross', command=lambda ind=i: self.event_delete_confirm(str(self.date)+','+str(bst[bst.index(lst[ind])][0])),borderwidth=1)
                labelle.pack()
                notes = Button(self.date_info_frame, text=str(lst[i][1]), fg='#525453', width=42, command=lambda inde=i: self.full_note_info(inde, lst), borderwidth=0)
                notes.pack(pady=3)
    
    def deleting_event(self, input_):
        Text_Manage.event_remove(input_)
        self.confirm_delete_window.destroy()
        self.date_window.destroy()
        self.date_info()

        self.upcoming_events.destroy()
        self.upcoming_events = LabelFrame(self.window, width=150, height=500, text="Upcoming Events", bg='lightgray')
        self.upcoming_events.grid(row=1, column=0, padx=2)
        self.lst = Text_Manage.init_read_new(Text_Manage)
        self.upcomint_ev(self.lst)
    
    
    def event_delete_confirm(self, event_del):
        #print(event_del)
        self.date_window.grab_release()
        self.confirm_delete_window = Toplevel(bg='black')
        self.confirm_delete_window.geometry=('200x75')
        self.confirm_delete_window.resizable(height=False, width=False)
        self.confirm_delete_window.title('')
        self.delete_event = Button(self.confirm_delete_window, bg='black',bd=0,fg='red',text='DELETE', command=lambda: self.deleting_event(event_del))
        self.delete_event.pack(side='top',pady=8)
        self.delete_instruction = Label(self.confirm_delete_window, bg='black', fg='lightgray', text='Close This Window To Keep The Event.')
        self.delete_instruction.pack(side='top', pady=10,padx=10)
        self.confirm_delete_window.grab_set()

    def date_info(self):
        Text_Manage.old_remove_g(Text_Manage)
        self.date = str(self.calen.selection_get())
        self.date_window = Toplevel(width=350,bg='white')
        self.date_window.title("Date ~ " + self.date)
        self.date_window.resizable(width=False, height=False)
        self.date_window.grab_set()

        self.date_label = Label(self.date_window, text=self.date_interpret(self.date), width=47, borderwidth=7, bg='lightgray')
        self.date_label.grid(row=0, column=0, padx=2, pady=2)

        self.date_info_frame = Frame(self.date_window, width=350,height=195)
        self.date_info_frame.grid(row=1,column=0,pady=2)

        self.event_display_info(Text_Manage.events_one_date(self.date))

        self.date_info_entry_frame = Frame(self.date_window, width=350, height=110)
        self.date_info_entry_frame.grid(row=2, column=0, pady=2)

        self.date_time_entry = Spinbox(self.date_info_entry_frame, width=5,from_=0, to=23, state='readonly',repeatdelay=150,repeatinterval=85)
        self.date_time_entry.insert(0,"[Hour]   ")
        self.date_time_entry.grid(row=1,column=0,padx=20)

        self.date_minute_entry = Spinbox(self.date_info_entry_frame, width=5,from_=0, to=60, state='readonly',repeatdelay=100,repeatinterval=50)
        self.date_minute_entry.insert(0,"[Minute]   ")
        self.date_minute_entry.grid(row=1, column=1,padx=10)

        self.date_note_entry = Entry(self.date_info_entry_frame, width=23)
        self.date_note_entry.insert(0, "Delete Then Enter [Notes]")
        self.date_note_entry.grid(row=1,column=2, padx=10)

        self.date_info_schedule = Button(self.date_info_entry_frame, text="Schedule", borderwidth=1, width=40, height=2, command=lambda: self.create_event(self.date),bg='#16334d',fg='#9ac8f5',activebackground='#7fbaf0',activeforeground='#10151a')
        self.date_info_schedule.grid(column=0,row=2,columnspan=20,pady=20, sticky='s')

        #lobal date_info_tabs -<<-- add tab counters to limit tab numbers

    
    def label_create_test(self):
        text_ = self.label_input.get()
        self.test = Label(self.window, text=text_, borderwidth=5)
        self.test.pack(side = TOP)

class Text_Manage():
    def __init__(self, name):
        self.f_name = name
    
    def init_read(self):
        text_f = open('event_save.txt', 'a')
        text_f = open('event_save.txt', 'r')
        ttb = text_f.readlines()
        fin = []
        for i in range(0,len(ttb),2):
            fin.append([ttb[i][:len(ttb[i])-1],ttb[i+1][:len(ttb[i+1])-1]]) 
        return(fin)
    
    def init_read_new(self):
        text_f = open('event_save_new.txt', 'a')
        text_f = open('event_save_new.txt', 'r')
        ttb = text_f.readlines()
        fin = []
        for i in range(0,len(ttb),2):
            fin.append([ttb[i][:len(ttb[i])-1],ttb[i+1][:len(ttb[i+1])-1]]) 
        return(fin)
    
    def new_event(self, obj, input_):
        text_f = open('event_save.txt', 'a')
        text_f = open('event_save.txt', 'r')
        pre_ex_lines = text_f.readlines()
        if str(self)+','+str(obj)+'\n' in pre_ex_lines:
            print("already added")
        else:
            text_f = open('event_save.txt', 'a')
            text_f.write(str(self)+','+str(obj)+'\n'+str(input_)+'\n')
            if M_W.old_check(M_W, str(self)+','+str(obj)+'\n'+str(input_)+'\n') == 'future':
                text_n = open('event_save_new.txt', 'a')
                text_n.write(str(self)+','+str(obj)+'\n'+str(input_)+'\n')
        text_f.close

    def events_one_date(self):
        text_f = open('event_save.txt', 'r')
        substance = text_f.readlines()
        event_list = []
        for i in range(len(substance)):
            if substance[i][:10] == str(self):
                #print(i, i+2, len(substance), substance[i])
                event_list.append([substance[i].split(",")[1][:len(substance[i].split(",")[1])-1], substance[i+1][:len(substance[i+1])-1]])
        text_f.close
        return(event_list)
    
    def event_remove(self):
        Text_Manage.old_remove_g(Text_Manage)
        text_f = text_f = open('event_save.txt', 'r')
        substance = text_f.readlines()
        #print(substance)
        for i in range(len(substance)):
            if substance[i][:len(substance[i])-1] == str(self):
                #print(substance[i], str(self), substance[i+1],substance[i-1], 'i->', i)
                substance.pop(i)
                substance.pop(i)
                break
            else:
                pass
                #print('nope')
        print('event removed')
        text_f = open('event_save.txt', 'w')
        text_f.writelines(substance)
        text_f.close
    
    def old_remove_g(self):
        t_f = open('event_save_new.txt','a')
        t_f = open('event_save_new.txt','r')
        t_o = open('event_save.txt','a')
        t_o = open('event_save.txt','r')
        cont = t_f.readlines()
        conto = t_o.readlines()
        if len(cont) == 0:
            return(0)
        for i in range(0,len(cont),2):
            if M_W.old_check(M_W, cont[i]) != 'future':
                #print(i, len(cont), cont[i], M_W.old_check(M_W, cont[i]))
                cont.pop(i)
                cont.pop(i)
                t_f = open('event_save_new.txt', 'w')
                t_f.writelines(cont)
                t_f.close()
                return(self.old_remove_g(self))
            if cont[i] not in conto:
                #print(i, len(cont), cont[i], M_W.old_check(M_W, cont[i]))
                cont.pop(i)
                cont.pop(i)
                t_f = open('event_save_new.txt', 'w')
                t_f.writelines(cont)
                t_f.close()
                return(self.old_remove_g(self))
        t_f.close()
        t_o.close()

        return(0)



def read_me():
    def main_app():
        CalendarApp.destroy()
        M_W(20,20, "Calendar App")

    CalendarApp = Tk()
    CalendarApp.title('Time Manage')
    instruction = Label(CalendarApp,justify=LEFT, text='Formatting:\n- Time must be in 24 hour format.\n   e.g - 4:05 pm would be 16:05 to be correct\n\n\nWhen finished reading, click button below.\nFeatures:\n- You can create events by clicking the "view Information" button in the top left, then selecting the time, adding a note then pressing the "Schedule" Button.\n- You can also delete an event by clicking on the time when viewing events on a specific day.\n- You can hold down on the arrows to rapidly increase or decrease values, when selecting time.\n- Click on the light gray note buttons underneath their corresponding time to view the full note. (main page and info page)\n- Stop alarms By leaving checkbox unchecked when alarm window is present.\n', bg='lightgray')
    instruction.pack(pady=10, padx=10)
    pta = Button(CalendarApp, text='Proceed', command=main_app)
    pta.pack(pady=8)
    CalendarApp.resizable(width=False, height=False)

    CalendarApp.mainloop()

def other_processes():
    Text_Manage.old_remove_g(Text_Manage)
    event_reminder.go()


Thread(target= read_me).start()
Thread(target= other_processes).start()


