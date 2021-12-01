import tkinter as tk
from tkinter import ttk
import time
import pyttsx3
import smtplib
import random
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk,Image
import webbrowser
#====================================================================
#---------main window configuration start----------------------------
#====================================================================
root=tk.Tk()
root.geometry('700x500')
root.title("Bus Enquiry System (BES)")
#root.iconbitmap('C:/Users/Rahu/Desktop/project images/aa.png')
root.resizable(0,0)
#====================================================================
#---------main window configuration closed---------------------------
#====================================================================

bg_image=ImageTk.PhotoImage(Image.open("C:/users/Dell/Downloads/Bus.png"))
bg_image2=ImageTk.PhotoImage(Image.open("C:/users/Dell/Downloads/blur bus.png"))
background_image=ImageTk.PhotoImage(Image.open("C:/Users/Dell/Downloads/india2.jpg"))


#=======================================================================================================================
#----------------------------------------------Group Details is started-------------------------------------------------
#=======================================================================================================================
def group_details():
    def groupdetail():
        new_window = tk.Toplevel(root)
        new_window.title("Group Members")
        new_window.geometry("350x250")
        new_window.resizable(0,0) 

        for_speak("Name of Group members")

        label=tk.LabelFrame(new_window , text="Our Group Member" ,font="timesnewroman 20 bold underline " , foreground="red" , bg="black" , height=350,width=350)
        label.place(x=0,y=0)

        def group_code():
            for_speak("M P T E 10")

        group_name_label = tk.Button(label , text="MPTE10" , font="timesnewroman 10 bold" , relief="flat" , bd=0 ,foreground="white" , background="black" , command=group_code)
        group_name_label.place(x=13,y=40)

        pointing_label = tk.Label(label , text="=======>" , font="timesnewroman 10 bold" , relief="flat" , bd=0 ,foreground="white" , background="black")
        pointing_label.place(x=70,y=40)

        def pooja():
            for_speak("pooja mahajan")

        name_label_pooja = tk.Button(label , text="4) Pooja Mahajan." , font="timesnewroman 10 bold" , relief="flat" , bd=0 ,foreground="white" , background="black" , command=pooja)
        name_label_pooja.place(x=150,y=115)

        def jagruti():
            for_speak("jaagruti chaudhari")

        name_label_jagruti = tk.Button(label , text="5) Jagruti Chaudhari." , font="timesnewroman 10 bold" , relief="flat" , bd=0 ,foreground="white" , background="black" , command=jagruti)
        name_label_jagruti.place(x=150,y=140)

        def saurav():
            for_speak("sau rav ranjan")

        name_label_saurav = tk.Button(label , text="2) Saurav Ranjan." , font="timesnewroman 10 bold" , relief="flat" , bd=0 ,foreground="white" , background="black" , command=saurav)
        name_label_saurav.place(x=150,y=65)

        def rahul():
            for_speak("raahul pa til")

        name_label_rahul = tk.Button(label , text="1) Rahul Patil." , font="timesnewroman 10 bold" , relief="flat" , bd=0 ,foreground="white" , background="black" , command=rahul)
        name_label_rahul.place(x=150,y=40)

        def vinay():
            for_speak("vinay thomb re")

        name_label_vinay = tk.Button(label , text="3) Vinay Thombare." , font="timesnewroman 10 bold" , relief="flat" , bd=0 ,foreground="white" , background="black" , command=vinay)
        name_label_vinay.place(x=150,y=90)

    button=tk.Button(label , text="Group Details" ,font="Calibri 11 underline bold" , foreground="black",cursor="hand2" , background="#FFEBCD" ,activebackground="yellow",activeforeground='black',relief="flat",bd=0,command=groupdetail)
    button.place(x=585,y=450)

#=======================================================================================================================
#----------------------------------------------Group Details is Ended---------------------------------------------------
#=======================================================================================================================


def clock():                                   #Common clock with live timing
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    am_or_pm = time.strftime("%p")

    def live_time():
        for_speak("This is live time")

    live_time= tk.Button(root, text="" ,font="timesnewroman 13 bold underline" , fg="white" , bg="black",command=live_time ,cursor="hand2")
    live_time.place(x=570,y=10)

    live_time.config(text=hour + ":" + minute + ":" + second + " "+ am_or_pm)
    live_time.after(1000 , clock)

speak=pyttsx3.init()
def for_speak(str):
    speak.setProperty("rate",150)
    speak.setProperty("volume",1)
    voices=speak.getProperty('voices')  #get present voice 
    speak.setProperty('voice', voices[1].id)  #set voice
    speak.say(str)
    speak.runAndWait()



for_speak("welcoe to Bus Enquiry system")


#=======================================================================================================================
#----------------------------------------------Admin section is started----------------------------------------------------
#=======================================================================================================================

label=tk.Label(root,image=bg_image)
label.place(x=0,y=0)
main_frame=tk.Label(label , text="    WELCOME TO BUS ENQUIRY SYSTEM       " ,font=" Georgia 23 bold underline" ,background="#800000" ,fg="white")
main_frame.place(x=0,y=45)
clock()

def admin():
    for_speak("admin section")
    admin_label=tk.Label(root, image=bg_image)
    admin_label.place(x=0,y=0)

