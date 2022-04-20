import tkinter as tk
import sqlite3

window = tk.Tk()
window.title("Cardiopage")
window.minsize(1208, 532)

# Read the width and height from the text file and store them in a dictionary
with open('geometry.txt','r') as f:
     geometry = f.readlines()
# Initialise window properties dictionary
window_dict = {'title':'CONFIRMATION',
               'geometry': geometry} 
window.title(window_dict['title'])
window.geometry(window_dict['geometry'])


with open('user.txt','r') as f:
        USER_ID = f.readlines()[0]


def save_geometry():
    ''' Updates geometry.txt file to let screen size persist across windows '''
    with open('geometry.txt','w') as f:
        f.write(window.geometry())

def close_window():
    save_geometry()
    window.destroy()
window.protocol("WM_DELETE_WINDOW", close_window)


def delete_record():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    delete_query = f"DELETE FROM record WHERE id = {USER_ID}"
    cur.execute(delete_query)
    delete_query = f"DELETE FROM bmi WHERE id = {USER_ID}"
    cur.execute(delete_query)
    con.commit()
    window.destroy()

def Confirmation():
    Confirmation = tk.Frame(master=window)
    Confirmation.grid(row=0, column=0)
    Confirmation = tk.Button(master=Confirmation, text="Are you sure you want \n to delete your account?".upper(), font="Arial", fg="red", width=30, height=5, command=delete_record)
    Confirmation.pack(padx=10, pady=10)

def Back():
    Back = tk.Frame(master=window)
    Back.grid(row=2, column=0)
    Back = tk.Button(master=Back, text="Back", width=30, height=5, bg="yellow", fg="red", command=Go_back)
    Back.pack(padx=10, pady=10)

def Go_back():
    window.destroy()
    import Menu


Confirmation()
Back()
window.mainloop()
