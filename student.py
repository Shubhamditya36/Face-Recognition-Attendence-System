from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("3000x790+0+0")
        self.root.title("Face Recognition System")

        ############### All variablese ##############
        self.dep_var=StringVar()
        self.course_var=StringVar()
        self.year_var=StringVar()
        self.sem_var=StringVar()
        self.stud_id_var=StringVar()
        self.name_var=StringVar()
        self.div_var=StringVar()
        self.roll_var=StringVar()
        self.gender_var=StringVar()
        self.dob_var=StringVar()
        self.email_var=StringVar()
        self.phone_var=StringVar()

        # first image
        img  = Image.open(r"C:\Users\hp\Desktop\PROJECT\Face Recognition Attendence System\images\college_images\face-recognition.png")
        img = img.resize((500,120),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        first_lbl = Label(self.root,image=self.photoimg)
        first_lbl.place(x=0,y=0,width=500,height=130)

        # second image
        img1  = Image.open(r"C:\Users\hp\Desktop\PROJECT\Face Recognition Attendence System\images\college_images\smart-attendance.jpg")
        img1 = img1.resize((500,120),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        first_lbl = Label(self.root,image=self.photoimg1)
        first_lbl.place(x=500,y=0,width=500,height=130)


        # third image
        img2  = Image.open(r"C:\Users\hp\Desktop\PROJECT\Face Recognition Attendence System\images\college_images\iStock-182059956_18390_t12.jpg")
        img2 = img2.resize((450,120),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        first_lbl = Label(self.root,image=self.photoimg2)
        first_lbl.place(x=1000,y=0,width=400,height=130)

        # background image
        img3=Image.open(r"C:\Users\hp\Desktop\PROJECT\Face Recognition Attendence System\images\college_images\bg.jpg")
        img3=img3.resize((1560,660),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1500,height=660)

        title_lbl = Label(bg_img,text="STUDENT DETAILS",font=("times new roman",30,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1280,height=40)

        main_frame=Frame(bg_img,bg="white",bd=2)
        main_frame.place(x=5,y=50,width=1260,height=460)

        # left label frame
        left_frame=LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=2,width=600,height=450)

        # current course frame
        course_frame=LabelFrame(left_frame,bg="white",bd=2,relief=RIDGE,text="Currrent course information",font=("times new roman",12,"bold"))
        course_frame.place(x=5,y=5,width=588,height=120)

        # Department
        dep_label = Label(course_frame,bg="white",text="Department",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=10,sticky="w")

        dep_combo=ttk.Combobox(course_frame,textvariable=self.dep_var,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo['values']=("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky="w")

        # Course

        course_label = Label(course_frame,bg="white",text="Course",font=("times new roman",12,"bold"))
        course_label.grid(row=0,column=2,padx=15,sticky="w")

        course_combo=ttk.Combobox(course_frame,textvariable=self.course_var,font=("times new roman",12,"bold"),width=17,state="readonly")
        course_combo['values']=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=1,pady=10,sticky="w")

        # year
        year_label = Label(course_frame,bg="white",text="Year",font=("times new roman",12,"bold"))
        year_label.grid(row=1,column=0,padx=15,sticky="w")

        year_combo=ttk.Combobox(course_frame,textvariable=self.year_var,font=("times new roman",12,"bold"),width=17,state="readonly")
        year_combo['values']=("Select year","1","2","3","4")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=1,pady=10,sticky="w")

        # Semester
        sem_label=Label(course_frame,bg="white",text="Semester",font=("times new roman",12,"bold"))
        sem_label.grid(row=1,column=2,padx=10)

        sem_combo=ttk.Combobox(course_frame,textvariable=self.sem_var,font=("times new roman",12,"bold"),width=17,state="readonly")
        sem_combo['values']=("Select Semester","1","2","3","4","5","6","7","8")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=1,pady=10,sticky="w")

        # class student info frame
        class_student_frame=LabelFrame(left_frame,bg="white",bd=2,relief=RIDGE,text="Class Student information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=130,width=588,height=290)

        # Student ID
        studentID_label=Label(class_student_frame,bg="white",text="StudentID:",font=("times new roman",12,"bold"))
        studentID_label.grid(row=0,column=0,padx=10,sticky="w")

        sudentID_entry = ttk.Entry(class_student_frame,textvariable=self.stud_id_var,width=15,font=("times new roman",13,"bold"))
        sudentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky="w")

        # student name
        studentName_label=Label(class_student_frame,bg="white",text="Student Name:",font=("times new roman",12,"bold"))
        studentName_label.grid(row=0,column=2,padx=2,sticky="w")

        sudentName_entry = ttk.Entry(class_student_frame,textvariable=self.name_var,width=18,font=("times new roman",13,"bold"))
        sudentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky="w")

        # class division
        class_div_label=Label(class_student_frame,bg="white",text="Class Division:",font=("times new roman",12,"bold"))
        class_div_label.grid(row=1,column=0,padx=10,sticky="w")

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.div_var,font=("times new roman",12,"bold"),width=15,state="readonly")
        div_combo['values']=("Select Division","A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky="w")

        # roll No
        roll_label=Label(class_student_frame,bg="white",text="Roll No:",font=("times new roman",12,"bold"))
        roll_label.grid(row=1,column=2,padx=2,sticky="w")

        roll_entry = ttk.Entry(class_student_frame,textvariable=self.roll_var,width=18,font=("times new roman",13,"bold"))
        roll_entry.grid(row=1,column=3,padx=10,pady=5,sticky="w")

        # gender
        gender_label=Label(class_student_frame,bg="white",text="Gender:",font=("times new roman",12,"bold"))
        gender_label.grid(row=2,column=0,padx=10,sticky="w")

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.gender_var,font=("times new roman",12,"bold"),width=15,state="readonly")
        gender_combo['values']=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky="w")

        # D.O.B
        sdob_label=Label(class_student_frame,bg="white",text="D.O.B:",font=("times new roman",12,"bold"))
        sdob_label.grid(row=2,column=2,padx=2,sticky="w")

        dob_entry = ttk.Entry(class_student_frame,textvariable=self.dob_var,width=18,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky="w")

        # email
        email_label=Label(class_student_frame,bg="white",text="Email:",font=("times new roman",12,"bold"))
        email_label.grid(row=3,column=0,padx=10,sticky="w")

        email_entry = ttk.Entry(class_student_frame,textvariable=self.email_var,width=15,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky="w")

        # phone number
        ph_no_label=Label(class_student_frame,bg="white",text="Phone:",font=("times new roman",12,"bold"))
        ph_no_label.grid(row=3,column=2,padx=2,sticky="w")

        ph_no_entry = ttk.Entry(class_student_frame,textvariable=self.phone_var,width=18,font=("times new roman",13,"bold"))
        ph_no_entry.grid(row=3,column=3,padx=10,pady=5,sticky="w")

        # radio buttons
        self.radio_var1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.radio_var1,text="Take photo sample",value="Yes")
        radiobtn1.grid(row=4,column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.radio_var1,text="No photo sample",value="No")
        radiobtn2.grid(row=4,column=1)

        # buttons frame
        btn_frame = Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=160,width=585,height=40)

        # save button
        save_btn = Button(btn_frame,text="Save",command=self.add_data,width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        # update button
        update_btn = Button(btn_frame,text="Update",command=self.update_data,width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        # delete button
        del_btn = Button(btn_frame,text="Delete",command=self.delete_data,width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        del_btn.grid(row=0,column=2)

        # Reset button
        reset_btn = Button(btn_frame,text="Reset",command=self.reset,width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1 = Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame1.place(x=0,y=200,width=585,height=90)

        # take photo sample button
        take_photo_btn = Button(btn_frame1,text="Take photo sample",command=self.generate_dataset,width=29,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=1,column=0)

        # update photo button
        update_photo_btn = Button(btn_frame1,text="Update photo sample",width=29,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=1,column=1)

        # right label frame
        right_frame=LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=620,y=2,width=628,height=450)

        ########### search System ######################

        search_frame=LabelFrame(right_frame,bg="white",bd=2,relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=5,width=620,height=60)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,sticky="w")

        search_combo = ttk.Combobox(search_frame,width=15,font=("times new roman",12,"bold"),state="readonly")
        search_combo['values']=("Select","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky="w")

        search_entry = ttk.Entry(search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky="w")

        search_btn = Button(search_frame,text="Search",width=13,font=("times new roman",9,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=2)

        ahowAll_btn = Button(search_frame,text="Show All",width=13,font=("times new roman",9,"bold"),bg="blue",fg="white")
        ahowAll_btn.grid(row=0,column=4,padx=2)

        ############# Table Frame #############################
        table_frame=Frame(right_frame,bg="white",bd=2,relief=RIDGE)
        table_frame.place(x=5,y=70,width=620,height=350)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.Student_table = ttk.Treeview(table_frame,columns=('dep','course','year','sem','id','name','div','roll','gender','dob','email','phone','photo'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("dep",text="Department")
        self.Student_table.heading("course",text="Course")
        self.Student_table.heading("year",text="Year")
        self.Student_table.heading("sem",text="Semester")
        self.Student_table.heading("id",text="StudentID")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("div",text="Division")
        self.Student_table.heading("roll",text="Roll No")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("dob",text="D.O.B")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("phone",text="Phone")
        self.Student_table.heading("photo",text="Photo")
        self.Student_table["show"]="headings"

        self.Student_table.column("dep",width=100)
        self.Student_table.column("course",width=100)
        self.Student_table.column("year",width=100)
        self.Student_table.column("sem",width=100)
        self.Student_table.column("id",width=100)
        self.Student_table.column("name",width=100)
        self.Student_table.column("div",width=100)
        self.Student_table.column("roll",width=100)
        self.Student_table.column("gender",width=100)
        self.Student_table.column("dob",width=100)
        self.Student_table.column("email",width=100)
        self.Student_table.column("phone",width=100)
        self.Student_table.column("photo",width=100)
        
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    
    ################ Function Declaration #################
    def add_data(self):
        if(self.dep_var.get()=="Select Department" or self.name_var.get()=="" or self.stud_id_var.get()==""):
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=pymysql.connect(host="localhost",user="root",password="",database="face recognition")
                my_cursor=conn.cursor()
                val=(self.dep_var.get(),self.course_var.get(),self.year_var.get(),self.sem_var.get(),self.stud_id_var.get(),self.name_var.get(),self.div_var.get(),self.roll_var.get(),self.gender_var.get(),self.dob_var.get(),self.email_var.get(),self.phone_var.get(),self.radio_var1.get())
                query='insert into student(department,course,year,semester,student_id,name,division,roll_no,gender,dob,email,phone,photo) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

                my_cursor.execute(query,val)
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added succesfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    ########### fetch Data ############
    def fetch_data(self):
        conn=pymysql.connect(host="localhost",user="root",password="",database="face recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for i in data:
                self.Student_table.insert("",END,values=i)
        conn.commit()
        conn.close()
    ########### Get Cursor ##############
    def get_cursor(self,event=""):
        cursor_focus=self.Student_table.focus()
        content=self.Student_table.item(cursor_focus)
        data=content["values"]
        
        self.dep_var.set(data[0])
        self.course_var.set(data[1])
        self.year_var.set(data[2])
        self.sem_var.set(data[3])
        self.stud_id_var.set(data[4])
        self.name_var.set(data[5])
        self.div_var.set(data[6])
        self.roll_var.set(data[7])
        self.gender_var.set(data[8])
        self.dob_var.set(data[9])
        self.email_var.set(data[10])
        self.phone_var.set(data[11])
        self.radio_var1.set(data[12])

    # update data
    def update_data(self):
        if(self.dep_var.get()=="Select Department" or self.name_var.get()=="" or self.stud_id_var.get()==""):
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update this record",parent=self.root)
                print(update)
                if update==True:
                    conn=pymysql.connect(host="localhost",user="root",password="",database="face recognition")
                    my_cursor=conn.cursor()
                    
                    
                    my_cursor.execute("UPDATE student SET department=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,roll_no=%s,gender=%s,dob=%s,email=%s,phone=%s,photo=%s where student_id=%s",(self.dep_var.get(),
                                                                                                                                                                                                    self.course_var.get(),  
                                                                                                                                                                                                    self.year_var.get(),
                                                                                                                                                                                                    self.sem_var.get(),
                                                                                                                                                                                                    self.name_var.get(),
                                                                                                                                                                                                    self.div_var.get(),
                                                                                                                                                                                                    self.roll_var.get(),
                                                                                                                                                                                                    self.gender_var.get(),
                                                                                                                                                                                                    self.dob_var.get(),
                                                                                                                                                                                                    self.email_var.get(),
                                                                                                                                                                                                    self.phone_var.get(),
                                                                                                                                                                                                    self.radio_var1.get(),
                                                                                                                                                                                                    self.stud_id_var.get()
                                                                                                                                                                                                    ))
                else:
                    if update==False:
                        return
                messagebox.showinfo("Success","Record has been updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    # delete data
    def delete_data(self):
        if self.stud_id_var.get()=="":
            messagebox.showerror("Error","Student ID must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete the record",parent=self.root)
                if delete>0:
                    conn=pymysql.connect(host="localhost",user="root",password="",database="face recognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.stud_id_var.get())
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","record has been deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    

    # reset data
    def reset(self):
        self.dep_var.set("Select Department")
        self.course_var.set("Select Course")
        self.year_var.set("Select Year")
        self.sem_var.set("Select Semester")
        self.stud_id_var.set("")
        self.name_var.set("")
        self.div_var.set("Select Division")
        self.roll_var.set("")
        self.gender_var.set("Male")
        self.dob_var.set("")
        self.email_var.set("")
        self.phone_var.set("")
        self.radio_var1.set("")
    
    ################### Generate data set and Take photo sample #################
    def generate_dataset(self):
        if(self.dep_var.get()=="Select Department" or self.name_var.get()=="" or self.stud_id_var.get()==""):
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=pymysql.connect(host="localhost",user="root",password="",database="face recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                print(id)
                conn=pymysql.connect(host="localhost",user="root",password="",database="face recognition")
                my_cursor=conn.cursor()
                    
                    
                my_cursor.execute("UPDATE student SET department=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,roll_no=%s,gender=%s,dob=%s,email=%s,phone=%s,photo=%s where student_id=%s",(self.dep_var.get(),
                                                                                                                                                                                                    self.course_var.get(),  
                                                                                                                                                                                                    self.year_var.get(),
                                                                                                                                                                                                    self.sem_var.get(),
                                                                                                                                                                                                    self.name_var.get(),
                                                                                                                                                                                                    self.div_var.get(),
                                                                                                                                                                                                    self.roll_var.get(),
                                                                                                                                                                                                    self.gender_var.get(),
                                                                                                                                                                                                    self.dob_var.get(),
                                                                                                                                                                                                    self.email_var.get(),
                                                                                                                                                                                                    self.phone_var.get(),
                                                                                                                                                                                                    self.radio_var1.get(),
                                                                                                                                                                                                    self.stud_id_var.get()==id+1
                                                                                                                                                                                                ))

                
                
                conn.commit()
                self.fetch_data()
                self.reset()
                conn.close()

                ############## Load pre defined data on face frontals from opencv ############
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


                def face_cropped(img):
                    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum Neighbour=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                
                cap=cv2.VideoCapture(0)   # for webcam we give 0
                img_id=0
                while(True):
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face, str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed succesfully!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()