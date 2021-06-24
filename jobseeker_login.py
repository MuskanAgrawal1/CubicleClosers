from tkinter import *
import tkinter.messagebox as MessageBox
import JobSeeker_Options
import job_profile
import jobseeker_details
import mysql.connector
import JobList

mydb2=mysql.connector.connect(host="localhost",user="root",password="MuskanAg1@",auth_plugin="mysql_native_password",database="muskan")
mycursor2=mydb2.cursor(buffered=True)


def find(uid):
    q = "select jEmail, jPassword from JSdetails where jEmail ='" + str(uid) + "'"
    mycursor2.execute(q)
    return (mycursor2.fetchall())


def check(Email, Password):
    if(Email=="" or Password==""):
        MessageBox.showerror("Error", "All fields are required.")
    else:
        a = find(Email)
        try :
            if Password == a[0][1] :
                JobSeeker_Options.JO(Email)
            else :
                print(Email)
                print(Password)
                print(a[0][1])
                MessageBox.showerror("User: " + str(Email) + " doesn't exist.")
        except IndexError :
            MessageBox.showinfo("Error", "User: " + str(Email) + " doesn't exist.")



def jobSeekerLog():
        root = Tk()
        root.title("JobSeeker Log in:")
        root.geometry("550x540+0+0")


        frame1 = Frame(root)
        frame1.grid()

        frame2 = Frame(frame1, width=650, height=100, padx=10,pady=50,  relief=RIDGE)
        frame2.grid(row=1, column=0)

        frame3 = Frame(frame1, width=650, height=20, padx=10, pady=10, relief=RIDGE)
        frame3.grid(row=2, column=0)

        frame4 = Frame(frame1, width=650, height=150, padx=66,pady=40,  relief=RIDGE)
        frame4.grid(row=3, column=0)

        frame5 = Frame(frame1, width=50, height=50, padx=10, pady=20, relief=RIDGE)
        frame5.grid(row=0, column=0)

        Password = StringVar()
        Email = StringVar()

        lblLogin = Label(frame5, text='Log In', font=('arial', 30, 'bold'))
        lblLogin.grid(row=0, column=0, sticky=W)

        lblEmail = Label(frame2, text='Email:', font=('arial', 14, 'bold'), bd=12)
        lblEmail.grid(row=1, column=0, sticky=W)
        txtEmail = Entry(frame2, textvariable=Email, font=('arial', 14, 'bold'), bg='white', fg='black', bd=12)
        txtEmail.grid(row=1, column=1)

        lblPassword = Label(frame2, text='Password:', font=('arial', 14, 'bold'), bd=12)
        lblPassword.grid(row=2, column=0, sticky=W)
        txtPassword = Entry(frame2, textvariable=Password, font=('arial', 14, 'bold'), bg='white', fg='black', bd=12)
        txtPassword.grid(row=2, column=1)


        def Next():
            MessageBox.showinfo('Logged in Successfully.')


        def Reset():

            txtPassword.delete(0, END)
            Password = ""
            txtPassword.insert(END, Password)
            txtEmail.delete(0, END)
            Email = ""
            txtEmail.insert(END, Email)



        def Exit():
            root.destroy()

        btnSignUp = Button(frame3, text="Sign Up", font=('arial', 14, 'bold'), fg='black', bd=9, pady=5,padx=12, width=7,
                           command=lambda : jobseeker_details.jobSeeker()).grid(row=0, column=2)
        btnNext = Button(frame4, text="Next", font=('arial', 14, 'bold'),bg='red',fg='white', bd=12, pady=14, padx=12, width=7,
                               command=lambda : check(txtEmail.get(),txtPassword.get())).grid(row=0, column=0)
        btnReset = Button(frame4, text="Reset", font=('arial', 14, 'bold'),bg='yellow',fg='white', bd=12, pady=14, padx=12, width=7,
                               command=Reset).grid(row=0, column=1)
        btnExit = Button(frame4, text="Exit", font=('arial', 14, 'bold'),bg='green',fg='white', bd=12, pady=14, padx=12, width=7,
                              command=Exit).grid(row=0, column=2)


        root.mainloop()