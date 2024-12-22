import customtkinter as ctk
import subprocess
import Messagebox as msb
import os
import sys
from PIL import Image, ImageTk
from tkinter import filedialog
import win32com.client
import shutil
import json

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

def run_on_startup():
    create_shortcut(sys.executable,
                    os.path.join(os.path.expanduser("~"),
                                 "AppData", "Roaming", "Microsoft", "Windows",
                                 "Start Menu", "Programs", "Startup",
                                 "VVork Space.lnk"), msg=False)
    msb.CTkMessagebox.messagebox(title="Run on startup!", text="VVork Space will run on startup",
                                 sound="on", button_text="OK", 
                                 size="320x150", center=True, top=True)
      
def create_shortcut(target, shortcut_path, msg=True):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.TargetPath = target
    shortcut.WorkingDirectory = os.path.dirname(target)
    shortcut.IconLocation = target
    shortcut.save()
    if msg:
        msb.CTkMessagebox.messagebox(title="Shortcut created!", 
                                     text=f"Shortcut created at:\n{shortcut_path}", 
                                     sound="on", button_text="OK", size="320x150", 
                                     center=True, top=True)
       
def setting_init():
    setting_window = ctk.CTkToplevel(app)
    setting_window.title("Settings")
    setting_window.resizable(False, False)
    setting_window.grab_set()
    setting_window.config(cursor=cur, bg="black")
    
    screen_width = setting_window.winfo_screenwidth()
    screen_height = setting_window.winfo_screenheight()
    window_width = 720
    window_height = 480
    position_right = int(screen_width/2 - window_width/2)
    position_down = int(screen_height/2 - window_height/2)
    setting_window.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")
    
    #creat_shortcut button
    add_button(setting_window, "Create Shortcu", defaut_img.get("img_create_shortcut"), 
               lambda:  create_shortcut(sys.executable, 
                                        os.path.join(os.path.expanduser("~"), "Desktop", "VVork Space.lnk")),
               "black", "black", 0, 0, 0, 0, 20, 20)
    #run on startup button
    add_button(setting_window, "Run on startup",defaut_img.get("img_run_on_startup") , lambda: run_on_startup(), "black", "black", 0, 0, 1, 0, 20, 20)

def open_app(file_path):
    subprocess.Popen(f'start /MAX "" "{file_path}"', shell=True)
    
def open_file_dialog():
    file_path = filedialog.askopenfilename()
    if file_path:
        print(file_path)
        choose_icon(file_path)
    
def open_folder_dialog():
    folder_path = filedialog.askdirectory()
    if folder_path:
        choose_icon(folder_path)
    
def choose_icon(file_path):
    filetypes = [
        ('Image files', '*.png;*.jpg;*.jpeg;*.ico'),
        ('PNG files', '*.png'),
        ('JPEG files', '*.jpg;*.jpeg'),
        ('ICO files', '*.ico')
    ]
    
    icon_path = filedialog.askopenfilename(
        title="Choose an icon",
        filetypes=filetypes
    )
    
    if icon_path:
        try:
            if not os.path.exists('button_icon'):
                os.makedirs('button_icon')
            
            new_filename = os.path.basename(icon_path)
            new_path = os.path.join('button_icon', new_filename)
            
            shutil.copy2(icon_path, new_path)
            
            choose_position(file_path,icon_path)
            
            return new_path
            
        except Exception as e:
            msb.CTkMessagebox.messagebox(
                title="Error!",
                text=f"Error copying icon: {e}",
                sound="off",
                button_text="OK",
                size="320x150",
                center=True,
                top=True
            )
            return None
    return None

def choose_position(file_path, icon_path):
    position_window = ctk.CTkToplevel(app)
    position_window.title("Choose Position")
    position_window.resizable(False, False)
    position_window.grab_set()
    position_window.config(cursor=cur, bg="black")
    
    screen_width = position_window.winfo_screenwidth()
    screen_height = position_window.winfo_screenheight()
    window_width = 400
    window_height = 300
    position_right = int(screen_width/2 - window_width/2)
    position_down = int(screen_height/2 - window_height/2)
    position_window.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")
    
    for row in range(1, 4):
        for column in range(1, 7):
            button = ctk.CTkButton(
                position_window,
                text=f"({row}, {column})",
                command=lambda r=row, c=column: [
                    place_icon(file_path,icon_path, r, c),
                    position_window.destroy()
                ],
                width=50,
                height=50
            )
            button.grid(row=row, column=column, padx=5, pady=5)
            button.configure(cursor=cur)


def place_icon(file_path,icon_path, row, column):
    try:
        #tạo image
        icon = Image.open(icon_path)
        icon = icon.resize((100, 100), Image.Resampling.LANCZOS)
        icon_photo = ImageTk.PhotoImage(icon)
        
        add_button(app, None, icon_photo,lambda: open_app(file_path),
            "black","black",
            100,100,row, column,5,5
        )
        
        load_button_info(file_path, icon_path, row, column)
        
    except Exception as e:
        msb.CTkMessagebox.messagebox(
            title="Error!",text=f"Error placing icon: {e}",sound="off",button_text="OK",size="320x150",
            center=True,
            top=True
        )

