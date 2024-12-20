import customtkinter as ctk
import subprocess
import Messagebox as msb
import os
import sys
from PIL import Image, ImageTk
import win32com.client

def open_settings():
    settings_window = ctk.CTkToplevel(app)
    settings_window.title("Settings")
    settings_window.geometry("640x480")
    settings_window.resizable(False, False)
    settings_window.grab_set()
    settings_window.config(cursor="@cursor.cur", bg="black")
    
    screen_width = settings_window.winfo_screenwidth()
    screen_height = settings_window.winfo_screenheight()
    window_width = 640
    window_height = 480
    position_right = int(screen_width/2 - window_width/2)
    position_down = int(screen_height/2 - window_height/2)
    settings_window.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")
    
    # img
    img_shortcut = ImageTk.PhotoImage(Image.open("icon_png/shortcut.png").resize((100, 100)))
    img_run_on_startup = ImageTk.PhotoImage(Image.open("icon_png/run_on_startup.png").resize((100, 100)))
    
    # button shortcut
    btn_create_shortcut = ctk.CTkButton(settings_window, text="Shortcut", 
                                        image=img_shortcut,
                                        command=lambda: create_shortcut(sys.executable, 
                                        os.path.join(os.path.expanduser("~"), "Desktop", "VVork Space.lnk")),
                                        bg_color="black", fg_color="black",
                                        width=20, height=2)
    btn_create_shortcut.grid(row=3, column=2, padx=20, pady=20)
    btn_create_shortcut.configure(cursor="@cursor.cur")
    
    # button run_on_startup
    btn_run_on_startup = ctk.CTkButton(settings_window, text="Run on startup", 
                                       image=img_run_on_startup,
                                       command=lambda: run_on_startup(),
                                       bg_color="black", fg_color="black",
                                       width=20, height=2)
    btn_run_on_startup.grid(row=3, column=3, padx=20, pady=20)
    btn_run_on_startup.configure(cursor="@cursor.cur")

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

def run_on_startup():
    create_shortcut(sys.executable,
                    os.path.join(os.path.expanduser("~"),
                                 "AppData", "Roaming", "Microsoft", "Windows",
                                 "Start Menu", "Programs", "Startup",
                                 "VVork Space.lnk"), msg=False)
    msb.CTkMessagebox.messagebox(title="Run on startup!", text="VVork Space will run on startup",
                                 sound="on", button_text="OK", 
                                 size="320x150", center=True, top=True)

def open_app(app_path):
    subprocess.Popen(f'start /MAX "" "{app_path}"', shell=True)

