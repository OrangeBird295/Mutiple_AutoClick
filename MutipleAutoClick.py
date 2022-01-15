import pyautogui
from pynput import mouse, keyboard
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
from tkinter import * # พวกGUI MAIN Modul
from tkinter import ttk # ไฟล์ย่อย
from time import sleep

################################# Config #################################
listener = None  # to keep listener
NumberOfSubmit = 0
data = []




GUI = Tk()
GUI.geometry('500x400+300+50')
GUI.title('Auto Click')
FONT1 = (None, 30) #(ชื่อฟ้อน, ขนาด)
FONT2 = (None, 20) #(ชื่อฟ้อน, ขนาด)

################################# Tab #################################
Tab = ttk.Notebook(GUI)
T1 = Frame(GUI)
T2 = Frame(GUI)
T3 = Frame(GUI)
# T4 = Frame(GUI)
Tab.pack(fill=BOTH, expand=1) #ทำให้Tabของเรามีขนาดใหญ่ทั้งหมด
iconT1 = PhotoImage(file='add-icon.png')
iconT2 = PhotoImage(file='check-list.png')
iconT3 = PhotoImage(file='start.png')
Tab.add(T1, text='Add Position',image=iconT1, compound='left') #compound อยากจะให้ icon ไปอยู่ด้านไหน
Tab.add(T2, text='List',image=iconT2, compound='left')  
Tab.add(T3, text='Start-Stop',image=iconT3, compound='left')  

################################# Action Button #################################
def onMouseClick(x, y, button, pressed):  ## Check Click Mouse
    global listener
    Commentx.set(x)
    Commenty.set(y)
    print(x, y)
    if not pressed: # Stop listener
        listener = None
        return False

def GetPosition():  ## Find Position (x, y)
    global listener
    if not listener:
        print("Start listener...")
        listener = mouse.Listener(on_click=onMouseClick)
        listener.start() # start thread
        
def SubmitPositon(): ## Submit Position
    global NumberOfSubmit
    tempx = Commentx.get()
    tempy = Commenty.get()
    tempdelay = Commentd.get()
    if isinstance(tempx, int) & isinstance(tempy, int) & isinstance(tempdelay, float):
        data.insert(NumberOfSubmit, [tempx, tempy, tempdelay])
        NumberOfSubmit = NumberOfSubmit + 1
        print(data)
        print(data[0][1])

def Refreshtable(): ## Refresd Data
    clear_all()
    for i in range(len(data)):
        Table1.insert(parent='', index='end', iid=i, text='',
        values=(i+1, data[i][0], data[i][1], data[i][2]))

def clear_all(): ## Clear Values in treeview before refresh
   for item in Table1.get_children():
      Table1.delete(item)

def StartClick(): ## Start Click
    ButtonPress = True
    mouse = Controller()
    if ButtonPress:
        for i in range(len(data)):
            print('In Loop', i)
            mouse.position = (data[i][0], data[i][1])
            print(data[i][0], data[i][1])
            # delay=float(((data[i][2])*1000))
            GUI.after(4000,None)
            # mouse.click(Button.left, 20)  cant use (idk)
            pyautogui.click()
            ## time.sleep(3) cant use with tkinter
        StartClick()

################################# Frame1 #################################
F1 = ttk.Labelframe(T1,text='Position') #สร้างเฟรมใหม่
F1.place(x=50, y=50) #และสามารถใช้แบบ place ได้5
### Label1 ###
L1 = ttk.Label(F1, text='X', font=FONT2)
L1.grid(row=0, column=0, padx=20)
    # L1.pack(padx=20)
L2 = ttk.Label(F1, text='Y', font=FONT2)
L2.grid(row=1, column=0, padx=20)
L3 = ttk.Label(F1, text='Delay', font=FONT2)
L3.grid(row=2, column=0, padx=20)
### Comment ###
Commentx = IntVar()
Commentx.set('Position X')
C1 = ttk.Entry(F1, textvariable=Commentx,font=FONT2, width=15)
C1.grid(row=0, column=1, padx=20)
Commenty = IntVar()
Commenty.set('Position Y')
C2 = ttk.Entry(F1, textvariable=Commenty, font=FONT2, width=15)
C2.grid(row=1, column=1, padx=20)
Commentd = DoubleVar()
Commentd.set('Delay Time')
C3 = ttk.Entry(F1, textvariable=Commentd, font=FONT2, width=15)
C3.grid(row=2, column=1, padx=20)
### Button ###
B1 = ttk.Button(F1, text='Add', command=GetPosition) 
B1.grid(row=3, column=1, padx=20, pady=10, ipady=10, ipadx=20) #ipadx,y ทำให้ตัวปุ่มใหญ่ขึ้น
B2 = ttk.Button(F1, text='Submit', command=SubmitPositon) 
B2.grid(row=4, column=1, padx=20, pady=10, ipady=10, ipadx=20) #ipadx,y ทำให้ตัวปุ่มใหญ่ขึ้น


################################# Frame2 #################################
F2 = ttk.Labelframe(T2,text='CheckList') #สร้างเฟรมใหม่
F2.place(x=50, y=50) #และสามารถใช้แบบ place ได้5
scroll = Scrollbar(F2,orient='vertical' )
scroll.pack(side=RIGHT, fill=Y)
Table1 = ttk.Treeview(F2,yscrollcommand=scroll.set)
Table1.pack()
scroll.config(command=Table1.yview)
Table1['columns'] = ('Id', 'Position X', 'Position Y', 'Delay Time')
### format our column ###
Table1.column("#0", width=0,  stretch=NO)
Table1.column("Id",anchor=CENTER, width=100)
Table1.column("Position X",anchor=CENTER, width=100)
Table1.column("Position Y",anchor=CENTER,width=100)
Table1.column("Delay Time",anchor=CENTER,width=100)
### Create Headings ###
Table1.heading("#0",text="",anchor=CENTER)
Table1.heading("Id",text="Id",anchor=CENTER)
Table1.heading("Position X",text="x",anchor=CENTER)
Table1.heading("Position Y",text="y",anchor=CENTER)
Table1.heading("Delay Time",text="delay",anchor=CENTER)
Table1.pack()

B3 = ttk.Button(F2, text='Refresh', command=Refreshtable)   #### แก้ไม่เอาไป pack ด้วย เพราะในอนาคตจะเพิ่มปุ่ม delete move อื่นๆ
# B3.grid(row=4, column=1, padx=20, pady=10, ipady=10, ipadx=20) #ipadx,y ทำให้ตัวปุ่มใหญ่ขึ้น
B3.pack()


################################# Frame3 #################################
F3 = ttk.Labelframe(T3,text='Start-Stop') #สร้างเฟรมใหม่
F3.place(x=170, y=50) #และสามารถใช้แบบ place ได้5
B4 = ttk.Button(F3, text='Start or Press s', command=StartClick) 
B4.grid(row=3, column=1, padx=20, pady=10, ipady=10, ipadx=20) #ipadx,y ทำให้ตัวปุ่มใหญ่ขึ้น
# B5 = ttk.Button(F3, text='Stop or Press e', command=EndClick) 
# B5.grid(row=4, column=1, padx=20, pady=10, ipady=10, ipadx=20) #ipadx,y ทำให้ตัวปุ่มใหญ่ขึ้น







GUI.mainloop()