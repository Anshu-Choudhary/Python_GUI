from tkinter import*
import datetime
import random
def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_input.set(operator)
def btnClearDisplay():
    global operator
    operator=""
    text_input.set("")
def btnequalinput():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
def reset():
    Tic.set('')
    clas.set('')
    ref.set('')
    route.set('')
    from_.set('')
    to.set('')
    route.set('')
    price.set('')
    adu.set('')
    chl.set('')
    e1.set(0)
    st1.set(0)
    sub_total.set(0)
    tc2.set(0)
    
def total():
    pr=price.get()
    #set tax
    if(pr<=50):
        tax=0
    elif(pr<=100):
        tax=2
    elif(pr<=200):
        tax=3
    elif(pr<=400):
        tax=4
    elif(pr<=600):
        tax=5
    elif(pr<=800):
        tax=6
    elif(pr<=1000):
        tax=7
    mul=st1.set(tax)
    #set ticket price based on passenger
    en=e1.get()
    st2=pr*en
    sub_total.set(st2)
    
    
    
win=Tk()
win.configure(bg='orange')
win.geometry("1450x750")
win.resizable(False,False)
e1=IntVar()
c1=IntVar()
st1=IntVar()
sub_total=IntVar()
tc2=IntVar()
#TopFrame----------------------------------------------------------------
topframe=Frame(win,width=1300,height=150,bg='orange',relief='raise',bd=10)
topframe.pack()
lb=Label(topframe,text="BUS Ticketing Portal",
         fg="orange",font=('Arial Black',41,'bold'),width=40)
lb.grid(row=0,column=0)
#FirstFrame---------------------------------------------------------------
cframe=Frame(win,width=865,height=250,relief='raise',bd=10)
cframe.place(x=5,y=101)
cframe1=Frame(cframe,relief='raise',bd=10)
cframe1.place(x=0,y=0)
#Class--------------------------------------------------------------------
def print_1():
    To=variable.get()
    if(cc.get()==1):
        Na="Non A.C"
        clas.set(Na)
    elif(cc.get()==2):
        Na="A.C Class"
        clas.set(Na)
    else:
        Na="VOLVO"
        clas.set(Na)
    #enter ticket
    en=e1.get()
    mul=Tic.set(en)
    #refcode
    r=f"REF{random.randint(1000,9999)}"
    ref.set(r)
    #route
    fr="New Delhi"
    from_.set(fr)
    #to
    to.set(To)
    route.set(To)
    v=variable.get()
    pr=options.get(v,"key not found")
    price.set(pr)
    if(vara.get()==1):
        adult="yes"
        child_="No"
        adu.set(adult)
        chl.set(child_)
    elif(vara.get()==2):
        adult="No"
        child_="Yes"
        adu.set(adult)
        chl.set(child_)
    else:
        adult="Yes"
        child_="Yes"
        adu.set(adult)
        chl.set(child_)
    DT2=datetime.datetime.now()
    ti=DT2.strftime('%H:%M:%S')
    time.set(ti)
    DT1=datetime.datetime.now()
    da=DT1.strftime('%Y,%b,%d')
    date.set(da)

    obj=open("Bus_Ticket_Portal.docx","w")
    obj.write(f"\t\t\t\t\t\tWELCOME TO BUS TICKET PORTAL\n\n\n\t\t\t\t\t\tRef ID: {r}\n\n\t\t\t\t\t\tTime: {ti}\n\n\t\t\t\t\t\tDate: {da}\n\n\t\t\t\t\t\tFrom: {fr}\n\n\t\t\t\t\t\tTo: {To}\n\n\t\t\t\t\t\tClass: {Na}\n\n\t\t\t\t\t\tTicket: {en}")

        
cc=IntVar()    
lb1=Label(cframe1,text="Class",font=('italic',30,'bold'),fg="blue")
lb1.grid(row=0,column=0,sticky="w")
rb1=Radiobutton(cframe1,text="Non A.C  ",font=('italic',25,'bold')
                ,variable=cc,value=1)
rb1.grid(row=1,column=0)
rb2=Radiobutton(cframe1,text="A.C Class",font=('italic',25,'bold')
                ,variable=cc,value=2)
