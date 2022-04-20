import tkinter as tk

window = tk.Tk()
window.title("Armspage")
window.minsize(1208, 532)

# Read the width and height from the text file and store them in a dictionary
with open('geometry.txt','r') as f:
     geometry = f.readlines()
# Initialise window properties dictionary
window_dict = {'title':'Arms',
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

def Arms_Select():
    Arms_Select = tk.Frame(master=window)
    Arms_Select.grid(row=0, column=0)
    Arms_Select = tk.Label(master=Arms_Select, text="Select an arms workout", fg="blue", width=30, height=5)
    Arms_Select.pack(padx=10, pady=10)

def Press_ups():
    Press_ups = tk.Frame(master=window)
    Press_ups.grid(row=1, column=0)
    Press_ups = tk.Button(master=Press_ups, text="Press ups", width=30, height=5, command=Press_ups_page)
    Press_ups.pack(padx=10, pady=10)

def Pull_ups():
    Pull_ups = tk.Frame(master=window)
    Pull_ups.grid(row=1, column=1)
    Pull_ups = tk.Button(master=Pull_ups, text="Pull ups", width=30, height=5, command=Pull_ups_page)
    Pull_ups.pack(padx=10, pady=10)

def Arm_curls():
    Arm_curls = tk.Frame(master=window)
    Arm_curls.grid(row=1, column=2)
    Arm_curls = tk.Button(master=Arm_curls, text="Arm curls", width=30, height=5, command=Arm_curls_page)
    Arm_curls.pack(padx=10, pady=10)

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

def Press_ups_page():
    window.destroy()
    import Pressupspage

def Pull_ups_page():
    window.destroy()
    import Pullupspage

def Arm_curls_page():
    window.destroy()
    import Armcurlspage

Arms_Select()
Press_ups()
Pull_ups()
Arm_curls()
Back()
window.mainloop()
