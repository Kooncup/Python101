from tkinter import *
from tkinter import ttk #them of tk
from tkinter import messagebox
GUI = Tk() #หน้าจอหลักโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #ชื่อโปรแกรม
GUI.geometry('500x400') #ขนาด(กว้างxสูง)

#B1 = ttk.Button(GUI,text='เงินมีอยู่กี่บาท')
#B1.pack(ipadx=20,ipady=20) #ขนาดปุ่ม
L1 = Label(GUI,text='โปรแกรมบันทึกความรู้',font=('Angsana New',30),fg='green')
L1.place(x=30,y=20)
####################################################
def Button2():
    text = 'ตอนนี้มีเงินในบัญชีอยู่ 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text) # .showwarning , .showerror

#B2 = Button(GUI,text='เงินมีอยู่กี่บาท')
#B2.pack()


FB1 = Frame(GUI) #คล้ายกระดาน LabelFrame
FB1.place(x=200,y=200)
B3 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2)
B3.pack(ipadx=20,ipady=20)
#B3.place(x=50,y=200) กำหนด position ปุ่ม
####################################################
GUI.mainloop()
