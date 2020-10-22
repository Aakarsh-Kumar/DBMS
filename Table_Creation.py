from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Table Creation")
        self.root.geometry("1350x700+0+0")
        self.root.iconbitmap("icon1.ico")
        #============VAriable==============================================
        self.name=StringVar()
        self.Password=StringVar()
        self.port=IntVar()
        self.database=StringVar()
        self.n_table=StringVar()
        #========================Frame=========================================
        Manage_Frame=Frame(self.root,bd=20,highlightcolor="Red",relief=RIDGE,bg="Light Blue")
        Manage_Frame.place(x=330,y=100,width=725,height=375)

        #==================== LAble===========================================

        m_title=Label(Manage_Frame,text="You need to fill the following data of MySql:",bg="crimson",fg="White", font=("times new roman",25,"bold","underline"))
        m_title.grid(row=0,columnspan=3,pady=0,padx=30)


        lbl_Password=Label(Manage_Frame,text="Password",bg="Orange",fg="White", font=("times new roman",20,"bold"))
        lbl_Password.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_Password=Entry(Manage_Frame, font=("times new roman",15,"bold"),show='•',textvariable=self.Password,bd=5,relief=GROOVE)
        txt_Password.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_Port=Label(Manage_Frame,text="Port No.",bg="Orange",fg="White", font=("times new roman",20,"bold"))
        lbl_Port.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_Port=Entry(Manage_Frame, font=("times new roman",15,"bold"),textvariable=self.port,bd=5,relief=GROOVE)
        txt_Port.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_nm=Label(Manage_Frame,text="Name of Database",bg="Orange",fg="White", font=("times new roman",20,"bold"))
        lbl_nm.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_nm=Entry(Manage_Frame, font=("times new roman",15,"bold"),textvariable=self.name,bd=5,relief=GROOVE)
        txt_nm.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_tb=Label(Manage_Frame,text="Name of New Table",bg="Orange",fg="White", font=("times new roman",20,"bold"))
        lbl_tb.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        txt_nTAble=Entry(Manage_Frame, font=("times new roman",15,"bold"),textvariable=self.n_table,bd=5,relief=GROOVE)
        txt_nTAble.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        #================Button=================================================
        Submitbtn=Button(root,text="Submit",bd=5,bg='Light Green',fg='Blue',font=("Algerian",15,"bold"),width=20,command=self.Submit).place(x=550,y=400)
    

    def Submit(self):
        if str(self.Password.get()).lstrip()!="" and str(self.port.get()).lstrip()!="" and str(self.name.get()).lstrip()!="" and str(self.n_table.get()).lstrip()!="":
            try:
                mydb=mysql.connector.connect(host="localhost",user="root",port=int(self.port.get()),password=self.Password.get(),\
                                    database=self.name.get())
                mycursor=mydb.cursor()
                mycursor.execute("CREATE TABLE "+self.n_table.get()+" (Adm_No int(100) Primary Key,\
                name varchar(100),class varchar(100), gender varchar(100),father varchar(100),contact varchar(100),dob varchar(100),school varchar(100),address varchar(200))")
                mydb.commit()
                mydb.close()
                messagebox.showinfo("Created","Table successfully created")
                ob=messagebox.askyesno("Open DBMS","Do you want to open Management System")
                if ob>0:
                    self.root.destroy()
                    import Student_DBMS
            
            except Exception as e:
                messagebox.showerror("Error!",e)
        else:
            messagebox.showerror("Error!","All data required.")




root=Tk()
ob=Student(root)
root.mainloop()