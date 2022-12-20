from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from student import Student
from train import Train_Data
from attendance import Attendence
from help import Help
import tkinter
from face_recongnition import Face_recognition
import os
import pymysql
import cv2


def main():
    win=Tk()
    app=Login(win)
    win.mainloop()

class Login:
    def __init__(self,root):
        self.root=root
        self.root.geometry("3000x790+0+0")
        self.root.title("Login Window")

         # background image
        img=Image.open(r"C:\Users\hp\Desktop\PROJECT\Face Recognition Attendence System\images\college_images\password.jpg")
        img=img.resize((1380,660),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img = Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1380,height=660)

        ############# Login Frame ###############
        login_frame = Frame(bg_img,bg="black")
        login_frame.place(x=430,y=100,width=400,height=500)

        UserImg=Image.open(r"C:\Users\hp\Desktop\PROJECT\Face Recognition Attendence System\images\college_images\LoginIconAppl.png")
        UserImg=UserImg.resize((80,80),Image.ANTIALIAS)
        self.photoUserImg=ImageTk.PhotoImage(UserImg)

        user_img = Label(login_frame,image=self.photoUserImg,bg="black",borderwidth=0)
        user_img.grid(row=0,column=0,padx=145,pady=10)

        title_label = Label(login_frame,text="Get Started",font=("times new roman",18,"bold"),bg="black",fg="white")
        title_label.grid(row=1,column=0,padx=145,pady=10)

        # uder ID
        user_id_label=Label(login_frame,text="User ID",font=("times new roman",12),bg="black",fg="white")
        user_id_label.grid(row=2,column=0,padx=70,pady=10,sticky="w")

        self.user_id_entry=ttk.Entry(login_frame,font=("times new roman",12),width=38)
        self.user_id_entry.place(x=45,y=190)

        # Password
        password_label=Label(login_frame,text="Password",font=("times new roman",12),bg="black",fg="white")
        password_label.grid(row=3,column=0,padx=70,pady=25,sticky="w")

        self.password_id_entry=ttk.Entry(login_frame,show="*",font=("times new roman",12),width=38)
        self.password_id_entry.place(x=45,y=250)


        ############### icon images ######################
        IconImg1=Image.open(r"C:\Users\hp\Desktop\PROJECT\Face Recognition Attendence System\images\college_images\LoginIconAppl.png")
        IconImg1=IconImg1.resize((25,25),Image.ANTIALIAS)
        self.photoIconImg1=ImageTk.PhotoImage(IconImg1)

        self.user_img = Label(login_frame,image=self.photoIconImg1,bg="black",borderwidth=0)
        self.user_img.place(x=45,y=160,width=25,height=25)

        IconImg2=Image.open(r"C:\Users\hp\Desktop\PROJECT\Face Recognition Attendence System\images\college_images\lock-512.png")
        IconImg2=IconImg2.resize((25,25),Image.ANTIALIAS)
        self.photoIconImg2=ImageTk.PhotoImage(IconImg2)

        self.user_img = Label(login_frame,image=self.photoIconImg2,bg="black",borderwidth=0)
        self.user_img.place(x=45,y=222,width=25,height=25)

        # Login Button
        login_btn = Button(login_frame,text="Login",command=self.login,font=("times new roman",13,"bold"),borderwidth=0,bg="green",fg="white",activeforeground="white",activebackground="green")
        login_btn.place(x=45,y=300,width=100,height=40)

        # Register New User Button
        register_btn = Button(login_frame,command=self.register_win,text="New User Register",font=("times new roman",11),borderwidth=0,bg="black",fg="white",activeforeground="white",activebackground="black")
        register_btn.place(x=46,y=390,width=120,height=25)

        # Forgot Password Button
        forgot_pass_btn = Button(login_frame,command=self.forgot_pssWin,text="Forgot Password",font=("times new roman",11),borderwidth=0,bg="black",fg="white",activeforeground="white",activebackground="black")
        forgot_pass_btn.place(x=38,y=420,width=120,height=25)
    
    def register_win(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    
    def login(self):
        if self.user_id_entry.get()=="" or self.password_id_entry.get()=="":
            messagebox.showerror("Error","user ID and Password is needed to login")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="face recognition")
            my_cursor=con.cursor()
            my_cursor.execute("select * from newregistrations where email=%s and password=%s",(self.user_id_entry.get(),self.password_id_entry.get()))

            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid User ID and Password",parent=self.root)
            else:
                open_main=messagebox.askyesno("YesNo","Access only Admin")
                if open_main==True:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_recognition_system(self.new_window)
                else:
                    return
            con.commit()
            con.close()
