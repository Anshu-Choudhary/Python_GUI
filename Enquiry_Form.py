from tkinter import*
from pymysql import*
import pymysql.cursors
from tkinter import messagebox
from PIL import ImageTk,Image


win=Tk()
win.geometry("800x11200")


win.title("Tech Access Enquiry Form")

mframe=Frame(win,width=800,height=1200,relief='raise',bd=10)

mframe.pack(side=TOP)

s_no=StringVar()
date=StringVar()
canN=StringVar()
email=StringVar()
contact=StringVar()
add=StringVar()
add2=StringVar()
BQ=StringVar()
IC=StringVar()
cf=StringVar()
bd=StringVar()
ev=StringVar()
r=StringVar()

lb=Label(mframe,text="A-12,FIEE Company,Okhla Phase-2,New Delhi-110020\n\tPhone:9643320085/89"
         ,font=('Bookman Old Style',10,'bold')).place(x=200,y=100)


lb2=Label(mframe,text="ENQUIRY FORM",font=('Bookman Old Style',20,'bold'),bd=5).place(x=300,y=140)
tb3=Label(win,text="Date :",font=('Bookman Old Style',10,'bold')).place(x=600,y=170)

lb1=Label(mframe,text="Sl.No :",font=('Bookman Old Style',10,'bold')).place(x=20,y=170)
tb1=Entry(mframe,textvariable=s_no,width=15,bd=5,justify=CENTER).place(x=70,y=170)
lb3=Entry(mframe,textvariable=date,width=15,bd=5,justify=CENTER).place(x=650,y=170)
lb4=Label(mframe,text="Candidate Name:",font=('Bookman Old Style',10,'bold')).place(x=20,y=220)
tb4=Entry(mframe,textvariable=canN,width=80,bd=2,justify=CENTER).place(x=250,y=220)
lb5=Label(mframe,text="Father's/Husband Name :",font=('Bookman Old Style',10,'bold')).place(x=20,y=270)
tb5=Entry(mframe,textvariable=canN,width=80,bd=2,justify=CENTER).place(x=250,y=270)
lb6=Label(mframe,text="Email Id :",font=('Bookman Old Style',10,'bold')).place(x=20,y=320)
tb6=Entry(mframe,textvariable=email,width=80,bd=2,justify=CENTER).place(x=250,y=320)
lb7=Label(mframe,text="Contact No:",font=('Bookman Old Style',10,'bold')).place(x=20,y=370)
tb7=Entry(mframe,textvariable=contact,width=80,bd=2,justify=CENTER).place(x=250,y=370)
lb8=Label(mframe,text="Address",font=('Bookman Old Style',10,'bold')).place(x=20,y=420)
tb8=Entry(mframe,textvariable=add,width=80,bd=2,justify=CENTER).place(x=250,y=420)
tb9=Entry(mframe,textvariable=add2,width=80,bd=2,justify=CENTER).place(x=250,y=460)
lb10=Label(mframe,text="Basic Qualification :",font=('Bookman Old Style',10,'bold')).place(x=20,y=510)
tb10=Entry(mframe,textvariable=BQ,width=80,bd=2,justify=CENTER).place(x=250,y=510)
lb11=Label(mframe,text="Intersted Course(S) :",font=('Bookman Old Style',10,'bold')).place(x=20,y=560)
tb11=Entry(mframe,textvariable=IC,width=80,bd=2,justify=CENTER).place(x=250,y=560)

lb12=Label(mframe,text="From where you get the information about Tech Access",font=('Bookman Old Style',13,'bold'),bg='gray',bd=5,width=60).place(x=70,y=610)
Rb=Radiobutton(mframe,text='Letter/Pamphiets',value=1,font=('Bookman Old Style',10,'bold')).place(x=20,y=660)
Rb2=Radiobutton(mframe,text='College',value=2,font=('Bookman Old Style',10,'bold')).place(x=250,y=660)
Rb3=Radiobutton(mframe,text='Calling',value=3,font=('Bookman Old Style',10,'bold')).place(x=450,y=660)
Rb4=Radiobutton(mframe,text='Hoarding',value=4,font=('Bookman Old Style',10,'bold')).place(x=650,y=660)
Rb5=Radiobutton(mframe,text='Friends/Neighbour',value=5,font=('Bookman Old Style',10,'bold')).place(x=20,y=700)
Rb6=Radiobutton(mframe,text='Mall',value=6,font=('Bookman Old Style',10,'bold')).place(x=250,y=700)
Rb7=Radiobutton(mframe,text='Seminar/Workshop',value=7,font=('Bookman Old Style',10,'bold')).place(x=450,y=700)
Rb8=Radiobutton(mframe,text='Web(Google,Etc)',value=8,font=('Bookman Old Style',10,'bold')).place(x=650,y=700)

lb13=Label(mframe,text="For Office Use Only",font=('Bookman Old Style',11,'bold'),bg='black',fg='white',bd=5,width=40).place(x=200,y=740)

lb14=Label(mframe,text="Course Fee:",font=('Bookman Old Style',10,'bold')).place(x=20,y=790)
tb14=Entry(mframe,textvariable=cf,width=80,bd=2,justify=CENTER).place(x=250,y=790)
lb15=Label(mframe,text="Batch Date:",font=('Bookman Old Style',10,'bold')).place(x=20,y=840)
tb15=Entry(mframe,textvariable=bd,width=80,bd=2,justify=CENTER).place(x=250,y=840)
lb16=Label(mframe,text="Expected Visit:",font=('Bookman Old Style',10,'bold')).place(x=20,y=890)
tb16=Entry(mframe,textvariable=ev,width=80,bd=2,justify=CENTER).place(x=250,y=890)
lb17=Label(mframe,text="Remark(if any):",font=('Bookman Old Style',10,'bold')).place(x=20,y=940)
tb17=Entry(mframe,textvariable=r,width=80,bd=2,justify=CENTER).place(x=250,y=940)












