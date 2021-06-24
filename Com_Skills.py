from tkinter import *
import tkinter as tk
import company_login
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="MuskanAg1@",auth_plugin="mysql_native_password",database="muskan")
mycursor=mydb.cursor(buffered=True)

def SkillsC(uid):
    root = Tk()
    root.title("My Skills:")
    root.geometry("550x540+0+0")

    frame1 = Frame(root)
    frame1.grid()

    frame2 = Frame(frame1, width=550, height=200, padx=20, pady=30, relief=RIDGE)
    frame2.grid(row=0, column=0)

    frame3 = Frame(frame1, width=550, height=200, padx=66, pady=30, relief=RIDGE)
    frame3.grid(row=1, column=0)

    frame4 = Frame(frame1, width=550, height=60, padx=66, pady=30, relief=RIDGE)
    frame4.grid(row=2, column=0)


    #MAINOPTIONS = ["Technology", "Medical", "Art and Creativity", "Business and Marketing", "Engineering", "Extra"]
    #OPTIONS1 = ["Android Developer", "Web developer", "Data Analyst", "Graphics Designer"]
    #OPTIONS2 = ["Nursing", "Opthalmologist", "Dentist", "Doctor", "Pharmacist"]
    #OPTIONS3 = ["Dancing", "Painting and Arts", "Singing"]
    #OPTIONS4 = ["Managing", "Account Executive", "Sales Manager", "HR"]
    #OPTIONS5 = ["Mechanical Engineer", "Civil Engineer", "Electrical Engineering", "Electronics Engineering",
    #            "Chemical Engineer"]
    #OPTIONS6 = ["Teaching", "Cooking", "Driving"]


    options = tk.StringVar(root)
    options.set("Select One")  # default value

    lblField = Label(frame2, text='Select the domain of required employee:', font=('arial', 17, 'bold'), bd=12, fg='maroon')
    lblField.grid(row=1, column=0, sticky=W,padx=25,pady=10)

    om1 = tk.OptionMenu(frame2, options, "Technology", "Medical", "Art and Creativity", "Business and Marketing", "Engineering", "Other")
    om1.place(x=40, y=68)

    b1 = tk.Button(frame2, text='Save', command=lambda : my_show(uid),font=('arial', 16, 'bold'), bg='pink')
    b1.place(x=280, y=60)


    def my_show(uid) :
        opt=(options.get())
        print(opt)
        query = "UPDATE comdetails SET cInterest=%s where cEmail=%s"
        val = (opt,uid)
        mycursor.execute(query, val)
        mydb.commit()
        choose(opt)

    def choose(opt):
        opt2 = tk.StringVar(root)
        options2 = tk.StringVar(root)
        options2.set("Select One")  # default value

        if (opt == 'Technology') :
            om2 = tk.OptionMenu(frame3, options2, "Android Developer", "Web developer", "Data Analyst",
                                "Graphics Designer")
            om2.place(x=30, y=68)
        elif (opt == 'Medical') :
            om2 = tk.OptionMenu(frame3, options2, "Nursing", "Opthalmologist", "Dentist", "Doctor", "Pharmacist")
            om2.place(x=30, y=68)
        elif (opt == 'Art and Creativity') :
            om2 = tk.OptionMenu(frame3, options2, "Dancing", "Painting and Arts", "Singing")
            om2.place(x=30, y=68)
        elif (opt == "Business and Marketing") :
            om2 = tk.OptionMenu(frame3, options2, "Managing", "Account Executive", "Sales Manager", "HR")
            om2.place(x=30, y=68)
        elif (opt == 'Engineering') :
            om2 = tk.OptionMenu(frame3, options2, "Mechanical Engineer", "Civil Engineer", "Electrical Engineering",
                                "Electronics Engineering",
                                "Chemical Engineer")
            om2.place(x=30, y=68)
        elif (opt == 'Other') :
            om2 = tk.OptionMenu(frame3, options2, "Teaching", "Cooking", "Driving")
            om2.place(x=30, y=68)


        lblRole = Label(frame3, text='Select the job specification:', font=('arial', 17, 'bold'), bd=12,fg='maroon')
        lblRole.grid(row=1, column=0, sticky=W, padx=35, pady=20)

        b2 = tk.Button(frame3, text='Save', command=lambda : my_show2(uid),font=('arial', 16, 'bold'), bg='pink')
        b2.place(x=260, y=60)

        def my_show2(uid) :
            opt2 = (options2.get())
            query = "UPDATE comdetails SET cRole=%s where cEmail=%s"
            value = (opt2,uid)
            mycursor.execute(query, value)
            mydb.commit()
            print(opt2)



    btnNext = Button(frame4, text="Next", font=('arial', 14, 'bold'),  fg='maroon', bd=12, pady=14, padx=10,
                     width=7,
                     command=lambda: company_login.companyLog()).grid(row=0, column=1)
    root.mainloop()
