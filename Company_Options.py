from tkinter import *
import JobList
import company_profile
import jobseeker_details
import tkinter.messagebox as MessageBox
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="MuskanAg1@",auth_plugin="mysql_native_password",database="muskan")
cursor=mydb.cursor(buffered=True)

def CO(uid):
    root = Tk()
    root.title("Options")
    root.geometry("550x540+0+0")

    frame1 = Frame(root)
    frame1.grid()

    frame2 = Frame(frame1, width=650, height=200, padx=65, pady=180, relief=RIDGE)
    frame2.grid(row=0, column=0)

    def Next(uid):
        query="SELECT cinterest,cRole FROM comdetails where cEmail='" + str(uid) + "'"
        cursor.execute(query)
        A=cursor.fetchall()
        mydb.commit()
        i=A[0][0]
        r=A[0][1]
        JobList.Candidates(i,r,uid)

    btnProfile = Button(frame2, text="My Profile", font=('arial', 14, 'bold'), bg='cyan', fg='black', bd=12, padx=75,
                        pady=10, width=20,
                        command=lambda: company_profile.company_prof(uid)).grid(row=0, column=0)
    btnLJ = Button(frame2, text="List of Jobseekers", font=('arial', 14, 'bold'), bg='light pink', fg='black', bd=12,
                   padx=75, pady=10, width=20,
                   command=lambda: Next(uid)).grid(row=1, column=0)

    root.mainloop()