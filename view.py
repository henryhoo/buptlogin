from Tkinter import *
import logincheck2
import autologin
top=Tk()
top.geometry('300x200')
top.title('Bupt login')
var = StringVar()
var.set("hello")
label = Label(top,textvariable=var,font='Helvetica -20 bold')  
label.pack(fill=Y,expand=1)

def login():
    var.set(autologin.login())
    label.pack()
def money():
    if(autologin.test()=='http://10.3.8.211'):
        var.set('please login')
    else:
        var.set((str)((float)(logincheck2.checkmoney())/10000)+'Y')
        label.pack()
def usage():
    if(autologin.test()=='http://10.3.8.211'):
        var.set('please login')
    else:
        var.set((str)((float)(logincheck2.check())/1024)+'MB')
        label.pack()
def logout():
    var.set(autologin.logout())
    label.pack()

Button(top,text='login',command=login,activeforeground='white',
activebackground='red').pack(expand='yes',side='left')
Button(top,text='logout',command=logout,activeforeground='white',
activebackground='red').pack(expand='yes',side='left')
Button(top,text='money',command=money,activeforeground='white',
activebackground='red').pack(expand='yes',side='left')
Button(top,text='usage',command=usage,activeforeground='white',
activebackground='red').pack(expand='yes',side='left')


mainloop()
