from tkinter import *
from tkinter import messagebox
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == 'admin' and password == '123':
        login_window.destroy()
        main_window()
    else:
        messagebox.showerror('Error', 'Incorrect username or password.')

def main_window():
   
    window = Tk()
    window.title('Hospital Management System')


    window.mainloop()

login_window = Tk()
login_window.title('Login')

username_label = Label(login_window, text='Username:')
username_label.pack()
username_entry = Entry(login_window)
username_entry.pack()

password_label = Label(login_window, text='Password:')
password_label.pack()
password_entry = Entry(login_window, show='*')
password_entry.pack()

login_button = Button(login_window, text='Login', command=login, bg='blue', fg='white')

def on_enter(e):
    login_button['background'] = 'light blue'

def on_leave(e):
    login_button['background'] = 'blue'

login_button.bind("<Enter>", on_enter)
login_button.bind("<Leave>", on_leave)

login_button.pack()

login_window.mainloop()
