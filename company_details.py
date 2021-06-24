from tkinter import *
import tkinter
import company_login
import Company_Options
import Com_Skills
import mysql.connector
import tkinter.messagebox as MessageBox

mydb=mysql.connector.connect(host="localhost",user="root",password="MuskanAg1@",auth_plugin="mysql_native_password",database="muskan")
mycursor=mydb.cursor(buffered=True)

def company():
        root = Tk()
        root.title("Company Sign Up:")
        root.geometry("550x540+0+0")


        frame1 = Frame(root)
        frame1.grid()

        frame2 = Frame(frame1, width=650, height=200, padx=30,pady=40, relief=RIDGE)
        frame2.grid(row=1, column=0)

        frame3 = Frame(frame1, width=650, height=150, padx=66,pady=20,  relief=RIDGE)
        frame3.grid(row=2, column=0)

        frame4 = Frame(frame1, width=650, height=50, padx=66, pady=15, relief=RIDGE)
        frame4.grid(row=0, column=0)

        Name = StringVar()
        Address = StringVar()
        Contact = StringVar()
        Password = StringVar()
        Email = StringVar()


        lblSign = Label(frame4, text='Sign Up', font=('arial', 30, 'bold'))
        lblSign.grid(row=0, column=0, sticky=W)

        lblName = Label(frame2, text='Name:', font=('arial', 14, 'bold'), bd=12)
        lblName.grid(row=0, column=0, sticky=W)
        txtName = Entry(frame2, textvariable=Name, font=('arial', 14, 'bold'),bg='white', fg='black', bd=12)
        txtName.grid(row=0, column=1)

        lblAddress = Label(frame2, text='Address:', font=('arial', 14, 'bold'), bd=12)
        lblAddress.grid(row=1, column=0, sticky=W)
        txtAddress = Entry(frame2, textvariable=Address, font=('arial', 14, 'bold'),bg='white', fg='black', bd=12)
        txtAddress.grid(row=1, column=1)

        lblContact = Label(frame2, text='Contact no.:', font=('arial', 14, 'bold'), bd=12)
        lblContact.grid(row=2, column=0, sticky=W)
        txtContact = Entry(frame2, textvariable=Contact, font=('arial', 14, 'bold'),bg='white', fg='black', bd=12)
        txtContact.grid(row=2, column=1)

        lblPassword = Label(frame2, text='Password:', font=('arial', 14, 'bold'), bd=12)
        lblPassword.grid(row=3, column=0, sticky=W)
        txtPassword = Entry(frame2, textvariable=Password, font=('arial', 14, 'bold'), bg='white', fg='black', bd=12)
        txtPassword.grid(row=3, column=1)

        lblEmail = Label(frame2, text='Email:', font=('arial', 14, 'bold'), bd=12)
        lblEmail.grid(row=4, column=0, sticky=W)
        txtEmail = Entry(frame2, textvariable=Email, font=('arial', 14, 'bold'),bg='white', fg='black', bd=12)
        txtEmail.grid(row=4, column=1)



        def add(Name,Address,Contact,Password,Email):
            if (Name == "" or Address == "" or Contact == "" or Password == "" or Email == "") :
                MessageBox.showerror("Insert status", "All fields are required.")
            else:
                try :
                    query = "INSERT INTO Comdetails(cName,cAddress,cContact,cPassword,cEmail) VALUES(%s,%s,%s,%s,%s)"
                    values = (Name, Address, Contact, Password, Email)
                    mycursor.execute(query, values)
                    mydb.commit()
                    Com_Skills.SkillsC(Email)

                except :
                    MessageBox.showinfo("Error", "User already Exists.")



        def Reset():
            txtName.delete(0, END)
            Name = ""
            txtName.insert(END, Name)
            txtAddress.delete(0, END)
            Address = ""
            txtAddress.insert(END, Address)
            txtContact.delete(0, END)
            Phone = ""
            txtContact.insert(END, Phone)
            txtPassword.delete(0, END)
            Password = ""
            txtPassword.insert(END, Password)
            txtEmail.delete(0, END)
            Email = ""
            txtEmail.insert(END, Email)

        def Exit():
            root.destroy()

        btnNext = Button(frame3, text="Next", font=('arial', 14, 'bold'),bg='green',fg='white', bd=12, pady=14, padx=12, width=7,
                              command=lambda : add(txtName.get(), txtAddress.get(), txtContact.get(), txtPassword.get(), txtEmail.get())).grid(row=0, column=0)
        btnReset = Button(frame3, text="Reset", font=('arial', 14, 'bold'),bg='yellow',fg='white', bd=12, pady=14, padx=12, width=7,
                               command=Reset).grid(row=0, column=8)
        btnExit = Button(frame3, text="Exit", font=('arial', 14, 'bold'),bg='red',fg='white', bd=12, pady=14, padx=12, width=7,
                              command=Exit).grid(row=0, column=4)


        root.mainloop()