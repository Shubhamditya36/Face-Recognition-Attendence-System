from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("3000x790+0+0")
        self.root.title("Face Recognition System")

        # background image
        img=Image.open(r"C:\Users\hp\Desktop\PROJECT\Face Recognition Attendence System\images\college_images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img=img.resize((1380,660),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img = Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1380,height=660)

        title_lbl = Label(bg_img,text="sc5921353@gmail.com",font=("times new roman",30,"bold"),bg="green",fg="white")
        title_lbl.place(x=430,y=150,width=500,height=45)

if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()