save_file = r"./bin/saved_buttons.json"

def load_saved_buttons():
    if os.path.exists(save_file):
        try:
            with open(save_file, 'r') as f:
                return json.load(f)
        except:
            return []
    return []

# Thiếu tính năng copy icon vào folder button_icon
def load_button_info(file_path, icon_path, row, column):
    buttons = load_saved_buttons()
    
    if os.path.dirname(icon_path) == 'button_icon':
        icon_path = os.path.join('button_icon', os.path.basename(icon_path))
    
    button_info = {
        'file_path': file_path,
        'icon_path': icon_path,
        'row': row,
        'column': column
    }
    
    buttons = [b for b in buttons if not (b['row'] == row and b['column'] == column)]
    buttons.append(button_info)
    
    with open(save_file, 'w') as f:
        json.dump(buttons, f, indent=4)
        
def restor_button_onStart():
    buttons = load_saved_buttons()
    for button in buttons:
        try:
            icon = Image.open(button['icon_path'])
            icon = icon.resize((100, 100), Image.Resampling.LANCZOS)
            icon_photo = ImageTk.PhotoImage(icon)
            
            add_button(app, None, icon_photo,
                      lambda path=button['file_path']: open_app(path),
                      "black", "black",
                      100, 100,
                      button['row'], button['column'],
                      5, 5)
        except Exception as e:
            print(f"Error restoring button: {e}")
            
def add_app():
    add_app_window = ctk.CTkToplevel(app)
    add_app_window.title("Add an app to VVorkSpace")
    add_app_window.resizable(False, False)
    add_app_window.grab_set()
    add_app_window.config(cursor=cur, bg="black")
    
    screen_width = add_app_window.winfo_screenwidth()
    screen_height = add_app_window.winfo_screenheight()
    window_width = 720
    window_height = 480
    position_right = int(screen_width/2 - window_width/2)
    position_down = int(screen_height/2 - window_height/2)
    add_app_window.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")
    
    add_app_window.grid_rowconfigure(0, weight=0)
    add_app_window.grid_rowconfigure(1, weight=1)
    add_app_window.grid_rowconfigure(2, weight=1)
    add_app_window.grid_rowconfigure(3, weight=1)
    add_app_window.grid_rowconfigure(4, weight=1)
    add_app_window.grid_rowconfigure(5, weight=0)
    add_app_window.grid_columnconfigure(0, weight=0)
    add_app_window.grid_columnconfigure(1, weight=1)
    add_app_window.grid_columnconfigure(2, weight=1)
    add_app_window.grid_columnconfigure(3, weight=1)
    add_app_window.grid_columnconfigure(4, weight=0) 
    
    add_button(add_app_window, "Choose the app", None, lambda: open_file_dialog(), "blue", "blue", 0, 0, 2, 2, 20, 20)
    add_button(add_app_window, "Choose the folder", None, lambda: open_folder_dialog(), "blue", "blue", 0, 0, 3, 2, 20, 20)
    
    

if __name__ == "__main__":
    app_init()
    
    #default images
    defaut_img = {
        "img_setting": ImageTk.PhotoImage(Image.open(r"./button_icon/setting.png").resize((100, 100))),
        "img_visualize": ImageTk.PhotoImage(Image.open(r"./button_icon/visualize.png").resize((100, 100))),
        "img_create_shortcut": ImageTk.PhotoImage(Image.open(r"./button_icon/shortcut.png").resize((100, 100))),
        "img_add": ImageTk.PhotoImage(Image.open(r"./button_icon/add.png").resize((100, 100))),
        "img_exit": ImageTk.PhotoImage(Image.open(r"./button_icon/exit.png").resize((100, 100))),
        "img_run_on_startup": ImageTk.PhotoImage(Image.open(r"./button_icon/run_on_startup.png").resize((100, 100)))
    }
    
    #add some default buttons
    #setting button
    add_button(app, None, defaut_img.get("img_setting") , lambda: setting_init(), "black", "black", 0, 0, 0, 7, 20, 20)
    #view visualize grid button
    add_button(app, None ,defaut_img.get("img_visualize") , lambda: visualize_grid(), "black", "black", 0, 0, 0, 0, 20, 20)
    #add button
    add_button(app, None, defaut_img.get("img_add"), lambda: add_app(), "black", "black", 0, 0, 4, 0, 20, 20)
    #exit button
    add_button(app, None, defaut_img.get("img_exit"), app.destroy, "black", "black", 0, 0, 4, 7, 20, 20)

    restor_button_onStart()

    app.mainloop()