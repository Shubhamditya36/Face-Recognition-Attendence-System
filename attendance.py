from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql
import os
import csv
from tkinter import filedialog
import cv2

myData=[]
class Attendence:
    def __init__(self,root):
        self.root=root
        self.root.geometry("3000x790+0+0")
        self.root.title("Face Recognition System")

        ########### all variables ##############
        self.id_var=StringVar()
        self.roll_var=StringVar()
        self.name_var=StringVar()
        self.dep_var=StringVar()
        self.time_var=StringVar()
        self.date_var=StringVar()
        self.attendnc_var=StringVar()

        # first image
        img  = Image.open(r"C:\Users\hp\Desktop\PROJECT\Face Recognition Attendence System\images\college_images\smart-attendance.jpg")
        img = img.resize((650,120),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        first_lbl = Label(self.root,image=self.photoimg)
        first_lbl.place(x=0,y=0,width=650,height=130)

        # second image
        img1  = Image.open(r"C:\Users\hp\Desktop\PROJECT\Face Recognition Attendence System\images\college_images\AdobeStock_303989091.jpeg")
        img1 = img1.resize((700,120),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        first_lbl = Label(self.root,image=self.photoimg1)
        first_lbl.place(x=650,y=0,width=700,height=130)

        # background image
        img3=Image.open(r"C:\Users\hp\Desktop\PROJECT\Face Recognition Attendence System\images\college_images\bg.jpg")
        img3=img3.resize((1560,660),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1500,height=660)

        title_lbl = Label(bg_img,text="ATTENDANCE",font=("times new roman",30,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1280,height=40)

        main_frame=Frame(bg_img,bg="white",bd=2)
        main_frame.place(x=5,y=50,width=1260,height=460)

        # left label frame
        left_frame=LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=2,width=600,height=450)

        # Attendance ID
        sattendanceID_label=Label(left_frame,bg="white",text="AttendanceID:",font=("times new roman",12,"bold"))
        sattendanceID_label.grid(row=0,column=0,padx=10,pady=10,sticky="w")

        attendanceID_entry = ttk.Entry(left_frame,textvariable=self.id_var,width=18,font=("times new roman",13,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=10,sticky="w")

        # student name
        studentName_label=Label(left_frame,bg="white",text="Student Name:",font=("times new roman",12,"bold"))
        studentName_label.grid(row=0,column=2,padx=2,pady=10,sticky="w")

        sudentName_entry = ttk.Entry(left_frame,textvariable=self.name_var,width=17,font=("times new roman",13,"bold"))
        sudentName_entry.grid(row=0,column=3,padx=10,pady=10,sticky="w")

        # roll No
        roll_label=Label(left_frame,bg="white",text="Roll No:",font=("times new roman",12,"bold"))
        roll_label.grid(row=1,column=0,padx=10,pady=10,sticky="w")

        roll_entry = ttk.Entry(left_frame,textvariable=self.roll_var,width=18,font=("times new roman",13,"bold"))
        roll_entry.grid(row=1,column=1,padx=10,pady=10,sticky="w")

        # Department
        dep_label=Label(left_frame,bg="white",text="Department:",font=("times new roman",12,"bold"))
        dep_label.grid(row=1,column=2,padx=2,pady=10,sticky="w")

        dep_entry = ttk.Entry(left_frame,width=17,textvariable=self.dep_var,font=("times new roman",13,"bold"))
        dep_entry.grid(row=1,column=3,padx=10,pady=10,sticky="w")

        # Time
        time_label=Label(left_frame,bg="white",text="Time:",font=("times new roman",12,"bold"))
        time_label.grid(row=2,column=0,padx=10,pady=10,sticky="w")

        time_entry = ttk.Entry(left_frame,width=18,textvariable=self.time_var,font=("times new roman",13,"bold"))
        time_entry.grid(row=2,column=1,padx=10,pady=10,sticky="w")

        # Date
        dep_label=Label(left_frame,bg="white",text="Date:",font=("times new roman",12,"bold"))
        dep_label.grid(row=2,column=2,padx=10,pady=10,sticky="w")

        dep_entry = ttk.Entry(left_frame,width=17,textvariable=self.date_var,font=("times new roman",13,"bold"))
        dep_entry.grid(row=2,column=3,padx=10,pady=10,sticky="w")

        # Attendance frame
        attendance_frame=LabelFrame(left_frame,bg="white",bd=2,relief=RIDGE,text="Attendance",font=("times new roman",12,"bold"))
        attendance_frame.place(x=5,y=150,width=588,height=60)

        # Attendance
        attendance_label=Label(attendance_frame,bg="white",text="Attendance Status",font=("times new roman",12,"bold"))
        attendance_label.grid(row=0,column=0,padx=10,pady=5,sticky="w")

        attendance_combo=ttk.Combobox(attendance_frame,textvariable=self.attendnc_var,font=("times new roman",12,"bold"),width=17,state="readonly")
        attendance_combo['values']=("Status","Present","Absent")
        attendance_combo.current(0)
        attendance_combo.grid(row=0,column=1,pady=5,sticky="w")

        # buttons frame
        btn_frame = Frame(left_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=325,width=595,height=100)

        # import csv button
        import_btn = Button(btn_frame,text="Import csv",command=self.import_csv,width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        import_btn.grid(row=0,column=0)

        # Export csv button
        export_btn = Button(btn_frame,text="Export csv",command=self.exportcsv,width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        export_btn.grid(row=0,column=1)

        # Update button
        update_btn = Button(btn_frame,text="Update",width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2)

        # Reset button
        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        # right label frame
        right_frame=LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        right_frame.place(x=620,y=2,width=628,height=450)

        ############# Table Frame #############################
        table_frame=Frame(right_frame,bg="white",bd=2,relief=RIDGE)
        table_frame.place(x=2,y=5,width=620,height=350)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,columns=('id','roll','name','department','time','date','attendance'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll No.")
        self.AttendanceReportTable.heading("name",text="Student Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Attendance Time")
        self.AttendanceReportTable.heading("date",text="Attendance Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    ############ Fetch Data ###################
    def fetch_data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    # import csv
    def import_csv(self):
        global myData
        myData.clear()
        file_name=filedialog.askopenfilename(initialdir=os.getcwd(),title="open csv",filetype=(("CSV File",".csv"),("ALL File","*.*")),parent=self.root)
        with open(file_name) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                myData.append(i)
            self.fetch_data(myData)

    # export csv
    def exportcsv(self):
        try:
            if len(myData)<1:
                messagebox.showerror("Error","No Data Found To Export",parent=self.root)
                return False
            file_name=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open csv",filetype=(("CSV File",".csv"),("ALL File","*.*")),parent=self.root)
            with open(file_name,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in myData:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data is Exported to" +os.path.basename(file_name)+" Successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    ########## get cursor ############
    def get_cursor(self,event=""):
        cursor_focus=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_focus)
        data=content["values"]

        self.id_var.set(data[0])
        self.roll_var.set(data[1])
        self.name_var.set(data[2])
        self.dep_var.set(data[3])
        self.time_var.set(data[4])
        self.date_var.set(data[5])
        self.attendnc_var.set(data[6])

    def reset_data(self):
        self.id_var.set("")
        self.roll_var.set("")
        self.name_var.set("")
        self.dep_var.set("")
        self.time_var.set("")
        self.date_var.set("")
        self.attendnc_var.set("") 



if __name__=="__main__":
    root=Tk()
    obj=Attendence(root)
    root.mainloop()