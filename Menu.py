import tkinter as tk
window = tk.Tk()
window.title("Menu")
window.minsize(1208, 532)

# Read the width and height from the text file and store them in a dictionary
with open('geometry.txt','r') as f:
     geometry = f.readlines()
# Initialise window properties dictionary
window_dict = {'title':'Menu',
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


def Cardio_page():
    save_geometry()
    window.destroy()
    import Cardiopage

def Arms_page():
    save_geometry()
    window.destroy()
    import Armspage

def Legs_page():
    save_geometry()
    window.destroy()
    import Legspage

def Core_page():
    save_geometry()
    window.destroy()
    import Corepage

def Settings_page():
    save_geometry()
    window.destroy()
    import SETTINGS
    
def Profile_page():
    save_geometry()
    window.destroy()
    import Profile

# Option select
Option_Select = tk.Frame(master=window)
Option_Select.grid(row=0, column=0)
Option_Select = tk.Label(master=Option_Select, text="Select an option", fg="blue", width=30, height=5)
Option_Select.pack(padx=10, pady=10)

# Exit
Exit = tk.Frame(master=window)
Exit.grid(row=3, column=1)
Exit = tk.Button(master=Exit, text="Exit", width=30, height=5, bg="yellow", fg="red", command=quit)
Exit.pack(padx=10, pady=10)

# Cardio
Cardio = tk.Frame(master=window)
Cardio.grid(row=1, column=0)
Cardio = tk.Button(master=Cardio, text="Cardio", width=30, height=5, command=Cardio_page)
Cardio.pack(padx=10, pady=10)

# Arms
Arms = tk.Frame(master=window)
Arms.grid(row=1, column=1)
Arms = tk.Button(master=Arms, text="Arms/Upper Body", width=30, height=5, command=Arms_page)
Arms.pack(padx=10, pady=10)

# Legs
Legs = tk.Frame(master=window)
Legs.grid(row=2, column=0)
Legs = tk.Button(master=Legs, text="Legs/Lower Body", width=30, height=5, command=Legs_page)
Legs.pack(padx=10, pady=10)

# Core
Core = tk.Frame(master=window)
Core.grid(row=2, column=1)
Core = tk.Button(master=Core, text="Core", width=30, height=5, command=Core_page)
Core.pack(padx=10, pady=10)

# Settings
Core = tk.Frame(master=window)
Core.grid(row=3, column=0)
Core = tk.Button(master=Core, text="Settings", bg="light blue", width=30, height=5, command=Settings_page)
Core.pack(padx=10, pady=10)

# Profile
Profile = tk.Frame(master=window)
Profile.grid(row=2, column=2)
Profile = tk.Button(master=Profile, text="Profile",bg='green', width=30, height=5, command=Profile_page)
Profile.pack(padx=10, pady=10)


window.mainloop()
# or just mainloop() but something .mainloop lets you do many mainloops if you wanted to
