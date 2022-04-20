import tkinter as tk
import sqlite3
import hashlib

root = tk.Tk() # root window (Tk) must be created
root.withdraw() # remove from screen, working with Toplevel instead
window = tk.Toplevel() # can check resizing events with Toplevel but not Tk 
window.minsize(1208, 532)

import os
print(os.getcwd())

# Read the width and height from the text file and store them in a dictionary
with open('geometry.txt','r') as f:
     geometry = f.readlines()
# Initialise window properties dictionary
window_dict = {'title':'Stepbuddy',
               'geometry': geometry} 
window.title(window_dict['title'])
window.geometry(window_dict['geometry'])

# Initialise radio button variables
var = tk.StringVar()
var.set('male')

# Define variables for email and password verification functions
ALLOWED_DOMAINS = ['com', 'co', 'uk', 'org', 'net']
NUMBERS = ['0','1','2','3','4','5','6','7','8','9']


# Make widgets responsive to resizing
for i in range(0, 3):
    window.columnconfigure(i, weight=1, minsize=50)
    window.rowconfigure(i, weight=1, minsize=50)

# Create the database if it doesn't exist
con = sqlite3.connect('data.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS record(
    id integer PRIMARY KEY,
    name text,
    age number,
    gender text, 
    height number,
    weight number,
    email text, 
    password text)
''')
cur.execute('''CREATE TABLE IF NOT EXISTS bmi(
    id integer PRIMARY KEY,
    bmi number,
    running_pb text,
    walking_pb text,
    biking_pb text,
    pressups_pb number,
    pullups_pb number,
    armcurls_pb number,
    squats_pb number,
    stepups_pb number,
    lunges_pb number,
    burpees_pb number,
    situps_pb number,
    plank_pb text,
    FOREIGN KEY(id) REFERENCES record(id))
