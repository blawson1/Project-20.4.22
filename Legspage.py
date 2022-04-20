import tkinter as tk

window = tk.Tk()
window.title("Legspage")
window.minsize(1208, 532)

# Read the width and height from the text file and store them in a dictionary
with open('geometry.txt','r') as f:
     geometry = f.readlines()
# Initialise window properties dictionary
window_dict = {'title':'Legs',
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

def Legs_Select():
    Legs_Select = tk.Frame(master=window)
    Legs_Select.grid(row=0, column=0)
    Legs_Select = tk.Label(master=Legs_Select, text="Select a legs workout", fg="blue", width=30, height=5)
    Legs_Select.pack(padx=10, pady=10)

def Squats():
    Squats = tk.Frame(master=window)
    Squats.grid(row=1, column=0)
    Squats = tk.Button(master=Squats, text="Squats", width=30, height=5, command=Squats_page)
    Squats.pack(padx=10, pady=10)

def Step_ups():
    Step_ups = tk.Frame(master=window)
    Step_ups.grid(row=1, column=1)
    Step_ups = tk.Button(master=Step_ups, text="Step ups", width=30, height=5, command=Step_ups_page)
    Step_ups.pack(padx=10, pady=10)

def Lunges():
    Lunges = tk.Frame(master=window)
    Lunges.grid(row=1, column=2)
    Lunges = tk.Button(master=Lunges, text="Lunges", width=30, height=5, command=Lunges_page)
    Lunges.pack(padx=10, pady=10)

def Back():
    Back = tk.Frame(master=window)
    Back.grid(row=2, column=3)
    Back = tk.Button(master=Back, text="Back", width=30, height=5, bg="yellow", fg="red", command=Go_back)
    Back.pack(padx=10, pady=10)

def Go_back():
    window.destroy()
    import subprocess
    cmd = 'Menu.py'
    p = subprocess.Popen(cmd, shell=True)

def Squats_page():
    window.destroy()
    import Squatspage

def Step_ups_page():
    window.destroy()
    import Stepupspage

def Lunges_page():
    window.destroy()
    import Lungespage

Legs_Select()
Squats()
Step_ups()
Lunges()
Back()
window.mainloop()
