from tkinter import *
import tkinter.messagebox as MessageBox
import JobSeeker_Options
import jobseeker_login
import job_profile
import mysql.connector
import JS_Skills
import JobList

mydb2=mysql.connector.connect(host="localhost",user="root",password="MuskanAg1@",auth_plugin="mysql_native_password",database="muskan")
mycursor2=mydb2.cursor(buffered=True)

def jobSeeker():
        root = Tk()
        root.title("JobSeeker Sign Up:")
        root.geometry("550x540+0+0")


        frame1 = Frame(root)
        frame1.grid()

        frame2 = Frame(frame1, width=650, height=200, padx=30, pady=20, relief=RIDGE)
        frame2.grid(row=0, column=0)

        frame3 = Frame(frame1, width=650, height=150, padx=66, pady=20, relief=RIDGE)
        frame3.grid(row=1, column=0)


        Name = StringVar()
        Address = StringVar()
        Phone  = StringVar()
        Password = StringVar()
        Email = StringVar()
        Skills = StringVar()
        Experience = StringVar()
        DesiredL = StringVar()

        lblName = Label(frame2, text='Name:', font=('arial', 14, 'bold'), bd=12)
        lblName.grid(row=0, column=0, sticky=W)
        txtName = Entry(frame2, textvariable=Name, font=('arial', 14, 'bold'), bg='white', fg='black', bd=12)
        txtName.grid(row=0, column=1)

        lblAddress = Label(frame2, text='Address:', font=('arial', 14, 'bold'), bd=12)
        lblAddress.grid(row=1, column=0, sticky=W)
        txtAddress = Entry(frame2, textvariable=Address, font=('arial', 14, 'bold'), bg='white', fg='black', bd=12)
        txtAddress.grid(row=1, column=1)

        lblContact = Label(frame2, text='Contact no.:', font=('arial', 14, 'bold'), bd=12)
        lblContact.grid(row=2, column=0, sticky=W)
        txtContact = Entry(frame2, textvariable=Phone, font=('arial', 14, 'bold'), bg='white', fg='black', bd=12)
        txtContact.grid(row=2, column=1)

        lblPassword = Label(frame2, text='Password:', font=('arial', 14, 'bold'), bd=12)
        lblPassword.grid(row=3, column=0, sticky=W)
        txtPassword = Entry(frame2, textvariable=Password, font=('arial', 14, 'bold'), bg='white', fg='black', bd=12)
        txtPassword.grid(row=3, column=1)

        lblEmail = Label(frame2, text='Email:', font=('arial', 14, 'bold'), bd=12)
        lblEmail.grid(row=4, column=0, sticky=W)
        txtEmail = Entry(frame2, textvariable=Email, font=('arial', 14, 'bold'), bg='white', fg='black', bd=12)
        txtEmail.grid(row=4, column=1)

        lblSkills = Label(frame2, text='Skills:', font=('arial', 14, 'bold'), bd=12)
        lblSkills.grid(row=5, column=0, sticky=W)
        txtSkills = Entry(frame2, textvariable=Skills, font=('arial', 14, 'bold'),bg='white', fg='black', bd=12)
        txtSkills.grid(row=5, column=1)


        lblExperience = Label(frame2, text='Experience:', font=('arial', 14, 'bold'), bd=12)
        lblExperience.grid(row=6, column=0, sticky=W)
        txtExperience= Entry(frame2, textvariable=Experience, font=('arial', 14, 'bold'),bg='white', fg='black', bd=12)
        txtExperience.grid(row=6, column=1)

        lblDesiredL = Label(frame2, text='Desired Location:', font=('arial', 14, 'bold'), bd=12)
        lblDesiredL.grid(row=7, column=0, sticky=W)
        txtDesiredL = Entry(frame2, textvariable=DesiredL, font=('arial', 14, 'bold'), bg='white', fg='black', bd=12)
        txtDesiredL.grid(row=7, column=1)



        def add(Name,Address,Contact,Password,Email,Skills,Experience, DesiredL):
            if (Name == "" or Address == "" or Contact == "" or Password == "" or Email == "" or Skills=="" or Experience=="" or DesiredL=="") :
                MessageBox.showerror("Insert status", "All fields are required.")
            else:
                try :
                    query = "INSERT INTO JSdetails(jName,jAddress,jContact,jPassword,jEmail,jSkills,jExperience, jDesiredL) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
                    values = (Name, Address, Contact, Password, Email, Skills, Experience, DesiredL)
                    mycursor2.execute(query, values)
                    mydb2.commit()
                    JS_Skills.Skills(Email)

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
            txtSkills.delete(0, END)
            Skills = ""
            txtSkills.insert(END, Skills)
            txtExperience.delete(0, END)
            Experience = ""
            txtExperience.insert(END, Experience)
            txtDesiredL.delete(0, END)
            DesiredL = ""
            txtDesiredL.insert(END, DesiredL)



        def Exit():
            root.destroy()

        btnNext = Button(frame3, text="Next", font=('arial', 14, 'bold'),bg='red',fg='white', bd=12, pady=14, padx=12, width=7,
                               command=lambda : add(txtName.get(), txtAddress.get(), txtContact.get(), txtPassword.get(), txtEmail.get(), txtSkills.get(), txtExperience.get(), txtDesiredL.get())).grid(row=0, column=0)
        btnReset = Button(frame3, text="Reset", font=('arial', 14, 'bold'),bg='yellow',fg='white', bd=12, pady=14, padx=12, width=7,
                               command=Reset).grid(row=0, column=1)
        btnExit = Button(frame3, text="Exit", font=('arial', 14, 'bold'),bg='green',fg='white', bd=12, pady=14, padx=12, width=7,
                              command=Exit).grid(row=0, column=2)


        root.mainloop()