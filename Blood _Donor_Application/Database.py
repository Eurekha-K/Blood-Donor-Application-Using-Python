import tkinter as tk
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector








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
    