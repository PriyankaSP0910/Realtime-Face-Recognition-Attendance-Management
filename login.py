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
from register import Register_Window
from main import Face_Recognition_System



class Login_Window:
    def __init__(self,root):    #calling constructor #root is root window
        self.root=root
        self.root.geometry("1530x790+0+0")    #setting window width and height where 0,0 symbolize x,y axis
        self.root.title("Facial recognition Attendence Management System")     #setting the title

        background=Image.open(r"C:\Users\91900\Desktop\face_recognition_system\college_images\pbp.jpg")
        background=background.resize((1530,950),Image.Resampling.LANCZOS)    #we resized width and height of image to 500 and 130, ANTIALIAS ued to return resized images
        self.photoimg2=ImageTk.PhotoImage(background)          #img stored in a variable self.photoimg     #create an object of tkinter ImageTk
        bglb=Label(self.root,image=self.photoimg2)      #we set image on window using label
        bglb.place(x=0,y=0,width=1530,height=950)

        #Frame for Login box
        frame=Frame(self.root,bg="black")
        frame.place(x=535,y=130,width=350,height=450)


        #Startup Text
        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=105,y=85)

        #Label after Username
        username=lbl=Label(frame,text="E-mail / Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=40,y=155)
        self.txtuser=ttk.Entry(frame,font=("times new roman",20))
        self.txtuser.place(x=40,y=180,width=270)

        #Label for Password
        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=40,y=239)
        self.txtpass=ttk.Entry(frame,font=("times new roman",20),show='*')
        self.txtpass.place(x=40,y=270,width=270)

        #Login Button
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="green",activeforeground="white",cursor="hand2",activebackground="Red")
        loginbtn.place(x=98,y=320,width=150,height=35)

        #New Register Button
        register=Button(frame,text="New User Register",command=self.register,font=("times new roman",10,"bold"),borderwidth=0,fg="#004999",bg="black",activeforeground="white",activebackground="black",cursor="hand2")
        register.place(x=20,y=365,width=300)

        #Forgot password Button
        passwordbtn=Button(frame,text="Forgot Password ?",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black",cursor="hand2")
        passwordbtn.place(x=20,y=390,width=300)

    def login(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition_System(self.new_window)

    def register(self):
        self.new_window=Toplevel(self.root)
        self.app=Register_Window(self.new_window)




if __name__== "__main__":   #used to call main 
    root=Tk()       #Create an instance of tkinter window
    obj=Login_Window(root)
    root.mainloop()  #method will loop forever, waiting for events from the user, until the user exits the program 

