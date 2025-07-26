from tkinter import*
from pymysql import*
import pymysql.cursors
from tkinter import messagebox
win=Tk()
win.geometry("1450x800")
win.resizable(False,False)
win.title("TECH")
topframe=Frame(win,relief="raise",width=1500,height=150,bd=10)
topframe.pack()
lb=Label(topframe,text="TECH Medicos",font=("Baskerville Old Face",45,"bold"),width=40)
lb.grid(row=0,column=0)

chframe=Frame(win,width=300,height=700,bd=3,relief="raise")
chframe.place(x=0,y=98)
emp=IntVar()
def employee():
    def dbadem():
        fname=ftb.get()
        mname=mtb.get()
        lname=ltb.get()
        name=fname+mname+lname
        Adhaar=atb.get()
        Address=Atb.get()
        #dob=dtb.get()
        State=stb.get()
        Phone_no=ptb.get()
        position=potb.get()
        #Date_of_join=dojtb.get()
        email=emtb.get()
        pincode=pintb.get()
        year_of_Experience=yoetb.get()
        pay_rate=prtb.get()
        gender=g1.get()
        day=d
            
        
        
        
        conn=pymysql.connect(host='localhost',user='root',password='',db='tech_medicos')
        a=conn.cursor()
        a.execute("insert into add_emp(Name,Adhar_Card,DOB,Phone_no,Email_ID,Gender,Address,State,Pincode,DOJ,Position,Pay_rate,Year_of_Experience)values('"+name+"','"+Adhaar+"','"+dob+"','"+phone+"','"+email+"','"+gtb+"','"+add+"','"+State+"','"+pin+"','"+doj+"','"+position+"','"+pr+"','"+yoe+"')")
        conn.commit()
        messagebox.showinfo("message","Record saved")
    if(emp.get()==1):
        emframe=Frame(win,width=900,height=650,relief='raise',bd=10)
        emframe.place(x=400,y=105)
        g=StringVar()
        r1=StringVar()
        fname=Label(emframe,text="First Name",font=("Baskerville Old Face",15,"bold"))
        fname.place(x=300,y=40)
        Fn=StringVar()
        Mn=StringVar()
        Ln=StringVar()
        ftb=Entry(emframe,textvariable=Fn,width=17,bd=2,font=("Baskerville Old Face",15,"bold"))
        ftb.place(x=270,y=90)
        mname=Label(emframe,text="Middle Name",font=("Baskerville Old Face",15,"bold"))
        mname.place(x=500,y=40)
        mtb=Entry(emframe,textvariable=Mn,width=17,bd=2,font=("Baskerville Old Face",15,"bold"))
        mtb.place(x=470,y=90)
        lname=Label(emframe,text="Last Name",font=("Baskerville Old Face",15,"bold"))
        lname.place(x=700,y=40)
        ltb=Entry(emframe,textvariable=Ln,width=17,bd=2,font=("Baskerville Old Face",15,"bold"))
        ltb.place(x=670,y=90)
        name=Label(emframe,text="Name",
                   font=("Baskerville Old Face",15,"bold"))
        name.place(x=100,y=90)
        Aadhar=Label(emframe,text="Aadhar ID",
                   font=("Baskerville Old Face",15,"bold"))
        Aadhar.place(x=100,y=140)
        ad=StringVar()
        atb=Entry(emframe,textvariable=ad,width=20,bd=2,font=("Baskerville Old Face",15,"bold"))
        atb.place(x=270,y=140)
        dob=Label(emframe,text="D.O.B",font=("Baskerville Old Face",15,"bold"))
        dob.place(x=530,y=140)
        lbd=Label(emframe,text="Date",font=("Baskerville Old Face",5,"bold"))
        lbd.place(x=670,y=140)
        
        lbm=Label(emframe,text="Month",font=("Baskerville Old Face",5,"bold"))
        lbm.place(x=690,y=140)
        
        lby=Label(emframe,text="Year",font=("Baskerville Old Face",5,"bold"))
        lby.place(x=710,y=140)
        
        spd=Spinbox(emframe,from_=1,to=31,width=5,font=("Baskerville Old Face",10,"bold"))
        spd.place(x=670,y=150)
        spm=Spinbox(emframe,from_=1,to=12,width=5,font=("Baskerville Old Face",10,"bold"))
        spm.place(x=700,y=150)
        spy=Spinbox(emframe,from_=1965,to=2007,width=5,font=("Baskerville Old Face",10,"bold"))
        spy.place(x=730,y=150)
        
        Address=Label(emframe,text="Address",
                   font=("Baskerville Old Face",15,"bold"))
        Address.place(x=100,y=190)
        ad=StringVar()
        Atb=Entry(emframe,textvariable=ad,width=53,bd=2,font=("Baskerville Old Face",15,"bold"))
        Atb.place(x=270,y=190)
        state=Label(emframe,text="State",
                   font=("Baskerville Old Face",15,"bold"))
        state.place(x=100,y=240)
        st1=StringVar()
        stb=Entry(emframe,textvariable=st1,width=17,bd=2,font=("Baskerville Old Face",15,"bold"))
        stb.place(x=270,y=240)
        phone=Label(emframe,text="Phone",
                   font=("Baskerville Old Face",15,"bold"))
        phone.place(x=100,y=290)
        p1=StringVar()
        ptb=Entry(emframe,textvariable=p1,width=17,bd=2,font=("Baskerville Old Face",15,"bold"))
        ptb.place(x=270,y=290)
        position=Label(emframe,text="Position",
                   font=("Baskerville Old Face",15,"bold"))
        position.place(x=100,y=340)
        po1=StringVar()
        potb=Entry(emframe,textvariable=po1,width=17,bd=2,font=("Baskerville Old Face",15,"bold"))
        potb.place(x=270,y=340)
        Pay_Rate=Label(emframe,text="Pay Rate",
                   font=("Baskerville Old Face",15,"bold"))
        Pay_Rate.place(x=100,y=390)
        pr1=StringVar()
        prtb=Entry(emframe,textvariable=pr1,width=17,bd=2,font=("Baskerville Old Face",15,"bold"))
        prtb.place(x=270,y=390)
        Doj=Label(emframe,text="Date of join",
                   font=("Baskerville Old Face",15,"bold"))
        Doj.place(x=100,y=425)
        doj1=StringVar()
        lbd=Label(emframe,text="Date",font=("Baskerville Old Face",5,"bold"))
        lbd.place(x=270,y=425)
        
        lbm=Label(emframe,text="Month",font=("Baskerville Old Face",5,"bold"))
        lbm.place(x=290,y=425)
        
        lby=Label(emframe,text="Year",font=("Baskerville Old Face",5,"bold"))
        lby.place(x=310,y=425)
        
        spd=Spinbox(emframe,from_=1,to=31,width=5,font=("Baskerville Old Face",10,"bold"))
        spd.place(x=270,y=440)
        spm=Spinbox(emframe,from_=1,to=12,width=5,font=("Baskerville Old Face",10,"bold"))
        spm.place(x=300,y=440)
        spy=Spinbox(emframe,from_=1965,to=2007,width=5,font=("Baskerville Old Face",10,"bold"))
        spy.place(x=330,y=440)
        
        pin=Label(emframe,text="Pincode",
                   font=("Baskerville Old Face",15,"bold"))
        pin.place(x=520,y=240)
        pin1=StringVar()
        pintb=Entry(emframe,textvariable=pin1,width=17,bd=2,font=("Baskerville Old Face",15,"bold"))
        pintb.place(x=670,y=240)
        email=Label(emframe,text="Email",
                   font=("Baskerville Old Face",15,"bold"))
        email.place(x=520,y=290)
        em1=StringVar()
        emtb=Entry(emframe,textvariable=em1,width=17,bd=2,font=("Baskerville Old Face",15,"bold"))
        emtb.place(x=670,y=290)
        yoe=Label(emframe,text="Year of Experience",
                   font=("Baskerville Old Face",15,"bold"))
        yoe.place(x=510,y=350)
        yoe1=StringVar()
        yoetb=Entry(emframe,textvariable=yoe1,width=10,bd=2,font=("Baskerville Old Face",15,"bold"))
        yoetb.place(x=670,y=340)
        gender=Label(emframe,text="Sex",
                   font=("Baskerville Old Face",15,"bold"))
        gender.place(x=510,y=390)
        mrb=Radiobutton(emframe,text="Male",variable=g,
                value='1',font=("Baskerville Old Face",15,"bold"))
        mrb.place(x=670,y=390)
        frb=Radiobutton(emframe,text="Female",variable=g,
                value='2',font=("Baskerville Old Face",15,"bold"))
        frb.place(x=750,y=390)
        Rating=Label(emframe,text="Employee Rating",
                   font=("Baskerville Old Face",15,"bold"))
        Rating.place(x=100,y=490)
        star1=Radiobutton(emframe,text="*",variable=r1,
                value='1',font=("Baskerville Old Face",15,"bold"))
        star1.place(x=270,y=490)
        star2=Radiobutton(emframe,text="**",variable=r1,
                value='2',font=("Baskerville Old Face",15,"bold"))
        star2.place(x=330,y=490)
        star3=Radiobutton(emframe,text="***",variable=r1,
                value='3',font=("Baskerville Old Face",15,"bold"))
        star3.place(x=380,y=490)
        star4=Radiobutton(emframe,text="****",variable=r1,
                value='4',font=("Baskerville Old Face",15,"bold"))
        star4.place(x=440,y=490)
        star5=Radiobutton(emframe,text="*****",variable=r1,
                value='5',font=("Baskerville Old Face",15,"bold"))
        star5.place(x=490,y=490)
        btn=Button(emframe,text="Submit",width=25,command=dbadem
                   ,bd=4,font=("Baskerville Old Face",20,"bold"))
        btn.place(x=270,y=540)
