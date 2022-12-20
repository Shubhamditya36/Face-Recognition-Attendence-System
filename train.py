from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql
import cv2
import os
import numpy as np

class Train_Data:
    def __init__(self,root):
        self.root=root
        self.root.geometry("3000x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root,text="TRAIN DATA SET",font=("times new roman",30,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1280,height=40)
        
        # Top image
        img_top= Image.open(r"C:\Users\hp\Desktop\PROJECT\Face Recognition Attendence System\images\college_images\facialrecognition.png")
        img_top = img_top.resize((1280,250),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        first_lbl = Label(self.root,image=self.photoimg_top)
        first_lbl.place(x=0,y=40,width=1280,height=250)

        # Bottom image
        img_bottom= Image.open(r"C:\Users\hp\Desktop\PROJECT\Face Recognition Attendence System\images\college_images\photos.jpg")
        img_bottom = img_bottom.resize((1280,320),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        first_lbl = Label(self.root,image=self.photoimg_bottom)
        first_lbl.place(x=0,y=330,width=1280,height=320)


        # train data button
        train_btn = Button(self.root,cursor="hand2",command=self.train_classifier,text="TRAIN DATA",font=("times new roman",20,"bold"),bg="green",fg="white")
        train_btn.place(x=0,y=290,width=1280,height=40)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # gray scale conversion
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        ############ Train the classifier and save #################
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training data set completed")




if __name__=="__main__":
    root=Tk()
    obj=Train_Data(root)
    root.mainloop()
