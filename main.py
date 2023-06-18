import os
from tkinter import*        #import tkinter
from tkinter import ttk     #ttk is module used to style tkinter widgets
from PIL import Image,ImageTk      #PILLOW LIBRARY which helps in image processing (editing,cropping image)
from student import Student
from train import Train
from face_recognition import Face_Recognition
import pandas as pd
import numpy as np
from tkinter import filedialog as fd
from tkinter import messagebox


class Face_Recognition_System:
    def __init__(self,root):    #calling constructor #root is root window
        self.root=root
        self.root.geometry("1530x790+0+0")    #setting window width and height where 0,0 symbolize x,y axis
        self.root.title("Facial recognition Attendence Management System")     #setting the title

        
        img=Image.open(r"C:\Users\91900\Desktop\face_recognition_system\college_images\header.png")   #diplay image
        img=img.resize((1530,85),Image.Resampling.LANCZOS)    #we resized width and height of image to 500 and 130, ANTIALIAS ued to return resized images
        self.photoimg=ImageTk.PhotoImage(img)          #img stored in a variable self.photoimg     #create an object of tkinter ImageTk
        f_lbl=Label(self.root,image=self.photoimg)      #we set image on window using label
        f_lbl.place(x=0,y=0,width=1530,height=85)

        #bg image
        bg=Image.open(r"C:\Users\91900\Desktop\face_recognition_system\college_images\middle.png")
        bg=bg.resize((1530,750),Image.Resampling.LANCZOS)    #we resized width and height of image to 500 and 130, ANTIALIAS ued to return resized images
        self.photoimg2=ImageTk.PhotoImage(bg)          #img stored in a variable self.photoimg     #create an object of tkinter ImageTk
        bglbl=Label(self.root,image=self.photoimg2)      #we set image on window using label
        bglbl.place(x=0,y=85,width=1530,height=750)

        #title
        title=Label(f_lbl,text="Facial Recognition Attendence Tracker",font=("Comic Sans MS",22),bg="white",fg="black")
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


        #button student
        bs=Image.open(r"C:\Users\91900\Desktop\face_recognition_system\college_images\stud.jpeg")
        bs=bs.resize((220,400),Image.Resampling.LANCZOS)    #we resized width and height of image to 500 and 130, ANTIALIAS ued to return resized images
        self.photoimg3=ImageTk.PhotoImage(bs)          #img stored in a variable self.photoimg 
        b1=Button(bglbl,image=self.photoimg3,command=self.student_details,cursor="hand2")
        b1.place(x=62,y=177,width=220,height=400)

         #button train data
        btd=Image.open(r"C:\Users\91900\Desktop\face_recognition_system\college_images\train.jpeg")
        btd=btd.resize((220,400),Image.Resampling.LANCZOS)    #we resized width and height of image to 500 and 130, ANTIALIAS ued to return resized images
        self.photoimg4=ImageTk.PhotoImage(btd)          #img stored in a variable self.photoimg 
        b2=Button(bglbl,image=self.photoimg4,cursor="hand2",command=self.train_data)
        b2.place(x=292,y=177,width=220,height=400)


        #button train data
        bp=Image.open(r"C:\Users\91900\Desktop\face_recognition_system\college_images\photos.jpeg")
        bp=bp.resize((230,400),Image.Resampling.LANCZOS)    #we resized width and height of image to 500 and 130, ANTIALIAS ued to return resized images
        self.photoimg5=ImageTk.PhotoImage(bp)          #img stored in a variable self.photoimg 
        b3=Button(bglbl,image=self.photoimg5,cursor="hand2",command=self.open_img)
        b3.place(x=518,y=177,width=230,height=400)

        
        #button attendence
        ba=Image.open(r"C:\Users\91900\Desktop\face_recognition_system\college_images\recog.jpeg")
        ba=ba.resize((230,400),Image.Resampling.LANCZOS)    #we resized width and height of image to 500 and 130, ANTIALIAS ued to return resized images
        self.photoimg6=ImageTk.PhotoImage(ba)          #img stored in a variable self.photoimg 
        ba=Button(bglbl,image=self.photoimg6,cursor="hand2",command=self.face_data)
        ba.place(x=755,y=177,width=230,height=400)


        
        #button fg
        bfg=Image.open(r"C:\Users\91900\Desktop\face_recognition_system\college_images\attend.jpeg")
        bfg=bfg.resize((230,400),Image.Resampling.LANCZOS)    #we resized width and height of image to 500 and 130, ANTIALIAS ued to return resized images
        self.photoimg7=ImageTk.PhotoImage(bfg)          #img stored in a variable self.photoimg 
        bfg=Button(bglbl,image=self.photoimg7,cursor="hand2",command=self.uni)
        bfg.place(x=992,y=177,width=230,height=400)
       

       
        #button train data
        be=Image.open(r"C:\Users\91900\Desktop\face_recognition_system\college_images\exit.jpeg")
        be=be.resize((230,400),Image.Resampling.LANCZOS)    #we resized width and height of image to 500 and 130, ANTIALIAS ued to return resized images
        self.photoimg8=ImageTk.PhotoImage(be)          #img stored in a variable self.photoimg 
        be=Button(bglbl,image=self.photoimg8,cursor="hand2",command=self.i_exit)
        be.place(x=1229,y=177,width=230,height=400)

    #Photos (Gallery) button
    def open_img(self):
        os.startfile("data")

    def uni(self):
        df=pd.read_csv("attendance.csv")
        pf=df.drop_duplicates(subset='ID', keep="last")
        pf.to_csv("final_attendence/raw_data.csv", index=False)
        os.startfile("final_attendence")
        
    def i_exit(self):
        self.i_exit=messagebox.askyesno("Auto-Log Attendance","Are you sure to exit?",parent=self.root)
        if self.i_exit>0:
            self.root.destroy()
        else:
            return
    
    
        #***************************************************************************************************
        #functions
    def student_details(self):
        self.new_window=Toplevel(self.root)    #used to open root window in newtab
        self.app=Student(self.new_window)      #passing new window to Student class

    def train_data(self):
        self.new_window=Toplevel(self.root)    #used to open root window in newtab
        self.app=Train(self.new_window)      #passing new window to Student class

    def face_data(self):
        self.new_window=Toplevel(self.root)    #used to open root window in newtab
        self.app=Face_Recognition(self.new_window)      #passing new window to Student class

    

                                                                 


if __name__== "__main__":   #used to call main 
    root=Tk()       #Create an instance of tkinter window
    obj=Face_Recognition_System(root)
    root.mainloop()  #method will loop forever, waiting for events from the user, until the user exits the program 


    
    

