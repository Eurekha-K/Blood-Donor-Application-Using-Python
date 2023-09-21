import tkinter as tk
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector




def register():

    
    global f_name_entry
    global b_group_entry
    global gender_entry
    global country_entry
    global state_entry
    global district_entry
    global zipcode_entry
    global mobile_entry
    global email_entry
    global pswd_entry
    global cp_entry
    global img
    global photoimg

    #Registration --------------
    

    #img=Image.open(r"C:\Users\Welcome\Desktop\Blood _Donor_Application\Blood Donation\blood-donation.jpg")
    #img=img.resize((500,300))
    #photoimg=ImageTk.PhotoImage(img)

    #Label(root,image=photoimg).pack()
    

    
    
    frame2=Frame(root,width=610,height=700,bg="red",bd=8)
    frame2.place(x=450,y=50)

    heading=Label(frame2,text='Donor Registration',font=('Italic',20,'bold'),bg='red',fg='white')
    heading.place(x=120,y=10)

            #---------------- first name------------
    f_name=Label(frame2,text='Full Name :',font=('Italic',14,'bold'),bg='red',fg='white')
    f_name.place(x=25,y=80)

    f_name_entry=Entry(frame2,width=30,borderwidth=4,font=('Caliber',15,'bold'))
    f_name_entry.place(x=240,y=80)



    #--Blood Group--

    b_group=Label(frame2,text='Blood Group :',font=('Italic',14,'bold'),bg='red',fg='white')
    b_group.place(x=25,y=130)

    b_group_entry=Entry(frame2,width=30,borderwidth=4,font=('Caliber',15,'bold'))
    b_group_entry.place(x=240,y=130)

    #---email--

    email=Label(frame2,text='Email:',font=('Italic',14,'bold'),bg='red',fg='white')
    email.place(x=25,y=180)

    email_entry=Entry(frame2,width=30,borderwidth=4,font=('Caliber',15,'bold'))
    email_entry.place(x=240,y=180)


    #---gender-

    gender=Label(frame2,text='Gender:',font=('Italic',14,'bold'),bg='red',fg='white')
    gender.place(x=25,y=230)

    gender_entry=Entry(frame2,width=30,borderwidth=4,font=('Caliber',15,'bold'))
    gender_entry.place(x=240,y=230)

    #Country----

    country_label=Label(frame2,text='Country:',font=('Italic',14,'bold'),bg='red',fg='white',border=4)
    country_label.place(x=25,y=280)

    country_entry=Entry(frame2,width=30,borderwidth=4,font=('Caliber',15,'bold'))

    country_entry.place(x=240,y=280)

    #State

    state_label=Label(frame2,text='State:',font=('Italic',14,'bold'),bg='red',fg='white',border=4)
    state_label.place(x=25,y=330)

    state_entry=Entry(frame2,width=30,borderwidth=4,font=('Caliber',15,'bold'))

    state_entry.place(x=240,y=330)

    #District------------------

    district_label=Label(frame2,text='District:',font=('Italic',14,'bold'),bg='red',fg='white',border=4)
    district_label.place(x=25,y=380)

    district_entry=Entry(frame2,width=30,borderwidth=4,font=('Caliber',15,'bold'))

    district_entry.place(x=240,y=380)
    #Zipcode

    zipcode_label=Label(frame2,text='Zipcode:',font=('Italic',14,'bold'),bg='red',fg='white',border=4)
    zipcode_label.place(x=25,y=430)

    zipcode_entry=Entry(frame2,width=30,borderwidth=4,font=('Caliber',15,'bold'))

    zipcode_entry.place(x=240,y=430)

    #Mobile Number
    mobile_label=Label(frame2,text='Mobile Number:',font=('Italic',14,'bold'),bg='red',fg='white',border=4)
    mobile_label.place(x=25,y=480)

    mobile_entry=Entry(frame2,width=30,borderwidth=4,font=('Caliber',15,'bold'))

    mobile_entry.place(x=240,y=480)


    #--Password
    pswd_label=Label(frame2,text='Password:',font=('Italic',14,'bold'),bg='red',fg='white')
    pswd_label.place(x=25,y=530)

    pswd_entry=Entry(frame2,width=30,borderwidth=4,font=('Caliber',15,'bold'),show="*")
    pswd_entry.place(x=240,y=530)

    #-- Confirm Password
    cp_label=Label(frame2,text='Confirm Password:',font=('Italic',14,'bold'),bg='red',fg='white')
    cp_label.place(x=25,y=580)

    cp_entry=Entry(frame2,width=30,borderwidth=4,font=('Caliber',15,'bold'),show="*")
    cp_entry.place(x=240,y=580)

    #---Submit Button
    submit=Button(frame2,text='Submit',bg='White',cursor='hand2',font=('Italic',12,'bold'),fg='black',width=17)
    submit.place(x=190,y=640)

root=tk.Tk()
root.geometry('1500x800')
root.title('Registration Page')
register()
root.mainloop()