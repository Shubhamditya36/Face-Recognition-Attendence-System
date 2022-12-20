from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql
import cv2

class Register:
    def __init__(self,root):
        self.root=root
        self.root.geometry("3000x790+0+0")
        self.root.title("Register New User")

        ########### all variables ###############
        self.fname_var=StringVar()
        self.lname_var=StringVar()
        self.contNo_var=StringVar()
        self.email_var=StringVar()
        self.Ques_var=StringVar()
        self.sec_ans_var=StringVar()
        self.pass_var=StringVar()
        self.confrm_pass_var=StringVar()

        # background image
        img=Image.open(r"C:\Users\hp\Desktop\PROJECT\Face Recognition Attendence System\images\college_images\hackers2.jpg")
        img=img.resize((1380,660),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img = Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1380,height=660)

        # Left image
        lftimg=Image.open(r"C:\Users\hp\Desktop\PROJECT\Face Recognition Attendence System\images\college_images\thought-good-morning-messages-LoveSove.jpg")
        lftimg=lftimg.resize((450,550),Image.ANTIALIAS)
        self.photolftimg=ImageTk.PhotoImage(lftimg)

        bg_img = Label(bg_img,image=self.photolftimg)
        bg_img.place(x=30,y=80,width=450,height=550)

        # main frame
        main_frame=Frame(self.root,bg="white")
        main_frame.place(x=480,y=80,width=700,height=550)

        # title label
        title_label=Label(main_frame,text="REGISTER HERE",font=("times new roman",12,"bold"),bg="white",fg="green")
        title_label.place(x=10,y=10,width=150,height=40)

        # First name
        first_name_level=Label(main_frame,text="First Name",font=("times new roman",14),bg="white",fg="black")
        first_name_level.place(x=15,y=92)

        first_name_entry=ttk.Entry(main_frame,textvariable=self.fname_var,font=("times new roman",13),width=34)
        first_name_entry.place(x=17,y=115)

        # Last name
        last_name_level=Label(main_frame,text="Last Name",font=("times new roman",14),bg="white",fg="black")
        last_name_level.place(x=368,y=92)

        last_name_entry=ttk.Entry(main_frame,textvariable=self.lname_var,font=("times new roman",13),width=34)
        last_name_entry.place(x=370,y=115)

        # Contact Number
        contact_no_level=Label(main_frame,text="Contact No",font=("times new roman",14),bg="white",fg="black")
        contact_no_level.place(x=15,y=170)

        contact_no_entry=ttk.Entry(main_frame,textvariable=self.contNo_var,font=("times new roman",13),width=34)
        contact_no_entry.place(x=17,y=194)

         # Email
        email_level=Label(main_frame,text="Email",font=("times new roman",14),bg="white",fg="black")
        email_level.place(x=368,y=170)

        email_name_entry=ttk.Entry(main_frame,textvariable=self.email_var,font=("times new roman",13),width=34)
        email_name_entry.place(x=370,y=194)

        # Security Question
        security_Q=Label(main_frame,text="Select security Question",font=("times new roman",14),bg="white",fg="black")
        security_Q.place(x=15,y=250)

        security_combobox =ttk.Combobox(main_frame,textvariable=self.Ques_var,font=("times new roman",14),width=32,state="readonly")
        security_combobox["values"]=("select","what is your pet Name","Your Birth Place","Your Favorite Sport")
        security_combobox.current(0)
        security_combobox.place(x=17,y=275)

         # Security Answer
        security_answerlbl=Label(main_frame,text="Security Answer",font=("times new roman",14),bg="white",fg="black")
        security_answerlbl.place(x=368,y=250)

        security_ans_entry=ttk.Entry(main_frame,textvariable=self.sec_ans_var,font=("times new roman",13),width=34)
        security_ans_entry.place(x=370,y=275)

        # Password
        contact_no_level=Label(main_frame,text="Password",font=("times new roman",14),bg="white",fg="black")
        contact_no_level.place(x=15,y=330)

        contact_no_entry=ttk.Entry(main_frame,textvariable=self.pass_var,font=("times new roman",13),width=34)
        contact_no_entry.place(x=17,y=354)

         # Confirm Password
        security_answerlbl=Label(main_frame,text="Confirm Password",font=("times new roman",14),bg="white",fg="black")
        security_answerlbl.place(x=368,y=330)

        security_ans_entry=ttk.Entry(main_frame,textvariable=self.confrm_pass_var,font=("times new roman",13),width=34)
        security_ans_entry.place(x=370,y=354)

        ############# check Button ###################
        self.check_var=IntVar()
        check_btn=Checkbutton(main_frame,variable=self.check_var,text="I agree to Terms and Conditions",font=("times new roman",12),fg="black",bg="white",onvalue=1,offvalue=0)
        check_btn.place(x=15,y=400)

        # Register Button
        reg_btn=Button(main_frame,command=self.register_data,text=("Register Now"),font=("times new roman",14),width=14,bg="blue",fg="white",activeforeground="white",activebackground="blue",borderwidth=0)
        reg_btn.place(x=15,y=450)

        # Go to login Button
        gotoLog_btn=Button(main_frame,text=("Go to Login Page"),font=("times new roman",12),width=12,bg="white",fg="black",activeforeground="black",activebackground="white",borderwidth=0)
        gotoLog_btn.place(x=15,y=485)


    ############ all functions #############
    def register_data(self):
        if self.fname_var.get()=="" or self.email_var.get()=="" or self.Ques_var.get()=="Select":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.pass_var.get()!=self.confrm_pass_var.get():
            messagebox.showerror("Error","Password and Confirm Password must be same",parent=self.root)
        elif self.check_var.get()==0:
            messagebox.showerror("Error","Please agree  to our Terms and Conditions",parent=self.root)
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="face recognition")
            my_cursor=con.cursor()
            query="select * from newregistrations where email=%s"
            value=(self.email_var.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another email",parent=self.root)
            else:
                my_cursor.execute("insert into newregistrations values(%s,%s,%s,%s,%s,%s,%s)",(self.fname_var.get(),
                                                                                                self.lname_var.get(),
                                                                                                self.contNo_var.get(),
                                                                                                self.email_var.get(),
                                                                                                self.Ques_var.get(),
                                                                                                self.sec_ans_var.get(),
                                                                                                self.pass_var.get()
                                                                                                ))

                messagebox.showinfo("Welcome","welcome to the Face Recognition System",parent=self.root)      
            con.commit()
            con.close()



if __name__=="__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()