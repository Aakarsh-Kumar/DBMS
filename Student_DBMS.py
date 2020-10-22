from tkinter import*
from tkinter import ttk
from tkinter import messagebox
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("User Status")
        self.root.geometry("1350x700+0+0")
        self.root.iconbitmap("icon1.ico")

        #=============Title=====================================
        title=Label(self.root,text="Database and Table Status",bd=10,relief=GROOVE, font=("times new roman",40,"bold"),bg="yellow",fg="Red")
        title.pack(side=TOP,fill=X)

        #=====================variables Defined=================================
        self.Db_Status=IntVar()
        self.Tb_Status=IntVar()
        


        #========================Frame=========================================
        Manage_Frame=Frame(self.root,bd=20,highlightcolor="Red",relief=RIDGE,bg="Light Blue")
        Manage_Frame.place(x=330,y=100,width=725,height=350)

        #==================== LAble===========================================

        m_title=Label(Manage_Frame,text="Do you have the following for DBMS Existing:- ",bg="crimson",fg="White", font=("times new roman",25,"bold","underline"))
        m_title.grid(row=0,columnspan=3,pady=0,padx=3)


        lbl_Database=Label(Manage_Frame,text="Database ",bg="Orange",fg="White", font=("times new roman",30,"bold"))
        lbl_Database.grid(row=1,column=0,pady=20,padx=20,sticky="w")

        lbl_Table=Label(Manage_Frame,text="Table ",bg="Orange",fg="White", font=("times new roman",30,"bold"))
        lbl_Table.grid(row=2,column=0,pady=20,padx=20,sticky="w")

        #========================Button Frame=====================================================
        
        R_Db_yes = Radiobutton(Manage_Frame,width=10, text="YES",font=("times new roman",15,"bold"),variable=self.Db_Status, value=1,
                  command=self.Db_yes)
        R_Db_yes.grid( row=1,column=1,sticky='w')

        R_Db_no = Radiobutton(Manage_Frame,width=10, text="NO",font=("times new roman",15,"bold"), variable=self.Db_Status, value=2,
                  command=self.Db_no)
        R_Db_no.grid( row=1,column=2,sticky='w' )

        R_Tb_yes = Radiobutton(Manage_Frame,width=10, text="YES",font=("times new roman",15,"bold"), variable=self.Tb_Status, value=1,
                  command=self.Tb_yes)
        R_Tb_yes.grid( row=2,column=1,sticky='w')

        R_Tb_no = Radiobutton(Manage_Frame,width=10, text="NO",font=("times new roman",15,"bold"), variable=self.Tb_Status, value=2,
                  command=self.Tb_no)
        R_Tb_no.grid( row=2,column=2,sticky='w' )
           #========================Button================================
        Submitbtn=Button(Manage_Frame,text="Submit",bd=5,bg='Light Green',fg='Blue',font=("Algerian",15,"bold"),width=20,command=self.Submit).grid(row=3,column=1,padx=10,pady=10)

    def Db_yes(self):
        self.Db_Status=1
        return
       
    
    def Db_no(self):
        self.Db_Status=2
        return
            
    def Tb_yes(self):
        self.Tb_Status=1
        return
       
    
    def Tb_no(self):
        self.Tb_Status=2
        return

    def Submit(self):
        if self.Db_Status==2 and self.Tb_Status==2:
            ob=messagebox.askokcancel(" Databse and Table","You need to create the Database and Table in MySql")
            if ob>0:
                self.root.destroy()
                import Db_tb_creation  
                return
            return        
        elif self.Db_Status==2 and self.Tb_Status==1:
            messagebox.showerror("!Error!","You Cannot have Table, If there is no database.!")
            return
        elif self.Db_Status==1 and self.Tb_Status==2:
            ob=messagebox.askokcancel("Table","You need to create the Table in MySql")
            if ob>0:
                self.root.destroy()
                import Table_Creation
                return
            return
        elif self.Db_Status==1 and self.Tb_Status==1:  
            self.root.destroy()
            import Student_DBMS_main
            return
        return
root=Tk()
ob=Student(root)
root.mainloop()
