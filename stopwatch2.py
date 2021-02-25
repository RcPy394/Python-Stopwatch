from tkinter import *
from tkinter.ttk import *
sc=0;mn=0;hr=0;stp=False
window =Tk()
def start():
    global sc,mn,hr
    button1['state']=DISABLED
    sc=0
    mn=0
    hr=0
    count()

def count():
    global sc,mn,hr
    if(stp==False):
        sc = sc + 1
        lbl['text'] = '%02d:%02d:%02d' % (hr, mn, sc)
        lbl.after(1000,count)
    if(sc==60):
        mn=mn+1
        sc=0
        lbl['text'] = '%02d:%02d:%02d' % (hr, mn, sc)
    if(mn==60):
        hr=hr+1
        mn=0
        lbl['text'] = '%02d:%02d:%02d' % (hr, mn, sc)
def stopRes():
    global stp
    if(stp==False):
        stp=True
        B['text']='Resume'
    elif(stp==True):
        stp=False
        B['text'] = 'Stop'
        count()
def reset():
    global sc, mn, hr
    stopRes()
    sc=0
    mn=0
    hr=0
    lbl['text'] = '%02d:%02d:%02d' % (hr, mn, sc)

window.config(bg="DeepSkyBlue4")
lbl = Label(window,text = '%02d:%02d:%02d' % (hr, mn, sc), font=('OCR A Extended', 30, 'bold'), foreground="blue")
lbl.place(x=40, y=60)
button1=Button(window,text="Start",command=start)
button1.place(x=10,y=10)
B=Button(window, text = 'Stop' ,command=stopRes)
B.place(x=100,y=10)
window.title("Stopwatch")
window.geometry("280x150")
Button3=Button(window,text="Reset",command=reset).place(x=190, y=10)
window.mainloop()