def delete():
    if(emp.get()==2):
        demframe=Frame(win,width=900,height=650,relief='raise',bd=10)
        demframe.place(x=400,y=105)
        empid=Label(demframe,text="Employee ID",
            font=("Baskerville Old Face",15,"bold"))
        empid.place(x=250,y=140)
        de1=StringVar()
        demptb=Entry(demframe,textvariable=de1,width=17,bd=2,font=("Baskerville Old Face",15,"bold"))
        demptb.place(x=420,y=140)
        name=Label(demframe,text="Name",
            font=("Baskerville Old Face",15,"bold"))
        name.place(x=250,y=190)
        n1=StringVar()
        ptb=Entry(demframe,textvariable=n1,width=17,bd=2,font=("Baskerville Old Face",15,"bold"))
        ptb.place(x=420,y=190)
        btn=Button(demframe,text="Delete",width=15
                   ,bd=4,font=("Baskerville Old Face",20,"bold"))
        btn.place(x=300,y=240)

def upemp():
    def dbupemp():
        Idd=idemptb.get()
        name=ntb1.get()
        salary=stb1.get()
        conn=pymysql.connect(host='localhost',user='root',password='',db='tech_medicos')
        a=conn.cursor()
        a.execute("update update_emp set Salary=Salary+'"+salary+"' where id='"+Idd+"'")
        conn.commit()
        messagebox.showinfo("message","Updated")
        print(Id,name,salary)
    if(emp.get()==3):
        upemframe=Frame(win,width=900,height=650,relief='raise',bd=10)
        upemframe.place(x=400,y=105)
        id1=StringVar()
        n1=StringVar()
        s1=StringVar()
        emp_id=Label(upemframe,text="Employee ID",
            font=("Baskerville Old Face",15,"bold"))
        emp_id.place(x=250,y=140)
        
        idemptb=Entry(upemframe,textvariable=id1,width=17,bd=2,font=("Baskerville Old Face",15,"bold"))
        idemptb.place(x=420,y=140)
        emp_name=Label(upemframe,text="Name",
            font=("Baskerville Old Face",15,"bold"))
        emp_name.place(x=250,y=190)
        
        ntb1=Entry(upemframe,textvariable=n1,width=17,bd=2,font=("Baskerville Old Face",15,"bold"))
        ntb1.place(x=420,y=190)
        emp_salary=Label(upemframe,text="Salary",
            font=("Baskerville Old Face",15,"bold"))
        emp_salary.place(x=250,y=240)
        
        stb1=Entry(upemframe,textvariable=s1,width=17,bd=2,font=("Baskerville Old Face",15,"bold"))
        stb1.place(x=420,y=240)
        btn1=Button(upemframe,text="Update",width=15,command=dbupemp
                   ,bd=4,font=("Baskerville Old Face",20,"bold"))
        btn1.place(x=300,y=290)
        print(Id,name,salary)
