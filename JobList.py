from tkinter import *
import mysql.connector
import functools
import Company_Options
import Email1
import tkinter as tk
import tkinter.messagebox as MessageBox

mydb=mysql.connector.connect(host="localhost",user="root",password="MuskanAg1@",auth_plugin="mysql_native_password",database="muskan")
mycursor=mydb.cursor(buffered=True)

def Candidates(i,r,uid):
    def _on_mousewheel(event) :
        # print(-1*(event.delta/120))
        canvas_container.yview_scroll(int(-1 * (event.delta / 120)), "units")

    root = Tk()
    root.title("List Of Jobs:")
    root.geometry("550x540+0+0")
    root.configure(background='white')

    frame_container = Frame(root, width=550, height=1500, bg="white")

    canvas_container = Canvas(frame_container, height=1500, width=550, bg="white")
    frame2 = Frame(canvas_container, bg="white",height=3000,width=1000)
    myscrollbar = Scrollbar(frame_container, orient="vertical", command=canvas_container.yview,
                            width=5)  # will be visible if the frame2 is to to big for the canvas
    canvas_container.bind_all('<MouseWheel>', _on_mousewheel)
    canvas_container.create_window((0, 0), window=frame2, anchor='w')

    # Details = Label(root, width=76, height=50, font=("Helvetica", 12), anchor='nw')
    # Details.place(x=310, y=0)

    def func(name) :
        # Details.config(text=name[1] + "\n\n" + name[2])
        print(name)
        MsgBox = tk.messagebox.askquestion('Apply Status', 'Are you sure you want to hire this person?')
        if MsgBox == 'yes' :
            Email1.send_message(name[3])
        else :
            tk.messagebox.showinfo('Return', 'You will now return to the application screen')

    sql = "SELECT jName,jAddress,jContact,jEmail,jSkills, jExperience,jDesiredL,role from jsdetails where interest=%s and role=%s"
    val = (i, r)
    mycursor.execute(sql, val)
    mylist = mycursor.fetchall()
    print(mylist)
    if(mylist==[]):
        MsgBox1 = tk.messagebox.askquestion('Data', 'No data available. Do you want to exit?')
        if MsgBox1 == 'yes' :
            tk.messagebox.showinfo('Exiting')
        else :
            tk.messagebox.showinfo('Return', 'You will now return to the application screen')
            Company_Options.CO(uid)
    a=0
    i=180

    # (p_name,disc)
    # mylist = ['item1','item2','item3','item4','item5','item6','item7','item8','item9','item1','item2','item3','item4','item5','item6','item7','item8','item9','item1','item2','item3','item4','item5','item6','item7','item8','item9',
    #         'item1','item2','item3','item4','item5','item6','item7','item8','item9','item1','item2','item3','item4','item5','item6','item7','item8','item9','item1','item2','item3','item4','item5','item6','item7','item8','item9']
    for item in mylist :
        a=a+i
        val2 = "Name:   " + item[0] + "\n" + "Address:   " + item[1] + "\n" + "Contact:   " + item[
            2] + "\n" + "Email:   " + item[3] + "\n" + "Skills:   " + item[4] + "\n"+ "Experience:   "+item[5] + "\n" + "Desired Location:   "+item[6] + "\n" + "Role:   " + item[7] +"\n"
        button = Button(frame2, text=val2, command=functools.partial(func, item), height=8,pady=8, width=60, bd=2,
                        bg="white", fg="black", font=("Helvetica", 12), justify="left", anchor='w')
        button.place(x=0,y=a+i)
        print(item)

    frame2.update()  # update frame2 height so it's no longer 0 ( height is 0 when it has just been created )
    canvas_container.configure(yscrollcommand=myscrollbar.set,
                               scrollregion="0 0 0 %s" % frame2.winfo_height())  # the scrollregion mustbe the size of the frame inside it,
    # in this case "x=0 y=0 width=0 height=frame2height"
    # width 0 because we only scroll verticaly so don't mind about the width.

    canvas_container.pack(side=LEFT)
    myscrollbar.pack(side=RIGHT, fill=Y)

    frame_container.grid(row=0, column=0)

    root.mainloop()