rb2.grid(row=2,column=0)
rb3=Radiobutton(cframe1,text="VOLVO    ",font=('italic',25,'bold')
                ,variable=cc,value=3)
rb3.grid(row=3,column=0)

cframe2=Frame(cframe,relief='raise',bd=10)
cframe2.place(x=205,y=0)

lb2=Label(cframe2,text="Select Destination",font=('italic',30,'bold'),fg="blue")
lb2.grid(row=0,column=0,sticky="w")
lb3=Label(cframe2,text="Destination",font=('italic',25,'bold'))
lb3.grid(row=1,column=0,sticky="w",pady=5)
options={
    'Shrinagar':'400',
    'Dehradun':'500',
    'Srilanka':'900',
    'Shimla':'300',
    'Mumbai':'300',
    'Goa':'500',
    'Hydrabad':'600',
    'Odisha':'700',
    'Kolkata':'750'
    }
variable=StringVar()
value="Select"
variable.set(value)
w=OptionMenu(cframe2,variable,"Select",*options)
w.place(x=200,y=55)
w.config(font=25)
vara=IntVar()

rb4=Radiobutton(cframe2,text="Adult ",font=('italic',25,'bold')
                ,vari=vara,value=1)
rb4.grid(row=2,column=0,sticky="w")
rb5=Radiobutton(cframe2,text="Child ",font=('italic',25,'bold')
                ,vari=vara,value=2)
rb5.grid(row=3,column=0,sticky="w")
rb6=Radiobutton(cframe2,text="Both  ",font=('italic',25,'bold')
                ,vari=vara,value=3)
rb6.place(x=200,y=150)

cframe3=Frame(cframe,relief='raise',bd=10)
cframe3.place(x=570,y=0)
lb4=Label(cframe3,text="Ticket",font=('italic',30,'bold'),fg="blue")
lb4.grid(row=0,column=0,sticky="w",pady=10)
def Chk_button2():
    if(var10.get()==1):
        e1.set("0")
        ch4.configure(state=NORMAL)
    elif(var10.get()==0):
        ch4.configure(state=NORMAL)
        e1.set("0")
var10=IntVar()
ch4=Checkbutton(cframe3,text="Enter",font=('italic',20,'bold')
                ,variable=var10,onvalue=1,offvalue=0,command=Chk_button2)
ch4.grid(row=1,column=0,sticky="w",pady=15)

ch4=Entry(cframe3,textvariable=e1,state=DISABLED,width=10,
          font=('italic',15,'bold'))
ch4.grid(row=1,column=1,pady=15)
lb6=Label(cframe3,text="Comment",font=('italic',20,'bold'))
lb6.grid(row=2,column=0,sticky="w",pady=15)
tb2=Entry(cframe3,textvariable=c1,width=10,font=('italic',15,'bold'))
tb2.grid(row=2,column=1,pady=15)

sframe=Frame(win,width=865,height=370,relief='raise',bd=10)
sframe.place(x=10,y=350)
sframe1=Frame(sframe,width=350,height=300,relief='raise',bd=7)
sframe1.place(x=0,y=0)

lb6=Label(sframe1,text="STATE TAX",font=('italic',20,'bold'))
lb6.grid(row=0,column=0)
tb3=Entry(sframe1,textvariable=st1,font=('italic',15,'bold'),bd=5,width=25)
tb3.grid(row=0,column=1,pady=20,padx=15)

lb7=Label(sframe1,text="SUB TOTAL",font=('italic',20,'bold'))
lb7.grid(row=1,column=0)

tb4=Entry(sframe1,textvariable=sub_total,width=25,font=('italic',15,'bold'),bd=5)
tb4.grid(row=1,column=1,pady=20,padx=15)

lb8=Label(sframe1,text="TOTAL COST",font=('italic',20,'bold'))
lb8.grid(row=2,column=0)

tb5=Entry(sframe1,textvariable=tc2,width=25,font=('italic',15,'bold'),bd=5)
tb5.grid(row=2,column=1,pady=20,padx=15)

