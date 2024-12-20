import customtkinter as ctk
import subprocess
import Messagebox as msb
import os
import sys
from PIL import Image, ImageTk
import win32com.client

def app_init():
    global app, cur
    cur = "@./cursor/cursor.cur"
    app = ctk.CTk()
    app.title("VVorkSpace Beta")
    app.iconbitmap("./icon/VVorkSpace.ico")
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    window_width = 1600
    window_height = 900
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    app.geometry(f"{window_width}x{window_height}+{x}+{y-20}")
    app.config(bg="black", cursor=cur)
    app.resizable(False, False)
    
    #grid (5x8)
    app.grid_rowconfigure(0, weight=0)
    app.grid_rowconfigure(1, weight=1)
    app.grid_rowconfigure(2, weight=1)
    app.grid_rowconfigure(3, weight=1)
    app.grid_rowconfigure(4, weight=0)
    app.grid_columnconfigure(0, weight=0)
    app.grid_columnconfigure(1, weight=1)
    app.grid_columnconfigure(2, weight=1)
    app.grid_columnconfigure(3, weight=1)
    app.grid_columnconfigure(4, weight=1)
    app.grid_columnconfigure(5, weight=1)
    app.grid_columnconfigure(6, weight=1)
    app.grid_columnconfigure(7, weight=0)
    
    #exit grid visualization
    app.bind("<Escape>", lambda event: visualize_grid(status=False))
    global frames
    frames = []
    
#visualize_grid()
def visualize_grid(status=True):
    if status == True:
        for row in range(5):
            for col in range(8):
                frame = ctk.CTkFrame(app, width=100, height=100, bg_color="black", fg_color="black")
                frame.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                label = ctk.CTkLabel(frame, text=f"({row}, {col})")
                label.place(relx=0.5, rely=0.5, anchor="center")
                frames.append(frame)
    else:
        for frame in frames:
            frame.destroy()
        frames.clear()

    
            
            
def add_button(parent, text, image, command, bg_color, fg_color, width, height, row, column, padx, pady):
    button = ctk.CTkButton(parent, text=text, 
                                image=image, command=command, 
                                bg_color=bg_color, fg_color=fg_color, 
                                width=width, height=height)
    button.grid(row=row, column=column, padx=padx, pady=pady)
    button.configure(cursor=cur)

def open_settings():
    settings_window = ctk.CTkToplevel(app)
    settings_window.title("Settings")
    settings_window.resizable(False, False)
    settings_window.grab_set()
    settings_window.config(cursor=cur, bg="black")
    
    screen_width = settings_window.winfo_screenwidth()
    screen_height = settings_window.winfo_screenheight()
    window_width = 720
    window_height = 480
    position_right = int(screen_width/2 - window_width/2)
    position_down = int(screen_height/2 - window_height/2)
    settings_window.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")
    
if __name__ == "__main__":
    app_init()
    
    #default images
    defaut_img = {
        "img_setting": ImageTk.PhotoImage(Image.open(r"./button_icon/setting.png").resize((100, 100))),
        "img_visualize": ImageTk.PhotoImage(Image.open(r"./button_icon/visualize.png").resize((100, 100))),
        
    }
    
    
    #add some default buttons
    #setting button
    add_button(app, None, defaut_img.get("img_setting") , lambda: open_settings(), "black", "black", 0, 0, 0, 7, 20, 20)
    #view visualize grid button
    add_button(app, None ,defaut_img.get("img_visualize") , lambda: visualize_grid(), "black", "black", 0, 0, 0, 0, 20, 20)
    
    
    app.mainloop()