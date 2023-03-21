from tkinter import*        #import tkinter
from tkinter import ttk     #ttk is module used to style tkinter widgets
from PIL import Image,ImageTk      #PILLOW LIBRARY which helps in image processing (editing,cropping image)
from PIL import*

class Student:
    def __init__(self,root):    #calling constructor #root is root window
        self.root=root
        self.root.geometry("1530x790+0+0")    #setting window width and height where 0,0 symbolize x,y axis
        self.root.title("Facial recognition Attendence Management System")     #setting the title

        img=Image.open(r"C:\Users\91900\Desktop\face_recognition system\college_images\header.png")   #diplay image
        img=img.resize((1530,85),Image.Resampling.LANCZOS)    #we resized width and height of image to 500 and 130, ANTIALIAS ued to return resized images
        self.photoimg=ImageTk.PhotoImage(img)          #img stored in a variable self.photoimg     #create an object of tkinter ImageTk
        f_lbl=Label(self.root,image=self.photoimg)      #we set image on window using label
        f_lbl.place(x=0,y=0,width=1530,height=85)


        #bg image
        bg=Image.open(r"C:\Users\91900\Desktop\face_recognition system\college_images\sbg.jpeg")
        bg=bg.resize((1530,750),Image.Resampling.LANCZOS)    #we resized width and height of image to 500 and 130, ANTIALIAS ued to return resized images
        self.photoimg2=ImageTk.PhotoImage(bg)          #img stored in a variable self.photoimg     #create an object of tkinter ImageTk
        bglbl=Label(self.root,image=self.photoimg2)      #we set image on window using label
        bglbl.place(x=0,y=85,width=1530,height=750)

        #title
        title=Label(f_lbl,text="Student Management System",font=("Comic Sans MS",22),bg="white",fg="black")
        title.place(x=0,y=0,width=1530,height=55)


        #logo image
        logo=Image.open(r"C:\Users\91900\Desktop\face_recognition system\college_images\logo.png")
        logo=logo.resize((80,80),Image.Resampling.LANCZOS)    #we resized width and height of image to 500 and 130, ANTIALIAS ued to return resized images
        self.photoim=ImageTk.PhotoImage(logo)          #img stored in a variable self.photoimg     #create an object of tkinter ImageTk
        lg=Label(self.root,image=self.photoim)      #we set image on window using label
        lg.place(x=15,y=16,width=60,height=60)

        
        #user image
        user=Image.open(r"C:\Users\91900\Desktop\face_recognition system\college_images\user.png")
        user=user.resize((55,55),Image.Resampling.LANCZOS)    #we resized width and height of image to 500 and 130, ANTIALIAS ued to return resized images
        self.photoimg9=ImageTk.PhotoImage(user)          #img stored in a variable self.photoimg     #create an object of tkinter ImageTk
        ul=Label(self.root,image=self.photoimg9)      #we set image on window using label
        ul.place(x=1400,y=16,width=55,height=55)


         #logout image
        exit=Image.open(r"C:\Users\91900\Desktop\face_recognition system\college_images\logout.png")
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
        dep_combo=ttk.Combobox(lf_l,font=("times new roman",15),width=19,state="read only")                             #to make combobox
        dep_combo["values"]=("MCA","Computer Science","ECE","IT","Civil","Mechanical","Mtech")   #pass value to combobox in tuple
        dep_combo.current(0)                                                                            #default value is select department
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)                                     #to make sure the combobox is in front of label
                                                                                                   #sticky highlight the selected combobox option
        #semester label
        sem_label=Label(lf_l,text=" Semester ",font=("times new roman",17),bg="white",fg="black")
        sem_label.grid(row=0,column=2,padx=2,pady=10,sticky=W)


        #semester
        dep_combo1=ttk.Combobox(lf_l,font=("times new roman",15),width=19,state="read only")                             #to make combobox
        dep_combo1["values"]=("Semester 1","Semester 2","Semester 3","Semester 4","Semester 5","Semester 6")   #pass value to combobox in tuple
        dep_combo1.current(0)                                                                            #default value is select department
        dep_combo1.grid(row=0,column=3,padx=2,pady=10,sticky=W)                                     #to make sure the combobox is in front of label
                                                                                                   #sticky highlight the selected combobox option

        #Courses label
        sem_label2=Label(lf_l,text=" Courses ",font=("times new roman",17),bg="white",fg="black")
        sem_label2.grid(row=1,column=0,padx=2,pady=10,sticky=W)


        #Courses
        dep_combo2=ttk.Combobox(lf_l,font=("times new roman",15),width=19,state="read only")                             #to make combobox
        dep_combo2["values"]=("C Programming","Environmental Studies","Chemistry","Physics","Kannada","Legislator")   #pass value to combobox in tuple
        dep_combo2.current(0)                                                                            #default value is select department
        dep_combo2.grid(row=1,column=1,padx=2,pady=10,sticky=W)     
        
        #year
        sem_label3=Label(lf_l,text=" Year ",font=("times new roman",17),bg="white",fg="black")
        sem_label3.grid(row=1,column=2,padx=2,pady=10,sticky=W)


        #Courses
        dep_combo3=ttk.Combobox(lf_l,font=("times new roman",15),width=19,state="read only")                             #to make combobox
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
        stud_entry=ttk.Entry(lf_b,width=20,font=("times new roman",15))
        stud_entry.grid(row=0,column=1,padx=0,pady=0,sticky=W)

         #student name label
        sname_label=Label(lf_b,text=" Student Name ",font=("times new roman",17),bg="white",fg="black")
        sname_label.grid(row=0,column=2,padx=2,pady=10,sticky=W)

         #student name entry
        sname_entry=ttk.Entry(lf_b,width=20,font=("times new roman",15))
        sname_entry.grid(row=0,column=3,padx=0,pady=0,sticky=W)

        #class label
        class_label=Label(lf_b,text=" Class ",font=("times new roman",17),bg="white",fg="black")
        class_label.grid(row=1,column=0,padx=2,pady=10,sticky=W)

         #class entry
        class_entry=ttk.Entry(lf_b,width=20,font=("times new roman",15))
        class_entry.grid(row=1,column=1,padx=0,pady=0,sticky=W)

         #section label
        sec_label=Label(lf_b,text=" Section ",font=("times new roman",17),bg="white",fg="black")
        sec_label.grid(row=1,column=2,padx=2,pady=10,sticky=W)

         #section entry
        sec_entry=ttk.Entry(lf_b,width=20,font=("times new roman",15))
        sec_entry.grid(row=1,column=3,padx=0,pady=0,sticky=W)

         #DOB label
        dob_label=Label(lf_b,text=" DOB ",font=("times new roman",17),bg="white",fg="black")
        dob_label.grid(row=2,column=0,padx=2,pady=10,sticky=W)

         #DOB entry
        dob_entry=ttk.Entry(lf_b,width=20,font=("times new roman",15))
        dob_entry.grid(row=2,column=1,padx=0,pady=0,sticky=W)

         #Email label
        email_label=Label(lf_b,text=" Email ",font=("times new roman",17),bg="white",fg="black")
        email_label.grid(row=2,column=2,padx=2,pady=10,sticky=W)

         #Email entry
        email_entry=ttk.Entry(lf_b,width=20,font=("times new roman",15))
        email_entry.grid(row=2,column=3,padx=0,pady=0,sticky=W)

         #phone label
        phone_label=Label(lf_b,text=" Phone ",font=("times new roman",17),bg="white",fg="black")
        phone_label.grid(row=3,column=0,padx=2,pady=10,sticky=W)

         #phone entry
        phone_entry=ttk.Entry(lf_b,width=20,font=("times new roman",15))
        phone_entry.grid(row=3,column=1,padx=0,pady=0,sticky=W)

        #address label
        address_label=Label(lf_b,text=" Address ",font=("times new roman",17),bg="white",fg="black")
        address_label.grid(row=3,column=2,padx=2,pady=10,sticky=W)

         #address entry
        address_entry=ttk.Entry(lf_b,width=20,font=("times new roman",15))
        address_entry.grid(row=3,column=3,padx=0,pady=0,sticky=W)

        #radio buttons
        radiobtn1=ttk.Radiobutton(lf_b,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=1)

         #radio buttons
        radiobtn2=ttk.Radiobutton(lf_b,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=3)

        #button sve
        button_l=Frame(bglbl,bd=1,relief=RIDGE,bg="white")
        button_l.place(x=64,y=430,width=320,height=40)

        save_btn=Button(button_l,text="Save",width=28,font=("times new roman",15),bg="#1261A0",fg="white",cursor="hand2")
        save_btn.grid(row=0,column=0)

        #button update
        button_l2=Frame(bglbl,bd=1,relief=RIDGE,bg="white")
        button_l2.place(x=400,y=430,width=320,height=40)

        save_btn2=Button(button_l2,text="Update",width=28,font=("times new roman",15),bg="#1261A0",fg="white",cursor="hand2")
        save_btn2.grid(row=0,column=1)

         #button delete
        button_l3=Frame(bglbl,bd=1,relief=RIDGE,bg="white")
        button_l3.place(x=64,y=480,width=320,height=40)

        save_btn3=Button(button_l3,text="Delete",width=28,font=("times new roman",15),bg="#1261A0",fg="white",cursor="hand2")
        save_btn3.grid(row=1,column=0)

         #button reset
        button_l4=Frame(bglbl,bd=1,relief=RIDGE,bg="white")
        button_l4.place(x=400,y=480,width=320,height=40)

        save_btn4=Button(button_l4,text="Reset",width=28,font=("times new roman",15),bg="#1261A0",fg="white",cursor="hand2")
        save_btn4.grid(row=1,column=1)


        
       
        

        

        
        
       







        

       











        

        


         













        


if __name__== "__main__":   #used to call main 
    root=Tk()       #Create an instance of tkinter window
    obj=Student(root)
    root.mainloop()  #method will loop forever, waiting for events from the user, until the user exits the program 

