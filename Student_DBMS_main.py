from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector 
import math,random,os
import datetime
class Student:
        
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System(2.0v)")
        self.root.geometry("1350x700+0+0")
        self.root.iconbitmap("icon1.ico")
#============================================================================================
        

        title=Label(self.root,text="Company Name",bd=10,relief=GROOVE, font=("times new roman",40,"bold"),bg="yellow",fg="Red")
        title.pack(side=TOP,fill=X)

        
        
        

        #================All Variables==============================

        
        self.name=StringVar()
        self.Password=StringVar()
        self.port=IntVar()
        self.database=StringVar()
        self.n_table=StringVar()

        #======================Home frame=====================================
        self.Home_Frame=Frame(self.root,bd=20,highlightcolor="Red",relief=RIDGE,bg="Light Blue")
        self.Home_Frame.place(x=330,y=100,width=725,height=375)
        Home_Frame=self.Home_Frame
        #==================== LAble===========================================
    
        m_title=Label(Home_Frame,text="You need to fill the following data of MySql:",bg="crimson",fg="White", font=("times new roman",25,"bold","underline"))
        m_title.grid(row=0,columnspan=3,pady=0,padx=30)


        lbl_Password=Label(Home_Frame,text="Password",bg="Orange",fg="White", font=("times new roman",20,"bold"))
        lbl_Password.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_Password=Entry(Home_Frame, font=("times new roman",15,"bold"),show='•',textvariable=self.Password,bd=5,relief=GROOVE)
        txt_Password.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_Port=Label(Home_Frame,text="Port No.",bg="Orange",fg="White", font=("times new roman",20,"bold"))
        lbl_Port.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_Port=Entry(Home_Frame, font=("times new roman",15,"bold"),textvariable=self.port,bd=5,relief=GROOVE)
        txt_Port.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_nm=Label(Home_Frame,text="Name of Database",bg="Orange",fg="White", font=("times new roman",20,"bold"))
        lbl_nm.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_nm=Entry(Home_Frame, font=("times new roman",15,"bold"),textvariable=self.name,bd=5,relief=GROOVE)
        txt_nm.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_tb=Label(Home_Frame,text="Name of Table",bg="Orange",fg="White", font=("times new roman",20,"bold"))
        lbl_tb.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        txt_nTAble=Entry(Home_Frame, font=("times new roman",15,"bold"),textvariable=self.n_table,bd=5,relief=GROOVE)
        txt_nTAble.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        #================Button=================================================
        Submitbtn=Button(root,text="Submit",bd=5,bg='Light Green',fg='Blue',font=("Algerian",15,"bold"),width=20,command=self.Submit).place(x=550,y=400)
    
        
    def Submit(self):
        if str(self.Password.get()).lstrip()!="" and str(self.port.get()).lstrip()!="" and int(self.port.get())!=0 and str(self.name.get()).lstrip()!="" and str(self.n_table.get())!="":
            try:
                con=mysql.connector.connect(host="localhost",user="root",port=self.port.get(),password=self.Password.get(),database=self.name.get())
                cur=con.cursor()
                cur.execute("select * from "+self.n_table.get())
                con.close()
                self.start()
            except Exception as qw:

                messagebox.showinfo("Error!","An Error occured.\n"+str(qw))

        else:
            messagebox.showerror("Error!","All details are must")
            
    def start(self):

        self.Home_Frame.destroy()

        self.roll_no_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        self.father_var=StringVar()
        self.school_var=StringVar()
        x =str(datetime.datetime.now().strftime("%d/%m/%Y"))
    
            

        
        self.class_var=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()
        self.search_by.set("Select")
        

        #=========================date_time frame===============================
        Date_Frame=Frame(self.root,relief=RIDGE,bg="yellow")
        Date_Frame.place(x=1100,y=15,width=200,height=40)

        date_title=Label(Date_Frame,text=x,bg="yellow",fg="Black", font=("times new roman",25,"bold","underline"))
        date_title.grid(row=0,column=0)
        

        #============Manage Frame=============================
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=450,height=580)

        m_title=Label(Manage_Frame,text="Manage Students",bg="crimson",fg="White", font=("times new roman",25,"bold","underline"))
        m_title.grid(row=0,columnspan=2,pady=0)

        lbl_roll=Label(Manage_Frame,text="Adm No.",bg="crimson",fg="White", font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=0,padx=20,sticky="w")

        txt_Roll=Entry(Manage_Frame, font=("times new roman",15,"bold"),state=DISABLED,bd=5,relief=GROOVE,textvariable=self.roll_no_var)
        txt_Roll.grid(row=1,column=1,pady=0,padx=20,sticky="w")

        lbl_name=Label(Manage_Frame,text="Name",bg="crimson",fg="White", font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_name=Entry(Manage_Frame, font=("times new roman",15,"bold"),textvariable=self.name_var,bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_class=Label(Manage_Frame,text="Class",bg="crimson",fg="White", font=("times new roman",20,"bold"))
        lbl_class.grid(row=3,column=0,pady=5,padx=20,sticky="w")
        
        combo_class=ttk.Combobox(Manage_Frame, font=("times new roman",13,"bold"),textvariable=self.class_var,state="readonly")
        combo_class['values']=("6","7","8","9","10","11","12","Programming","Crash Course","Other Courses")
        combo_class.grid(row=3,column=1,padx=20,pady=5)

        '''txt_email=Entry(Manage_Frame, font=("times new roman",15,"bold"),textvariable=self.email_var,bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")'''

        lbl_gender=Label(Manage_Frame,text="Gender",bg="crimson",fg="White", font=("times new roman",20,"bold"))
        lbl_gender.grid(row=4,column=0,pady=0,padx=20,sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame, font=("times new roman",13,"bold"),textvariable=self.gender_var,state="readonly")
        combo_gender['values']=("Male","Female","Others")
        combo_gender.grid(row=4,column=1,padx=20,pady=0)

        lbl_father=Label(Manage_Frame,text="Father's Name",bg="crimson",fg="White", font=("times new roman",18,"bold"))
        lbl_father.grid(row=5,column=0,pady=10,padx=20,sticky="w") 

        txt_father=Entry(Manage_Frame, font=("times new roman",15,"bold"),textvariable=self.father_var,bd=5,relief=GROOVE)
        txt_father.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lbl_contact=Label(Manage_Frame,text="Contact",bg="crimson",fg="White", font=("times new roman",20,"bold"))
        lbl_contact.grid(row=6,column=0,pady=5,padx=20,sticky="w")

        txt_contact=Entry(Manage_Frame, font=("times new roman",15,"bold"),textvariable=self.contact_var,bd=5,relief=GROOVE)
        txt_contact.grid(row=6,column=1,pady=5,padx=20,sticky="w") 
    

        lbl_dob=Label(Manage_Frame,text="D.O.B",bg="crimson",fg="White", font=("times new roman",20,"bold"))
        lbl_dob.grid(row=7,column=0,pady=5,padx=20,sticky="w")
    
        txt_dob=Entry(Manage_Frame, font=("times new roman",15,"bold"),textvariable=self.dob_var,bd=5,relief=GROOVE)
        txt_dob.grid(row=7,column=1,pady=5,padx=20,sticky="w") 

        lbl_school=Label(Manage_Frame,text="School",bg="crimson",fg="White", font=("times new roman",20,"bold"))
        lbl_school.grid(row=8,column=0,pady=10,padx=20,sticky="w")

        txt_school=Entry(Manage_Frame, font=("times new roman",15,"bold"),textvariable=self.school_var,bd=5,relief=GROOVE)
        txt_school.grid(row=8,column=1,pady=5,padx=20,sticky="w")

        lbl_address=Label(Manage_Frame,text="Address",bg="crimson",fg="White", font=("times new roman",20,"bold"))
        lbl_address.grid(row=9,column=0,pady=10,padx=20,sticky="w")

        self.txt_address=Text(Manage_Frame,width=30,height=4,font=("",10))
        self.txt_address.grid(row=9,column=1,pady=10,padx=20,sticky='w')

#========================Button Frame===========================
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=15,y=515,width=420)

        addbtn=Button(btn_Frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(btn_Frame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        deletebtn=Button(btn_Frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        Clearbtn=Button(btn_Frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)

        #==================Detail Frame========================
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Detail_Frame.place(x=500,y=100,width=850,height=580)

        lbl_search=Label(Detail_Frame,text="Search By",bg="crimson",fg="White", font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,width=10,textvariable=self.search_by, font=("times new roman",13,"bold"),state="readonly")
        combo_search['values']=("Adm_No","Name","Contact","Class")
        combo_search.grid(row=0,column=1,padx=20,pady=10)

        txt_search=Entry(Detail_Frame,width=20,textvariable=self.search_txt, font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w") 

        searchbtn=Button(Detail_Frame,text="Search",command=self.search_data,width=8,pady=0,padx=2).grid(row=0,column=3,padx=5,pady=10)
        showallbtn=Button(Detail_Frame,text="Show All",width=8,pady=0,padx=2,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)
        closebtn=Button(Detail_Frame,text="Exit",width=8,pady=0,padx=2,command=self.exit).grid(row=0,column=5,padx=10,pady=10)
        hidebtn=Button(Detail_Frame,text="Hide",command=self.hide,width=8,padx=2,pady=0).grid(row=0,column=6,padx=5,pady=10)

#===================TABLE FRAME===============================
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=10,y=70,width=760,height=500)
        
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)

        self.Student_table=ttk.Treeview(Table_Frame,column=("Adm_No","Name","Class","Gender","Father","Contact","D.O.B","School","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("Adm_No",text="Adm No.")
        self.Student_table.heading("Name",text="Name")
        self.Student_table.heading("Class",text="Class")
        self.Student_table.heading("Gender",text="Gender")
        self.Student_table.heading("Father",text="Father's Name")
        self.Student_table.heading("Contact",text="Contact")
        self.Student_table.heading("D.O.B",text="D.O.B")
        self.Student_table.heading("School",text="School")
        self.Student_table.heading("Address",text="Address")
        self.Student_table['show']='headings'
        self.Student_table.column("Adm_No",width=60)
        self.Student_table.column("Name",width=225)
        self.Student_table.column("Class",width=100)
        self.Student_table.column("Gender",width=50)
        self.Student_table.column("Father",width=200)
        self.Student_table.column("Contact",width=100)
        self.Student_table.column("D.O.B",width=100)
        self.Student_table.column("School",width=175)
        self.Student_table.column("Address",width=250)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        self.refresh()
    

    def add_students(self):
            self.random_roll()
            if self.roll_no_var.get().lstrip()=="" or self.name_var.get().lstrip()=="" or self.class_var.get().lstrip()=="" or self.class_var.get()=="Select" or self.gender_var.get().lstrip()=="" or self.gender_var.get()=="Select" or self.father_var.get().lstrip()=="" or self.contact_var.get().lstrip()=="" or self.dob_var.get()=="".lstrip() or self.school_var.get().lstrip()=="" or self.txt_address.get('1.0',END).lstrip()=="":
                messagebox.showerror("!Error!","All fields are reqiured.!")
            elif len(self.contact_var.get())!=10:
                messagebox.showerror("!Error!","Contact No. is incorrect!")
            else:
                con=mysql.connector.connect(host="localhost",user="root",port=self.port.get(),password=self.Password.get(),database=self.name.get())
                cur=con.cursor()
                cur.execute("insert into "+self.n_table.get()+" values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.roll_no_var.get(),
                                                                                    self.name_var.get(),
                                                                                    self.class_var.get(),
                                                                                    self.gender_var.get(),
                                                                                    self.father_var.get(),
                                                                                    self.contact_var.get(),
                                                                                    self.dob_var.get(),
                                                                                    self.school_var.get(),
                                                                                    self.txt_address.get('1.0',END)
                                                                                    ))

                con.commit()
                
                self.fetch_data()
                self.refresh()
                self.clear()
                con.close()
                messagebox.showinfo("Inserted","Data is Insrted successfully")
                
    def fetch_data(self):
        con=mysql.connector.connect(host="localhost",user="root",port=self.port.get(),password=self.Password.get(),database=self.name.get())
        cur=con.cursor()
        cur.execute("select * from "+self.n_table.get()) 
        rows=cur.fetchall()
        if len(rows)>=0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                        self.Student_table.insert('',END,values=row)
                con.commit()
                
        con.close()
    def refresh(self):
        self.Student_table.column("Adm_No",width=60)
        self.Student_table.column("Name",width=225)
        self.Student_table.column("Class",width=100)
        self.Student_table.column("Gender",width=50)
        self.Student_table.column("Father",width=200)
        self.Student_table.column("Contact",width=100)
        self.Student_table.column("D.O.B",width=100)
        self.Student_table.column("School",width=175)
        self.Student_table.column("Address",width=250)
        self.class_var.set("Select")
        self.gender_var.set("Select")
    
    def clear(self):
        self.roll_no_var.set("")
        self.name_var.set("")
        self.class_var.set("Select")
        self.gender_var.set("Select")
        self.father_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.school_var.set("")
        self.txt_address.delete("1.0",END)
        self.refresh()

    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        content=self.Student_table.item(cursor_row)
        row=content['values']
        self.roll_no_var.set(row[0])
        self.name_var.set(row[1])
        self.class_var.set(row[2])
        self.gender_var.set(row[3])
        self.father_var.set(row[4])
        self.contact_var.set(row[5])
        self.dob_var.set(row[6])
        self.school_var.set(row[7])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[8])
    
    def hide(self):
        con=mysql.connector.connect(host="localhost",user="root",port=self.port.get(),password=self.Password.get(),database=self.name.get())
        cur=con.cursor()
        cur.execute("select * from "+self.n_table.get()+" where Adm_No=''") 
        rows=cur.fetchall()
        self.Student_table.delete(*self.Student_table.get_children())
        for row in rows:
                self.Student_table.insert('',END,values=row)
        con.commit()
    
        con.close()
        self.refresh()


    def update_data(self):
        op=messagebox.askyesno("Clear","Are you sure, you want to Update!")
        if op>0:
            if self.roll_no_var.get().lstrip()=="" or self.name_var.get().lstrip()=="" or self.class_var.get().lstrip()=="" or self.class_var.get()=="Select" or self.gender_var.get().lstrip()=="" or self.gender_var.get()=="Select" or self.father_var.get().lstrip()=="" or self.contact_var.get().lstrip()=="" or self.dob_var.get()=="".lstrip() or self.school_var.get().lstrip()=="" or self.txt_address.get('1.0',END).lstrip()=="":
                messagebox.showerror("!Error!","All fields are reqiured.!")
            elif len(self.contact_var.get())!=10:
                messagebox.showerror("!Error!","Contact No. is incorrect!")
            else:
 
                con=mysql.connector.connect(host="localhost",user="root",port=self.port.get(),password=self.Password.get(),database=self.name.get())
                cur=con.cursor()
                cur.execute("update "+self.n_table.get()+" set name=%s,class=%s,gender=%s,father=%s,contact=%s,dob=%s,school=%s,address=%s where Adm_No=%s",(
                                                                                                        self.name_var.get(),
                                                                                                        self.class_var.get(),
                                                                                                        self.gender_var.get(),
                                                                                                        self.father_var.get(),
                                                                                                        self.contact_var.get(),
                                                                                                        self.dob_var.get(),
                                                                                                        self.school_var.get(),
                                                                                                        self.txt_address.get('1.0',END),
                                                                                                        self.roll_no_var.get()
                                                                                                        ))
                con.commit()
                self.fetch_data()
                self.refresh()
                self.clear()
                con.close() 
                messagebox.showinfo("Updated","Data Updated successfully")
    
    def delete_data(self):
        op=messagebox.askyesno("Delete","Are you sure, you want to Delete!")
        if op>0:
            con=mysql.connector.connect(host="localhost",user="root",port=self.port.get(),password=self.Password.get(),database=self.name.get())
            cur=con.cursor()
            cur.execute("delete from "+ self.n_table.get()+" where Adm_No= "+self.roll_no_var.get())
            con.commit()
            con.close()
            self.fetch_data()
            self.clear()
            self.refresh()
            messagebox.showinfo("Deleted","Your data is successfully deleted.")
    
    def search_data(self):
        if self.search_by.get() !="Select" and self.search_txt.get()!="" :
            con=mysql.connector.connect(host="localhost",user="root",port=self.port.get(),password=self.Password.get(),database=self.name.get())
            cur=con.cursor()
            cur.execute("select * from "+self.n_table.get()+ " where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'") 
            rows=cur.fetchall()
            if len(rows)!=0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                        self.Student_table.insert('',END,values=row)
                con.commit()
            else:
                messagebox.showinfo("No Data","No data found related to your search.")
            con.close()
            self.refresh()
        else:
            messagebox.showerror("No Text!","No text found in the search by area")
            self.refresh()
    
    def random_roll(self):
        self.x=random.randint(1,10000)
        self.roll_no_var.set(str(self.x))
        
    def exit(self):
        op=messagebox.askyesno("Exit","Are you sure, you want to Exit!")
        if op>0:
            self.root.destroy()
        else:
            messagebox.showinfo("Thanks","Thanks for staying back!")  

    


root=Tk()
ob=Student(root)
root.mainloop()


