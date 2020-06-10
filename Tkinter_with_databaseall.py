from tkinter import *
from PIL import ImageTk, Image
import sqlite3
import tkinter.messagebox as MessageBox
from tkinter import ttk


root = Tk()
root.title('LOGIN TO PROCEED')
root.configure(background = "#EEEEEE")
root.geometry("370x200")

#Creating a Database:
conn = sqlite3.connect("student_Cgpa.db")
c=conn.cursor()

#Create Table
'''
c.execute(""" CREATE TABLE student_Cgpa (
     name text,
     branch text,
     RegistrationId integer,
     Subject1,
     Subject2,
     Subject3 
     )""")
'''

def cgpacalc():
    percentage = ((int(marks_box1.get()) + int(marks_box2.get()) + int(marks_box3.get()))/300)* 100
    cgpa_output= round((percentage + 5)/10,2)
    my_label3 = Label(gui3, text="Your CGPA is "+ str(cgpa_output)).place(height=25, x=116, y=300)

def gradecalc():
    percentage = ((int(marks_box1.get()) + int(marks_box2.get()) + int(marks_box3.get())) / 300) * 100
    cgpa_output = (percentage + 5) / 10
    grade_output = ""

    if cgpa_output>9 and cgpa_output<=10 :
        grade_output = 'O'
    elif cgpa_output>8 and cgpa_output<=9 :
        grade_output = 'E'
    elif cgpa_output>7 and cgpa_output<=8 :
        grade_output = 'A'
    elif cgpa_output>6 and cgpa_output<=7 :
        grade_output = 'B'
    elif cgpa_output>5 and cgpa_output<=6 :
        grade_output = 'C'
    elif cgpa_output>4 and cgpa_output<=5 :
        grade_output = 'D'
    else :
        grade_output = 'FAIL'

    my_label4 = Label(gui3, text="Your GRADE is " + grade_output).place(height=25, x=117, y=325)


def new_window():
    gui2.destroy()
    root.destroy()
    gui3.destroy()


def closeall():
    root.quit()

def submit_marks():
    conn = sqlite3.connect("student_Cgpa.db")
    c = conn.cursor()

    # Update The Table
    c.execute(""" UPDATE student_Cgpa SET
        Subject1 = :marks1,
        Subject2 = :marks2,
        Subject3 = :marks3
        
        WHERE oid=:oid""",
           {
             'marks1' : marks_box1.get(),
             'marks2' : marks_box2.get(),
             'marks3' : marks_box3.get(),

             'oid' : rowid
           })
    conn.commit()
    conn.close()

    # Opening GUI3
    global gui3
    gui3 = Tk()
    gui3.title('CGPA-GRADE CAlCULATOR')
    gui3.geometry("320x370")

    # Creating 4 Buttons in GUI3:
    my_label2 = Label(gui3, text="What to do next ?").place(height=55, x=117, y=35)

    cgpacalc_btn = ttk.Button(gui3, text="CGPA", command=cgpacalc)
    cgpacalc_btn.place(height=40, width=120, x=35, y=100)

    gradecalc_btn = ttk.Button(gui3, text="GRADE", command=gradecalc)
    gradecalc_btn.place(height=40, width=120, x=165, y=100)

    new_window_btn = ttk.Button(gui3, text="NEW WINDOW", command=new_window)
    new_window_btn.place(height=40, width=120, x=35, y=200)

    closeall_btn = ttk.Button(gui3, text="CLOSE", command=closeall)
    closeall_btn.place(height=40, width=120, x=165, y=200)


s = "Enter Marks Here"
def onclick1():
    global marks_box1
    marks_box1 = Entry(gui2, width=30)
    marks_box1.grid(row=3, column=2, padx=10, pady=10)
    marks_box1.insert(0,s)
def onclick2():
    global marks_box2
    marks_box2 = Entry(gui2, width=30)
    marks_box2.grid(row=5, column=2, padx=10, pady=10)
    marks_box2.insert(0, s)
