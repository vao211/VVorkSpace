import os
import winreg as reg
from tkinter import messagebox

def run_on_startup():
    app_name = "VVork Space"
    exe_path = os.path.abspath(__file__)

    #Registry
    try:
        key = reg.OpenKey(reg.HKEY_CURRENT_USER,
                          r"Software\Microsoft\Windows\CurrentVersion\Run",
                          0, reg.KEY_SET_VALUE)
        reg.SetValueEx(key, app_name, 0, reg.REG_SZ, exe_path)
        reg.CloseKey(key)
        messagebox.showinfo("Success", "Application added to startup successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to add to startup:\n{e}")
        
if __name__ == "__main__":
    run_on_startup()