


import tkinter as tk
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector

def submit_fun():
    full_name=f_name_entry.get()
    blood_group=b_group_entry.get()
    email_address=email_entry.get()
    gender_name=gender_entry.get()
    country_name=country_entry.get()
    state_name=state_entry.get()
    district_name=district_entry.get()
    zipcode_num=zipcode_entry.get()
    mobile_num=mobile_entry.get()
    pswd_=pswd_entry.get()
    cp_=cp_entry.get()
    if f_name_entry.get()=="":
        messagebox.showerror('Alert!','First Name cant be empty!')
    elif b_group_entry.get()=="":
        messagebox.showerror('Alert!','Blood group cant be empty!')
    elif email_entry.get()=="":
        messagebox.showerror('Alert!','Email cant be empty!')
    elif gender_entry.get()=="":
        messagebox.showerror('Alert!','Gender cant be empty!')
    elif pswd_entry.get()=="":
        messagebox.showerror('Alert!','Password cant be empty!')
    elif cp_entry.get()=="":
        messagebox.showerror('Alert!','Confirm password cant be empty!')
    elif country_entry.get()=="":
        messagebox.showerror('Alert!','Country cant be empty!')
    elif zipcode_entry.get()=="":
        messagebox.showerror('Alert!','Zipcode cant be empty!')
    elif state_entry.get()=="":
        messagebox.showerror('Alert!','State cant be empty!')
    elif district_entry.get()=="":
        messagebox.showerror('Alert!','District cant be empty!')
    elif mobile_entry.get()=="":
        messagebox.showerror('Alert!','Mobile Number cant be empty!')
    elif pswd_entry.get()!=cp_entry.get():
        messagebox.showerror('Alert!','Password and Confirm Password should match !')
    else:
        mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = 'Registrations'
        )
        mycursor = mydb.cursor(buffered=True)
        
        mycursor.execute("SELECT count(*) FROM Blood_Donors WHERE Full_name = '{}'".format(full_name))
        count=mycursor.fetchall()
        mycursor.execute("SELECT count(*) FROM Blood_Donors WHERE Email = '{}'".format(email_address))
        e_count=mycursor.fetchall()
        if count[0][0]==1 or e_count[0][0]==1 :
            messagebox.showerror('User Already Registered.Please Login !')
        else:
            mycursor.execute('CREATE DATABASE IF NOT EXISTS Registrations')
            mycursor.execute('USE Registrations')
            mycursor.execute("CREATE TABLE IF NOT EXISTS Blood_Donors (Full_name VARCHAR(20) ,Blood_group VARCHAR(20),Email VARCHAR(20),Gender VARCHAR(20),Country VARCHAR(20),State VARCHAR(20),District VARCHAR(20),Zipcode INT,Mobile INT,Password VARCHAR(20))")

            mycursor.execute("""
            INSERT INTO Blood_Donors(Full_name,Blood_group,Email,Gender,Country,State,District,Zipcode,Mobile,Password)
            VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')
            """.format(full_name,blood_group,email_address,gender_name,country_name,state_name,district_name,zipcode_num,mobile_num,pswd_))
            mydb.commit()
            messagebox.showinfo('message','Successfully Registered')
            f_name_entry.delete(0,END)
            b_group_entry.delete(0,END)
            gender_entry.delete(0,END)
            country_entry.delete(0,END)
            state_entry.delete(0,END)
            district_entry.delete(0,END)
            zipcode_entry.delete(0,END)
            mobile_entry.delete(0,END)
            email_entry.delete(0,END)
            pswd_entry.delete(0,END)
            cp_entry.delete(0,END)
            root.destroy()
            

    

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
    #root=tk.Tk()
    #root.destroy()
    root=Toplevel()
    root.geometry('1500x800')
    root.title('Registration Page')

    img=Image.open(r"C:\Users\Welcome\Desktop\Blood _Donor_Application\real-red-blood-drop-clip-art-clkerm-vector-clip-0.png")
    
    img=img.resize((500,500))
    photoimg=ImageTk.PhotoImage(img)
    

    Im=Label(root,image=photoimg)
    Im.place(x=900,y=150)

    
    
    frame2=Frame(root,width=610,height=700,bg="red",bd=8)
    frame2.place(x=50,y=50)

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
    submit=Button(frame2,text='Submit',bg='White',cursor='hand2',font=('Italic',12,'bold'),fg='black',width=17,command=submit_fun)
    submit.place(x=190,y=640)

    #gender=Label(frame2,text='Last Name :',font=('Italic',18,'bold'),bg='red',fg='white')
    #gender.place(x=90,y=13)



root=tk.Tk()
root.geometry('1530x790')
root.title('Save Life')
def clear():
    entry1.delete(0,END)
    entry2.delete(0,END)
    
    
def database():
    import mysql.connector
    
    
    mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = 'Registrations'
        )

    print(mydb)
    mycursor = mydb.cursor(buffered=True)
    
    mycursor.execute("SELECT Full_name,Blood_group,Email,Gender,Country,State,District,Zipcode,Mobile from Blood_Donors where Country='{}' and State='{}' and District='{}' and Zipcode='{}'".format(country_e.get(),state_e.get(),district_e.get(),zipcode_e.get()))      
    res=mycursor.fetchall()
   # print(tabulate(res, ['Full_name','Blood_group','Email','Gender','Country','State','District','Zipcode','Mobile']))
    for data in res:
        print(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8])
    

def show():
    window=Toplevel()
    #Country----

    country_l=Label(window,text='Country:',font=('Italic',14,'bold'),bg='red',fg='white',border=4)
    country_l.place(x=25,y=280)

    country_e=Entry(window,width=30,borderwidth=4,font=('Caliber',15,'bold'))

    country_e.place(x=240,y=280)

    #State

    state_l=Label(window,text='State:',font=('Italic',14,'bold'),bg='red',fg='white',border=4)
    state_l.place(x=25,y=330)

    state_e=Entry(window,width=30,borderwidth=4,font=('Caliber',15,'bold'))

    state_e.place(x=240,y=330)

    #District------------------

    district_l=Label(window,text='District:',font=('Italic',14,'bold'),bg='red',fg='white',border=4)
    district_l.place(x=25,y=380)

    district_e=Entry(window,width=30,borderwidth=4,font=('Caliber',15,'bold'))

    district_e.place(x=240,y=380)
    
   
    
    #Zipcode--------------------------
    
    zipcode_l=Label(window,text='District:',font=('Italic',14,'bold'),bg='red',fg='white',border=4)
    zipcode_l.place(x=25,y=380)

    zipcode_e=Entry(window,width=30,borderwidth=4,font=('Caliber',15,'bold'))

    zipcode_e.place(x=240,y=380)
    
    Button(window,text='Show Details',command=database).place(x=240,y=430)
    
    
        

    
def sign_in():
    
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
        clear()
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
sign_up=Button(frame1,text='Register',width=7,pady=4,bg='red',border=0,fg='white',cursor='hand2',font=('Microsoft Yamei UI Light',11,'bold'),command=register)
sign_up.place(x=130,y=280)


        
        

root.mainloop()
    

            


        