def Attemp():
    def dbpre():
        Id=idemptb.get()
        name=ntb.get()
        intime=ittb.get()
        outime=outb.get()
        conn=pymysql.connect(host='localhost',user='root',password='',db='tech_medicos')
        a=conn.cursor()
        a.execute("insert into Attendence_emp(Idd,Name,In_Time,Out_Time)values('"+Id+"','"+name+"','"+intime+"','"+outime+"')")
        conn.commit()
        messagebox.showinfo("message","Present")
        print(Id,name,intime,outime)

    if(emp.get()==4):
        atemframe=Frame(win,width=900,height=650,relief='raise',bd=10)
        atemframe.place(x=400,y=105)
        empid=Label(atemframe,text="Employee ID",
            font=("Baskerville Old Face",15,"bold"))
        empid.place(x=250,y=140)
        de1=StringVar()
        idemptb=Entry(atemframe,textvariable=de1,width=17,bd=2,font=("Baskerville Old Face",15,"bold"))
        idemptb.place(x=420,y=140)
        name=Label(atemframe,text="Name",
            font=("Baskerville Old Face",15,"bold"))
        name.place(x=250,y=190)
        n1=StringVar()
        ntb=Entry(atemframe,textvariable=n1,width=17,bd=2,font=("Baskerville Old Face",15,"bold"))
        ntb.place(x=420,y=190)
        Fathers_name=Label(atemframe,text="Father's Name",
            font=("Baskerville Old Face",15,"bold"))
        Fathers_name.place(x=250,y=240)
        fn1=StringVar()
        fntb=Entry(atemframe,textvariable=fn1,width=17,bd=2,font=("Baskerville Old Face",15,"bold"))
        fntb.place(x=420,y=240)
        Intime=Label(atemframe,text="In Time",
            font=("Baskerville Old Face",15,"bold"))
        Intime.place(x=250,y=290)
        it=StringVar()
        ittb=Entry(atemframe,textvariable=it,width=17,bd=2,font=("Baskerville Old Face",15,"bold"))
        ittb.place(x=420,y=290)
        outime=Label(atemframe,text="Out Time",
            font=("Baskerville Old Face",15,"bold"))
        outime.place(x=250,y=340)
        ot=StringVar()
        outb=Entry(atemframe,textvariable=ot,width=17,bd=2,font=("Baskerville Old Face",15,"bold"))
        outb.place(x=420,y=340)
        btn=Button(atemframe,text="Present",width=15,command=dbpre
                   ,bd=4,font=("Baskerville Old Face",20,"bold"))
        btn.place(x=300,y=390)