#------------------------------------------------------------------------------------------------------------------------
#=========================================Sign Up section started========================================================
#------------------------------------------------------------------------------------------------------------------------
    def sign_up():
        
        for_speak("create account")




        window = tk.Toplevel(root)
        window.geometry("400x250")
        window.title("Sign-up")

        Signup_frame = tk.Frame(window , bg="black" ,height=500 , width=500)
        Signup_frame.place(x=0 , y=0)

        sign_up_email_label = tk.Label(Signup_frame , text="E-mail" , width=13)
        sign_up_email_label.place(x=40 ,y=50)

        sign_up_password_label = tk.Label(Signup_frame , text="Password" , width=13)
        sign_up_password_label.place(x=40 ,y=80)

        sign_up_mobile_number_label = tk.Label(Signup_frame , text="Mobile number" , width=13)
        sign_up_mobile_number_label.place(x=40 ,y=110)
        
        otp_label = tk.Label(Signup_frame ,text="Enter OTP here" , width=13)
        otp_label.place(x=40,y=140)

        email_entry = tk.StringVar()
        sign_up_email_entry = tk.Entry(Signup_frame , textvariable=email_entry,width=29)
        sign_up_email_entry.place(x=190 , y=50)

        password_enrty = tk.StringVar()
        sign_up_password_entry = tk.Entry(Signup_frame , textvariable=password_enrty,width=29)
        sign_up_password_entry.place(x=190 , y=80)

        mobile_number_entry = tk.StringVar()
        sign_up_mobile_number_entry = tk.Entry(Signup_frame , textvariable=mobile_number_entry,width=29)
        sign_up_mobile_number_entry.place(x=190, y=110)
        
        
        otp_entry = tk.StringVar()
        otp_entry = tk.Entry(Signup_frame ,textvariable=otp_entry,width=16)
        otp_entry.place(x=190,y=140)

        send_otp = random.randint(1000,9999)    
        def getotp():
            server=smtplib.SMTP("smtp.gmail.com" , 587)
            server.starttls()
            server.login('rahulgpatil29@gmail.com',password='nptumalrssgnhoaz')
            msg = f"Hello Dear , \nYour OTP is {send_otp} .\nThank you for using our system . Have a good day.\n\n\n\n"
            mail=email_entry.get()
            server.sendmail("rahulgpatil29@gmail.com" , mail , msg)
            server.quit()

        get_otp_button = tk.Button(Signup_frame , text="Get OTP" ,background="white" , foreground="black" , activebackground="yellow" , activeforeground="black",command=getotp)
        get_otp_button.place(x=315,y=140)

        #new user
        def new_user():
            #restriction needed 
            
            if email_entry.get()=="" :
                messagebox.showerror("Error" , "All Fields Are Required")
            elif password_enrty.get()=="" :
                messagebox.showerror("Error" , "All Fields Are Required")
            elif mobile_number_entry.get()=="":
                messagebox.showerror("Error" , "All Fields Are Required")
            elif otp_entry.get()=="" :
                messagebox.showerror("Error" , "All Fields Are Required")

            else :
                mydb=mysql.connector.connect(host="localhost" , user="root" , password="" , database="bes_add_record")
                mycursor = mydb.cursor()
                sql="INSERT INTO new_user (email , password , number) VALUES (%s,%s,%s)"
                val=(email_entry.get() , password_enrty.get() , mobile_number_entry.get())
                mycursor.execute(sql,val)
                mydb.commit()
                mydb.close()
                window.destroy()
                messagebox.showinfo("Success" , "Now Try To Login")

        button = tk.Button(Signup_frame , text = "Sign Up" ,command=new_user)
        button.place(x=140 , y=190)

        def error1():    

            messagebox.showerror("Error" , "Wrong OTP Please Try Again.")

        error1button = tk.Button(Signup_frame , text="         "  ,background="black" , activebackground="black"  ,relief="flat"  ,command=error1)
        error1button.place(x=190,y=195)




    sign_up = tk.Button(admin_label , text="Create Account",font="timesnewroman 10 bold" ,background="black" ,foreground="white" ,activebackground="yellow" ,activeforeground="black" ,cursor="hand2" ,relief="raised" ,bd=4 ,command=sign_up)
    sign_up.place(x=345 , y=300)


