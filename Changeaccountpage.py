import sqlite3
import tkinter as tk
import hashlib
window = tk.Tk()
window.title("Main_program")
window.minsize(1208, 532)

# Read the width and height from the text file and store them in a dictionary
with open('geometry.txt','r') as f:
     geometry = f.readlines()
# Initialise window properties dictionary
window_dict = {'title':'Change Account',
               'geometry': geometry} 
window.title(window_dict['title'])
window.geometry(window_dict['geometry'])

ALLOWED_DOMAINS = ['com', 'co', 'uk', 'org', 'net']
NUMBERS = ['0','1','2','3','4','5','6','7','8','9']

def save_geometry():
    ''' Updates geometry.txt file to let screen size persist across windows '''
    with open('geometry.txt','w') as f:
        f.write(window.geometry())

def Cancel():
    window.destroy()
    import subprocess
    cmd = 'SETTINGS.py'
    p = subprocess.Popen(cmd, shell=True)

def close_window():
    save_geometry()
    window.destroy()
window.protocol("WM_DELETE_WINDOW", close_window)

var = tk.StringVar()
var.set('male')

for i in range(0, 3):
    window.columnconfigure(i, weight=1, minsize=50)
    window.rowconfigure(i, weight=1, minsize=50)

# Get current information
with open('user.txt','r') as f:
        USER_ID = f.readlines()[0]
con = sqlite3.connect('data.db')
cur = con.cursor()
user_query = f"SELECT * FROM record WHERE id = {USER_ID}"
cur.execute(user_query)
user_data = cur.fetchall()[0]


print(user_data)


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
def update():

    error_text='Update Successful!'

    # Check name
    if len(ent_new_name.get()) > 20:
        error_text='Name cannot be more than 20 characters long'
    else:
        # Check age
        if ent_age.get() != '':
            try:
                int(ent_age.get())
            except:
                error_text='Age must be a whole number'
            else:
                if int(ent_age.get()) <= 0:
                    error_text = 'Age must be greater than 0'
                else:
                    # Check height
                    if ent_height.get() != '':
                        try:
                            int(ent_height.get())
                        except:
                            error_text='Height must be a whole number'
                        else:
                            if int(ent_height.get()) <= 0:
                                error_text='Height must be greater than 0cm'
                            else:
                                # Check weight
                                if ent_weight.get() != '':
                                    try:
                                        int(ent_weight.get())
                                    except:
                                        error_text='Weight must be a whole number'
                                    else:
                                        if int(ent_weight.get()) <= 0:
                                            error_text='Weight must be greater than 0kg'
                                        else:
                                            # Check email address
                                            if ent_new_email.get() != '':
                                                email_address = ent_new_email.get()
                                                error_text = verify_email(email_address, error_text)
                                                if error_text == 'Update Successful!':
                                                    # Check if email address exists already in the database
                                                    error_text = check_email_exists(email_address, error_text)
                                                    if error_text == 'Update Successful!':
                                                        # Check password
                                                        if ent_new_password.get() != '':
                                                            password = ent_new_password.get()
                                                            error_text = verify_password(password, error_text)

    # Display results
    lbl_reg_verification['text'] = error_text
    if error_text == 'Update Successful!':
        lbl_reg_verification['fg'] = 'green'
    else:
        lbl_reg_verification['fg'] = 'red'

    if error_text =='Update Successful!':
        ''' Updates entry in the database for a user '''
        con = sqlite3.connect('data.db')
        cur = con.cursor()

        if ent_new_name.get() == '':
            name = user_data[1]
        else:
            name = ent_new_name.get()
        
        if ent_age.get() == '':
            age = user_data[2]
        else:
            age = ent_age.get()

        if var.get() != user_data[3]:
            gender = user_data[3]
        else:
            gender = var.get()

        if ent_height.get() == '':
            height = user_data[4]
        else:
            height = ent_height.get()

        if ent_weight.get() == '':
            weight = user_data[5]
        else:
            weight = ent_weight.get()

        if ent_new_email.get() == '':
            email = user_data[6]
        else:
            email = ent_new_email.get()

        if ent_new_password.get() == '':
            password = user_data[7]
        else:
            password = ent_new_password.get().encode()
            password = hashlib.sha3_512(password).hexdigest()

        BMI = int(weight) / (int(height)/100)**2

        cur.execute(f"UPDATE record SET name={name}, age={age}, gender={gender}, height={height}, weight={weight}, email={email}, password={password})")
        cur.execute(f"UPDATE bmi SET BMI={BMI}")

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

btn_register = tk.Button(master=frm_right, text='Change account details', fg='black', bg='white', height=1, width=20, command=update)
btn_register.grid(row=9, column=1)

btn_cancel = tk.Button(master=frm_right, text='Cancel', fg='red', bg='white', height=1, width=20, command=Cancel)
btn_cancel.grid(row=9, column=0)

# mainloop
window.mainloop()