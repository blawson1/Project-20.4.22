from datetime import datetime
import tkinter as tk
import sqlite3

window = tk.Tk()
window.title("Bikepage")
window.minsize(1208, 532)

# Read the width and height from the text file and store them in a dictionary
with open('geometry.txt','r') as f:
     geometry = f.readlines()
# Initialise window properties dictionary
window_dict = {'title':'Cycling',
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

# --------------------- Personal Best Handling --------------------- #
with open('user.txt','r') as f:
     USER_ID = f.readlines()[0]

def get_pb():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    pb_query = f"SELECT biking_pb FROM bmi WHERE id={USER_ID}"
    cur.execute(pb_query)
    pb = cur.fetchall()[0][0]
    return pb

def update_pb():
    global pb
    current_value = stopwatch_lbl['text']

    # if no pb exists in the database
    if pb == '00:00:00' and current_value != '00:00:00':
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        pb_query = f'UPDATE bmi set biking_pb = "{current_value}" WHERE id={USER_ID}'
        cur.execute(pb_query)
        con.commit()
        lbl_success['text'] = 'New PB!'
        lbl_success['fg'] = 'green'

    # check current value is better than database
    else:
        pb_hours, pb_minutes, pb_seconds = pb.split(':')
        current_hours, current_minutes, current_seconds = current_value.split(':')

        # Booleans
        hours_less = current_hours < pb_hours
        minutes_less = current_hours == pb_hours and current_minutes < pb_minutes
        seconds_less = current_hours == pb_hours and current_minutes == pb_minutes and current_seconds < pb_seconds

        if hours_less or minutes_less or seconds_less:
            con = sqlite3.connect('data.db')
            cur = con.cursor()
            pb_query = f'UPDATE bmi set biking_pb = "{current_value}" WHERE id={USER_ID}'
            cur.execute(pb_query)
            con.commit()
            lbl_success['text'] = 'New PB!'
            lbl_success['fg'] = 'green'
            
        else:
            lbl_success['text'] = 'PB better than current time'
            lbl_success['fg'] = 'red'

    pb = get_pb()
    lbl_pb['text'] = f"Personal Best: {pb}"


pb = get_pb()

# ------------------------------------------------------------------- #



# Define counter
counter = 0


def go_back():
    window.destroy()
    import subprocess
    cmd = 'Cardiopage.py'
    p = subprocess.Popen(cmd, shell=True)


def time_label(stopwatch_lbl):
    def count():
        if running:
            global counter
            timestamp = datetime.fromtimestamp(counter)
            stopwatch_lbl['text'] = timestamp.strftime("%H:%M:%S")# [:-4] strftime('%Y-%m-%dT%H:%M:%S.%f')
            stopwatch_lbl.after(1000, count)
            counter += 1

    count()


def start_timer(stopwatch_lbl):
    global running
    running = True
    time_label(stopwatch_lbl)
    btn_start_timer['state'] = 'disabled'
    btn_stop_timer['state'] = 'normal'
    btn_reset_timer['state'] = 'normal'


def stop_timer():
    global running
    btn_start_timer['state'] = 'normal'
    btn_stop_timer['state'] = 'disabled'
    btn_reset_timer['state'] = 'normal'
    running = False


def reset_timer(stopwatch_lbl):
    global counter
    counter = 0

    # If reset is pressed after pressing stop.
    if running == False:
        btn_reset_timer['state'] = 'disabled'
        stopwatch_lbl['text'] = '00:00:00'

    # If reset is pressed while the stopwatch is running.
    else:
        stopwatch_lbl['text'] = 'Starting...'


# ---------- Start Timer Label ---------- #
frm_start_timer_label = tk.Frame(master=window)
frm_start_timer_label.grid(row=0, column=1)
lbl_start_timer = tk.Label(master=frm_start_timer_label, text="Start stopwatch for run", fg="green", width=30,
                           height=5)
lbl_start_timer.pack(padx=10, pady=10)

# ---------- Start Timer Button ---------- #
frm_start_timer_btn = tk.Frame(master=window)
frm_start_timer_btn.grid(row=1, column=0)
btn_start_timer = tk.Button(master=frm_start_timer_btn, text="Start", width=30, height=5,
                            command=lambda: start_timer(stopwatch_lbl))
btn_start_timer.pack(padx=10, pady=10)

# ---------- Stop Timer Label ---------- #
frm_stop_timer_button = tk.Frame(master=window)
frm_stop_timer_button.grid(row=2, column=0)
btn_stop_timer = tk.Button(master=frm_stop_timer_button, text="Stop", width=30, height=5, command=stop_timer)
btn_stop_timer.pack(padx=10, pady=10)

# ---------- Reset Timer Label ---------- #
frm_reset_timer_label = tk.Frame(master=window)
frm_reset_timer_label.grid(row=0, column=1)
lbl_reset_timer = tk.Label(master=frm_reset_timer_label, text="Start stopwatch for 20km bike", fg="green", width=30, height=5)
lbl_reset_timer.pack(padx=10, pady=10)

# ---------- Reset Timer Button ---------- #
frm_reset_timer_btn = tk.Frame(master=window)
frm_reset_timer_btn.grid(row=3, column=0)
btn_reset_timer = tk.Button(master=frm_reset_timer_btn, text="Reset", width=30, height=5,
                            command=lambda: reset_timer(stopwatch_lbl))
btn_reset_timer.pack(padx=10, pady=10)


# ---------- Submit Button ---------- #
frm_submit = tk.Frame(master=window)
frm_submit.grid(row=2, column=2)
btn_submit = tk.Button(master=frm_submit, text="Enter", width=30, height=5, command=update_pb)
btn_submit.pack(padx=10, pady=10)

# ---------- Personal Best Label ---------- #
frm_pb = tk.Frame(master=window)
frm_pb.grid(row=1, column=2)
lbl_pb = tk.Label(master=frm_pb, width=30, text=f"Personal Best: {pb}")
lbl_pb.pack()

# ---------- Success Label ---------- #
frm_success_lbl = tk.Frame(master=window)
frm_success_lbl.grid(row=3, column=2)
lbl_success = tk.Label(master=frm_success_lbl, text="", width=30, height=5)
lbl_success.pack(padx=10, pady=10)

# ---------- Back Button ---------- #
frm_back = tk.Frame(master=window)
frm_back.grid(row=2, column=3)
btn_back = tk.Button(master=frm_back, text="Go Back", width=30, height=5, bg="yellow", fg="red", command=go_back)
btn_back.pack(padx=10, pady=10)

# ---------- Stopwatch Label ---------- #
stopwatch_frm = tk.Frame(master=window)
stopwatch_frm.grid(row=1, column=1)
stopwatch_lbl = tk.Label(master=stopwatch_frm, text="00:00:00", fg="black", font="30")
stopwatch_lbl.pack(padx=10, pady=10)

window.mainloop()