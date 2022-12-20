from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("3000x790+0+0")
        self.root.title("Face Recongnition System")

        title_lbl = Label(self.root,text="FACE RECOGNITION",font=("times new roman",30,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1280,height=40)

        # Top image
        img_top= Image.open(r"C:\Users\hp\Desktop\PROJECT\Face Recognition Attendence System\images\college_images\face_detector1.jpg")
        img_top = img_top.resize((500,600),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        first_lbl = Label(self.root,image=self.photoimg_top)
        first_lbl.place(x=0,y=42,width=500,height=600)

        # right image
        img_right= Image.open(r"C:\Users\hp\Desktop\PROJECT\Face Recognition Attendence System\images\college_images\img1.jpg")
        img_right = img_right.resize((950,600),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        first_lbl = Label(self.root,image=self.photoimg_right)
        first_lbl.place(x=500,y=42,width=950,height=600)

        # button
        train_btn = Button(first_lbl,cursor="hand2",command=self.face_recog,text="Face Recognition",font=("times new roman",18,"bold"),bg="green",fg="white")
        train_btn.place(x=370,y=530,width=200,height=40)

    ################# mark attendence #############
    def mark_attendence(self,i,n,r,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                date=now.strftime("%d/%m/%Y")
                attendence_time=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{attendence_time},{date},Present")

    ############### face Recognition ###############
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))  # formula

                con=pymysql.connect(host="localhost",user="root",password="",database="face recognition")
                my_cursor=con.cursor()

                my_cursor.execute("select student_id from student where student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                my_cursor.execute("select name from student where student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select roll_no from student where student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select department from student where student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                con.commit()
                con.close()

                if confidence>77:
                    cv2.putText(img, f"Student ID:{i}", (x,y-79),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                    cv2.putText(img, f"Name:{n}", (x,y-56),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img, f"Roll:{r}", (x,y-31),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img, f"Department:{d}", (x,y-8),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendence(i,n,r,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img, "Unknown Face", (x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]
            return coord   

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
            
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0) # 0 for web cam

        while(True):
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

if __name__=="__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()


