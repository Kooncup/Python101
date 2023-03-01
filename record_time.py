from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox
import csv
#########################################csv#######################################################
def writecsv(datalist):
    with open('Record.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file)
        fw.writerow(datalist)

#def readcsv():
   # with open('Record.csv',encoding='utf-8',newline='') as file:
        #fr = csv.reader(file) # fr = file reader
        #data = list(fr)
   # return data

####################################################################################################



GUI = Tk()
GUI.title('Record time IN-OUT')
GUI.geometry('800x400')

L1 = Label(GUI,text='บันทึกเวลา เข้า-ออกงาน',font=('sukhumvit',25),fg='black')
L1.place(x=250,y=20)

name = StringVar() #ตัวแปรพิเศษใช้กับข้อความใน GUI
LF1 = ttk.LabelFrame(GUI,text='ชื่อ')
LF1.place(x=10,y=75)
L2 = ttk.Entry(LF1,textvariable=name,font=('sukhumvit',16))
L2.pack(padx=5,pady=5)

sur = StringVar()
LF2 = ttk.LabelFrame(GUI,text='นามสกุล')
LF2.place(x=300,y=75)
L3 = ttk.Entry(LF2,textvariable=sur,font=('sukhumvit',16))
L3.pack(padx=5,pady=5)

number = StringVar()
LF3 = ttk.LabelFrame(GUI,text='รหัสพนักงาน')
LF3.place(x=10,y=150)
L4 = ttk.Entry(LF3,textvariable=number,font=('sukhumvit',16))
L4.pack(padx=5,pady=5)

LF4 = Label(GUI,text='สถานะ',font=('sukhumvit',16),fg='black')
LF4.place(x=10,y=225)

def In_work():
    t = datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
    d1 = name.get()
    d2 = sur.get()
    d3 = number.get()
    data = [d1,d2,d3]
    text = ['****เข้างาน****',t,data]
    writecsv(text) 
    messagebox.showinfo('submit', message='บันทึกข้อมูลสำเร็จ')
    name.set('')
    sur.set('')
    number.set('')
    

def Out_work():
    t = datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
    d1 = name.get()
    d2 = sur.get()
    d3 = number.get()
    data = [d1,d2,d3]
    text = ['***ออกงาน***',t,data]
    writecsv(text)
    messagebox.showinfo('submit', message='บันทึกข้อมูลสำเร็จ')
    name.set('')
    sur.set('')
    number.set('')
    






FB1 = Frame(GUI)
FB1.place(x=150,y=225)
B1 = Button(FB1,text='เข้างาน', bg='green',fg='white',font='20',command=In_work)
B1.pack(ipadx=5,ipady=5)

FB2 = Frame(GUI)
FB2.place(x=250,y=225)
B2 = Button(FB2,text='ออกงาน', bg='red',fg='white',font='20',command=Out_work)
B2.pack(ipadx=5,ipady=5)



GUI.mainloop()