def stock():
    
    if(emp.get()==6):
        fstock=Frame(win,width=900,height=650,relief='raise',bd=10)
        fstock.place(x=400,y=105)
        lbe=Label(fstock,text="Add Stock ",font=("Baskerville Old Face",35,"bold"))
        lbe.place(x=300,y=90)
        rbs1=Radiobutton(fstock,text="Medicines              "
                 ,variable=emp,value=11,command=stock,font=("Baskerville Old Face",15,"bold"))
        rbs1.place(x=300,y=140)
        rbs2=Radiobutton(fstock,text="Cosmetics              "
                 ,variable=emp,value=12,command=stock,font=("Baskerville Old Face",15,"bold"))
        rbs2.place(x=300,y=190)
        rbs3=Radiobutton(fstock,text="Surgical Equipments    "
                 ,variable=emp,value=13,command=stock,font=("Baskerville Old Face",15,"bold"))
        rbs3.place(x=300,y=240)
        rbs4=Radiobutton(fstock,text="Baby Products          "
                 ,variable=emp,value=14,command=stock,font=("Baskerville Old Face",15,"bold"))
        rbs4.place(x=300,y=290)
        rbs5=Radiobutton(fstock,text="Personal Care          "
                 ,variable=emp,value=15,command=stock,font=("Baskerville Old Face",15,"bold"))
        rbs5.place(x=300,y=340)
        rbs6=Radiobutton(fstock,text="Diet and Nutrition    "
                 ,variable=emp,value=16,command=stock,font=("Baskerville Old Face",15,"bold"))
        rbs6.place(x=300,y=390)
        btns=Button(fstock,text="Select",width=15
                   ,bd=4,font=("Baskerville Old Face",20,"bold"))
        btns.place(x=300,y=440)
