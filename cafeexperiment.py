from tkinter import *
from tkinter import messagebox
import os
import time
from datetime import date, datetime
import datetime
import tkinter
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from matplotlib.figure import Figure
from PIL import ImageTk,Image
import math, random, os
import mysql.connector
from mysql.connector.constants import CharacterSet

class Cafe:
    global drop_category
    global drop_items,drop_items3
    def __init__ (self,root):
        
        self.root=root
        self.root.title("TheCafe Manager")
        self.root.geometry("500x600")#Width*ht
        self.root.resizable(False, False)
        self.root.iconbitmap(r"attachment_88583168.png")
        self.root.config(background='#F6E4C6')
        #self.root = Toplevel(self.root)
        #image display
        cafeimg = Image.open(r"attachment_88583168.png")
        test = ImageTk.PhotoImage(cafeimg)

        label1 = tkinter.Label(self.root, image=test, height = 500, width=500)
        label1.image = test
        label1.place(x = 0, y=0)

        ct = datetime.datetime.now()
        time_Display=ct.strftime("%x %X")#%x-Local version of date %X-Local version of time

        label2= Label(self.root, text =time_Display,width = 30, font = ("arial", 10,'bold'),bg='#F6E4C6')
        label2.place(x = 312, y=565)

        bt_Admin = Button(self.root, text="Admin",height = 2, width = 10, fg="Black", bg="#D8D0C1", command=self.Admin_Win,relief=RAISED)
        bt_Bill = Button(self.root, text="Generate Bill",height = 2, width = 10, fg="Black", bg="#D8D0C1",relief=RAISED, command=self.GenerateBill)
        bt_Admin.place(x=212, y=456)
        bt_Bill.place(x=212, y=508)
        return         
    
    
    
    def login_Window(self):
        global login_window
        global user
        global passw
        self.user=StringVar()
        self.passw=StringVar()
        login_window = Toplevel(self.root)
        login_window.title("Login")
        login_window.geometry("250x300")#Width*ht
        login_window.resizable(False, False)
        login_window.config(background='#F6E4C6')
            
        user =Label(login_window, text ="User-ID", font = ("arial", 10,'bold'),bg='#F6E4C6').place(x = 16, y=90)
        user = Entry(login_window,textvariable=self.user, width=10, relief=SUNKEN).place(x = 110, y=93)
        passw = Label(login_window, text ="Password", font = ("arial",10,'bold'),bg='#F6E4C6').place(x = 16, y=140)
        passw = Entry(login_window,textvariable=self.passw, width=10, relief=SUNKEN).place(x = 110, y=143)
        bt_enter = Button(login_window, text="Enter",height = 2, width = 10, fg="Black", bg="#D8D0C1",relief=RAISED,command=self.Enter)
        bt_enter.place(x=85, y=220)
        return
        
        
    
    
    def Enter(self):
        connectiondb = mysql.connector.connect(host="localhost",user="root",password="#mysql2021",database='cafeManager')
        cursordb = connectiondb.cursor()
        
        usernamepy = self.user.get()
        passwordpy = self.passw.get()
        print(usernamepy)
        cursordb.execute("select * from login where username = %s and password = %s",(usernamepy,passwordpy))
        results = cursordb.fetchall()
        print(results)           

        if results:
            self.Admin_Win()
            login_window.withdraw()
            #messagebox.showinfo("ACCESS","User and Password is Correct")

        elif results == []:
            #return self.Admin_Win
            messagebox.showinfo("ACCESS DENIED","Recheck User and Password")
            #my_user.delete(0,END)
            #my_password.delete(0,END)
        

        cursordb.close()
        connectiondb.close()
        return
        #---------DropDown____MENU
        #cursordb.execute("insert into main values('{}', {})".format(str(user), passwd))


    def categorypicker(self):
        connectiondb = mysql.connector.connect(host="localhost",user="root",password="#mysql2021",database='cafeManager')
        cursordb = connectiondb.cursor()

        global resultcat,outc
        cursordb.execute("SELECT category_name FROM categories ;")
        resultcat = cursordb.fetchall()        
        print(resultcat)
        outc = [a1 for b1 in resultcat for a1 in b1]
        print(outc)        
        cursordb.close()
        connectiondb.close()
        
        return outc

    def itempicker(self,a):
        connectiondb = mysql.connector.connect(host="localhost",user="root",password="#mysql2021",database='cafeManager')
        cursordb = connectiondb.cursor()
        
        global resultitem,outi
        print(drop_category.get())
        cursordb.execute("SELECT items.item_name FROM items  INNER JOIN categories ON items.category_id=categories.category_id WHERE category_name = %s",(drop_category.get(),))
        resultitem = cursordb.fetchall()        
        print(resultitem)
        outi = [a2 for b2 in resultitem for a2 in b2]
        print(outi)  
        drop_items.config(value=outi)
        drop_items.current(0)    
        cursordb.close()
        connectiondb.close()
        
        return

    def itempicker3(self,a):
        connectiondb = mysql.connector.connect(host="localhost",user="root",password="#mysql2021",database='cafeManager')
        cursordb = connectiondb.cursor()
        
        global resultitem,outi3
        print(drop_category3.get())
        cursordb.execute("SELECT items.item_name FROM items  INNER JOIN categories ON items.category_id=categories.category_id WHERE category_name = %s",(drop_category3.get(),))
        resultitem = cursordb.fetchall()        
        print(resultitem)
        outi3 = [a2 for b2 in resultitem for a2 in b2]
        print(outi3)  
        drop_items3.config(value=outi3)
        drop_items3.current(0)    
        cursordb.close()
        connectiondb.close()
        
        return

    


    #Bill Generate Section=============
    def GenerateBill(self):
        global bill_window
        global cust_name
        global cust_age
        global cust_phone
        bill_window = Toplevel(self.root)
        bill_window.title("Calculate BIll")
        bill_window.geometry("1000x600")#Width*ht
        bill_window.resizable(False, False)
        bill_window.config(background='#F6E4C6')
        
        cafeimg1 = Image.open(r"delicious-digital-vertical-restaurant-menu.jpg")
        test1 = ImageTk.PhotoImage(cafeimg1)

        label3 = tkinter.Label(bill_window, image=test1, height = 600, width=500)
        label3.image = test1
        label3.place(x = 0, y=0)

        self.cust_name=StringVar()
        self.cust_age=StringVar()
        self.cust_phone=StringVar()


        cust_details = Label(bill_window, text ="Customer Details", font = ("arial", 10,'bold'),bg='#F6E4C6').place(x = 700, y=12)
        cust_name = Label(bill_window, text ="Name", font = ("arial", 10,'bold'),bg='#F6E4C6').place(x = 620, y=50)
        cust_name = Entry(bill_window,textvariable=self.cust_name, width=18, font="arial 11", bd=2, relief=SUNKEN).place(x = 720, y=48)
        cust_age = Label(bill_window, text ="Age", font = ("arial",10,'bold'),bg='#F6E4C6').place(x = 620, y=100)
        cust_age = Entry(bill_window,textvariable=self.cust_age, width=18, font="arial 11", bd=2, relief=SUNKEN).place(x = 720, y=98)
        cust_phone = Label(bill_window, text ="Phone No.", font = ("arial",10,'bold'),bg='#F6E4C6').place(x = 620, y=150)
        cust_phone = Entry(bill_window,textvariable=self.cust_phone, width=18, font="arial 11", bd=2, relief=SUNKEN).place(x = 720, y=150)
        bt_enter = Button(bill_window, text="Enter",height = 1, width = 8, fg="Black", bg="#D8D0C1",relief=RAISED,command=self.Enter_Details).place(x=900, y=277)
        bt_printBill = Button(bill_window, text="Print",height = 1, width = 8, fg="Black", bg="#D8D0C1",relief=RAISED).place(x=905, y=565)
        #gender drop down
        cust_gender = Label(bill_window, text ="Gender", font = ("arial",10,'bold'),bg='#F6E4C6').place(x = 620, y=200)
        global drop_gender   
        gender=['Male','Female','Others']
        drop_gender = ttk.Combobox(bill_window,width=22, value=gender).place(x = 720, y=200)
        

        # Create a drop box
        global drop_category   
        drop_category = ttk.Combobox(bill_window, value=self.categorypicker())
        #drop_category.current(0)
        drop_category.place(x = 570, y=280)
        drop_category.bind("<<ComboboxSelected>>", self.itempicker)

        # Combo box
        global drop_items
        drop_items = ttk.Combobox(bill_window, value=[" "])
        #drop_items.current(0)
        drop_items.place(x = 735, y=280)
        

        #Bill Area=============
        Frame_Preview = Frame(bill_window, bd=8, relief=GROOVE)
        Frame_Preview.place(x = 530, y=320, width=440, height=240)
        bill_title = Label(Frame_Preview, text="Bill Preview", font="arial 13", bd=3, relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(Frame_Preview, orient=VERTICAL)
        txtarea = Text(Frame_Preview, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=txtarea.yview)
        txtarea.pack(fill=BOTH, expand=1)
        return

    #Admin PAge=============
    def Admin_Win(self):
        global admin_window
        admin_window = Toplevel(self.root)
        admin_window.title("Admim")
        admin_window.geometry("650x600")#Width*ht
        admin_window.resizable(False, False)
        admin_window.config(background='#F6E4C6')
        
        cafeimg2 = Image.open(r"coffee-shop-banner.jpg")
        test2 = ImageTk.PhotoImage(cafeimg2)

        label = tkinter.Label(admin_window, image=test2, height = 240, width=650)
        label.image = test2
        label.place(x = 0, y=0)
        self.edit_menu=StringVar()
        self.add_menu=StringVar()

        
        Header = Label(admin_window, text ="Admin Room", font = ("arial", 10,'bold'),bg='#F6E4C6').place(x = 280, y=0)
        edit_menu = Label(admin_window, text ="Edit Item", font = ("arial", 10,'bold'),bg='#F6E4C6').place(x = 20, y=273)
        edit_menu = Entry(admin_window,textvariable=self.edit_menu, width=17, font="arial 11", bd=2, relief=SUNKEN).place(x = 362, y=272)
        edit_price= Entry(admin_window,textvariable=self.add_menu, width=10, font="arial 11", bd=2, relief=SUNKEN).place(x = 515, y=272)
        
        add_menu = Label(admin_window, text ="Add Item", font = ("arial",10,'bold'),bg='#F6E4C6').place(x = 20, y=323)
        add_menu= Entry(admin_window,textvariable=self.add_menu, width=17, font="arial 11", bd=2, relief=SUNKEN).place(x = 240, y=322)
        add_price= Entry(admin_window,textvariable=self.add_menu, width=10, font="arial 11", bd=2, relief=SUNKEN).place(x = 390, y=322)
        delete_menu = Label(admin_window, text ="Delete Item", font = ("arial",10,'bold'),bg='#F6E4C6').place(x =20, y=373)
        #delete_menu = Entry(admin_window, width=10, font="arial 15", bd=4, relief=SUNKEN).place(x = 120, y=370)
        data_analy = Label(admin_window, text ="View Stastics", font = ("arial",10,'bold'),bg='#F6E4C6').place(x =20, y=430)
        bt_show = Button(admin_window, text="View",height = 1, width = 8, fg="Black", bg="#D8D0C1",relief=RAISED,command=self.viewStats).place(x=120, y=430)
        bt_save = Button(admin_window, text="Save",height = 1, width = 8, fg="Black", bg="#D8D0C1",relief=RAISED,command=self.Enter_Details).place(x=300, y=550)
        
        #Edit Menu-dropdown(1)
        global drop_category
        cate=self.categorypicker()
        drop_category = ttk.Combobox(admin_window, value=cate,width=15)
        drop_category.current(0)
        drop_category.place(x = 120, y=273)     
        drop_category.bind("<<ComboboxSelected>>", self.itempicker)

        #Edit Menu-dropdown(2)
        global drop_items
        drop_items = ttk.Combobox(admin_window, value=[" "],width=15)        
        drop_items.current(0)
        drop_items.place(x = 240, y=273)        


        #Add Menu-dropdown(2)
        drop_category2 = ttk.Combobox(admin_window, value=cate,width=15)
        drop_category2.current(0)
        drop_category2.place(x = 120, y=323)        
        #drop_category.bind("<<ComboboxSelected>>", self.itempicker)



        #DELETE Menu-dropdown(3)
        global drop_category3
        drop_category3 = ttk.Combobox(admin_window, value=cate,width=15)
        drop_category3.current(0)
        drop_category3.place(x = 120, y=370)        
        drop_category3.bind("<<ComboboxSelected>>", self.itempicker3)

        #DELETE Menu-dropdown(3)
        global drop_items3
        drop_items3 = ttk.Combobox(admin_window, value=[" "],width=15)        
        drop_items3.current(0)
        drop_items3.place(x = 240, y=370)
        return

    
        
    def Enter_Details(self):
        
        c_name = cust_name.get()
        c_age = cust_age.get()
        c_phone = cust_phone.get()
        #result = cafedb.login(admin)
        return

    def viewStats(self):
        global statistics
        #global user
        #global passw
        #self.user=StringVar()
        #self.passw=StringVar()
        statistics = Toplevel(self.root)

        statistics.title("Data Analytics")
        statistics.geometry("650x600")#Width*ht
        statistics.resizable(False, False)
        statistics.config(background='#F6E4C6')
        return


if __name__== "__main__":
    root=Tk()
    obj=Cafe(root)
    root.mainloop()