#------------------------------------------------------------------------------------------------------------------------
#=========================================Sign Up section started========================================================
#------------------------------------------------------------------------------------------------------------------------



    #======================================Admin login=========================================================
    login_label = tk.Label(admin_label,text="Login Here" ,background="black" ,foreground="white" ,font="timesnewroman 20 bold underline" ,relief="groove" ,bd=8)
    login_label.place(x=270,y=10)

    def back_button():
        admin_label.destroy()

    back_button = tk.Button(admin_label , text="<--BACK",fg="white" ,bg="black" , activebackground="red" ,activeforeground="black",cursor="hand2",relief="raised",bd=5,command = back_button)
    back_button.place(x=20 , y=50)


    email_label = tk.Label(admin_label ,text="E-mail" ,background="black" ,foreground="white" ,font="timesnewroman 12 bold" ,relief="groove" ,bd=3,width=10 ,height=1)
    email_label.place(x=160,y=150)

    password_label = tk.Label(admin_label ,text="Password" ,background="black" ,foreground="white" ,font="timesnewroman 12 bold" ,relief="groove" ,bd=3,width=10 ,height=1)
    password_label.place(x=160,y=200)

    email_entry_login = tk.StringVar()
    email_entry = tk.Entry(admin_label ,font="timesnewroman 13" ,relief="groove" ,bd=3 ,textvariable=email_entry_login ,width=27 )
    email_entry.place(x=300,y=150)

    password_entry_login = tk.StringVar()
    password_entry = tk.Entry(admin_label ,font="timesnewroman 13" ,relief="groove" ,bd=3 ,textvariable=password_entry_login , show="*" ,width=27)
    password_entry.place(x=300,y=200)


    def admin_login_button():

        mydb=mysql.connector.connect(host="localhost" , user="root" , password="" , database="bes_add_record")
        mycursor = mydb.cursor()
        username = email_entry_login.get()
        pwd = password_entry_login.get()
        
        query = "SELECT * FROM new_user WHERE email = '" + username + "' AND password = '" + pwd + "'"  
        
        mycursor.execute(query)  
        mycursor.fetchall()
        mycursor.rowcount 
        #print(rowcount)
        if mycursor.rowcount == 1: 
            for_speak("login successful")
            

            bg_label=tk.Label(root,image=bg_image2)
            bg_label.place(x=0,y=0)


            def back():
                bg_label.destroy()
                admin_label.destroy()

            back = tk.Button(bg_label , text = '<--BACK' , font='timesnewroman 10' , command=back ,cursor="hand2")
            back.place(x=5,y=5)

            def create():  
                for_speak("create section")
                label=tk.LabelFrame(bg_label , text="CREATE New Entry Here" ,font="timesnewroman 15 bold underline", height=480 ,width=525 , background="#3399ff")        
                label.place(x=160,y=5)

                bus_number_label = tk.Label(label ,text="Bus Number",font="timesnewroman 10 bold",background="black",foreground="white",relief="groove",bd=3 , width=19)
                bus_number_label.place(x=90,y=15)

                bus_route_label = tk.Label(label,text="Enter Bus Route Here",font="timesnewroman 10 bold",background="black",foreground="white",relief="groove",bd=3, width=19)
                bus_route_label.place(x=90,y=50)

                bus_route_label_from = tk.Label(label,text="From -->",font="timesnewroman 10 bold",background="black",foreground="white",relief="groove",bd=3,width=19)
                bus_route_label_from.place(x=90,y=85)

                bus_route_label_to = tk.Label(label,text="To -->",font="timesnewroman 10 bold",background="black",foreground="white",relief="groove",bd=3,width=19)
                bus_route_label_to.place(x=90,y=120)

                bus_arrivaltime_label = tk.Label(label,text="Arrival time",font="timesnewroman 10 bold",background="black",foreground="white",relief="groove",bd=3,width=19,height=1)
                bus_arrivaltime_label.place(x=90,y=161)

                bus_departuretime_label = tk.Label(label,text="Departure time",font="timesnewroman 10 bold",background="black",foreground="white",relief="groove",bd=3,width=19,height=1)
                bus_departuretime_label.place(x=90,y=196)

                bus_id_label = tk.Label(label,text="Enter Unique ID",font="timesnewroman 10 bold",background="black",foreground="white",relief="groove",bd=3,width=19,height=1)
                bus_id_label.place(x=90,y=241)




                ##Entries for above labels--->>>>

                bus_number_entry = tk.StringVar()
                bus_number_entry = tk.Entry(label ,font="timesnewroman 10 ",relief="raised",bd=3,textvariable=bus_number_entry)
                bus_number_entry.place(x=300, y=15)

                bus_route_entry_from = tk.StringVar()
                bus_route_entry_from = tk.Entry(label ,font="timesnewroman 10 ",relief="raised",bd=3,textvariable=bus_route_entry_from)
                bus_route_entry_from.place(x=300, y=85)

                bus_route_entry_to = tk.StringVar()
                bus_route_entry_to = tk.Entry(label ,font="timesnewroman 10 ",relief="raised",bd=3,textvariable=bus_route_entry_to)
                bus_route_entry_to.place(x=300, y=120)

                bus_arrivaltime_entry=ttk.Combobox(label, values=["12 AM" ,"1 AM" ,"2 AM" ,"3 AM" ,"4 AM" ,"5 AM" ,"6 AM" ,"7 AM" ,"8 AM" ,"9 AM" ,"10 AM ","11 AM" ,"12 PM" ,"1 PM" ,"2 PM" ,"3 PM" ,"4 PM" ,"5 PM" ,"6 PM" ,"7 PM" ,"8 PM" ,"9 PM" ,"10 PM" ,"11 PM"])
                bus_arrivaltime_entry.place(x=303, y=160)

                bus_departuretime_entry=ttk.Combobox(label, values=["12 AM" ,"1 AM" ,"2 AM" ,"3 AM" ,"4 AM" ,"5 AM" ,"6 AM" ,"7 AM" ,"8 AM" ,"9 AM" ,"10 AM ","11 AM" ,"12 PM" ,"1 PM" ,"2 PM" ,"3 PM" ,"4 PM" ,"5 PM" ,"6 PM" ,"7 PM" ,"8 PM" ,"9 PM" ,"10 PM" ,"11 PM"])
                bus_departuretime_entry.place(x=303, y=195)

                bus_uniqueid = tk.StringVar()
                bus_id_entry = tk.Entry(label ,font="timesnewroman 10 ",relief="raised",bd=3,textvariable=bus_uniqueid)
                bus_id_entry.place(x=300, y=241)



                def add_record():
                    if bus_number_entry.get()=="":
                        messagebox.showerror("Error" , "All Fields Are Required")
                    elif bus_route_entry_from.get()=="":
                        messagebox.showerror("Error" , "All Fields Are Required")
                    elif bus_route_entry_to.get()=="":
                        messagebox.showerror("Error" , "All Fields Are Required")
                    elif bus_arrivaltime_entry.get()=="--select--":
                        messagebox.showerror("Error" , "All Fields Are Required")
                    elif bus_departuretime_entry.get()=="--select--":
                        messagebox.showerror("Error" , "All Fields Are Required")
                    else:    
                        mydb=mysql.connector.connect(host="localhost" , user="root" , password="" , database="bes_add_record")
                        mycursor=mydb.cursor()
                        #mycursor.execute("CREATE TABLE buses (bus_number VARCHAR(255) , from VARCHAR(255) , to VARCHAR(255) , arrival_time VARCHAR(255) , departure_time VARCHAR(255))")
                        sql="INSERT INTO bus_records (bus_number , bus_route_from , bus_route_to , arrival_time , departure_time,bus_id) VALUES (%s,%s,%s,%s,%s,%s)"
                        val=(bus_number_entry.get() , bus_route_entry_from.get() , bus_route_entry_to.get() ,bus_arrivaltime_entry.get() ,bus_departuretime_entry.get(),bus_uniqueid.get())
                        mycursor.execute(sql,val)
                        mydb.commit()
                        mydb.close()

                        for_speak("please wait!!!")
                        messagebox.showinfo("congratulation" , "Your record is successfully added.")



                        bus_number_entry.delete(0,len(bus_number_entry.get()))
                        bus_route_entry_from.delete(0,len(bus_route_entry_from.get()))
                        bus_route_entry_to.delete(0,len(bus_route_entry_to.get()))
                        #arrival_times.delete(0,len(arrival_times.get()))
                        #departure_times.delete(0,len(departure_times.get()))

                add_record_button = tk.Button(label,
                                    text="Add record" ,
                                    command=add_record)
                add_record_button.place(x=400,y=350)

            def read():
                for_speak("read section")
                read_label=tk.LabelFrame(bg_label , text="READ Old Entries Here" ,font="timesnewroman 15 bold underline", height=480 ,width=525 , background="#cc66ff")        
                read_label.place(x=160,y=5)

                label = tk.Label(read_label , height=50, width=50 ,relief="groove" , bd=6 , bg="black")
                label.place(x=10,y=10)

                def read_error(ev):
                    messagebox.showerror("Error" , "In READ section you will only able to read the records ,\n If you want to edit information then go to other sections like UPDATE , DELETE.")


                tree_view = ttk.Treeview(label , columns=("Bus number" , "From" , "To" , "Arrival time" , "Departure time") , height=20)
                tree_view.pack(fill="both")

                tree_view.heading("Bus number" , text="Bus number")
                tree_view.heading("From" , text="From")
                tree_view.heading("To" , text="To")
                tree_view.heading("Arrival time" , text="Arrival time")
                tree_view.heading("Departure time" , text="Departure time")                                                

                tree_view["show"] = "headings"

                tree_view.column("Bus number" , width=99)
                tree_view.column("From" , width=99)
                tree_view.column("To" , width=99)
                tree_view.column("Arrival time" , width=99)
                tree_view.column("Departure time" , width=99)

                tree_view.bind("<ButtonRelease-1>" , read_error)

                #scrollbar
                hs=ttk.Scrollbar(label ,orient="vertical",command=tree_view.yview)
                #hs.pack(side="right",fill="y")
                hs.place(x=481,y=20,height=400)
                tree_view.configure(yscrollcommand=hs.set)


                mydb=mysql.connector.connect(host="localhost" , user="root" , password="" , database="bes_add_record")
                mycursor = mydb.cursor()

                mycursor.execute("select * from bus_records")
                rows=mycursor.fetchall()
                for i in rows:
                    tree_view.insert("" ,tk.END , values=i)

                mydb.commit()
                mydb.close()

            def update():  
                for_speak("update section")
                label=tk.LabelFrame(bg_label , text="UPDATE Old Record Here" ,font="timesnewroman 15 bold underline", height=480 ,width=525 , background="#33cc33")      
                label.place(x=160,y=5)

                label2 = tk.Label(label, height=50 , width=50, bg="black")
                label2.place(x=10,y=10)

                def next(ev):
                    cursor_row=tree_view.focus()
                    content=tree_view.item(cursor_row)
                    row=content['values']

                    new_update_window = tk.Toplevel(root)
                    new_update_window.geometry("525x480")
                    new_update_window.title("Update window")
                    new_update_window.resizable(0,0)

                    label=tk.LabelFrame(new_update_window , text="Update Your Records" ,font="timesnewroman 15 bold underline", height=480 ,width=525 , background="#3399ff")        
                    label.place(x=0,y=0)

                    bus_number_label = tk.Label(label ,text="Bus number",font="timesnewroman 10 bold",background="black",foreground="white",relief="groove",bd=3,width=19)
                    bus_number_label.place(x=90,y=15)

                    bus_route_label = tk.Label(label,text="Enter bus route here.",font="timesnewroman 10 bold",background="black",foreground="white",relief="groove",bd=3,width=19)
                    bus_route_label.place(x=90,y=50)

                    bus_route_label_from = tk.Label(label,text="From -->",font="timesnewroman 10 bold",background="black",foreground="white",relief="groove",bd=3,width=19)
                    bus_route_label_from.place(x=90,y=85)

                    bus_route_label_to = tk.Label(label,text="To -->",font="timesnewroman 10 bold",background="black",foreground="white",relief="groove",bd=3,width=19)
                    bus_route_label_to.place(x=90,y=120)

                    bus_arrivaltime_label = tk.Label(label,text="Arrival time",font="timesnewroman 10 bold",background="black",foreground="white",relief="groove",bd=3,width=19,height=1)
                    bus_arrivaltime_label.place(x=90,y=160)

                    bus_departuretime_label = tk.Label(label,text="Departure time",font="timesnewroman 10 bold",background="black",foreground="white",relief="groove",bd=3,width=19,height=1)
                    bus_departuretime_label.place(x=90,y=200)

                    bus_id_label = tk.Label(label,text="Enter Unique ID",font="timesnewroman 10 bold",background="black",foreground="white",relief="groove",bd=3,width=19,height=1)
                    bus_id_label.place(x=90,y=241)


                    ##Entries for above labels--->>>>

                    bus_number = tk.StringVar()
                    bus_number_entry = tk.Entry(label ,font="timesnewroman 10 ",relief="raised",bd=3,textvariable=bus_number)
                    bus_number_entry.place(x=300, y=15)

                    bus_route_from = tk.StringVar()
                    bus_route_entry_from = tk.Entry(label ,font="timesnewroman 10 ",relief="raised",bd=3,textvariable=bus_route_from)
                    bus_route_entry_from.place(x=300, y=85)

                    bus_route_to = tk.StringVar()
                    bus_route_entry_to = tk.Entry(label ,font="timesnewroman 10 ",relief="raised",bd=3,textvariable=bus_route_to)
                    bus_route_entry_to.place(x=300, y=120)

                    bus_arrivaltime_entry=ttk.Combobox(label, values=["12 AM" ,"1 AM" ,"2 AM" ,"3 AM" ,"4 AM" ,"5 AM" ,"6 AM" ,"7 AM" ,"8 AM" ,"9 AM" ,"10 AM ","11 AM" ,"12 PM" ,"1 PM" ,"2 PM" ,"3 PM" ,"4 PM" ,"5 PM" ,"6 PM" ,"7 PM" ,"8 PM" ,"9 PM" ,"10 PM" ,"11 PM"])
                    bus_arrivaltime_entry.place(x=303, y=160)

                    bus_departuretime_entry=ttk.Combobox(label, values=["12 AM" ,"1 AM" ,"2 AM" ,"3 AM" ,"4 AM" ,"5 AM" ,"6 AM" ,"7 AM" ,"8 AM" ,"9 AM" ,"10 AM ","11 AM" ,"12 PM" ,"1 PM" ,"2 PM" ,"3 PM" ,"4 PM" ,"5 PM" ,"6 PM" ,"7 PM" ,"8 PM" ,"9 PM" ,"10 PM" ,"11 PM"])
                    bus_departuretime_entry.place(x=303, y=195)

                    bus_uniqueid = tk.StringVar()
                    bus_id_entry = tk.Entry(label ,font="timesnewroman 10 ",relief="raised",bd=3,textvariable=bus_uniqueid)
                    bus_id_entry.place(x=300, y=241)



                    bus_number.set(row[0])
                    bus_route_from.set(row[1])
                    bus_route_to.set(row[2])
                    bus_arrivaltime_entry.set(row[3])
                    bus_departuretime_entry.set(row[4])
                    bus_uniqueid.set(row[5])
                    


                    def final_update():
                        if bus_number_entry.get() == "" :
                            messagebox.showerror("Error" , "All Fields Are Required")
                        elif bus_route_entry_from.get() == "" :
                            messagebox.showerror("Error" , "All Fields Are Required")
                        elif bus_route_entry_to.get() == "" :
                            messagebox.showerror("Error" , "All Fields Are Required")
                        elif bus_arrivaltime_entry.get() == "" :
                            messagebox.showerror("Error" , "All Fields Are Required")
                        elif bus_departuretime_entry.get() == "" :
                            messagebox.showerror("Error" , "All Fields Are Required")
                        else:
                            mydb=mysql.connector.connect(host="localhost" , user="root" , password="" , database="bes_add_record")
                            mycursor=mydb.cursor()
                            #sql="update bus_records set (bus_number , bus_route_from , bus_route_to , arrival_time , departure_time) VALUES (%s,%s,%s,%s,%s)"
                            #val=(bus_number_entry.get() , bus_route_entry_from.get() , bus_route_entry_to.get() ,arrival_times.get() ,departure_times.get())
                            Update="Update bus_records set bus_number='%s', bus_route_from='%s', bus_route_to='%s', arrival_time='%s', departure_time='%s' where bus_id='%s'  " %(bus_number_entry.get(),bus_route_entry_from.get() , bus_route_entry_to.get() ,bus_arrivaltime_entry.get() ,bus_departuretime_entry.get(),bus_uniqueid.get() )
                            #Update="Update bus_records set bus_route_from='%s', bus_route_to='%s', arrival_time='%s', departure_time='%s' where bus_number='%s' " %(bus_route_entry_from.get() , bus_route_entry_to.get() ,bus_arrivaltime_entry.get() ,bus_departuretime_entry.get(),bus_number_entry.get() )

                            mycursor.execute(Update)
                            mydb.commit()
                            mydb.close()


                            new_update_window.destroy()

                            messagebox.showinfo("Success", "Your Response Has Been Successfully Recorded ,\n Thanks Use It Again.")


                    final_update_button = tk.Button(new_update_window , text="Update" ,fg="white" , bg="black" , activebackground="crimson" ,activeforeground="white",cursor="hand2",relief="raised",bd=5,command = final_update)
                    final_update_button.place(x=400,y=400)



                tree_view = ttk.Treeview(label2 , columns=("Bus number" , "From" , "To" , "Arrival time" , "Departure time"),height=20)                  
                tree_view.heading("Bus number" , text = "Bus number")
                tree_view.heading("From" , text = "From")
                tree_view.heading("To" , text = "To")
                tree_view.heading("Arrival time" , text = "Arrival time")
                tree_view.heading("Departure time" , text = "Departure time")
                tree_view['show'] = "headings"

                tree_view.column("Bus number" , width=99)
                tree_view.column("From" , width=99)
                tree_view.column("To" , width=99)
                tree_view.column("Arrival time" , width=99)
                tree_view.column("Departure time" , width=99)  

                tree_view.bind("<ButtonRelease-1>",next)
                tree_view.pack(fill="both" )

                #scrollbar
                hs=ttk.Scrollbar(label2 ,orient="vertical",command=tree_view.yview)
                #hs.pack(side="right",fill="y")
                hs.place(x=481,y=20,height=400)
                tree_view.configure(yscrollcommand=hs.set)


                mydb = mysql.connector.connect(host="localhost" , user="root" , password="" , database="bes_add_record")
                mycursor = mydb.cursor()
                mycursor.execute("select * from bus_records")
                rows=mycursor.fetchall()          
                for i in rows:
                    tree_view.insert("",tk.END,values=i)
                mydb.commit()

            def delete():  

 
                for_speak("delete section")
                label=tk.LabelFrame(bg_label , text="DELETE Records Here" ,font="timesnewroman 15 bold underline", height=480 ,width=525 , background="#ff00ff")        
                label.place(x=160,y=5)

                label2 = tk.Label(label, height=50 , width=50, bg="black")
                label2.place(x=10,y=10)


                def del_data(ev):

                    cursor_row=tree_view.focus()
                    content=tree_view.item(cursor_row)
                    row=content['values']

                    new_delete_window = tk.Toplevel(root)
                    new_delete_window.geometry("525x480")
                    new_delete_window.title("Delete window")
                    new_delete_window.resizable(0,0)

                    label=tk.LabelFrame(new_delete_window , text="Delete your records permanantly" ,font="timesnewroman 15 bold underline", height=480 ,width=525 , background="#3399ff")        
                    label.place(x=0,y=0)

                    bus_number_label = tk.Label(label ,text="bus number",font="timesnewroman 10 bold",background="black",foreground="white",relief="groove",bd=3,width=19)
                    bus_number_label.place(x=90,y=15)

                    bus_route_label = tk.Label(label,text="Enter bus route here.",font="timesnewroman 10 bold",background="black",foreground="white",relief="groove",bd=3,width=19)
                    bus_route_label.place(x=90,y=50)

                    bus_route_label_from = tk.Label(label,text="From -->",font="timesnewroman 10 bold",background="black",foreground="white",relief="groove",bd=3,width=19)
                    bus_route_label_from.place(x=90,y=85)

                    bus_route_label_to = tk.Label(label,text="To -->",font="timesnewroman 10 bold",background="black",foreground="white",relief="groove",bd=3,width=19)
                    bus_route_label_to.place(x=90,y=120)

                    bus_arrivaltime_label = tk.Label(label,text="Arrival time",font="timesnewroman 10 bold",background="black",foreground="white",relief="groove",bd=3,width=19,height=1)
                    bus_arrivaltime_label.place(x=90,y=160)

                    bus_departuretime_label = tk.Label(label,text="Departure time",font="timesnewroman 10 bold",background="black",foreground="white",relief="groove",bd=3,width=19,height=1)
                    bus_departuretime_label.place(x=90,y=200)

                    ##Entries for above labels--->>>>

                    bus_number = tk.StringVar()
                    bus_number_entry = tk.Entry(label ,font="timesnewroman 10 ",relief="raised",bd=3,textvariable=bus_number,state="disable")
                    bus_number_entry.place(x=300, y=15)

                    bus_route_from = tk.StringVar()
                    bus_route_entry_from = tk.Entry(label ,font="timesnewroman 10 ",relief="raised",bd=3,textvariable=bus_route_from,state="disable")
                    bus_route_entry_from.place(x=300, y=85)

                    bus_route_to = tk.StringVar()
                    bus_route_entry_to = tk.Entry(label ,font="timesnewroman 10 ",relief="raised",bd=3,textvariable=bus_route_to,state="disable")
                    bus_route_entry_to.place(x=300, y=120)

                    bus_arrivaltime_entry=ttk.Combobox(label,state="disable", values=["12 AM" ,"1 AM" ,"2 AM" ,"3 AM" ,"4 AM" ,"5 AM" ,"6 AM" ,"7 AM" ,"8 AM" ,"9 AM" ,"10 AM ","11 AM" ,"12 PM" ,"1 PM" ,"2 PM" ,"3 PM" ,"4 PM" ,"5 PM" ,"6 PM" ,"7 PM" ,"8 PM" ,"9 PM" ,"10 PM" ,"11 PM"])
                    bus_arrivaltime_entry.place(x=303, y=160)

                    bus_departuretime_entry=ttk.Combobox(label, state="disable",values=["12 AM" ,"1 AM" ,"2 AM" ,"3 AM" ,"4 AM" ,"5 AM" ,"6 AM" ,"7 AM" ,"8 AM" ,"9 AM" ,"10 AM ","11 AM" ,"12 PM" ,"1 PM" ,"2 PM" ,"3 PM" ,"4 PM" ,"5 PM" ,"6 PM" ,"7 PM" ,"8 PM" ,"9 PM" ,"10 PM" ,"11 PM"])
                    bus_departuretime_entry.place(x=303, y=195)



                    bus_number.set(row[0])
                    bus_route_from.set(row[1])
                    bus_route_to.set(row[2])
                    bus_arrivaltime_entry.set(row[3])
                    bus_departuretime_entry.set(row[4])


                    def final_delete():
                        mydb=mysql.connector.connect(host="localhost" , user="root" , password="" , database="bes_add_record")
                        mycursor=mydb.cursor()
                        #sql="update bus_records set (bus_number , bus_route_from , bus_route_to , arrival_time , departure_time) VALUES (%s,%s,%s,%s,%s)"
                        #val=(bus_number_entry.get() , bus_route_entry_from.get() , bus_route_entry_to.get() ,arrival_times.get() ,departure_times.get())
                        remove="delete from bus_records where bus_number='%s'" %(bus_number_entry.get())

                        mycursor.execute(remove)
                        mydb.commit()
                        mydb.close()

                        messagebox.showinfo("Success" , "Your Record Has Been Permanently Deleted.")
                        new_delete_window.destroy()

                    final_update_button = tk.Button(new_delete_window , text="Delete" ,fg="white" , bg="black" , activebackground="red" ,activeforeground="black",cursor="hand2",relief="raised",bd=5,command = final_delete)
                    final_update_button.place(x=400,y=400)

                tree_view = ttk.Treeview(label2, columns=("Bus number" , "From" , "To", "Arrival time" ,"Departure time") , height=20)
                tree_view.heading("Bus number" , text="Bus number")
                tree_view.heading("From" , text="From")
                tree_view.heading("To" , text="To")
                tree_view.heading("Arrival time" , text="Arrival time")
                tree_view.heading("Departure time" , text="Departure time")
                tree_view['show']="headings"

                tree_view.column("Bus number" , width=99)
                tree_view.column("From" , width=99)
                tree_view.column("To" , width=99)
                tree_view.column("Arrival time" , width=99)
                tree_view.column("Departure time" , width=99)

                tree_view.bind("<ButtonRelease-1>",del_data)

                tree_view.pack(fill="both")

                                #scrollbar
                hs=ttk.Scrollbar(label2 ,orient="vertical",command=tree_view.yview)
                #hs.pack(side="right",fill="y")
                hs.place(x=481,y=20,height=400)
                tree_view.configure(yscrollcommand=hs.set)

                mydb=mysql.connector.connect(host="localhost" , user="root" , password="" , database="bes_add_record")
                mycursor=mydb.cursor()
                mycursor.execute("select * from bus_records")
                rows=mycursor.fetchall()
                for i in rows:
                    tree_view.insert("",tk.END,values=i)
                mydb.commit()


            #button for CRUD operations
            create_button= tk.Button(bg_label , text="CREATE" , width=15 ,command=create ,cursor="hand2")
            create_button.place(x=10,y=100)

            read_button= tk.Button(bg_label , text="READ" , width=15 , command=read , cursor="hand2")
            read_button.place(x=10,y=200)

            update_button= tk.Button(bg_label , text="UPDATE", width=15 , command=update ,cursor="hand2")
            update_button.place(x=10,y=300)

            delete_button= tk.Button(bg_label , text="DELETE", width=15 , command=delete,cursor="hand2")
            delete_button.place(x=10,y=400)
        
        else :

            messagebox.showerror('Error', "Login Failed\nInvalid Username or Password.\nTry again!!!")  
            for_speak("please try again.")

       
    submit_button = tk.Button(admin_label ,text="Log-in" ,font="timesnewroman 10 bold" ,background="black" ,foreground="white" ,activebackground="yellow" ,activeforeground="black" ,cursor="hand2" ,relief="raised" ,bd=4 ,command=admin_login_button)
    submit_button.place(x=260,y=300)