operator=""
text_input=StringVar()
calframe=Frame(sframe,bd=7,relief='raise')
calframe.place(x=515,y=0)
dis=Entry(calframe,textvariable=text_input,font=('arial',20,'bold'),bd=10,insertwidth=4,justify='right')
dis.grid(columnspan=4)
btn7=Button(calframe,padx=15,text="7",bd=8,font=('arial',20,'bold'),command=lambda:btnClick(7))
btn7.grid(row=1,column=0)

btn8=Button(calframe,padx=15,text="8",bd=8,font=('arial',20,'bold'),command=lambda:btnClick(8))
btn8.grid(row=1,column=1)


btn9=Button(calframe,padx=15,text="9",bd=8,font=('arial',20,'bold'),command=lambda:btnClick(9))
btn9.grid(row=1,column=2)

btn_=Button(calframe,padx=15,text="+",bd=8,font=('arial',20,'bold'),bg="lime",command=lambda:btnClick('+'))
btn_.grid(row=1,column=3)

btn4=Button(calframe,padx=15,text="4",bd=8,font=('arial',20,'bold'),command=lambda:btnClick(4))
btn4.grid(row=2,column=0)

btn5=Button(calframe,padx=15,text="5",bd=8,font=('arial',20,'bold'),command=lambda:btnClick(5))
btn5.grid(row=2,column=1)


btn6=Button(calframe,padx=15,text="6",bd=8,font=('arial',20,'bold'),command=lambda:btnClick(6))
btn6.grid(row=2,column=2)

btn_s=Button(calframe,padx=15,text="-",bd=8,font=('arial',20,'bold'),bg="lime",command=lambda:btnClick('-'))
btn_s.grid(row=2,column=3)

btn1=Button(calframe,padx=15,text="1",bd=8,font=('arial',20,'bold'),command=lambda:btnClick(1))
btn1.grid(row=3,column=0)

btn2=Button(calframe,padx=15,text="2",bd=8,font=('arial',20,'bold'),command=lambda:btnClick(2))
btn2.grid(row=3,column=1)


btn3=Button(calframe,padx=15,text="3",bd=8,font=('arial',20,'bold'),command=lambda:btnClick(3))
btn3.grid(row=3,column=2)

btn_m=Button(calframe,padx=15,text="*",bd=8,font=('arial',20,'bold'),bg="lime",command=lambda:btnClick('*'))
btn_m.grid(row=3,column=3)

btn0=Button(calframe,padx=15,text="0",bd=8,font=('arial',20,'bold'),command=lambda:btnClick(0))
btn0.grid(row=4,column=0)

btnC=Button(calframe,padx=15,text="C",bd=8,font=('arial',20,'bold'),command=btnClearDisplay)
btnC.grid(row=4,column=1)


btn_e=Button(calframe,padx=15,text="=",bd=8,font=('arial',20,'bold'),command=btnequalinput)
btn_e.grid(row=4,column=2)

btn_=Button(calframe,padx=15,text="/",bd=8,font=('arial',20,'bold'),bg="lime",command=lambda:btnClick('/'))
btn_.grid(row=4,column=3)

bframe=Frame(win,relief='raise',bg="orange",bd=10)
bframe.place(x=870,y=101)

bframe1=Frame(bframe,width=110,height=200,bd=10,relief='raise')
bframe1.grid(row=0,column=0)
lbd=Label(bframe1,text="Booking Details",width=31,fg='blue',font=('arial',20,'bold'))
lbd.grid(row=0,column=0,padx=10,pady=30)

clas=StringVar()
Tic=StringVar()
adu=StringVar()
chl=StringVar()
prt_ticket=Frame(bframe,width=500,height=200,relief='raise',bd=10)
prt_ticket.grid(row=1,column=0)
lb_c=Label(prt_ticket,text="CLASS",font=('arial',20,'bold'))
lb_c.grid(row=0,column=0,padx=15)
tb_c=Entry(prt_ticket,textvariable=clas,width=10,font=('Bahnschrift Condensed',20),bd=4)
tb_c.grid(row=1,column=0)

