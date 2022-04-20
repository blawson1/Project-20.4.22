import tkinter as tk
window2 = tk.Tk()
window2.title("Cardiopage")
window2.minsize(1208, 532)

# Read the width and height from the text file and store them in a dictionary
with open('geometry.txt','r') as f:
     geometry = f.readlines()
# Initialise window properties dictionary
window_dict = {'title':'Cardio',
               'geometry': geometry} 
window2.title(window_dict['title'])
window2.geometry(window_dict['geometry'])

def save_geometry():
    ''' Updates geometry.txt file to let screen size persist across windows '''
    with open('geometry.txt','w') as f:
        f.write(window2.geometry())

def close_window():
    save_geometry()
    window2.destroy()
window2.protocol("WM_DELETE_WINDOW", close_window)


def Cardio_Select():
    Cardio_Select = tk.Frame(master=window2)
    Cardio_Select.grid(row=0, column=0)
    Cardio_Select = tk.Label(master=Cardio_Select, text="Select a cardio activity", fg="blue", width=30, height=5)
    Cardio_Select.pack(padx=10, pady=10)

def Run():
    Run = tk.Frame(master=window2)
    Run.grid(row=1, column=0)
    Run = tk.Button(master=Run, text="Run", width=30, height=5, command=Running_page)
    Run.pack(padx=10, pady=10)

def Bike():
    Bike = tk.Frame(master=window2)
    Bike.grid(row=1, column=1)
    Bike = tk.Button(master=Bike, text="Bike", width=30, height=5, command=Bike_page)
    Bike.pack(padx=10, pady=10)

def Walk():
    Walk = tk.Frame(master=window2)
    Walk.grid(row=1, column=2)
    Walk = tk.Button(master=Walk, text="Walk", width=30, height=5, command=Walk_page)
    Walk.pack(padx=10, pady=10)

def Back():
    Back = tk.Frame(master=window2)
    Back.grid(row=2, column=3)
    Back = tk.Button(master=Back, text="Back", width=30, height=5, bg="yellow", fg="red", command=Go_back)
    Back.pack(padx=10, pady=10)

def Go_back():
    window2.destroy()
    import subprocess
    cmd = 'Menu.py'
    p = subprocess.Popen(cmd, shell=True)

def Running_page():
    window2.destroy()
    import Runningpage

def Bike_page():
    window2.destroy()
    import Bikepage

def Walk_page():
    window2.destroy()
    import Walkpage

Cardio_Select()
Bike()
Walk()
Run()
Back()
window2.mainloop()
