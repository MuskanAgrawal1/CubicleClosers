from tkinter import *
import tkinter.messagebox as MessageBox
import CompanyList
import mysql.connector
import jobseeker_login

mydb=mysql.connector.connect(host="localhost",user="root",password="MuskanAg1@",auth_plugin="mysql_native_password",database="muskan")
cursor = mydb.cursor(buffered=True)

def find_all(uid):
    q = "select * from jsdetails where jEmail ='" + str(uid) + "'"
    cursor.execute(q)
    return cursor.fetchall()


def job_prof(uid):
    x=uid
    print(uid)
    u = find_all(uid)
    root = Tk()
    root.title("Welcome")
    root.geometry("550x540+0+0")


    frame1 = Frame(root)
    frame1.grid()

    frame2 = Frame(frame1, width=550, height=140, padx=30, pady=10, relief=RIDGE)
    frame2.grid(row=1, column=0)

    frame3 = Frame(frame1, width=550, height=120, padx=66, pady=10, relief=RIDGE)
    frame3.grid(row=2, column=0)

    frame4 = Frame(frame1, width=550, height=50, padx=66, pady=10, relief=RIDGE)
    frame4.grid(row=0, column=0)



    lblSign = Label(frame4, text='My Profile', font=('arial', 20, 'bold'))
    lblSign.grid(row=0, column=0, sticky=W)

    lblName = Label(frame2, text='Name:   '+u[0][0], font=('arial', 14, 'bold'), bd=12, fg='black')
    lblName.grid(row=0, column=0, sticky=W)

    lblAddress = Label(frame2, text='Address:   '+u[0][1], font=('arial', 14, 'bold'), bd=12, fg='blue')
    lblAddress.grid(row=1, column=0, sticky=W)

    lblContact = Label(frame2, text='Contact:   '+u[0][2], font=('arial', 14, 'bold'), bd=12,fg='black')
    lblContact.grid(row=2, column=0, sticky=W)

    lblEmail = Label(frame2, text='Email:   '+u[0][4], font=('arial', 14, 'bold'), bd=12,fg='blue')
    lblEmail.grid(row=4, column=0, sticky=W)

    lblSkills = Label(frame2, text='Skills:   '+u[0][5], font=('arial', 14, 'bold'), bd=12,fg='black')
    lblSkills.grid(row=5, column=0, sticky=W)

    lblExperience = Label(frame2, text='Experience:   '+u[0][6], font=('arial', 14, 'bold'), bd=12,fg='blue')
    lblExperience.grid(row=6, column=0, sticky=W)

    lblDesiredL = Label(frame2, text='Desired Location:   '+u[0][7], font=('arial', 14, 'bold'), bd=12,fg='black')
    lblDesiredL.grid(row=7, column=0, sticky=W)


    def Exit() :
        root.destroy()

    def Delete(uid) :
        q2 = "Delete from jsdetails where jEmail ='" + str(uid) + "'"
        cursor.execute(q2)
        mydb.commit()
        MessageBox.showinfo("Status", "Account successfully deleted.")

    def Next(uid):
        query="SELECT interest,role FROM jsdetails where jEmail='" + str(uid) + "'"
        cursor.execute(query)
        A=cursor.fetchall()
        mydb.commit()
        i=A[0][0]
        r=A[0][1]
        CompanyList.Companies(i,r,uid)

    btnNext = Button(frame3, text="Next", font=('arial', 14, 'bold'), bg='green', fg='white', bd=12, pady=21, padx=12,
                     width=7,
                     command=lambda : Next(uid)).grid(row=0, column=0)
    btnDelete = Button(frame3, text="Delete\n"+"Account", font=('arial', 14, 'bold'), bg='yellow', fg='white', bd=12, pady=10,
                      padx=12, width=7,
                      command=lambda : Delete(x)).grid(row=0, column=1)
    btnExit = Button(frame3, text="Exit", font=('arial', 14, 'bold'), bg='red', fg='white', bd=12, pady=21, padx=12,
                     width=7, command=Exit).grid(row=0, column=2)

    root.mainloop()