def updatestock():
    if(emp.get()==7):
        upstock=Frame(win,width=900,height=650,relief='raise',bd=10)
        upstock.place(x=400,y=105)
        prname=Label(upstock,text="Product Name",
            font=("Baskerville Old Face",15,"bold"))
        prname.place(x=250,y=140)
        pr1=StringVar()
        prtb=Entry(upstock,textvariable=pr1,width=17,bd=2,font=("Baskerville Old Face",15,"bold"))
        prtb.place(x=420,y=140)
        Category=Label(upstock,text="Category",
            font=("Baskerville Old Face",15,"bold"))
        Category.place(x=250,y=190)
        c1=StringVar()
        Ctb=Entry(upstock,textvariable=c1,width=17,bd=2,font=("Baskerville Old Face",15,"bold"))
        Ctb.place(x=420,y=190)
        Quantity=Label(upstock,text="Quantity",
            font=("Baskerville Old Face",15,"bold"))
        Quantity.place(x=250,y=240)
        q1=StringVar()
        qtb=Entry(upstock,textvariable=q1,width=17,bd=2,font=("Baskerville Old Face",15,"bold"))
        qtb.place(x=420,y=240)
        mrp=Label(upstock,text="MRP",
            font=("Baskerville Old Face",15,"bold"))
        mrp.place(x=250,y=290)
        m1=StringVar()
        mrptb=Entry(upstock,textvariable=m1,width=17,bd=2,font=("Baskerville Old Face",15,"bold"))
        mrptb.place(x=420,y=290)
        
        btn=Button(upstock,text="Update",width=15
                   ,bd=4,font=("Baskerville Old Face",20,"bold"))
        btn.place(x=300,y=340)

def expandstock():
    if(emp.get()==8):
        exstock=Frame(win,width=900,height=650,relief='raise',bd=10)
        exstock.place(x=400,y=105)
        lbd=Label(exstock,text="Date",font=("Baskerville Old Face",15,"bold"))
        lbd.place(x=250,y=150)
        
        lbm=Label(exstock,text="Month",font=("Baskerville Old Face",15,"bold"))
        lbm.place(x=330,y=150)
        
        lby=Label(exstock,text="Year",font=("Baskerville Old Face",15,"bold"))
        lby.place(x=410,y=150)
        
        spd=Spinbox(exstock,from_=1,to=31,width=5,font=("Baskerville Old Face",15,"bold"))
        spd.place(x=250,y=190)
        spm=Spinbox(exstock,from_=1,to=12,width=5,font=("Baskerville Old Face",15,"bold"))
        spm.place(x=330,y=190)
        spy=Spinbox(exstock,from_=1965,to=2007,width=5,font=("Baskerville Old Face",15,"bold"))
        spy.place(x=410,y=190)
        
def Nearstock():
    if(emp.get()==9):
        nrstock=Frame(win,width=900,height=650,relief='raise',bd=10)
        nrstock.place(x=400,y=105)
        prname=Label(nrstock,text="Items Name",
            font=("Baskerville Old Face",15,"bold"))
        prname.place(x=250,y=140)
        pr1=StringVar()
        prtb=Entry(nrstock,textvariable=pr1,width=17,bd=2,font=("Baskerville Old Face",15,"bold"))
        prtb.place(x=420,y=140)
        Category=Label(nrstock,text="Batch No.",
            font=("Baskerville Old Face",15,"bold"))
        Category.place(x=250,y=190)
        c1=StringVar()
        Ctb=Entry(nrstock,textvariable=c1,width=17,bd=2,font=("Baskerville Old Face",15,"bold"))
        Ctb.place(x=420,y=190)
        Quantity=Label(nrstock,text="Expiry Date",
            font=("Baskerville Old Face",15,"bold"))
        Quantity.place(x=250,y=240)
        q1=StringVar()
        qtb=Entry(nrstock,textvariable=q1,width=17,bd=2,font=("Baskerville Old Face",15,"bold"))
        qtb.place(x=420,y=240)
        mrp=Label(nrstock,text="Quantity",
            font=("Baskerville Old Face",15,"bold"))
        mrp.place(x=250,y=290)
        m1=StringVar()
        mrptb=Entry(nrstock,textvariable=m1,width=17,bd=2,font=("Baskerville Old Face",15,"bold"))
        mrptb.place(x=420,y=290)
        lnr=Label(nrstock,text="Location",
            font=("Baskerville Old Face",15,"bold"))
        lnr.place(x=250,y=340)
        lo1=StringVar()
        nrtb=Entry(nrstock,textvariable=lo1,width=17,bd=2,font=("Baskerville Old Face",15,"bold"))
        nrtb.place(x=420,y=340)
        
        btn=Button(nrstock,text="Done",width=15
                   ,bd=4,font=("Baskerville Old Face",20,"bold"))
        btn.place(x=300,y=390)

