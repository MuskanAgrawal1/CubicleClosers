import smtplib
from tkinter import *


def send_message(em):
    root = Tk()
    root.geometry("550x540+0+0")
    root.title("Python Mail Send App")

    heading = Label(root,text="Send Email", bg="yellow", fg="black", font="10", width="500", height="3")

    heading.grid(row=0,column=0)

    address_field = Label(root,text="Recipient Address :",fg="dark blue")
    email_body_field = Label(root,text="Message :",fg="dark blue")

    address_field.place(x=15, y=70)
    email_body_field.place(x=15, y=140)

    address = StringVar()
    email_body = StringVar()

    address_entry = Label(root,text=em)
    email_body_entry = Text(root,height="5", width="30")

    address_entry.place(x=15, y=100)
    email_body_entry.place(x=15, y=180)


    def msg():
        address_info = "muskanagrawal7654321@gmail.com"
        email_body_info = email_body_entry.get("1.0",END)
        print(email_body_info)
        print(address_info, email_body_info)
        sender_email = "muskan000111888@gmail.com"
        sender_password = "muskan123_"
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        print("Login successful")
        server.sendmail(sender_email, address_info, email_body_info)
        print("Message sent")

    button = Button(root, text="Send Message", command=lambda:msg(), width="30", height="2", bg="grey")
    button.place(x=15, y=300)

    root.mainloop()