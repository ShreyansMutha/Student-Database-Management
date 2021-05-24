import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

mainwindow = tk.Tk()
mainwindow.title('Managment')
mainwindow.resizable(width=True, height=True)
mainwindow.geometry('{}x{}'.format(1350, 800))

bg_color = "lightgray"
TABLE_NAME = "management_table"
STUDENT_ID = "student_id"
STUDENT_NAME = "student_name"
STUDENT_COLLEGE = "student_college"
STUDENT_ADDRESS = "student_address"
STUDENT_PHONE = "student_phone"
connection = sqlite3.connect('management.db')
connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + STUDENT_ID +
                   " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                   STUDENT_NAME + " TEXT, " + STUDENT_COLLEGE + " TEXT, " +
                   STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE + " INTEGER);")
qlabel = tk.Label(mainwindow, text='Student Managment System',bg="lightgray", width=60)
qlabel.config(font=("times new roman", 30,"bold"))
qlabel.grid(row=0, columnspan=8, pady=(30, 0))
idlabel = tk.Label(mainwindow, text="ID", width=40, anchor='w',
                   font=("Sylfaen", 12)).grid(row=1, column=0, padx=(10, 0), pady=(30, 0))
nameLabel = tk.Label(mainwindow, text="NAME", width=40, anchor='w',
                     font=("Sylfaen", 12)).grid(row=2, column=0, padx=(10, 0), pady=(30, 0))
collegeLabel = tk.Label(mainwindow, text="COLLEGE", width=40, anchor='w',
                        font=("Sylfaen", 12)).grid(row=3, column=0, padx=(10, 0), pady=(30, 0))
phoneLabel = tk.Label(mainwindow, text="PHONE", width=40, anchor='w',
                      font=("Sylfaen", 12)).grid(row=4, column=0, padx=(10, 0), pady=(30, 0))
addressLabel = tk.Label(mainwindow, text="ADDRESS", width=40, anchor='w',
                        font=("Sylfaen", 12)).grid(row=5, column=0, padx=(10, 0), pady=(30, 0))

idEntry = tk.Entry(mainwindow, width=40)
nameEntry = tk.Entry(mainwindow, width=40)
collegeEntry = tk.Entry(mainwindow, width=40)
phoneEntry = tk.Entry(mainwindow, width=40)
addressEntry = tk.Entry(mainwindow, width=40)

idEntry.grid(row=1, column=2, padx=(10, 0), pady=(30, 0))
nameEntry.grid(row=2, column=2, padx=(10, 0), pady=(30, 0))
collegeEntry.grid(row=3, column=2, padx=(10, 0), pady=(30, 0))
phoneEntry.grid(row=4, column=2, padx=(10, 0), pady=(30, 0))
addressEntry.grid(row=5, column=2, padx=(10, 0), pady=(30, 0))
Button(mainwindow,bg=bg_color,bd=5,relief=GROOVE,font=("times new roman", 15,"bold"), text="INSERT", command=lambda: takeNameInput()).grid(row=6, column=0, padx=(10, 0), pady=(30, 0))
Button(mainwindow,bg=bg_color,bd=5,relief=GROOVE,font=("times new roman", 15,"bold"), text="UPDATE", command=lambda: UPDATE()).grid(row=6, column=1, padx=(10, 0), pady=(30, 0))
Button(mainwindow,bg=bg_color,bd=5,relief=GROOVE,font=("times new roman", 15,"bold"), text="SHOW", command=lambda: SHOW()).grid(row=6, column=2, padx=(10, 0), pady=(30, 0))


