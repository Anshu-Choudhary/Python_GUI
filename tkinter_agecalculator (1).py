def total_age():
    x=t1.get()
    y=m1.get()
    z=d1.get()
    ts=year+month+day
    y.set(ts)
    #if(year>=2025):
        
    
from tkinter import*

win=Tk()
win.geometry("1350x900")
win.title("Age Calcultor")
y1=StringVar()
m1=StringVar()
d1=StringVar()
t1=StringVar()

topframe=Frame(win,width=1500,height=200,bg='yellow',relief='raise',bd=10)
topframe.pack(side=TOP)
lb=Label(topframe,text="Age Calculator",font=('italic',40,'bold'),width=35,fg='orange',bd=4)
lb.grid(row=0,column=0)
mframe=Frame(win,width=500,height=500,relief='raise',bd=4,bg='orange')
mframe.pack(padx=50,pady=20)
lb1=Label(mframe,text="Welcome!!!",font=('italic',20,'bold'),width=31,bd=4,relief='raise',fg='orange')
lb1.grid(row=0,column=0,columnspan=2,padx=10,pady=10)


lb2=Label(mframe,text="Year",font=('italic',10,'bold'),width=10,bd=4)
lb2.grid(row=1,column=0,padx=10,pady=10)
tb2=Entry(mframe,textvariable=y1,width=15,font=('italic',10,'bold'),bd=4,justify=CENTER)
tb2.grid(row=1,column=1,padx=10,pady=10)


lb3=Label(mframe,text="Month",font=('italic',10,'bold'),width=10,bd=4)
lb3.grid(row=2,column=0,padx=10,pady=10)
tb3=Entry(mframe,textvariable=m1,width=15,font=('italic',10,'bold'),bd=4,justify=CENTER)
tb3.grid(row=2,column=1,padx=10,pady=10)

lb4=Label(mframe,text="Day",font=('italic',10,'bold'),width=10,bd=4)
lb4.grid(row=3,column=0,padx=10,pady=10)
tb4=Entry(mframe,textvariable=d1,width=15,font=('italic',10,'bold'),bd=4,justify=CENTER)
tb4.grid(row=3,column=1,padx=10,pady=10)

btn=Button(mframe,text="Click !!!",width=15,font=('italic',20,'bold'),fg='orange',bd=10,command=total_age)
btn.grid(row=4,column=1,padx=10,pady=10,ipadx=10)
y=StringVar
lb5=Label(mframe,text="Total_Age",font=('italic',10,'bold'),width=10,bd=4)
lb5.grid(row=5,column=0,padx=10,pady=10)
tb5=Entry(mframe,textvariable=y,width=25,font=('italic',10,'bold'),bd=4)
tb5.grid(row=5,column=1,padx=5,pady=10)