#################################### reset password #######################################
    def reset_pass(self):
        if self.security_combobox.get()=="select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.security_ans_entry.get()=="":
            messagebox.showerror("Error","Please enter the answer of security question",parent=self.root2)
        elif self.new_passentry.get()=="":
            messagebox.showerror("Error","Please enter the New Password",parent=self.root2)
        elif self.new_passentry.get()!=self.confirmnew_passentry.get():
            messagebox.showerror("Error","New Password and Confirm New Password must match",parent=self.root2)
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="face recognition")
            my_cursor=con.cursor()
            query="select * from newregistrations where email=%s and securityques=%s and securityans=%s"
            value=(self.user_id_entry.get(),self.security_combobox.get(),self.security_ans_entry.get())
            my_cursor.execute(query,value)

            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the correct answer",parent=self.root2)
            else:
                query="update newregistrations set password=%s where email=%s"
                value=(self.new_passentry.get(),self.user_id_entry.get())
                my_cursor.execute(query,value)

                con.commit()
                con.close()
                messagebox.showinfo("Success","Your password has been reset succesfully,Please login using New Password",parent=self.root2)
                self.root2.destroy()

################################ forgot password window ########################################
    def forgot_pssWin(self):
        if self.user_id_entry.get()=="":
            messagebox.showerror("Error","Please enter User Id to reset password")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="face recognition")
            my_cursor=con.cursor()
            query="select * from newregistrations where email=%s"
            value=(self.user_id_entry.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Please enter valid User ID")
            else:
                con.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+480+170")          
                

                l=Label(self.root2,text="Forgot Password",font=("times new roman",14,"bold"),bg="white",fg="red")
                l.place(x=0,y=10,relwidth=1)

                # Security Question for forgot password window
                security_Q=Label(self.root2,text="Select security Question",font=("times new roman",14),fg="black")
                security_Q.place(x=15,y=70)

                self.security_combobox =ttk.Combobox(self.root2,font=("times new roman",14),width=32,state="readonly")
                self.security_combobox["values"]=("select","what is your pet Name","Your Birth Place","Your Favorite Sport")
                self.security_combobox.current(0)
                self.security_combobox.place(x=17,y=99)

                # security answer for forgot password window
                security_answerlbl=Label(self.root2,text="Security Answer",font=("times new roman",14),fg="black")
                security_answerlbl.place(x=17,y=145)

                self.security_ans_entry=ttk.Entry(self.root2,font=("times new roman",13),width=34)
                self.security_ans_entry.place(x=17,y=175)

                # New Password
                new_passlbl=Label(self.root2,text="New Password",font=("times new roman",14),fg="black")
                new_passlbl.place(x=17,y=210)

                self.new_passentry=ttk.Entry(self.root2,show="*",font=("times new roman",13),width=34)
                self.new_passentry.place(x=17,y=239)

                # Confirm New Password
                new_passlbl=Label(self.root2,text="Confirm New Password",font=("times new roman",14),fg="black")
                new_passlbl.place(x=17,y=280)

                self.confirmnew_passentry=ttk.Entry(self.root2,show="*",font=("times new roman",13),width=34)
                self.confirmnew_passentry.place(x=17,y=310)

                # Reset Password Button
                reset_pass_btn=Button(self.root2,command=self.reset_pass,text="Reset Password",font=("times new roman",14),width=14,bg="green",fg="white",activeforeground="white",activebackground="green",borderwidth=0)
                reset_pass_btn.place(x=90,y=360) 






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
        pass_lbl=Label(main_frame,text="Password",font=("times new roman",14),bg="white",fg="black")
        pass_lbl.place(x=15,y=330)

        pass_entry=ttk.Entry(main_frame,textvariable=self.pass_var,show="*",font=("times new roman",13),width=34)
        pass_entry.place(x=17,y=354)

         # Confirm Password
        confirm_passlbl=Label(main_frame,text="Confirm Password",font=("times new roman",14),bg="white",fg="black")
        confirm_passlbl.place(x=368,y=330)

        confirm_passentry=ttk.Entry(main_frame,textvariable=self.confrm_pass_var,show="*",font=("times new roman",13),width=34)
        confirm_passentry.place(x=370,y=354)

        ############# check Button ###################
        self.check_var=IntVar()
        check_btn=Checkbutton(main_frame,variable=self.check_var,text="I agree to Terms and Conditions",font=("times new roman",12),fg="black",bg="white",onvalue=1,offvalue=0)
        check_btn.place(x=15,y=400)

        # Register Button
        reg_btn=Button(main_frame,command=self.register_data,text=("Register Now"),font=("times new roman",14),width=14,bg="blue",fg="white",activeforeground="white",activebackground="blue",borderwidth=0)
        reg_btn.place(x=15,y=450)

        # Go to login Button
        gotoLog_btn=Button(main_frame,command=self.goto_log,text=("Go to Login Page"),font=("times new roman",12),width=12,bg="white",fg="black",activeforeground="black",activebackground="white",borderwidth=0)
        gotoLog_btn.place(x=15,y=485)


    ############ all functions #############

    def goto_log(self):
        self.root.destroy()


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



class Face_recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("3000x790+0+0")
        self.root.title("Face Recognition System")
        # first image
        img  = Image.open(r"C:\Users\hp\Desktop\PROJECT\Face Recognition Attendence System\images\college_images\img1.jpg")
        img = img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        first_lbl = Label(self.root,image=self.photoimg)
        first_lbl.place(x=0,y=0,width=500,height=130)

        # second image
        img1  = Image.open(r"C:\Users\hp\Desktop\PROJECT\Face Recognition Attendence System\images\college_images\facialrecognition.png")
        img1 = img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        first_lbl = Label(self.root,image=self.photoimg1)
        first_lbl.place(x=500,y=0,width=500,height=130)


        # third image
        img2  = Image.open(r"C:\Users\hp\Desktop\PROJECT\Face Recognition Attendence System\images\college_images\images.jpg")
        img2 = img2.resize((450,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        first_lbl = Label(self.root,image=self.photoimg2)
        first_lbl.place(x=1000,y=0,width=400,height=130)

        # background image
        img3=Image.open(r"C:\Users\hp\Desktop\PROJECT\Face Recognition Attendence System\images\college_images\bg.jpg")
        img3=img3.resize((1560,660),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1500,height=660)

        title_lbl = Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1280,height=40)

        # student button
        img4=Image.open(r"C:\Users\hp\Desktop\PROJECT\Face Recognition Attendence System\images\college_images\gettyimages-1022573162.jpg")
        img4=img4.resize((190,190),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=130,y=100,width=188,height=120)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=130,y=200,width=190,height=40)

        # Detect Face button
        img5=Image.open(r"C:\Users\hp\Desktop\PROJECT\Face Recognition Attendence System\images\college_images\face_detector1.jpg")
        img5=img5.resize((190,190),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(bg_img,image=self.photoimg5,command=self.face_recognition,cursor="hand2")
        b1.place(x=400,y=100,width=188,height=120)

        b1_1=Button(bg_img,text="Face Detector",command=self.face_recognition,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=200,width=190,height=40)

        # Attendence Face button
        img6=Image.open(r"C:\Users\hp\Desktop\PROJECT\Face Recognition Attendence System\images\college_images\report.jpg")
        img6=img6.resize((190,190),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b1=Button(bg_img,image=self.photoimg6,command=self.attendance,cursor="hand2")
        b1.place(x=670,y=100,width=188,height=120)

        b1_1=Button(bg_img,text="Attendence",command=self.attendance,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=670,y=200,width=190,height=40)

        # Train Data button
        img7=Image.open(r"C:\Users\hp\Desktop\PROJECT\Face Recognition Attendence System\images\college_images\Train.jpg")
        img7=img7.resize((190,190),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        b1=Button(bg_img,image=self.photoimg7,command=self.train_data,cursor="hand2")
        b1.place(x=950,y=100,width=188,height=120)

        b1_1=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=950,y=200,width=190,height=40)

        # photos button
        img8=Image.open(r"C:\Users\hp\Desktop\PROJECT\Face Recognition Attendence System\images\college_images\photos.jpg")
        img8=img8.resize((190,190),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        b1=Button(bg_img,command=self.open_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=200,y=300,width=188,height=120)

        b1_1=Button(bg_img,command=self.open_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=400,width=190,height=40)

        # Help Desk button
        img9=Image.open(r"C:\Users\hp\Desktop\PROJECT\Face Recognition Attendence System\images\college_images\help.jpg")
        img9=img9.resize((190,190),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        b1=Button(bg_img,image=self.photoimg9,command=self.help_desk,cursor="hand2")
        b1.place(x=530,y=300,width=188,height=120)

        b1_1=Button(bg_img,text="Help Desk",command=self.help_desk,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=530,y=400,width=190,height=40)

        # Exit button
        img10=Image.open(r"C:\Users\hp\Desktop\PROJECT\Face Recognition Attendence System\images\college_images\exit.jpg")
        img10=img10.resize((190,190),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        b1=Button(bg_img,image=self.photoimg10,command=self.exit_win,cursor="hand2")
        b1.place(x=880,y=300,width=188,height=120)

        b1_1=Button(bg_img,text="Exit",command=self.exit_win,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=880,y=400,width=190,height=40)

    def open_img(self):
        os.startfile("data")

    def exit_win(self):
        iExit=tkinter.messagebox.askyesno("Exit Window","Are you sure you want to exit",parent=self.root)
        if iExit==True:
            self.root.destroy()
        else:
            return

    ####################### Fucntion Buttons ##########################
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train_Data(self.new_window)

    def face_recognition(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)
    
    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendence(self.new_window)

    def help_desk(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

    



if __name__=="__main__":
    main()