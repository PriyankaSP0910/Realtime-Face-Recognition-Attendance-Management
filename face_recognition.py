import os
from tkinter import*        #import tkinter
from tkinter import ttk     #ttk is module used to style tkinter widgets
from PIL import Image,ImageTk      #PILLOW LIBRARY which helps in image processing (editing,cropping image)
from student import Student
import numpy as np
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
from mysql.connector import Error

class Face_Recognition:
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
        title=Label(self.root,text="Face Recognizer",font=("Comic Sans MS",22),bg="white",fg="black")
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

        fr_btn=Frame(bglbl,bd=1,relief=RIDGE,bg="white")
        fr_btn.place(x=430,y=400,width=655,height=50)

        fr=Button(fr_btn,text="Recognize Face",command=self.face_recog,width=46,font=("times new roman",19),bg="#1261A0",fg="white",cursor="hand2")
        fr.grid(row=9,column=4)


        #Marking attendance function
    def mark_attendance(self,c,s,n,i):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((c not in name_list) and (s not in name_list) and (n not in name_list) and (i not in name_list)):
                now=datetime.now()
                d1=now.strftime("%D/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{c},{s},{n},{i},{dtString},{d1},Present")

    #Recognizing face function
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="face")
                my_cursor=conn.cursor()

                my_cursor.execute("select dep from student_table where id="+str(id))
                c=my_cursor.fetchone()
                print(c)

                my_cursor.execute("select sem from student_table where id="+str(id))
                s=my_cursor.fetchone()
                print(s)
        
                my_cursor.execute("select id from student_table where id="+str(id))
                n=my_cursor.fetchone()
                print(n)
                
                my_cursor.execute("select name from student_table where id="+str(id))
                i=my_cursor.fetchone()
                print(i)

                self.mark_attendance(c,s,n,i)
       

                

                if confidence>55:
                    cv2.putText(img,f"Dep:{c}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Sem:{s}",(x,y-60),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"ID:{n}",(x,y-40),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Name:{i}",(x,y-20),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)

                    self.mark_attendance(c,s,n,i)                    
                   
                   
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,f"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord=[x,y,w,h]
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()




if __name__== "__main__":   #used to call main 
    root=Tk()       #Create an instance of tkinter window
    obj=Face_Recognition(root)
    root.mainloop()  #method will loop forever, waiting for events from the user, until the user exits the program 