admin=tk.Button(label , text="Admin" ,font="timesnewroman 15 bold" ,foreground="white",cursor="hand2" ,background="black" ,activebackground="yellow",activeforeground='black', relief="sunken",bd=5 ,command=admin  ,width=7)
admin.place(x=300,y=150)

#=======================================================================================================================
#----------------------------------------------Admin section is over----------------------------------------------------
#=======================================================================================================================














#=======================================================================================================================
#----------------------------------------------User section is started--------------------------------------------------
#=======================================================================================================================


def search():
    
    for_speak("Check Available buses")
    search_frame = tk.Frame(root, height=490 , width=690 , background = "#ff6600")
    search_frame.place(x=5,y=5)

    clock()

    def back():
        search_frame.destroy()

    back_button = tk.Button(search_frame , text="<--BACK" , relief="sunken" , bd=2 ,cursor="hand2", activeforeground="white" , activebackground="black" , fg="black" , bg="white" , command=back)
    back_button.place(x=10 , y=10)

    from_label = tk.Label(search_frame ,text = "From" ,width=10 , relief="sunken" , bd=3)
    from_label.place(x=20 , y=50)

    to_label = tk.Label(search_frame ,text = "To" ,width=10 ,relief="sunken" , bd=3)
    to_label.place(x=20 , y=85)


    from_entry = tk.StringVar()
    from_entry = tk.Entry(search_frame ,font="timesnewroman 10" ,relief="raised" , bd=3 ,textvariable=from_entry)
    from_entry.place(x=200 , y=50)

    to_entry = tk.StringVar()
    to_entry = tk.Entry(search_frame ,font="timesnewroman 10" , relief="raised" , bd=3 , textvariable=to_entry)
    to_entry.place(x=200 , y=85)


    def search_bus_button():

        if from_entry.get()=="":
            messagebox.showerror("Error" , "All Fields Are Required")
        elif to_entry.get() == "":
            messagebox.showerror("Error" , "All Fields Are Required")
        else:
            search_bus_button_frame = tk.LabelFrame(search_frame , text="Available Buses" , font="timesnewroman 10 bold underline" , height=325 , width=680 , background="black" , fg="white" , relief="groove" , bd=3 )
            search_bus_button_frame.place(x=5 , y=160)
    
            for_speak("available buses is infront of you")
    
            label = tk.Label(search_bus_button_frame , width=50 , height=20 , relief="groove" , bd=5 ,bg="red")
            label.place(x=5,y=3)
    
            tree_view = ttk.Treeview(label , column=("Bus number" ,"From" , "To" , "Arrival time" , "Departure time") , height=13 )
            tree_view.pack(fill="both")
    
            tree_view.heading("Bus number" , text="Bus number")
            tree_view.heading("From" , text="From")
            tree_view.heading("To" , text="To")
            tree_view.heading("Arrival time" , text="Arrival time")
            tree_view.heading("Departure time" , text="Departure time")
    
            tree_view['show'] = "headings"
    
            tree_view.column("Bus number" , width=130)
            tree_view.column("From" , width=130)
            tree_view.column("To" , width=130)
            tree_view.column("Arrival time" , width=130)
            tree_view.column("Departure time" , width=130)
    
        
    
    
            mydb=mysql.connector.connect(host="localhost" , user="root" , password="" ,database="bes_add_record")
            mycursor=mydb.cursor()
            sql="select * from bus_records where bus_route_to='%s'"%(to_entry.get())


            mycursor.execute(sql)
            rows=mycursor.fetchall()
            
    
            for i in rows:          
                tree_view.insert("" , tk.END , values=i)
    
            mydb.commit()
            mydb.close() 

    search_bus_button = tk.Button(search_frame,text="Search Bus",relief="groove",bd=3,activebackground="yellow", activeforeground="black" ,cursor="hand2",command=search_bus_button)
    search_bus_button.place(x=150 , y=125)

    def details():

        if from_entry.get()=="":
            messagebox.showerror("Error" , "All Fields Are Required")
        elif to_entry.get() == "":
            messagebox.showerror("Error" , "All Fields Are Required")
        else:
            place_details=tk.Toplevel(root)
            place_details.geometry("550x450")
            place_details.title("Filter Place Details" )
            place_details.resizable(0,0)
            place_bg_label=tk.Label(place_details, image=background_image)
            place_bg_label.place(x=0,y=0)
            menu_label=tk.Label(place_bg_label,text="What You Want To See ?",font="Georgia 27  bold " ,background="#800000" ,foreground="white")
            menu_label.place(x=45,y=25)


            l2=tk.Label(place_bg_label , text="Just Click It Once" ,font='Georgia 25')
            l2.place(x=150,y=100)
            combobox=ttk.Combobox(place_bg_label, values=['Gardens','Temples','Restaurents','Hotels having OYO'], font='Arial 13 bold')
            combobox.place(x=180,y=160)
            combobox.current(0)

            def redirect():
                a=to_entry.get()
                b=combobox.get()
                c=f"{a}+{b}"
                webbrowser.open('http://www.google.com/search?q='+c)

            redirecting_button=tk.Button(place_bg_label, text="SEE" , width=6,font="timesnewroman 15 bold", command=redirect ,bg="black",foreground="white",bd=2,relief="groove",activebackground="yellow" , activeforeground="black")
            redirecting_button.place(x=250,y=230)

    best_place_button = tk.Button(search_frame , text="Place Details" , relief="groove" , bd=3 , activebackground="yellow" , activeforeground="black" ,command=details, cursor="hand2")
    best_place_button.place(x=300,y=125)

search=tk.Button(label,text="Search",font="timesnewroman 15 bold" ,foreground="white",cursor="hand2" , background="black" ,activebackground="yellow",activeforeground='black',relief="sunken", width=7 , bd=5,command=search)
search.place(x=300,y=210)


#=======================================================================================================================
#----------------------------------------------User section is over----------------------------------------------------
#=======================================================================================================================



group_details()

root.mainloop()
