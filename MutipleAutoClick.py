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








GUI.mainloop()