def takeNameInput():
    global idEntry, nameEntry, collegeEntry, phoneEntry, addressEntry
    # global username, collegeName, phone, address
    global list
    global TABLE_NAME, STUDENT_NAME, STUDENT_COLLEGE, STUDENT_ADDRESS, STUDENT_PHONE
    iidname = int(idEntry.get())
    idEntry.delete(0, tk.END)
    username = nameEntry.get()
    nameEntry.delete(0, tk.END)  # To clear fields after insertion
    collegeName = collegeEntry.get()
    collegeEntry.delete(0, tk.END)
    phone = int(phoneEntry.get())
    phoneEntry.delete(0, tk.END)
    address = addressEntry.get()
    addressEntry.delete(0, tk.END)

    connection.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_ID + ", " + STUDENT_NAME + ", " +
                       STUDENT_COLLEGE + ", " + STUDENT_ADDRESS + ", " +
                       STUDENT_PHONE + " ) VALUES (" + str(iidname) + ", '"
                       + username + "', '" + collegeName + "', '" +
                       address + "', " + str(phone) + " ); ")
    connection.commit()
    messagebox.showinfo("Success", "Data Saved Successfully.")


def DELETE():
    global id, miniwindow
    miniwindow = tk.Tk()
    miniwindow.title('DELETE DATA')
    miniwindow.geometry('{}x{}'.format(400, 300))
    hea = tk.Label(miniwindow, text='Enter the ID of student').grid(row=0, column=0, padx=50, pady=80)
    id = tk.Entry(miniwindow)
    id.grid(row=0, column=1)
    but = tk.Button(miniwindow,bg=bg_color,bd=5,relief=GROOVE,font=("times new roman", 10,"bold"), text='Delete', command=lambda: sdelete())
    but.grid(row=1, column=1)
    miniwindow.mainloop()


def sdelete():
    id1 = int(id.get())
    query = connection.execute("SELECT * FROM " + TABLE_NAME + " WHERE " + STUDENT_ID + " = {}".format(id1))
    # query=connection.fetchone()[0]
    if query:
        connection.execute("DELETE FROM " + TABLE_NAME + " WHERE " + STUDENT_ID + " =  {}".format(id1))
        connection.commit()
        miniwindow.destroy()

        messagebox.showinfo('DONE', "Data has been deleted")
    else:
        messagebox.showerror("ERROR", "Sorry ,No student with this id exist.")


def UPDATE():
    iidname = int(idEntry.get())
    idEntry.delete(0, tk.END)
    username = nameEntry.get()
    nameEntry.delete(0, tk.END)  # To clear fields after insertion
    collegeName = collegeEntry.get()
    collegeEntry.delete(0, tk.END)
    phone = int(phoneEntry.get())
    phoneEntry.delete(0, tk.END)
    address = addressEntry.get()
    addressEntry.delete(0, tk.END)

    connection.execute(
        "UPDATE " + TABLE_NAME + " SET " + STUDENT_NAME + " = " + "'" + username + "' ," + STUDENT_COLLEGE + " =" + "'" + collegeName + "' ,"
        + STUDENT_PHONE + " =" + str(
            phone) + " ," + STUDENT_ADDRESS + " =" + "'" + address + "' WHERE " + STUDENT_ID + " = {}".format(iidname))
    connection.commit()
    messagebox.showinfo('UPDATED', 'Information updated')


def SHOW():
    secondWindow = tk.Tk()
    secondWindow.title("Display results")
    secondWindow.resizable(width=False, height=False)
    secondWindow.geometry('{}x{}'.format(1350, 500))
    qlabel = tk.Label(secondWindow, text='Student Information', width=52, bg='light grey')
    qlabel.config(font=("Sylfaen", 30))
    qlabel.pack()

    tree = ttk.Treeview(secondWindow)  # treeview is used to print and allowing browsing through hierarchy of items.
    tree["columns"] = ("one", "two", "three", "four", "five")

    tree.heading("one", text="Student ID")
    tree.heading("two", text="Student Name")
    tree.heading("three", text="College Name")
    tree.heading("four", text="Address")
    tree.heading("five", text="Phone no")

    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
    i = 0

    for row in cursor:
        tree.insert('', i, text="Student " + str(i + 1),
                    values=(row[0], row[1], row[2],
                            row[3], row[4]))
        i = i + 1

    tree.pack()

    Button(secondWindow,bg=bg_color,bd=5,relief=GROOVE,font=("times new roman", 12,"bold"), text="DELETE", command=lambda: DELETE()).pack(pady=10)
    secondWindow.mainloop()


mainwindow.mainloop()
