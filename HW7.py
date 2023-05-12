import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pyautogui as pg
import webbrowser
import time


GUI = Tk()
GUI.title('Record Buy-Sell')
GUI.geometry('800x400')


frame = ttk.Frame()
frame.place(x=10,y=50)

Name_label = tkinter.Label(GUI, text="History Record",font=('Cascadia Code',28),fg='#E0C7EE')
Name_label.pack()

#info
info_frame = tkinter.LabelFrame(frame, text="Input",font=('JasmineUPC',16), fg='#D86511')
info_frame.grid(row=1,column=0)

stockname = tkinter.Label(info_frame, text="Stock Name",font=('JasmineUPC',14))
stockname.grid(row=2, column=0)
stockname_inbox = ttk.Entry(info_frame,font=('JasmineUPC',14))
stockname_inbox.grid(row=2, column=1)

pricein = tkinter.Label(info_frame,text='Price Action',font=('JasmineUPC',14))
pricein.grid(row=4,column=0)
pricein_inbox = ttk.Entry(info_frame,font=('JasmineUPC',14))
pricein_inbox.grid(row=4, column=1)

stoploss = tkinter.Label(info_frame,text='Stoploss',font=('JasmineUPC',14),fg='red')
stoploss.grid(row=5,column=0)
stoploss_inbox = ttk.Entry(info_frame,font=('JasmineUPC',14))
stoploss_inbox.grid(row=5, column=1)

priceloss = tkinter.Label(info_frame,text='Loss',font=('JasmineUPC',14),fg='red')
priceloss.grid(row=6,column=0)
priceloss_inbox = ttk.Entry(info_frame,font=('JasmineUPC',14))
priceloss_inbox.grid(row=6, column=1)
#output
frame_output =ttk.Frame()
frame_output.place(x=400,y=50)

out_frame = tkinter.LabelFrame(frame_output,text ="Calculation result",font=('JasmineUPC',16), fg='#D86511')
out_frame.grid(row=5,column=1)
result = Text(out_frame,font=('Cascadia Code',10),fg='black',bg='#E3EBFD', height=6, width=40)
#result = Entry(out_frame,font=('Cascadia Code',10),fg='black',bg='#E3EBFD')
result.pack(ipadx=5,ipady=5)

# เพิ่ม scrollbar
#scrollbar = Scrollbar(out_frame)
#scrollbar.pack(side=RIGHT, fill=Y)
# กำหนด scrollbar ให้กับ Text widget
#result.config(yscrollcommand=scrollbar.set)
#scrollbar.config(command=result.yview)

def datastock ():
    if len(stockname_inbox.get()) == 0:
        messagebox.showerror("Error", "Please enter Stock Name.")
    else:
        name = str(stockname_inbox.get())
        url = 'https://www.set.or.th/th/home'
        webbrowser.open(url)
        time.sleep(2)
        pg.click(547,180)
        pg.write(name,interval=0.25)
        time.sleep(2)
        pg.press('enter')

def cal ():
    result.delete('1.0',END)
    if len(stockname_inbox.get())==0 or len(pricein_inbox.get())==0 or len(stoploss_inbox.get())==0 or len(priceloss_inbox.get())==0:
        result.insert(END,'กรุณากรอกข้อมูลให้ครบไอ้สัส!!!')
    else:
        result.delete('1.0',END)
        com = 0.157/100
        vat = 7/100
        name = str(stockname_inbox.get())
        buy = float(pricein_inbox.get())
        sl = float(stoploss_inbox.get())
        loss = float(priceloss_inbox.get())
    #คำนวน
        sum = loss/(buy-sl)
        money = (((sum*buy)*com)*vat)+(sum*buy)
        result.insert(END, f'คุณควรซื้อหุ้น:{name}\nจำนวน>>>>>>{sum:,.0f} หุ้น\nเป็นเงิน>>>>>>{money:,.2f} บาท')
        #result.insert(0,f'คุณควรซื้อหุ้น:{name},\nจำนวน>>>>>>{sum:,.0f} หุ้น')
        #result.insert(0,f'เป็นเงิน>>>>>>{money} บาท')

def clear():
    stockname_inbox.delete(0,END)
    pricein_inbox.delete(0,END)
    stoploss_inbox.delete(0,END)
    priceloss_inbox.delete(0,END)
    result.delete(1.0,END)







data_bt_frame = Frame()
data_bt_frame.place(x=10,y=300)
data_bt = tkinter.Button(data_bt_frame,text='Data Stock', bg='#A8D1E7',fg='black',font=('Cascadia Code',14,'bold'),command=datastock)
data_bt.grid(row=9,column=0,padx=5,pady=5)

cal_bt_frame = Frame()
cal_bt_frame.place(x=170,y=300)
cal_bt = tkinter.Button(cal_bt_frame,text='Calculate',bg='#B3DBD8',fg='black',font=('Cascadia Code',14,'bold'),command=cal)
cal_bt.grid(row=9,column=2,padx=5,pady=5)

clear_bt_frame = Frame()
clear_bt_frame.place(x=320,y=300)
clear_bt = tkinter.Button(clear_bt_frame,text='Clear',bg='#D0F4DE',fg='black',font=('Cascadia Code',14,'bold'),command=clear)
clear_bt.grid(row=9,column=3,padx=5,pady=5)


GUI.mainloop()