def oos():
    if(emp.get()==10):
        def iost():
            batch=b1.get()
            
            if(batch%2==0):
                inout="In Stock"
            else:
                inout="Out of Stock"
            stk.set(inout)
        stk=StringVar()
        nrstock=Frame(win,width=900,height=650,relief='raise',bd=10)
        nrstock.place(x=400,y=105)
        prname=Label(nrstock,text="Item Name",
                     font=("Baskerville Old Face",15,"bold"))
        prname.place(x=250,y=140)
        pr1=StringVar()
        prtb=Entry(nrstock,textvariable=pr1,width=17,bd=2,font=("Baskerville Old Face",15,"bold"))
        prtb.place(x=420,y=140)
        Category=Label(nrstock,text="Batch No.",
                           font=("Baskerville Old Face",15,"bold"))
        Category.place(x=250,y=190)
        b1=IntVar()
        bat=Entry(nrstock,textvariable=b1,width=17,bd=2,font=("Baskerville Old Face",15,"bold"))
        bat.place(x=420,y=190)
        btn=Button(nrstock,text="Check",width=15,command=iost
                   ,bd=4,font=("Baskerville Old Face",20,"bold"))
        btn.place(x=300,y=250)
            
        tbio=Entry(nrstock,textvariable=stk,font=("Baskerville Old Face",20,"bold"))
        tbio.place(x=300,y=320)

        


       
    



lbe=Label(chframe,text="Employee ",font=("Baskerville Old Face",35,"bold"))
lbe.grid(row=0,column=0,sticky="w")

rbe1=Radiobutton(chframe,text="Add Employee    "
    ,font=("Baskerville Old Face",15,"bold"),variable=emp,value=1,command=employee)
rbe1.grid(row=1,column=0,sticky="w",pady=5)
rbe2=Radiobutton(chframe,text="Delete Employee ",
                 font=("Baskerville Old Face",15,"bold"),variable=emp,value=2,command=delete)
rbe2.grid(row=2,column=0,sticky="w",pady=5)
rbe3=Radiobutton(chframe,text="Update Employee "
                 ,variable=emp,value=3,command=upemp,font=("Baskerville Old Face",15,"bold"))
rbe3.grid(row=3,column=0,sticky="w",pady=5)
rbe4=Radiobutton(chframe,text="Attendence      "
                 ,variable=emp,value=4,command=Attemp,font=("Baskerville Old Face",15,"bold"))
rbe4.grid(row=4,column=0,sticky="w",pady=5)
rbe5=Radiobutton(chframe,text="Show Details    "
                 ,variable=emp,value=5,font=("Baskerville Old Face",15,"bold"))
rbe5.grid(row=5,column=0,sticky="w",pady=5)

lbs=Label(chframe,text="Stock ",font=("Baskerville Old Face",35,"bold"))
lbs.grid(row=6,column=0,sticky="w",pady=5)
rbe6=Radiobutton(chframe,text="Add Stock     "
                 ,variable=emp,value=6,command=stock,font=("Baskerville Old Face",15,"bold"))
rbe6.grid(row=7,column=0,sticky="w",pady=5)
rbe7=Radiobutton(chframe,text="Update Stock  "
                 ,variable=emp,value=7,command=updatestock,font=("Baskerville Old Face",15,"bold"))
rbe7.grid(row=8,column=0,sticky="w",pady=5)
rbe8=Radiobutton(chframe,text="Expand Stock  "
                 ,variable=emp,value=8,command=expandstock,font=("Baskerville Old Face",15,"bold"))
rbe8.grid(row=9,column=0,sticky="w",pady=5)
rbe9=Radiobutton(chframe,text="Near Expiry   "
                 ,variable=emp,value=9,command=Nearstock,font=("Baskerville Old Face",15,"bold"))
rbe9.grid(row=10,column=0,sticky="w",pady=5)
rbe10=Radiobutton(chframe,text="Out of Stock "
                  ,variable=emp,value=10,command=oos,font=("Baskerville Old Face",15,"bold"))
rbe10.grid(row=11,column=0,sticky="w",pady=5)
rbe11=Radiobutton(chframe,text="Show Details "
                  ,variable=emp,value=11,font=("Baskerville Old Face",15,"bold"))
rbe11.grid(row=12,column=0,sticky="w",pady=5)
btnbill=Button(chframe,text="Billings",font=("Baskerville Old Face",25,"bold"),bd=4)
btnbill.grid(row=13,column=0,sticky="w")













