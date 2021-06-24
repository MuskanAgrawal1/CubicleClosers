from tkinter import *
import company_login
import jobseeker_login
import JS_Skills
import tkinter.messagebox as MessageBox

root = Tk()
root.title("Options")
root.geometry("550x540+0+0")


frame1 = Frame(root)
frame1.grid()

frame2 = Frame(frame1, width=650, height=200, padx=65,pady=180, relief=RIDGE)
frame2.grid(row=0, column=0)


btnJobseeker = Button(frame2, text="Jobseeker", font=('arial', 14, 'bold'),bg='#872347',fg='white', bd=12, padx=75, pady=10, width=20,
                               command=lambda : jobseeker_login.jobSeekerLog()).grid(row=0, column=0)
btnCompany = Button(frame2, text="Company", font=('arial', 14, 'bold'),bg='#872347',fg='white', bd=12, padx=75, pady=10, width=20,
                               command=lambda : company_login.companyLog()).grid(row=1, column=0)

root.mainloop()