from tkinter import *
import os
from banking_app_oop import Bank, Read, User, Write
from PIL import ImageTk, Image


#### Use Bank class to be personal detail function
# Use Bank class to collect user detail include user nand password


# Main Screen
master = Tk()
master.title('Banking App')

# Functions
def finish_reg(): # will save the account as a plain file 
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()
    #to void the the same name users' overwrite in the file
    all_accounts = os.listdir()

    if name =='' or age =='' or gender =='' or password =='':
        notif.config(fg='red', text='All fields required !!!')
        return
    
    for name_check in all_accounts:
        if name == name_check:
            notif.config(fg='red', text='Account already existes')
            return
        else:
            user = Bank(name, age, gender, password)
            Write.write_new_account(user)
            notif.config(fg='green', text= 'Account has been created')

def register():
    # Vars
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global notif
    global register_screen
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()

    # register screen
    register_screen = Toplevel(master)
    register_screen.title('Register')

    # Labels
    Label(register_screen, text= 'Please enter your details below to register', font= ('Calibri', 12)).grid(row=0, sticky=N, pady=10)
    Label(register_screen, text= 'Name', font= ('Calibri', 12)).grid(row=1, sticky=W, pady=10)
    Label(register_screen, text= 'Age', font= ('Calibri', 12)).grid(row=2, sticky=W, pady=10)
    Label(register_screen, text= 'Gender', font= ('Calibri', 12)).grid(row=3, sticky=W, pady=10)
    Label(register_screen, text= 'Password', font= ('Calibri', 12)).grid(row=4, sticky=W, pady=10)
    notif = Label(register_screen, font= ('Calibri', 12))
    notif.grid(row=6, sticky=N, pady=10)

    # Entries
    Entry(register_screen, textvariable=temp_name).grid(row=1, column=0)
    Entry(register_screen, textvariable=temp_age).grid(row=2, column=0)
    Entry(register_screen, textvariable=temp_gender).grid(row=3, column=0)
    Entry(register_screen, textvariable=temp_password, show='*').grid(row=4, column=0)

    # Buttons
    Button(register_screen, text= 'Register', command= finish_reg, font= ('Calibri', 12)).grid(row=5, sticky=N, pady=10)

def login_session():
    global login_name
    global login_password
    global details_name
    global details_age
    global details_gender
    global read_data
    # account balance, deposit, withdraw
    all_accounts = os.listdir()
    login_name = temp_login_name.get()
    login_password = temp_login_password.get()
    
    
    for name in all_accounts:
        if login_name == name:
            read_data = Read(login_name)
            password = read_data.get_password()
            user_details = read_data.get_data()
            details_name = user_details[0]
            details_age = user_details[2]
            details_gender = user_details[3]
            
            
            # Account Dashboard, Login complete
            if login_password == password:
                login_screen.destroy()
                account_dashboard = Toplevel(master)
                account_dashboard.title('Account Dashboard')
                ###### img2 was import outsite the function #######                
                Label(account_dashboard, image= img2).grid(row=0, sticky=W, pady=5)
                # Labels
                Label(account_dashboard, text= 'Account Dashboard', font= ('Calibri', 12)).grid(row=1, sticky=N, pady=10)
                Label(account_dashboard, text= 'Welcome '+name, font= ('Calibri', 12)).grid(row=2, sticky=N, pady=10)
                # Buttons
                Button(account_dashboard, text= 'Personal Details', font= ('Calibri', 12), width=30, command= personal_details).grid(row=3, sticky=N, padx=10)
                Button(account_dashboard, text= 'Deposit', font= ('Calibri', 12), width=30, command= deposit).grid(row=4, sticky=N, padx=10)
                Button(account_dashboard, text= 'Withdraw', font= ('Calibri', 12), width=30, command= withdraw).grid(row=5, sticky=N, padx=10)
                Label(account_dashboard).grid(row=5, sticky=N, pady=10)
                return
            else:
                login_notif.config(fg= 'red', text= 'Incorrect Password !!')
                return
        else:
            login_notif.config(fg= 'red', text= 'Incorrect Username !!')
            
    login_notif.config(fg= 'red', text= 'Username and Password !!')

def deposit_finish():
    get_balance = read_data.get_balance()
    amount_deposit = temp_deposit.get()

    if amount_deposit == 0:
        notif_deposit.config(fg='red', text='Please insert amount !!!')
        return

    elif amount_deposit < 0:
        notif_deposit.config(fg='red', text='Nah, you cant withdraw here !!!')

    else:      
        bank = Bank(details_name, details_age, details_gender, login_password)
        bank = bank.deposit(get_balance, amount_deposit)
        notif_deposit.config(fg='green', text='THB {} has been deposit, Available balance THB: {}'.format(amount_deposit, read_data.get_balance()))

