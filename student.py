from tkinter import*        #import tkinter
from tkinter import ttk     #ttk is module used to style tkinter widgets
from PIL import Image,ImageTk      #PILLOW LIBRARY which helps in image processing (editing,cropping image)
from PIL import*
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):    #calling constructor #root is root window
        self.root=root
        self.root.geometry("1530x790+0+0")    #setting window width and height where 0,0 symbolize x,y axis
        self.root.title("Facial recognition Attendence Management System")     #setting the title


        #*************************************************************************************************
        self.var_dep=StringVar()
        self.var_sem=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_class=StringVar()
        self.var_section=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
       
  


        img=Image.open(r"C:\Users\91900\Desktop\face_recognition_system\college_images\header.png")   #diplay image
        img=img.resize((1530,85),Image.Resampling.LANCZOS)    #we resized width and height of image to 500 and 130, ANTIALIAS ued to return resized images
        self.photoimg=ImageTk.PhotoImage(img)          #img stored in a variable self.photoimg     #create an object of tkinter ImageTk
        f_lbl=Label(self.root,image=self.photoimg)      #we set image on window using label
        f_lbl.place(x=0,y=0,width=1530,height=85)


        #bg image
        bg=Image.open(r"C:\Users\91900\Desktop\face_recognition_system\college_images\sbg.jpeg")
        bg=bg.resize((1530,750),Image.Resampling.LANCZOS)    #we resized width and height of image to 500 and 130, ANTIALIAS ued to return resized images
        self.photoimg2=ImageTk.PhotoImage(bg)          #img stored in a variable self.photoimg     #create an object of tkinter ImageTk
        bglbl=Label(self.root,image=self.photoimg2)      #we set image on window using label
        bglbl.place(x=0,y=85,width=1530,height=750)

        #title
        title=Label(f_lbl,text="Student Data Management",font=("Comic Sans MS",22),bg="white",fg="black")
        title.place(x=0,y=0,width=1530,height=55)


        #logo image
        logo=Image.open(r"C:\Users\91900\Desktop\face_recognition_system\college_images\logo.png")
        logo=logo.resize((80,80),Image.Resampling.LANCZOS)    #we resized width and height of image to 500 and 130, ANTIALIAS ued to return resized images
        self.photoim=ImageTk.PhotoImage(logo)          #img stored in a variable self.photoimg     #create an object of tkinter ImageTk
        lg=Label(self.root,image=self.photoim)      #we set image on window using label
        lg.place(x=15,y=16,width=60,height=60)

        
        #user image
        user=Image.open(r"C:\Users\91900\Desktop\face_recognition_system\college_images\user.png")
        user=user.resize((55,55),Image.Resampling.LANCZOS)    #we resized width and height of image to 500 and 130, ANTIALIAS ued to return resized images
        self.photoimg9=ImageTk.PhotoImage(user)          #img stored in a variable self.photoimg     #create an object of tkinter ImageTk
        ul=Label(self.root,image=self.photoimg9)      #we set image on window using label
        ul.place(x=1400,y=16,width=55,height=55)


         #logout image
        exit=Image.open(r"C:\Users\91900\Desktop\face_recognition_system\college_images\logout.png")
        exit=exit.resize((55,55),Image.Resampling.LANCZOS)    #we resized width and height of image to 500 and 130, ANTIALIAS ued to return resized images
        self.photoimg10=ImageTk.PhotoImage(exit)          #img stored in a variable self.photoimg     #create an object of tkinter ImageTk
        logout=Label(self.root,image=self.photoimg10)      #we set image on window using label
        logout.place(x=1460,y=16,width=55,height=55)

        main_frame=Frame(bglbl,bd=2) #creating a frame
        main_frame.place(x=35,y=18,width=1455,height=610)


       #left top labelframe
        lf_l=Label(bglbl,bd=1,relief=RIDGE,font=("times new roman",20),bg="white",fg="black")
        lf_l.place(x=45,y=28,width=710,height=120)


        #department label
        depart_label=Label(lf_l,text=" Department ",font=("times new roman",17),bg="white",fg="black")    #create label 
        depart_label.grid(row=0,column=0,padx=2,pady=10,sticky=W)                                         #padx,pady is used to set the padding in the combobox
                                                                                                          #sticky is used to hightlight selected option in combobox


        #department
        dep_combo=ttk.Combobox(lf_l,font=("times new roman",15),textvariable=self.var_dep,width=19,state="read only")                             #to make combobox
        dep_combo["values"]=("MCA","Computer Science","ECE","IT","Civil","Mechanical","Mtech")   #pass value to combobox in tuple
        dep_combo.current(0)                                                                            #default value is select department
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)                                     #to make sure the combobox is in front of label
                                                                                                   #sticky highlight the selected combobox option
        #semester label
        sem_label=Label(lf_l,text=" Semester ",font=("times new roman",17),bg="white",fg="black")
        sem_label.grid(row=0,column=2,padx=2,pady=10,sticky=W)


        #semester
        dep_combo1=ttk.Combobox(lf_l,font=("times new roman",15),textvariable=self.var_sem,width=19,state="read only")                             #to make combobox
        dep_combo1["values"]=("Semester1","Semester2","Semester3","Semester4","Semester5","Semester6")   #pass value to combobox in tuple
        dep_combo1.current(0)                                                                            #default value is select department
        dep_combo1.grid(row=0,column=3,padx=2,pady=10,sticky=W)                                     #to make sure the combobox is in front of label
                                                                                                   #sticky highlight the selected combobox option

        #Courses label
        sem_label2=Label(lf_l,text=" Courses ",font=("times new roman",17),bg="white",fg="black")
        sem_label2.grid(row=1,column=0,padx=2,pady=10,sticky=W)


        #Courses
        dep_combo2=ttk.Combobox(lf_l,font=("times new roman",15),textvariable=self.var_course,width=19,state="read only")                             #to make combobox
        dep_combo2["values"]=("C Programming","Environmental Studies","Chemistry","Physics","Kannada","Legislator")   #pass value to combobox in tuple
        dep_combo2.current(0)                                                                            #default value is select department
        dep_combo2.grid(row=1,column=1,padx=2,pady=10,sticky=W)     
        
        #year
        sem_label3=Label(lf_l,text=" Year ",font=("times new roman",17),bg="white",fg="black")
        sem_label3.grid(row=1,column=2,padx=2,pady=10,sticky=W)


        #year 
        dep_combo3=ttk.Combobox(lf_l,font=("times new roman",15),textvariable=self.var_year,width=19,state="read only")                             #to make combobox
        dep_combo3["values"]=("2018-2019","2019-2020","2020-2021","2021-2022","2022-2023")   #pass value to combobox in tuple
        dep_combo3.current(0)                                                                            #default value is select department
        dep_combo3.grid(row=1,column=3,padx=2,pady=10,sticky=W)                                     #to make sure the combobox is in front of label
                                                                                                   #sticky highlight the selected combobox option
        #right labelframe
        lf_r=Label(bglbl,bd=1,relief=RIDGE,font=("times new roman",30),bg="white",fg="black")
        lf_r.place(x=770,y=28,width=710,height=588)

        #left bottom label
        lf_b=Label(bglbl,bd=1,relief=RIDGE,font=("times new roman",20),bg="white",fg="black")
        lf_b.place(x=45,y=153,width=710,height=464)

         #student id label
        sid_label=Label(lf_b,text=" Student ID ",font=("times new roman",17),bg="white",fg="black")
        sid_label.grid(row=0,column=0,padx=2,pady=10,sticky=W)

         #student id entry
        stud_entry=ttk.Entry(lf_b,width=20,textvariable=self.var_id,font=("times new roman",15))
        stud_entry.grid(row=0,column=1,padx=0,pady=0,sticky=W)

         #student name label
        sname_label=Label(lf_b,text=" Student Name ",font=("times new roman",17),bg="white",fg="black")
        sname_label.grid(row=0,column=2,padx=2,pady=10,sticky=W)

         #student name entry
        sname_entry=ttk.Entry(lf_b,width=20,textvariable=self.var_name,font=("times new roman",15))
        sname_entry.grid(row=0,column=3,padx=0,pady=0,sticky=W)

        #class label
        class_label=Label(lf_b,text=" Class ",font=("times new roman",17),bg="white",fg="black")
        class_label.grid(row=1,column=0,padx=2,pady=10,sticky=W)

         #class entry
        class_entry=ttk.Entry(lf_b,width=20,textvariable=self.var_class,font=("times new roman",15))
        class_entry.grid(row=1,column=1,padx=0,pady=0,sticky=W)

         #section label
        sec_label=Label(lf_b,text=" Section ",font=("times new roman",17),bg="white",fg="black")
        sec_label.grid(row=1,column=2,padx=2,pady=10,sticky=W)

         #section entry
        sec_entry=ttk.Entry(lf_b,width=20,textvariable=self.var_section,font=("times new roman",15))
        sec_entry.grid(row=1,column=3,padx=0,pady=0,sticky=W)

         #DOB label
        dob_label=Label(lf_b,text=" DOB ",font=("times new roman",17),bg="white",fg="black")
        dob_label.grid(row=2,column=0,padx=2,pady=10,sticky=W)

         #DOB entry
        dob_entry=ttk.Entry(lf_b,width=20,textvariable=self.var_dob,font=("times new roman",15))
        dob_entry.grid(row=2,column=1,padx=0,pady=0,sticky=W)

         #Email label
        email_label=Label(lf_b,text=" Email ",font=("times new roman",17),bg="white",fg="black")
        email_label.grid(row=2,column=2,padx=2,pady=10,sticky=W)

         #Email entry
        email_entry=ttk.Entry(lf_b,width=20,textvariable=self.var_email,font=("times new roman",15))
        email_entry.grid(row=2,column=3,padx=0,pady=0,sticky=W)

         #phone label
        phone_label=Label(lf_b,text=" Phone ",font=("times new roman",17),bg="white",fg="black")
        phone_label.grid(row=3,column=0,padx=2,pady=10,sticky=W)

         #phone entry
        phone_entry=ttk.Entry(lf_b,width=20,textvariable=self.var_phone,font=("times new roman",15))
        phone_entry.grid(row=3,column=1,padx=0,pady=0,sticky=W)

        #address label
        address_label=Label(lf_b,text=" Address ",font=("times new roman",17),bg="white",fg="black")
        address_label.grid(row=3,column=2,padx=2,pady=10,sticky=W)

         #address entry
        address_entry=ttk.Entry(lf_b,width=20,textvariable=self.var_address,font=("times new roman",15))
        address_entry.grid(row=3,column=3,padx=0,pady=0,sticky=W)

        #radio buttons
      

        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(lf_b,text="Take Photo Sample",variable=self.var_radio1,value="Yes")
        radiobtn1.grid(row=5,column=1)

         #radio buttons
        
        
        radiobtn2=ttk.Radiobutton(lf_b,text="No Photo Sample",variable=self.var_radio1,value="No")
        radiobtn2.grid(row=5,column=3)

        #button save
        button_l=Frame(bglbl,bd=1,relief=RIDGE,bg="white")
        button_l.place(x=240,y=430,width=300,height=40)

        save_btn=Button(button_l,text="Save",command=self.add_data,width=27,font=("times new roman",15),bg="#1261A0",fg="white",cursor="hand2")
        save_btn.grid(row=0,column=1)

       

         #button delete
        button_l3=Frame(bglbl,bd=1,relief=RIDGE,bg="white")
        button_l3.place(x=240,y=480,width=300,height=40)

        save_btn3=Button(button_l3,text="Delete",command=self.delete_data,width=27,font=("times new roman",15),bg="#1261A0",fg="white",cursor="hand2")
        save_btn3.grid(row=1,column=1)

         
         #button take photo sample
        button_l5=Frame(bglbl,bd=1,relief=RIDGE,bg="white")
        button_l5.place(x=240,y=530,width=300,height=40)

        save_btn5=Button(button_l5,text="Take Photo Sample",command=self.generate_dataset,width=27,font=("times new roman",15),bg="#1261A0",fg="white",cursor="hand2")
        save_btn5.grid(row=2,column=0)

         

        right_frame=Frame(lf_r,bd=1,relief=RIDGE,bg="white")
        right_frame.place(x=10,y=10,width=688,height=66)

        
        search_button=Button(right_frame,text="Refresh",command=self.refresh,width=16,font=("times new roman",15),bg="#1261A0",fg="white",cursor="hand2")
        search_button.grid(row=0,column=3)

        rightb_frame=Frame(lf_r,bd=1,relief=RIDGE,bg="white")
        rightb_frame.place(x=10,y=83,width=688,height=497)

        #bottom scrollbar
        scroll_x=Scrollbar(rightb_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(rightb_frame,orient=VERTICAL)


        self.student_table=ttk.Treeview(rightb_frame,column=("dep","sem","course","year","id","name","class","section","dob","email","phone","address","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("id",text="ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("class",text="Class")
        self.student_table.heading("section",text="Section")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("photo",text="Photo")
        self.student_table["show"]="headings"

       

        self.student_table.column("dep",width=167)
        self.student_table.column("sem",width=167)
        self.student_table.column("course",width=167)
        self.student_table.column("year",width=167)
        self.student_table.column("id",width=167)
        self.student_table.column("name",width=167)
        self.student_table.column("class",width=167)
        self.student_table.column("section",width=167)
        self.student_table.column("dob",width=167)
        self.student_table.column("email",width=167)
        self.student_table.column("phone",width=167)
        self.student_table.column("address",width=167)
        self.student_table.column("photo",width=167)
     
        self.student_table["show"]="headings"

      
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        

#****************************************************************************************************

    def add_data(self):
        if self.var_name.get()=="":    #if name or id field is empty display error message
            messagebox.showerror("Error","Please fill the Fields",parent=self.root)   #show error in root window only with message
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="face")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student_table values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.var_dep.get(),
                                                                                                    self.var_sem.get(),
                                                                                                    self.var_course.get(),
                                                                                                    self.var_year.get(),
                                                                                                    self.var_id.get(),
                                                                                                    self.var_name.get(),
                                                                                                    self.var_class.get(),
                                                                                                    self.var_section.get(),
                                                                                                    self.var_dob.get(),
                                                                                                    self.var_email.get(),
                                                                                                    self.var_phone.get(),
                                                                                                    self.var_address.get(),
                                                                                                    self.var_radio1.get()
                                                                                                   
                                                                                                    ))
    
               
                conn.commit()
                
                conn.close()
                messagebox.showinfo("Success","Student deatils inserted successfully!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


#*********************************************fetch data*************************************************************************
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="root",database="face")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student_table")
        data=my_cursor.fetchall()

        if len(data)!=0:
            
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

        
        #********************************************************8
    def refresh(self):
        self.new_window=Toplevel(self.root)    #used to open root window in newtab
        self.app=Student(self.new_window) 


        #*********************************get cursor*************************************

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_dep.set(data[0]),
        self.var_sem.set(data[1]),
        self.var_course.set(data[2]),
        self.var_year.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_class.set(data[6]),
        self.var_section.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_email.set(data[9]),
        self.var_phone.set(data[10]),
        self.var_address.set(data[11]),
        self.var_radio1.set(data[12])

        #delete function
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student ID is required to delete data.",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete Student Data???","Do you want to delete this student data?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="root",database="face")
                    my_cursor=conn.cursor()
                    sql="delete from student_table where id =%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)

                
                else:
                    if not delete:
                        return
                conn.commit()
                conn.close()
                
                messagebox.showinfo("Delete Student Data???","Student details has been deleted succesfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

#***********************************************Generate dataset by taking photo samples************************************************************

    def generate_dataset(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="face")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student_table")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student_table set dep=%s,sem=%s,course=%s,year=%s,name=%s,class=%s,section=%s,dob=%s,email=%s,phone=%s,address=%s,photo=%s where id=%s",(
                                                                                                                                                                                                    
                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                    self.var_sem.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_name.get(),
                                                                                                                                                                                    self.var_class.get(),
                                                                                                                                                                                    self.var_section.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                    self.var_id.get(),
                                                                                                                                                       ))
                conn.commit()
                self.fetch_data()
                conn.close()

                #---------------Loading Frontal face data from OpenCV------------------------------
                face_classifier=cv2.CascadeClassifier(r"C:\Users\91900\Desktop\face_recognition_system\haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor 1.3 , minimum neightbor=5 so 1.3 and 5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="C:\\Users\\91900\Desktop\\face_recognition_system\\data\\user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==50:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed successfully")

            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
            

          


    
    
if __name__== "__main__":   #used to call main 
    root=Tk()       #Create an instance of tkinter window
    obj=Student(root)
    root.mainloop()  #method will loop forever, waiting for events from the user, until the user exits the program 

