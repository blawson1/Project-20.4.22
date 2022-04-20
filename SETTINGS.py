import tkinter as tk
window = tk.Tk()
window.title("Cardiopage")
window.minsize(1208, 532)

# Read the width and height from the text file and store them in a dictionary
with open('geometry.txt','r') as f:
     geometry = f.readlines()
# Initialise window properties dictionary
window_dict = {'title':'SETTINGS',
               'geometry': geometry} 
window.title(window_dict['title'])
window.geometry(window_dict['geometry'])

def save_geometry():
    ''' Updates geometry.txt file to let screen size persist across windows '''
    with open('geometry.txt','w') as f:
        f.write(window.geometry())

def close_window():
    save_geometry()
    window.destroy()
window.protocol("WM_DELETE_WINDOW", close_window)


def Delete_Account():
    Delete_Account = tk.Frame(master=window)
    Delete_Account.grid(row=1, column=2)
    Delete_Account = tk.Button(master=Delete_Account, text="Delete Account", fg="red", width=30, height=5, command=Confirmation)
    Delete_Account.pack(padx=10, pady=10)

def Change_account():
    Change_account = tk.Frame(master=window)
    Change_account.grid(row=0, column=2)
    Change_account = tk.Button(master=Change_account, text="Change account details", fg="blue", width=30, height=5, command=Changeaccount)
    Change_account.pack(padx=10, pady=10)

def Back():
    Back = tk.Frame(master=window)
    Back.grid(row=2, column=2)
    Back = tk.Button(master=Back, text="Back", width=30, height=5, bg="yellow", fg="red", command=Go_back)
    Back.pack(padx=10, pady=10)

def Go_back():
    window.destroy()
    import subprocess
    cmd = 'Menu.py'
    p = subprocess.Popen(cmd, shell=True)

def Confirmation():
    window.destroy()
    import Confirmation

def Changeaccount():
    window.destroy()
    import subprocess
    cmd = 'Changeaccountpage.py'
    p = subprocess.Popen(cmd, shell=True)

Delete_Account()
Change_account()
Back()
window.mainloop()