def deposit():
    # Vars
    global temp_deposit
    global notif_deposit
    temp_deposit = IntVar()

    # Deposit screen
    deposit_screen = Toplevel(master)
    deposit_screen.title('Deposit')

    # Labels
    Label(deposit_screen, text= 'Deposit your money', font= ('Calibri', 12)).grid(row=0, column=0, sticky=N, pady=10)
    notif_deposit = Label(deposit_screen, font=('Calibri', 12))
    notif_deposit.grid(row=2, sticky=N, pady=5)
    # Entry
    Entry(deposit_screen, textvariable= temp_deposit, font= ('Calibri', 12)).grid(row=1, column=0, sticky=N, pady=20)
    
    # Button
    Button(deposit_screen, text= 'Confirm', command= deposit_finish, width=15, font=('Calibri', 12)).grid(row=3, column=0, sticky=N, padx=5, pady=10)

def withdraw_finish():
    get_balance = read_data.get_balance()
    amount_withdraw = temp_withdraw.get()

    if amount_withdraw == 0:
        notif_withdraw.config(fg='red', text='Done.!! You withdraw 0, I give you 0')
        return
    
    elif amount_withdraw < 0:
        notif_withdraw.config(fg='red', text='Without this function, the balance would be increased')
        return

    else:
        process = Bank(details_name, details_age, details_gender, login_password)
        process.withdraw(get_balance, amount_withdraw)
        notif_withdraw.config(fg='green', text='THB {} has been withdraw, Available balance THB: {}'.format(amount_withdraw, read_data.get_balance()))
        return

def withdraw():
    # Vars
    global temp_withdraw
    global notif_withdraw
    temp_withdraw = IntVar()

    print('Withdraw')

    # Withdraw screen
    withdraw_screen = Toplevel(master)
    withdraw_screen.title('Withdraw')

    # Labels
    Label(withdraw_screen, text= 'Withdraw your money', font=('Calibri',12)).grid(row=0, sticky=N, pady=10)
    notif_withdraw = Label(withdraw_screen, font=('Calibri', 12))
    notif_withdraw.grid(row=2, sticky=N, pady=5)

    # Entry
    Entry(withdraw_screen, textvariable= temp_withdraw, font=('Calibri', 12)).grid(row=1, sticky=N, pady=20)

    # Button
    Button(withdraw_screen, text= 'Confirm', command= withdraw_finish, width=15, font=('Calibri', 12)).grid(row=3, sticky=N, padx=5, pady=10)


def personal_details():
    # Vars
    get_balance = read_data.get_balance()
    # Personal details screen
    personal_details_screen = Toplevel(master)
    personal_details_screen.title('Personal Details')
    # Labels
    Label(personal_details_screen, text= 'Personal Details', font= ('Calibri', 12)).grid(row=0, sticky=N, pady=10)
    Label(personal_details_screen, text= 'Name : '+details_name, font= ('Calibri', 12)).grid(row=1, sticky=W, pady=10)
    Label(personal_details_screen, text= 'Age : '+details_age, font= ('Calibri', 12)).grid(row=2, sticky=W, pady=10)
    Label(personal_details_screen, text= 'Gender : '+details_gender, font= ('Calibri', 12)).grid(row=3, sticky=W, pady=10)
    Label(personal_details_screen, text= 'Balance : THB '+get_balance, font= ('Calibri', 12)).grid(row=4, sticky=W, pady=10)
                                                            

def login():
    # Vars
    global temp_login_name
    global temp_login_password
    global login_notif
    global login_screen
    temp_login_name = StringVar()
    temp_login_password = StringVar()

    # Login Screen
    login_screen = Toplevel(master)
    login_screen.title('Login')
    
    # Labels
    Label(login_screen, text= 'Login to your account', font=('Calibri', 12)).grid(row=0, sticky=N, pady=10)
    Label(login_screen, text= 'Username', font=('Calibri', 12)).grid(row=1, sticky=W)
    Label(login_screen, text= 'Password', font=('Calibri', 12)).grid(row=2, sticky=W)
    login_notif = Label(login_screen, font= ('Calibri', 12))
    login_notif.grid(row=4, sticky=N)

    # Entry
    Entry(login_screen, textvariable= temp_login_name).grid(row=1, column=1, padx=5)
    Entry(login_screen, textvariable= temp_login_password, show= '*').grid(row=2, column=1, padx=5)

    # Button
    Button(login_screen, text= 'Login', command= login_session, width=15, font=('Calibri', 12)).grid(row=3, sticky=W, padx=5, pady=5)


# Image import
# master_creen image 
img = Image.open('bank_icon.jpg')
img = img.resize((300,300))
img = ImageTk.PhotoImage(img)
# account_dashboard imange
img2 = Image.open('bank2.jpg')
img2 = img2.resize((300,300))
img2 = ImageTk.PhotoImage(img2) 

# Labels
Label(master, text= 'Dummy Banking System', font= ('Calibri', 14)).grid(row=0, sticky=N, pady=10)
Label(master, text= "Hey 1 2 3 ไม่ได้เป็นคนที่เกเร ", font= ('Calibri', 12)).grid(row=1, sticky=N)# sticky n: north
Label(master, image= img).grid(row=2, sticky=N, pady=15)

# Buttons
Button(master, text= 'Register', font= ('Calibri', 12), width=20, command= register).grid(row=3, sticky=N)
Button(master, text= 'Login', font= ('Calibri', 12), width=20, command= login).grid(row=4, sticky=N, pady= 10)




master.mainloop()