import tkinter as tk
from tkinter import messagebox
from py_mainform_2 import mainform
import mysql.connector

# connect to mysql database
connection = mysql.connector.connect(
     host = 'localhost',
     user = 'root',
     password = '',
     port = '3306',
     database='py_lg_rg_db'
)

c = connection.cursor()

root = tk.Tk()

# close function
def close_window():
    root.destroy()

# window dementions
w = 400
h = 260

class loginForm:
    def __init__(self,master):
        self.master = master
        # start center window
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws-w)/2
        y = (hs-h)/2
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # end center window

        # start create widgets
        self.frame = tk.Frame(self.master, bg='#fff')
        
        self.btnsFrame = tk.Frame(self.frame, bg='#fff', padx=40, pady=15)
        
        self.windowTitle = tk.Label(self.frame, text='Login Window', bg='#fff', fg='blue', font=('Tahoma',20), pady=30)
        
        self.usernameLabel = tk.Label(self.frame, text='Username:', bg='#fff', font=('Verdana',16))
        self.usernameTextbox = tk.Entry(self.frame, font=('Verdana',12), width=25, borderwidth='2', relief='ridge')
        
        self.passwordLabel = tk.Label(self.frame, text='password:', bg='#fff', font=('Verdana',16))
        self.passwordTextbox = tk.Entry(self.frame,show='*', font=('Verdana',12), width=25, borderwidth='2', relief='ridge')
        
        self.btnLogin = tk.Button(self.btnsFrame, text='Login', bg='green', font=('Verdana',12), fg='#fff', padx=25, pady=10, command=self.login_func)
        self.btnCancel = tk.Button(self.btnsFrame, text='Cancel', bg='orange', font=('Verdana',12), fg='#fff', padx=25, pady=10, command=close_window)
        # end create widgets

        # start place widgets
        self.frame.pack(fill='both')
        self.windowTitle.grid(row=0, column=0, columnspan=2)
        self.usernameLabel.grid(row=1, column=0)
        self.usernameTextbox.grid(row=1, column=1)
        self.passwordLabel.grid(row=2, column=0, pady=(10,0))
        self.passwordTextbox.grid(row=2, column=1, pady=(10,0))
        self.btnsFrame.grid(row=3, column=0, columnspan=2, pady=10)
        self.btnLogin.grid(row=0, column=0, padx=(0,35))
        self.btnCancel.grid(row=0, column=1)
        # end place widgets

    # login function
    def login_func(self):
        username = self.usernameTextbox.get()
        password = self.passwordTextbox.get()
        select_query = 'SELECT * FROM `users` WHERE `username` = %s and password = %s'
        vals = (username, password,)
        c.execute(select_query, vals)
        #print(c.fetchall())
        user = c.fetchone()
        if user is not None:
            #messagebox.showinfo('Login', 'Yes')
            mainformwindow = tk.Toplevel()
            app = mainform(mainformwindow)
            root.withdraw()
            mainformwindow.protocol('WM_DELETE_WINDOW', close_window)
        else:
            messagebox.showwarning('Error', 'Enter a Valid Username & password')



def main():
    login_window = loginForm(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    