def onclick3():
    global marks_box3
    marks_box3 = Entry(gui2, width=30)
    marks_box3.grid(row=7, column=2, padx=10, pady=10)
    marks_box3.insert(0, s)
def insertion():
    conn = sqlite3.connect("student_Cgpa.db")
    c = conn.cursor()

    #Insert into Table
    c.execute("INSERT INTO student_Cgpa VALUES (:name,:branch,:RegistrationId,:Subject1,:Subject2,:Subject3)",(
        {
            'name': name_gui1.get(),
            'branch': branch_gui1.get(),
            'RegistrationId' : regId_gui1.get(),
            'Subject1' : None,
            'Subject2': None,
            'Subject3': None

        }))


    global rowid
    rowid = c.lastrowid
    print(rowid)
    conn.commit()
    conn.close()

    #Clear the text boxes
    name_gui1.delete(0, END)
    branch_gui1.delete(0, END)
    regId_gui1.delete(0, END)

    global gui2
    gui2 = Tk()
    gui2.title('STUDENT SUBJECT-WISE MARKS')
    gui2.geometry("670x270")

    my_label=Label(gui2,text="Click On The Subject To Fill The Marks Field!").grid(row=0,column=0,columnspan=3)

    my_label1 = Label(gui2, text="                                  ").grid(row=1, column=0, columnspan=3)

    subject1_btn = ttk.Button(gui2, text="ANALOG ELECTRONICS", command=onclick1)
    subject1_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

    subject2_btn = ttk.Button(gui2, text="DIGITAL ELECTRONICS", command=onclick2)
    subject2_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=140)

    subject3_btn = ttk.Button(gui2, text="SIGNAL PROCESSING", command=onclick3)
    subject3_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=12, ipadx=145)

    submit_marks_btn = ttk.Button(gui2, text="SUBMIT", command=submit_marks)
    submit_marks_btn.place(height=35, width=100, x=325, y=180)


def submit():

    user_name = username_box.get()
    pass_word = password_box.get()

    if (user_name =="" or pass_word==""):
        MessageBox.showerror("Status","ERROR ! INVALID INPUT")
    else:
        global gui1
        gui1=Tk()
        gui1.title('STUDENT DETAILS')
        gui1.geometry("370x200")

        global name_gui1
        global branch_gui1
        global regId_gui1

        #Create Text Boxes:
        name_gui1=Entry(gui1, width =30)
        name_gui1.grid(row=0, column=1, padx=20, pady=(60, 0))
        branch_gui1 = Entry(gui1, width=30)
        branch_gui1.grid(row=1, column=1, padx=20)
        regId_gui1 = Entry(gui1, width=30)
        regId_gui1.grid(row=2, column=1, padx=20)


        # Create Textbox labels :
        name_gui1_label = Label(gui1,text = "NAME :                     ")
        name_gui1_label.grid(row=0, column=0, padx=20, pady=(60, 0))
        branch_gui1_label = Label(gui1, text="BRANCH :                ")
        branch_gui1_label.grid(row=1, column=0)
        regId_gui1_label = Label(gui1, text="REGISTRATION ID :")
        regId_gui1_label.grid(row=2, column=0)

        # Creating another submit button for GUI1:
        submit_btn = ttk.Button(gui1, text="SUBMIT", command=insertion)
        submit_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=137)





#Create Box for Username & Password
username_box = Entry(root, width =30)
username_box.grid(row = 0, column = 1, padx=20, pady=(60,0))

password_box = Entry(root, width =30)
password_box.grid(row = 1, column = 1, padx=20)


# Create Label for Username & Password
username_label=Label(root,text="USERNAME :")
username_label.grid(row=0,column=0,pady=(60,0))
password_label=Label(root,text="PASSWORD :")
password_label.grid(row=1,column=0)


#Creating a submit button :
submit_btn=ttk.Button(root, text= "SUBMIT", command = submit)
submit_btn.grid(row=4,column=0, columnspan=2, pady=10, padx=10, ipadx = 137)

conn.commit()
conn.close()

root.mainloop()