def app_init():
    global app
    app = ctk.CTk()
    app.title("VVork Space ")
    app.resizable(False, False)
    app.iconbitmap("VVorkSpace.ico")
    
    ''' _bg_image
    bg_image = Image.open("image.png")
    bg_image = bg_image.resize((1280, 720), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(bg_image)
    
    bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg_image
    '''    

    # giữa màn hình
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    window_width = 1280
    window_height = 720
    position_right = int(screen_width/2 - window_width/2)
    position_down = int(screen_height/2 - window_height/2)
    app.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")

    # con trỏ
    app.config(cursor="@cursor.cur", bg="black")

    # căn giữa btn
    app.grid_rowconfigure(0, weight=1)
    app.grid_rowconfigure(3, weight=1)
    app.grid_columnconfigure(0, weight=1)
    app.grid_columnconfigure(5, weight=1)

    img_lol = ImageTk.PhotoImage(Image.open("icon_png/lol.png").resize((100, 100)))
    img_vscode = ImageTk.PhotoImage(Image.open("icon_png/vscode.png").resize((100, 100)))
    img_coccoc = ImageTk.PhotoImage(Image.open("icon_png/coccoc.png").resize((100, 100)))
    img_word = ImageTk.PhotoImage(Image.open("icon_png/word.png").resize((100, 100)))
    img_youtube = ImageTk.PhotoImage(Image.open("icon_png/youtube.png").resize((100, 100)))
    img_poe = ImageTk.PhotoImage(Image.open("icon_png/poe.png").resize((100, 100)))
    img_discord = ImageTk.PhotoImage(Image.open("icon_png/discord.png").resize((100, 100)))
    img_game = ImageTk.PhotoImage(Image.open("icon_png/game.png").resize((100, 100)))
    img_setting = ImageTk.PhotoImage(Image.open("icon_png/setting.png").resize((100, 100)))

    # button
    
    # vscode
    btn_Open_vscode = ctk.CTkButton(app, 
                                    image=img_vscode, 
                                    text="", 
                                    width=20, height=100,
                                    bg_color="black",
                                    fg_color="black",
                                    command=lambda: open_app(r"C:\Users\NGAIVINH\Desktop\App Code\Visual Studio Code.lnk"))
    btn_Open_vscode.grid(row=1, column=1, padx=20, pady=20)
    btn_Open_vscode.configure(cursor="@cursor.cur")
    
    # lol
    btn_Open_lol = ctk.CTkButton(app, 
                                 text="", 
                                 image=img_lol,
                                 width=20, height=100,
                                 bg_color="black",
                                 fg_color="black",          
                                 command=lambda: open_app(r"C:\Users\NGAIVINH\Desktop\Game\League of Legends.lnk"))
    btn_Open_lol.grid(row=1, column=2, padx=20, pady=20)
    btn_Open_lol.configure(cursor="@cursor.cur")
    
    # coccoc
    btn_Open_coccoc = ctk.CTkButton(app, 
                                    text="", 
                                    image=img_coccoc,
                                    width=200, height=100,
                                    bg_color="black",
                                    fg_color="black",
                                    command=lambda: open_app(r"C:\Users\NGAIVINH\Desktop\Apps\Cốc Cốc.lnk"))
    btn_Open_coccoc.grid(row=1, column=3, padx=20, pady=20)
    btn_Open_coccoc.configure(cursor="@cursor.cur")
    
    # word
    btn_Open_word = ctk.CTkButton(app, 
                                  text="",
                                  image=img_word,
                                  width=200, height=100,
                                  bg_color="black",
                                  fg_color="black",
                                  command=lambda: open_app(r"C:\Users\NGAIVINH\Desktop\Offices\Word.lnk"))
    btn_Open_word.grid(row=1, column=4, padx=20, pady=20)
    btn_Open_word.configure(cursor="@cursor.cur")
    
    # youtube
    btn_Open_youtube = ctk.CTkButton(app, 
                                     text="", 
                                     image=img_youtube,
                                     width=200, height=100,
                                     bg_color="black",
                                     fg_color="black",
                                     command=lambda: open_app(r"C:\Users\NGAIVINH\Desktop\Apps\Youtube.lnk"))
    btn_Open_youtube.grid(row=2, column=1, padx=20, pady=20)
    btn_Open_youtube.configure(cursor="@cursor.cur")
    
    # poe
    btn_Open_poe = ctk.CTkButton(app, 
                                 text="", 
                                 image=img_poe,
                                 width=200, height=100,
                                 bg_color="black",
                                 fg_color="black",
                                 command=lambda: open_app(r"C:\Users\NGAIVINH\Desktop\Apps\Poe.lnk"))
    btn_Open_poe.grid(row=2, column=2, padx=20, pady=20)
    btn_Open_poe.configure(cursor="@cursor.cur")
    
    # discord
    btn_Open_discord = ctk.CTkButton(app, 
                                     text="", 
                                     image=img_discord,
                                     width=200, 
                                     height=100,
                                     bg_color="black",
                                     fg_color="black",
                                     command=lambda: open_app(r"C:\Users\NGAIVINH\Desktop\Game\Discord.lnk"))
    btn_Open_discord.grid(row=2, column=3, padx=20, pady=20)
    btn_Open_discord.configure(cursor="@cursor.cur")
    
    # game
    btn_Open_GAME = ctk.CTkButton(app,
                                  text="",
                                  image=img_game,
                                  width=200, height=100,
                                  bg_color="black",
                                  fg_color="black",
                                  command=lambda: open_app(r"C:\Users\NGAIVINH\Desktop\Game"))
    btn_Open_GAME.grid(row=2, column=4, padx=20, pady=20)
    btn_Open_GAME.configure(cursor="@cursor.cur")
 
    # settings button
    btn_settings = ctk.CTkButton(app, 
                                 text="",
                                 width=100, height=40,
                                 image=img_setting,
                                 bg_color="black",
                                 fg_color="black",
                                 command=lambda: open_settings())
    btn_settings.configure(cursor="@cursor.cur")
    btn_settings.place(relx=1.0, 
                       rely=0.0, 
                       anchor="ne", 
                       x=-10, y=10)
    
if __name__ == "__main__":
    app_init()
    app.mainloop()