''')
con.commit()


def verify_email(email_address, error_text):
    ''' Checks user email is valid and handle error messages if not '''
    email_address = email_address.lower()
    # Check if there is an @ symbol
    if '@' in email_address:
        recipient_domain_top_list = email_address.split('@')
        domain_top_list = recipient_domain_top_list[1].split('.')
        top_list = domain_top_list[1:]

        # Check if there is a recipient name
        if len(domain_top_list[0]) > 0:

            # Check domains are allowed
            for part in top_list:
                if part not in ALLOWED_DOMAINS:
                    error_text = 'Invalid address - one or more top-level domains not allowed or have been left blank'

        else:
            error_text = 'Invalid address - must enter a recipient name'
    else:
        error_text = 'Invalid address - must contain an @ symbol'

    return error_text

def verify_password(password, error_text):
    ''' Checks user passsword is valid and handle error messages if not '''
    min_length = 8
    max_length = 25
    # Check for capital and lowercase letters
    if not password.islower() and not password.isupper():
        num_exists = False
        for char in password:
            if char in NUMBERS:
                num_exists = True
                break
        # Check for number
        if num_exists == True:
            # Check minimum and maximum length
            if len(password) < min_length or len(password) > max_length:
                error_text = f'Password must be between {min_length} and {max_length} characters'
        else:
                error_text = 'Invalid password - please use numbers'
    else:
            error_text = 'Invalid password - cannot use all upper or lower case letters'

    return error_text


def check_email_exists(email_address, error_text):
    email_address = email_address.lower()
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    email_query = "SELECT email FROM record"
    cur.execute(email_query)
    emails = cur.fetchall()
    emails = [email[0] for email in emails]
    if email_address in emails:
        error_text = 'Account with that email address already exists'
    return error_text

def register():
    
    error_text='Registration Successful!'

    # Check name
    if len(ent_new_name.get()) == 0:
        error_text='Name cannot be 0 characters long'
    elif len(ent_new_name.get()) > 20:
        error_text='Name cannot be more than 20 characters long'
    else:
        # Check age
        try:
            int(ent_age.get())
        except:
            error_text='Age must be a whole number'
        else:
            if int(ent_age.get()) <= 0:
                error_text = 'Age must be greater than 0'
            else:
                # Check height
                try:
                    int(ent_height.get())
                except:
                    error_text='Height must be a whole number'
                else:
                    if int(ent_height.get()) <= 0:
                        error_text='Height must be greater than 0cm'
                    else:
                        # Check weight
                        try:
                            int(ent_weight.get())
                        except:
                            error_text='Weight must be a whole number'
                        else:
                            if int(ent_weight.get()) <= 0:
                                error_text='Weight must be greater than 0kg'
                            else:
                                # Check email address
                                email_address = ent_new_email.get()
                                error_text = verify_email(email_address, error_text)
                                if error_text == 'Registration Successful!':
                                    # Check if email address exists already in the database
                                    error_text = check_email_exists(email_address, error_text)
                                    if error_text == 'Registration Successful!':
                                        # Check password
                                        password = ent_new_password.get()
                                        error_text = verify_password(password, error_text)

    # Display results
    lbl_reg_verification['text'] = error_text
    if error_text == 'Registration Successful!':
        lbl_reg_verification['fg'] = 'green'
    else:
        lbl_reg_verification['fg'] = 'red'

    if error_text == 'Registration Successful!':
        ''' Creates a new entry in the database for a user '''
        # Hash the password
        BMI = int(ent_weight.get()) / ((int(ent_height.get()))/100)**2
        password = ent_new_password.get().encode()
        hashed_password = hashlib.sha3_512(password).hexdigest()
        con = sqlite3.connect('data.db')
        cur = con.cursor()

        cur.execute("INSERT INTO record VALUES (NULL, :name, :age, :gender, :height, :weight, :email, :password)", {
            'name': ent_new_name.get(),
            'age': ent_age.get(),
            'gender': var.get(),
            'height': ent_height.get(),
            'weight': ent_weight.get(),
            'email': ent_new_email.get().lower(),
            'password': hashed_password
        })
        cur.execute("INSERT INTO bmi VALUES (NULL, :BMI, :running_pb, :walking_pb, :biking_pb, :pressups_pb, :pullups_pb, :armcurls_pb, :squats_pb, :stepups_pb, :lunges_pb, :burpees_pb, :situps_pb, :plank_pb)", {
            'BMI': BMI,
            'running_pb': "00:00:00",
            'walking_pb': "00:00:00",
            'biking_pb': "00:00:00",
            'pressups_pb': 0,
            'pullups_pb': 0,
            'armcurls_pb': 0,
            'squats_pb': 0,
            'stepups_pb': 0,
            'lunges_pb': 0,
            'burpees_pb': 0,
            'situps_pb': 0,
            'plank_pb': "00:00:00"
        })
        con.commit()
        ent_new_name.delete(0, tk.END)
        ent_age.delete(0, tk.END)
        ent_height.delete(0, tk.END)
        ent_weight.delete(0, tk.END)
        ent_new_email.delete(0, tk.END)
        ent_new_password.delete(0, tk.END)
        ent_new_password_again.delete(0, tk.END)
    else:
        print(error_text)


def check_database(email_address, password, error_text):
    ''' Check email address exists and if it does, check password matches '''
    email_address = email_address.lower()

    password = password.encode()
    hashed_password = hashlib.sha3_512(password).hexdigest()

    con = sqlite3.connect('data.db')
    cur = con.cursor()
    email_query = "SELECT email FROM record"
    cur.execute(email_query)
    emails = cur.fetchall()
    emails = [email[0] for email in emails]

    if email_address in emails:
        index = emails.index(email_address)
        password_query = "SELECT password FROM record"
        cur.execute(password_query)
        passwords = cur.fetchall()
        passwords = [password[0] for password in passwords]
        if passwords[index] != hashed_password:
            error_text = 'Password does not match database'
    else:
        error_text = 'Email address not found in database'

    return error_text


def save_geometry():
    ''' Updates geometry.txt file to let screen size persist across windows '''
    with open('geometry.txt','w') as f:
        f.write(window.geometry())

def close_window():
    save_geometry()
    window.destroy()
window.protocol("WM_DELETE_WINDOW", close_window)

def get_user_id():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    email_address = ent_email.get()

    email_query = f"SELECT id FROM record WHERE email='{email_address}'"
    cur.execute(email_query)
    id = str(cur.fetchall()[0][0])
    return id
    #id = cur.lastrowid


def save_user_id(user_id):
    with open('user.txt','w') as f:
        f.write(user_id)


def submit_pressed():
    ''' Verfies email and password and calls check_database to see if they match records '''
    error_text='Success!'
    email_address = ent_email.get()
    error_text = verify_email(email_address, error_text)
    if error_text != 'Success!':
        lbl_verification['text'] = error_text
    else:
        password = ent_password.get()
        error_text = verify_password(password, error_text)
        if error_text != 'Success!':
            lbl_verification['text'] = error_text
        else:
            error_text = check_database(email_address, password, error_text)
            if error_text != 'Success!':
                lbl_verification['text'] = error_text
            else:
                lbl_verification['fg'] = 'green'
                USER_ID = get_user_id()
                save_user_id(USER_ID)
                save_geometry()
                window.destroy()
                import Menu




# ------------ Left Frame ----------------
frm_left = tk.Frame(master=window)
frm_left.grid(row=0, column=0)
# -------------------- login label ----------------
lbl_login = tk.Label(master=frm_left, text='Login if you \nhave an account', fg='black', width=60, height=3)
lbl_login.grid(row=0, column=0)
# -------------------- Email Label ----------------
lbl_email = tk.Label(master=frm_left, text='Email Address: ', fg='black', width=60, height=3)
lbl_email.grid(row=1, column=0)
# -------------------- Email Entry ----------------
ent_email = tk.Entry(master=frm_left, fg='black', bg='white',)
ent_email.grid(row=1, column=1)
# -------------------- Password Label ----------------
lbl_password = tk.Label(master=frm_left, text='Enter Password: ', fg='black', height=3)
lbl_password.grid(row=2, column=0)
# -------------------- Password Entry ----------------
ent_password = tk.Entry(master=frm_left)
ent_password.config(show="•")
ent_password.grid(row=2, column=1)
# -------------------- Verification Label ----------------
lbl_verification = tk.Label(master=frm_left, text='', fg='red', height=3)
lbl_verification.grid(row=3, column=0, padx=10, pady=10)
# -------------------- Submit Button ----------------
btn_submit = tk.Button(master=frm_left, text='LOGIN', fg='black', bg='white', height=3, width=20, command=submit_pressed)
btn_submit.grid(row=3, column=1)

# ------------ Right Frame ----------------
frm_right = tk.Frame(master=window)
frm_right.grid(row=0, column=1)
# Name, gender, age, height, weight, email, password
# -------------------- Name Label ----------------
lbl_new_name = tk.Label(master=frm_right, text='Name: ', fg='black', width=60, height=3)
lbl_new_name.grid(row=0, column=0)
# -------------------- Name Entry ----------------
ent_new_name = tk.Entry(master=frm_right, fg='black', bg='white')
ent_new_name.grid(row=0, column=1)
# -------------------- Age Label ----------------
lbl_age = tk.Label(master=frm_right, text='Age: ', fg='black', width=60, height=3)
lbl_age.grid(row=1, column=0)
# -------------------- Age Entry ----------------
ent_age = tk.Entry(master=frm_right, fg='black', bg='white')
ent_age.grid(row=1, column=1)
# -------------------- Gender Frame ----------------
frm_gender = tk.Frame(master=frm_right)
frm_gender.grid(row=2, column=0, columnspan=2)
# -------------------- Gender Frame Radio Buttons ----------------
male_rb = tk.Radiobutton(frm_gender, text='Male', variable=var, value='male')
female_rb = tk.Radiobutton(frm_gender, text='Female', variable=var, value='female')
others_rb = tk.Radiobutton(frm_gender, text='Other', variable=var, value='others')
male_rb.grid(row=0, column=0)
female_rb.grid(row=0, column=1)
others_rb.grid(row=0, column=2)
# -------------------- Height Label ----------------
lbl_height = tk.Label(master=frm_right, text='Height (cm): ', fg='black', width=60, height=3)
lbl_height.grid(row=4, column=0)
# -------------------- Height Entry ----------------
ent_height = tk.Entry(master=frm_right, fg='black', bg='white')
ent_height.grid(row=4, column=1)
# -------------------- Weight Label ----------------
lbl_weight = tk.Label(master=frm_right, text='Weight (kg): ', fg='black', width=60, height=3)
lbl_weight.grid(row=5, column=0)
# -------------------- Weight Entry ----------------
ent_weight = tk.Entry(master=frm_right, fg='black', bg='white')
ent_weight.grid(row=5, column=1)
# -------------------- New Email Label ----------------
lbl_new_email = tk.Label(master=frm_right, text='Email Address: ', fg='black', width=60, height=3)
lbl_new_email.grid(row=6, column=0)
ent_new_email = tk.Entry(master=frm_right, fg='black', bg='white')
ent_new_email.grid(row=6, column=1)

lbl_new_password = tk.Label(master=frm_right, text='Password: ', fg='black', width=60, height=3)
lbl_new_password.grid(row=7, column=0)
ent_new_password = tk.Entry(master=frm_right, fg='black', bg='white')
ent_new_password.config(show="•")
ent_new_password.grid(row=7, column=1)

lbl_new_password_again = tk.Label(master=frm_right, text='Password Again: ', fg='black', width=60, height=3)
lbl_new_password_again.grid(row=8, column=0)
ent_new_password_again = tk.Entry(master=frm_right, fg='black', bg='white')
ent_new_password_again.config(show="•")
ent_new_password_again.grid(row=8, column=1)

lbl_reg_verification = tk.Label(master=frm_right, text='', fg='red', height=3)
lbl_reg_verification.grid(row=9, column=0, padx=10, pady=10)

btn_register = tk.Button(master=frm_right, text='REGISTER', fg='black', bg='white', height=3, width=20, command=register)
btn_register.grid(row=9, column=1)


# mainloop
window.mainloop()

