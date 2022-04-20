from datetime import datetime
import tkinter as tk
import time
import sqlite3
window2 = tk.Tk()
window2.title("Profile")
window2.minsize(1208, 532)

# Read the width and height from the text file and store them in a dictionary
with open('geometry.txt','r') as f:
     geometry = f.readlines()
# Initialise window properties dictionary
window_dict = {'title':'Profile',
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

with open('user.txt','r') as f:
     USER_ID = f.readlines()[0]
# --------------------- RUNNING --------------------- #
def get_pb():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    pb_query = f"SELECT running_pb FROM bmi WHERE id={USER_ID}"
    cur.execute(pb_query)
    pb = cur.fetchall()[0][0]
    return pb
    pb = get_pb()
    lbl_pb['text'] = f"Personal Best: {pb}"
pb = get_pb()
# --------------------- Biking --------------------- #
def get_pb2():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    pb2_query = f"SELECT biking_pb FROM bmi WHERE id={USER_ID}"
    cur.execute(pb2_query)
    pb2 = cur.fetchall()[0][0]
    return pb2
    pb2 = get_pb2()
    lbl_pb2['text'] = f"Personal Best: {pb2}"
pb2 = get_pb2()
# --------------------- Walking --------------------- #
def get_pb3():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    pb3_query = f"SELECT walking_pb FROM bmi WHERE id={USER_ID}"
    cur.execute(pb3_query)
    pb3 = cur.fetchall()[0][0]
    return pb3
    pb3 = get_pb3()
    lbl_pb3['text'] = f"Personal Best: {pb3}"
pb3 = get_pb3()
# --------------------- Press ups --------------------- #
def get_pb4():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    pb4_query = f"SELECT pressups_pb FROM bmi WHERE id={USER_ID}"
    cur.execute(pb4_query)
    pb4 = cur.fetchall()[0][0]
    pb4 = int(pb4)
    return pb4
    pb4 = get_pb4()
    lbl_pb4['text'] = f"Personal Best: {pb4}"
pb4 = get_pb4()
# --------------------- Pull ups --------------------- #
def get_pb5():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    pb5_query = f"SELECT pullups_pb FROM bmi WHERE id={USER_ID}"
    cur.execute(pb5_query)
    pb5 = cur.fetchall()[0][0]
    pb5 = int(pb5)
    return pb5
    pb5 = get_pb5()
    lbl_pb5['text'] = f"Personal Best: {pb5}"
pb5 = get_pb5()
# --------------------- Arm curls --------------------- #
def get_pb6():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    pb6_query = f"SELECT armcurls_pb FROM bmi WHERE id={USER_ID}"
    cur.execute(pb6_query)
    pb6 = cur.fetchall()[0][0]
    pb6 = int(pb6)
    return pb6
    pb6 = get_pb6()
    lbl_pb6['text'] = f"Personal Best: {pb6}"
pb6 = get_pb6()
# --------------------- Squats --------------------- #
def get_pb7():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    pb7_query = f"SELECT squats_pb FROM bmi WHERE id={USER_ID}"
    cur.execute(pb7_query)
    pb7 = cur.fetchall()[0][0]
    pb7 = int(pb7)
    return pb7
    pb7 = get_pb7()
    lbl_pb7['text'] = f"Personal Best: {pb7}"
pb7 = get_pb7()
# --------------------- Step ups --------------------- #
def get_pb8():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    pb8_query = f"SELECT stepups_pb FROM bmi WHERE id={USER_ID}"
    cur.execute(pb8_query)
    pb8 = cur.fetchall()[0][0]
    pb8 = int(pb8)
    return pb8
    pb8 = get_pb8()
    lbl_pb8['text'] = f"Personal Best: {pb8}"
pb8 = get_pb8()
# --------------------- Lunges --------------------- #
def get_pb9():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    pb9_query = f"SELECT lunges_pb FROM bmi WHERE id={USER_ID}"
    cur.execute(pb9_query)
    pb9 = cur.fetchall()[0][0]
    pb9 = int(pb9)
    return pb9
    pb9 = get_pb9()
    lbl_pb9['text'] = f"Personal Best: {pb9}"
pb9 = get_pb9()
# --------------------- Burpees --------------------- #
def get_pb10():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    pb10_query = f"SELECT burpees_pb FROM bmi WHERE id={USER_ID}"
    cur.execute(pb10_query)
    pb10 = cur.fetchall()[0][0]
    pb10 = int(pb10)
    return pb10
    pb10 = get_pb10()
    lbl_pb10['text'] = f"Personal Best: {pb10}"
pb10 = get_pb10()
# --------------------- Sit ups --------------------- #
def get_pb11():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    pb11_query = f"SELECT situps_pb FROM bmi WHERE id={USER_ID}"
    cur.execute(pb11_query)
    pb11 = cur.fetchall()[0][0]
    pb11 = int(pb11)
    return pb11
    pb11 = get_pb11()
    lbl_pb11['text'] = f"Personal Best: {pb11}"
pb11 = get_pb11()
# --------------------- Plank --------------------- #
def get_pb12():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    pb12_query = f"SELECT plank_pb FROM bmi WHERE id={USER_ID}"
    cur.execute(pb12_query)
    pb12 = cur.fetchall()[0][0]
    return pb12
    pb12 = get_pb12()
    lbl_pb12['text'] = f"Personal Best: {pb12}"
pb12 = get_pb12()
# --------------------- BMI --------------------- #
def get_pb13():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    pb13_query = f"SELECT BMI FROM bmi WHERE id={USER_ID}"
    cur.execute(pb13_query)
    pb13 = cur.fetchall()[0][0]
    return pb13
    pb13 = get_pb13()
    lbl_pb13['text'] = f"Personal Best: {pb13}"
pb13 = get_pb13()
# --------------------- BMIhealth --------------------- #
def get_pb14():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    pb14_query = f"SELECT BMI FROM bmi WHERE id={USER_ID}"
    cur.execute(pb14_query)
    pb14 = cur.fetchall()[0][0]
    if pb14<18.5:
        pb14="Underweight"
    elif pb14>25:
        pb14="Overweight"
    else:
        pb14="Healthy Weight"
    return pb14
    pb14 = get_pb14()
    lbl_pb14['text'] = f"{pb14}"
pb14 = get_pb14()
# --------------------- Labels --------------------- #
def Profile():
    Profile = tk.Frame(master=window2)
    Profile.grid(row=0, column=0)
    Profile = tk.Label(master=Profile, text="Profile", fg="blue", width=30, height=5)
    Profile.pack(padx=10, pady=10)

def Back():
    Back = tk.Frame(master=window2)
    Back.grid(row=14, column=3)
    Back = tk.Button(master=Back, text="Back", width=30, height=5, bg="yellow", fg="red", command=Go_back)
    Back.pack(padx=10, pady=10)

def Go_back():
    window2.destroy()
    import subprocess
    cmd = 'Menu.py'
    p = subprocess.Popen(cmd, shell=True)

    

# ---------- PBRunning ---------- #
frm_pb = tk.Frame(master=window2)
frm_pb.grid(row=1, column=1)
lbl_pb = tk.Label(master=frm_pb, width=30, text="Running PB")
lbl_pb.pack()

# ---------- PBRunning ---------- #
frm_pb = tk.Frame(master=window2)
frm_pb.grid(row=1, column=2)
lbl_pb = tk.Label(master=frm_pb, width=30, text=f"{pb}")
lbl_pb.pack()

# ---------- PBBiking ---------- #
frm_pb2 = tk.Frame(master=window2)
frm_pb2.grid(row=2, column=1)
lbl_pb2 = tk.Label(master=frm_pb2, width=30, text="Biking PB")
lbl_pb2.pack()

# ---------- PBBiking ---------- #
frm_pb2 = tk.Frame(master=window2)
frm_pb2.grid(row=2, column=2)
lbl_pb2 = tk.Label(master=frm_pb2, width=30, text=f"{pb2}")
lbl_pb2.pack()

# ---------- PBWalking ---------- #
frm_pb3 = tk.Frame(master=window2)
frm_pb3.grid(row=3, column=1)
lbl_pb3 = tk.Label(master=frm_pb3, width=30, text="Walking PB")
lbl_pb3.pack()

# ---------- PBWalking ---------- #
frm_pb3 = tk.Frame(master=window2)
frm_pb3.grid(row=3, column=2)
lbl_pb3 = tk.Label(master=frm_pb3, width=30, text=f"{pb3}")
lbl_pb3.pack()

# ---------- PBpressups ---------- #
frm_pb4 = tk.Frame(master=window2)
frm_pb4.grid(row=4, column=1)
lbl_pb4 = tk.Label(master=frm_pb4, width=30, text="Press ups PB")
lbl_pb4.pack()

# ---------- PBpressups ---------- #
frm_pb4 = tk.Frame(master=window2)
frm_pb4.grid(row=4, column=2)
lbl_pb4 = tk.Label(master=frm_pb4, width=30,height=5, text=f"{pb4}")
lbl_pb4.pack()

# ---------- PBpullups ---------- #
frm_pb5 = tk.Frame(master=window2)
frm_pb5.grid(row=5, column=1)
lbl_pb5 = tk.Label(master=frm_pb5, width=30, text="Pull ups PB")
lbl_pb5.pack()

# ---------- PBpullups ---------- #
frm_pb5 = tk.Frame(master=window2)
frm_pb5.grid(row=5, column=2)
lbl_pb5 = tk.Label(master=frm_pb5, width=30, text=f"{pb5}")
lbl_pb5.pack()

# ---------- PBArmcurls ---------- #
frm_pb6 = tk.Frame(master=window2)
frm_pb6.grid(row=6, column=1)
lbl_pb6 = tk.Label(master=frm_pb6, width=30, text="Arm curls PB")
lbl_pb6.pack()

# ---------- PBArmcurls ---------- #
frm_pb6 = tk.Frame(master=window2)
frm_pb6.grid(row=6, column=2)
lbl_pb6 = tk.Label(master=frm_pb6, width=30,height=5, text=f"{pb6}")
lbl_pb6.pack()

# ---------- PBSquats ---------- #
frm_pb7 = tk.Frame(master=window2)
frm_pb7.grid(row=7, column=1)
lbl_pb7 = tk.Label(master=frm_pb7, width=30, text="Squats PB")
lbl_pb7.pack()

# ---------- PBSquats ---------- #
frm_pb7 = tk.Frame(master=window2)
frm_pb7.grid(row=7, column=2)
lbl_pb7 = tk.Label(master=frm_pb7, width=30, text=f"{pb7}")
lbl_pb7.pack()

# ---------- PBStepups ---------- #
frm_pb8 = tk.Frame(master=window2)
frm_pb8.grid(row=8, column=1)
lbl_pb8 = tk.Label(master=frm_pb8, width=30, text="Step ups PB")
lbl_pb8.pack()

# ---------- PBStepups ---------- #
frm_pb8 = tk.Frame(master=window2)
frm_pb8.grid(row=8, column=2)
lbl_pb8 = tk.Label(master=frm_pb8, width=30,height=5, text=f"{pb8}")
lbl_pb8.pack()

# ---------- PBLunges ---------- #
frm_pb9 = tk.Frame(master=window2)
frm_pb9.grid(row=9, column=1)
lbl_pb9 = tk.Label(master=frm_pb9, width=30, text="Lunges PB")
lbl_pb9.pack()

# ---------- PBLunges ---------- #
frm_pb9 = tk.Frame(master=window2)
frm_pb9.grid(row=9, column=2)
lbl_pb9 = tk.Label(master=frm_pb9, width=30, text=f"{pb9}")
lbl_pb9.pack()

# ---------- PBBurpees ---------- #
frm_pb10 = tk.Frame(master=window2)
frm_pb10.grid(row=10, column=1)
lbl_pb10 = tk.Label(master=frm_pb10, width=30, text="Burpees PB")
lbl_pb10.pack()

# ---------- PBBurpees ---------- #
frm_pb10 = tk.Frame(master=window2)
frm_pb10.grid(row=10, column=2)
lbl_pb10 = tk.Label(master=frm_pb10, width=30,height=5, text=f"{pb10}")
lbl_pb10.pack()

# ---------- PBSitups ---------- #
frm_pb11 = tk.Frame(master=window2)
frm_pb11.grid(row=11, column=1)
lbl_pb11 = tk.Label(master=frm_pb11, width=30, text="Sit ups PB")
lbl_pb11.pack()

# ---------- PBSitups ---------- #
frm_pb11 = tk.Frame(master=window2)
frm_pb11.grid(row=11, column=2)
lbl_pb11 = tk.Label(master=frm_pb11, width=30, text=f"{pb11}")
lbl_pb11.pack()

# ---------- PBPlank ---------- #
frm_pb12 = tk.Frame(master=window2)
frm_pb12.grid(row=12, column=1)
lbl_pb12 = tk.Label(master=frm_pb12, width=30, text="Plank PB")
lbl_pb12.pack()

# ---------- PBPlank ---------- #
frm_pb12 = tk.Frame(master=window2)
frm_pb12.grid(row=12, column=2)
lbl_pb12 = tk.Label(master=frm_pb12, width=30,height=5, text=f"{pb12}")
lbl_pb12.pack()

# ---------- PBBMI ---------- #
frm_pb13 = tk.Frame(master=window2)
frm_pb13.grid(row=13, column=1)
lbl_pb13 = tk.Label(master=frm_pb13, width=30, text="BMI")
lbl_pb13.pack()

# ---------- PBBMI ---------- #
frm_pb13 = tk.Frame(master=window2)
frm_pb13.grid(row=13, column=2)
lbl_pb13 = tk.Label(master=frm_pb13, width=30, text=f"{pb13:.3}")
lbl_pb13.pack()

# ---------- PBBMIhealth ---------- #
frm_pb14 = tk.Frame(master=window2)
frm_pb14.grid(row=14, column=1)
lbl_pb14 = tk.Label(master=frm_pb14, width=30, text="Health")
lbl_pb14.pack()

# ---------- PBBMIhealth ---------- #
frm_pb14 = tk.Frame(master=window2)
frm_pb14.grid(row=14, column=2)
lbl_pb14 = tk.Label(master=frm_pb14, width=30,text=f"{pb14}")
lbl_pb14.pack()

Profile()
Back()
window2.mainloop()

