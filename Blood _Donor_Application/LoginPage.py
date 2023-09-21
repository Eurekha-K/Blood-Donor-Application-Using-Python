import tkinter as tk
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector


def sign_in(root):
    
    global country_e
    global state_e
    global district_e
    global zipcode_e
    import mysql.connector

    mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = 'Registrations'
        )

    print(mydb)
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("SELECT count(*) FROM Blood_Donors WHERE Email = '{}'".format(entry1.get()))
    e_count=mycursor.fetchall()
    mycursor.execute("SELECT count(*) FROM Blood_Donors WHERE Password = '{}'".format(entry2.get()))
    count=mycursor.fetchall()
    if (e_count[0][0]!=1 or count[0][0]!=1):
        messagebox.showinfo('User is not Registered.Please Register!')
       # clear()
    elif (e_count[0][0]==1 and count[0][0]==1):
        window=Toplevel()
    
        #tree['columns']=('Full_name','Blood_group','Email','Gender','Country','State','District','Zipcode','Mobile')
        window.geometry('1500x800')
        #Country----

        country_l=Label(window,text='Country:',font=('Italic',14,'bold'),bg='red',fg='white',border=4)
        country_l.place(x=25,y=100)

        country_e=Entry(window,width=30,borderwidth=4,font=('Caliber',15,'bold'))

        country_e.place(x=240,y=100)

        #State

        state_l=Label(window,text='State:',font=('Italic',14,'bold'),bg='red',fg='white',border=4)
        state_l.place(x=25,y=150)

        state_e=Entry(window,width=30,borderwidth=4,font=('Caliber',15,'bold'))

        state_e.place(x=240,y=150)

        #District------------------

        district_l=Label(window,text='District:',font=('Italic',14,'bold'),bg='red',fg='white',border=4)
        district_l.place(x=25,y=200)

        district_e=Entry(window,width=30,borderwidth=4,font=('Caliber',15,'bold'))

        district_e.place(x=240,y=200)
        
        zipcode_l=Label(window,text='Zipcode:',font=('Italic',14,'bold'),bg='red',fg='white',border=4)
        zipcode_l.place(x=25,y=250)

        zipcode_e=Entry(window,width=30,borderwidth=4,font=('Caliber',15,'bold'))

        zipcode_e.place(x=240,y=250)

    
    

        Button(window,text='Show Details',command=database).place(x=240,y=450)
        

    
        

    
    
root=tk.Tk()
root.title('Sign_in Page')
root.geometry('1500x800')   
  
    

img=Image.open(r"C:\Users\Welcome\Desktop\Blood _Donor_Application\Blood Donation\blood-donation.jpg")
img=img.resize((970,445))
photoimg=ImageTk.PhotoImage(img)

Label(root,image=photoimg).place(x=500,y=250)
    


frame=Frame(root,width=1530,height=200,bg="red")
frame.place(x=0,y=0)

label=Label(frame,text='Blood Donor Application',bg='red',fg='white',font=('Microsoft Yamei UI Light',55,'bold'))
label.place(x=200,y=40)

frame1=Frame(root,width=400,height=350,bg="red")
frame1.place(x=20,y=300)
        
heading=Label(frame1,text='Sign in',font=('Italic',18,'bold'),bg='red',fg='white')
heading.place(x=135,y=30)
        
        #----------------------------

entry1= Entry(frame1,text="Sign in",bg='white', fg='grey',font=('Italic',15,'bold'))
entry1.place(x=60,y=100)
entry1.insert(0,'Username')
        
        #---------------------------
entry2= Entry(frame1,text="Username",bg='white', fg='grey',font=('Italic',15,'bold'),show='*')
entry2.place(x=60,y=150)
entry2.insert(0,'Password')


        
        
        
        #----------Login Button--------------
Button(frame1,text='Login',width=15,pady=4,bg='white',fg='grey',command=sign_in).place(x=120,y=200)

        
        #----------label-----
label3=Label(frame1,text='Dont have an account?',bg='red',fg='white',font=('Microsoft Yamei UI Light',10,'bold'))
label3.place(x=100,y=250)
        
        #-------signup--
sign_up=Button(frame1,text='Register',width=7,pady=4,bg='red',border=0,fg='white',cursor='hand2',font=('Microsoft Yamei UI Light',11,'bold'))
sign_up.place(x=130,y=280)


root.mainloop()