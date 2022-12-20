from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
from student import Student
from train import Train_Data
from attendance import Attendence
from help import Help
from face_recongnition import Face_recognition
import os

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
    root=Tk()
    obj=Face_recognition_system(root)
    root.mainloop()