import os
from tkinter import*        #import tkinter
from tkinter import ttk     #ttk is module used to style tkinter widgets
from PIL import Image,ImageTk      #PILLOW LIBRARY which helps in image processing (editing,cropping image)
from student import Student
from train import Train
import pandas as pd
import numpy as np
from tkinter import filedialog as fd
from tkinter import messagebox
from main import Face_Recognition_System


class Register_Window:
    def __init__(self,root):    #calling constructor #root is root window
        self.root=root
        self.root.geometry("1530x790+0+0")    #setting window width and height where 0,0 symbolize x,y axis
        self.root.title("Facial recognition Attendence Management System")     #setting the title

        backg=Image.open(r"C:\Users\91900\Desktop\face_recognition_system\college_images\pbp.jpg")
        backg=backg.resize((1530,950),Image.Resampling.LANCZOS)    #we resized width and height of image to 500 and 130, ANTIALIAS ued to return resized images
        self.photoimg2=ImageTk.PhotoImage(backg)          #img stored in a variable self.photoimg     #create an object of tkinter ImageTk
        bglbll=Label(self.root,image=self.photoimg2)      #we set image on window using label
        bglbll.place(x=0,y=0,width=1530,height=950)

     #Left Image
        self.bg2=ImageTk.PhotoImage(file=r"C:\Users\91900\Desktop\face_recognition_system\college_images\lady.png")
        bg_lbl2=Label(self.root,image=self.bg2)
        bg_lbl2.place(x=50,y=80,width=470,height=550)

        #Frame for Register box
        frame=Frame(self.root,bg="black")
        frame.place(x=520,y=80,width=800,height=550)

        #Text in Register Now frame
        register_lbl=Label(frame,text="Register Now !!!",font=("times new roman",20,"bold"),fg="white",bg="black")
        register_lbl.place(x=20,y=30)

        #Labels in Register Frame

        #left row 1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="black",fg="white")
        fname.place(x=90,y=90)

        self.fname_entry=ttk.Entry(frame,font=("times new roman",15))
        self.fname_entry.place(x=90,y=120,width=250)
       
        #right row 1
        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="black",fg="white")
        lname.place(x=390,y=90)

        self.txt_lname=ttk.Entry(frame,font=("times new roman",15))
        self.txt_lname.place(x=390,y=120,width=250)

        

        #left row 3
        security_q=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="black",fg="white")
        security_q.place(x=90,y=175)
        #setting up combobox on left
        self.txt_lname=ttk.Entry(frame,font=("times new roman",15))
        self.txt_lname.place(x=90,y=205,width=250)
        
        #right row 3
        security_a=Label(frame,text="Phone Number",font=("times new roman",15,"bold"),bg="black",fg="white")
        security_a.place(x=390,y=175)

        self.txt_security=ttk.Entry(frame,font=("times new roman",15))
        self.txt_security.place(x=390,y=205,width=250)

        #left row 4
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="black",fg="white")
        pswd.place(x=90,y=260)

        self.txt_pswd=ttk.Entry(frame,font=("times new roman",15))
        self.txt_pswd.place(x=90,y=285,width=250)

        #right row 4
        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="black",fg="white")
        confirm_pswd.place(x=390,y=260)

        self.txt_confirm_pswd=ttk.Entry(frame,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=390,y=285,width=250)

        
        #Buttons 
        #register button
       
        b2=Button(frame,text="Register",command=self.register,borderwidth=0,cursor="hand2",font=("times new roman",14,"bold"),bg="green",fg="white")
        b2.place(x=210,y=360,width=300)

    def register(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition_System(self.new_window)



if __name__== "__main__":   #used to call main 
    root=Tk()       #Create an instance of tkinter window
    obj=Register_Window(root)
    root.mainloop()  #method will loop forever, waiting for events from the user, until the user exits the program 