lb_t=Label(prt_ticket,text="TICKET",font=('arial',20,'bold'))
lb_t.grid(row=0,column=1,padx=15)
tb_t=Entry(prt_ticket,textvariable=Tic,width=10,font=('Bahnschrift Condensed',20),bd=4)
tb_t.grid(row=1,column=1)
lb_a=Label(prt_ticket,text="ADUlT",font=('arial',20,'bold'))
lb_a.grid(row=0,column=2,padx=15)
tb_a=Entry(prt_ticket,textvariable=adu,width=10,font=('Bahnschrift Condensed',20),bd=4)
tb_a.grid(row=1,column=2)
lb_ch=Label(prt_ticket,text="CHILD",font=('arial',20,'bold'))
lb_ch.grid(row=0,column=3,padx=15)
tb_ch=Entry(prt_ticket,textvariable=chl,width=10,font=('Bahnschrift Condensed',20),bd=4)
tb_ch.grid(row=1,column=3)
lbsp=Label(prt_ticket,text="      ",font=('arial',20,'bold'))
lbsp.grid(row=2,column=1,pady=10)

from_=StringVar()
to=StringVar()
price=IntVar()
lb_f=Label(prt_ticket,text="FROM",font=('arial',20,'bold'))
lb_f.grid(row=3,column=1,padx=30)
tb_f=Entry(prt_ticket,textvariable=from_,width=10,font=('Bahnschrift Condensed',20),bd=4)
tb_f.grid(row=3,column=2)
lb_t=Label(prt_ticket,text="TO",font=('arial',20,'bold'))
lb_t.grid(row=4,column=1,padx=30)
tb_t=Entry(prt_ticket,textvariable=to,width=10,font=('Bahnschrift Condensed',20),bd=4)
tb_t.grid(row=4,column=2)
lb_p=Label(prt_ticket,text="PRICE",font=('arial',20,'bold'))
lb_p.grid(row=5,column=1,padx=30)
tb_p=Entry(prt_ticket,textvariable=price,width=10,font=('Bahnschrift Condensed',20),bd=4)
tb_p.grid(row=5,column=2)


ref=IntVar()
time=IntVar()
date=IntVar()
route=StringVar()
lbsp=Label(prt_ticket,text="      ",font=('arial',20,'bold'))
lbsp.grid(row=6,column=1,pady=10)
lb_r=Label(prt_ticket,text="REF NO",font=('arial',20,'bold'))
lb_r.grid(row=7,column=0,padx=15)
tb_r=Entry(prt_ticket,textvariable=ref,width=10,font=('Bahnschrift Condensed',20),bd=4)
tb_r.grid(row=8,column=0)
lb_ti=Label(prt_ticket,text="TIME",font=('arial',20,'bold'))
lb_ti.grid(row=7,column=1,padx=15)
tb_ti=Entry(prt_ticket,textvariable=time,width=10,font=('Bahnschrift Condensed',20),bd=4)
tb_ti.grid(row=8,column=1)


lb_d=Label(prt_ticket,text="DATE",font=('arial',20,'bold'))
lb_d.grid(row=7,column=2,padx=15)
tb_d=Entry(prt_ticket,textvariable=date,width=10,font=('Bahnschrift Condensed',20),bd=4)
tb_d.grid(row=8,column=2)
lb_rt=Label(prt_ticket,text="ROUTE",font=('arial',20,'bold'))
lb_rt.grid(row=7,column=3,padx=15)
tb_rt=Entry(prt_ticket,textvariable=route,width=10,font=('Bahnschrift Condensed',20),bd=4)
tb_rt.grid(row=8,column=3)

btn_T=Button(prt_ticket,text="TOTAL",bd=5,font=('arial',15,'bold')
             ,fg="red",width=7,command=total)
btn_T.grid(row=9,column=0)

btn_P=Button(prt_ticket,text="PRINT",bd=5,font=('arial',15,'bold')
             ,fg="green",width=7,command=print_1)
btn_P.grid(row=9,column=1)
btn_R=Button(prt_ticket,text="RESET",bd=5,fg="blue",
             font=('arial',15,'bold'),width=7,command=reset)
btn_R.grid(row=9,column=2)
btn_E=Button(prt_ticket,text="EXIT",bd=5,font=('arial',15,'bold')
             ,fg="purple",width=7,command=win.destroy)
btn_E.grid(row=9,column=3)





