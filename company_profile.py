from tkinter import *
import tkinter.messagebox as MessageBox
import JobList
import mysql.connector
import jobseeker_login

mydb=mysql.connector.connect(host="localhost",user="root",password="MuskanAg1@",auth_plugin="mysql_native_password",database="muskan")
cursor = mydb.cursor(buffered=True)

def find_all(uid):
    q = "select * from comdetails where cEmail ='" + str(uid) + "'"
    cursor.execute(q)
    return cursor.fetchall()


def company_prof(uid):
    x=uid
    print(uid)
    u = find_all(uid)
    root = Tk()
    root.title("Welcome")
    root.geometry("550x540+0+0")


    frame1 = Frame(root)
    frame1.grid()

    frame2 = Frame(frame1, width=550, height=200, padx=30, pady=40, relief=RIDGE)
    frame2.grid(row=1, column=0)

    frame3 = Frame(frame1, width=550, height=180, padx=66, pady=20, relief=RIDGE)
    frame3.grid(row=2, column=0)

    frame4 = Frame(frame1, width=550, height=50, padx=66, pady=15, relief=RIDGE)
    frame4.grid(row=0, column=0)



    lblSign = Label(frame4, text='My Profile', font=('arial', 30, 'bold'))
    lblSign.grid(row=0, column=0, sticky=W)

    lblName = Label(frame2, text='Name:   '+u[0][0], font=('arial', 17, 'bold'), bd=12, fg='black')
    lblName.grid(row=0, column=0, sticky=W)

    lblAddress = Label(frame2, text='Address:   '+u[0][1], font=('arial', 17, 'bold'), bd=12, fg='blue')
    lblAddress.grid(row=1, column=0, sticky=W)

    lblContact = Label(frame2, text='Contact:   '+u[0][2], font=('arial', 17, 'bold'), bd=12,fg='black')
    lblContact.grid(row=2, column=0, sticky=W)

    lblEmail = Label(frame2, text='Email:   '+u[0][4], font=('arial', 17, 'bold'), bd=12,fg='blue')
    lblEmail.grid(row=4, column=0, sticky=W)


    def Exit() :
        root.destroy()

    def Delete(uid) :
        q2 = "Delete from comdetails where cEmail ='" + str(uid) + "'"
        cursor.execute(q2)
        mydb.commit()
        MessageBox.showinfo("Status", "Account successfully deleted.")

    def Next(uid):
        query="SELECT cinterest,cRole FROM comdetails where cEmail='" + str(uid) + "'"
        cursor.execute(query)
        A=cursor.fetchall()
        mydb.commit()
        i=A[0][0]
        r=A[0][1]
        JobList.Candidates(i,r,uid)


    btnNext = Button(frame3, text="Next", font=('arial', 14, 'bold'), bg='green', fg='white', bd=12, pady=25, padx=12,
                     width=7,
                     command=lambda : Next(uid)).grid(row=0, column=0)
    btnDelete = Button(frame3, text="Delete\n"+"Account", font=('arial', 14, 'bold'), bg='yellow', fg='white', bd=12, pady=14,
                      padx=12, width=7,
                      command=lambda : Delete(x)).grid(row=0, column=1)
    btnExit = Button(frame3, text="Exit", font=('arial', 14, 'bold'), bg='red', fg='white', bd=12, pady=25, padx=12,
                     width=7, command=Exit).grid(row=0, column=2)

    root.mainloop()
