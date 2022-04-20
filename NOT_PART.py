# ------------------------------------------------------------------
# Import Stuff here
# ------------------------------------------------------------------
# tk sets as an alias so you can type tk and it will act as tkinter
import time
import pandas as pd
import tkinter as tk
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime, timedelta
# import mysql connector to connect the mysql database to python
import mysql.connector
# ------------------------------------------------------------------


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="python_database"

)

class Form(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.initialize_interface()

    def initialize_interface(self):
        self.parent.title("Login")
        self.parent.geometry("300x100")
        global username  # our variables
        global password  # we use global for the other function to use it
        username = tkinter.StringVar()
        password = tkinter.StringVar()
        self.labelUser = tkinter.Label(self.parent, text="Username:")
        self.labelUser.place(x=25, y=25)
        self.entryUser = tkinter.Entry(self.parent, textvariable=username)
        self.entryUser.place(x=100, y=25)
        self.labelPass = tkinter.Label(self.parent, text="Password:")
        self.labelPass.place(x=25, y=50)
        self.entryPass = tkinter.Entry(self.parent, textvariable=password)
        self.entryPass.place(x=100, y=50)
        self.buttonLogin = tkinter.Button(self.parent, text="LOGIN", command=logs)
        self.buttonLogin.place(height=45, width=60, x=230, y=25)
def logs():
    mycursor = mydb.cursor()
    sql = "SELECT * FROM users WHERE BINARY username = '%s' AND BINARY password = '%s'" % (
    username.get(), password.get())
    mycursor.execute(sql)
    if mycursor.fetchone():
        print("Successfully")
    else:
        print("Invalid Credentials")
def main():
    root = tkinter.Tk()
    b = Form(root)
    b.mainloop()
if __name__ == "__main__":
    main()


# def database():
lb = pd.DataFrame({'Name': ['John', 'Mary', 'Ben'],
               'Age': ['14', '61', '17'],
               'Weight': [65, 45, 70],
               'Height': [178, 148, 165],
               '5km time': [40, 50, 25]})
# fivek_update = lb.sort_values(['5km time'], ascending=[True])
# print(fivek_update)

def new_entry():
    user_name = (input("Enter name: "))
    user_height = float(input("Enter height (cm): "))
    user_weight = float(input("Enter weight (kg): "))
    user_age = int(input("Enter your age: "))
    input("Press enter to start run")
    start_time = time.time()
    input("Press enter to finish run")
    stop_time = time.time()
    time_lapsed = stop_time - start_time
    new_row = {'Name': user_name, 'Age': user_age, 'Weight': user_weight, 'Height': user_height, '5km time': time_lapsed}
    lb_update = lb.append(new_row, ignore_index=True)
    print(lb_update)
    # return time_lapsed

def main_menu():
    choice = input("Press 1 for bmi calculator\nPress 2 for alarm stopwatch\nPress 3 for database:")
    if choice == "1":
        bmi_calculator()
    elif choice == "2":
        alarm_stopwatch()
    elif choice == "3":
        database()

def alarm_stopwatch():
    input("Press enter to start run")
    start_time = time.time()
    input("Press enter to finish run")
    stop_time = time.time()
    time_lapsed = stop_time - start_time
    print(time_lapsed)

def bmi_calculator():
    user_height = float(input("Enter height (cm): "))
    user_weight = float(input("Enter weight (kg): "))
    user_age = int(input("Enter your age: "))
    bmi = user_weight / (user_height / 100) ** 2
    print(bmi)

# main_menu()
new_entry()
