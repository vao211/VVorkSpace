import customtkinter as ctk
from tkinter import messagebox
import subprocess
import os
from PIL import Image, ImageTk #ảnh
import winreg as reg #auto mở

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
    except Exception as e:
        messagebox.showerror("Error", f"Failed to add to startup:\n{e}")

def open_app(app_path):
    subprocess.Popen(f'start /MAX "" "{app_path}"', shell=True)
    
def app_init():
    global app
    app = ctk.CTk()
    app.title("VVork Space ")
    app.resizable(False, False)
    app.iconbitmap("VVorkSpace.ico")
    
    # bg_image = Image.open("image.png")
    # bg_image = bg_image.resize((1280, 720), Image.LANCZOS)
    # bg_image = ImageTk.PhotoImage(bg_image)
    
    # bg_label = ctk.CTkLabel(app, image=bg_image, text="")
    # bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    # bg_label.image = bg_image
    
    #giữa màn hình
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    window_width = 1280
    window_height = 720
    position_right = int(screen_width/2 - window_width/2)
    position_down = int(screen_height/2 - window_height/2)
    app.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")

    #con trỏ
    app.config(cursor="@cursor.cur", bg="black")

    #căn giữa btn
    app.grid_rowconfigure(0, weight=1)
    app.grid_rowconfigure(3, weight=1)
    app.grid_columnconfigure(0, weight=1)
    app.grid_columnconfigure(5, weight=1)

    #icon
    img_lol = ImageTk.PhotoImage(Image.open("icon_png/lol.png").resize((100,100)))
    img_vscode = ImageTk.PhotoImage(Image.open("icon_png/vscode.png").resize((100,100)))
    img_coccoc = ImageTk.PhotoImage(Image.open("icon_png/coccoc.png").resize((100,100)))
    img_word = ImageTk.PhotoImage(Image.open("icon_png/word.png").resize((100,100)))
    img_youtube = ImageTk.PhotoImage(Image.open("icon_png/youtube.png").resize((100,100)))
    img_poe = ImageTk.PhotoImage(Image.open("icon_png/poe.png").resize((100,100)))
    img_discord = ImageTk.PhotoImage(Image.open("icon_png/discord.png").resize((100,100)))
    img_game = ImageTk.PhotoImage(Image.open("icon_png/game.png").resize((100,100)))
    
    #button
    
    #vscode
    btn_Open_vscode = ctk.CTkButton(app, 
                                    image=img_vscode, 
                                    text="", 
                                    width=20, height=100,
                                    bg_color="black",
                                    fg_color="black",
    command=lambda: open_app(r"C:\Users\NGAIVINH\Desktop\App Code\Visual Studio Code.lnk"))
    btn_Open_vscode.grid(row=1, column=1, padx=20, pady=20)
    btn_Open_vscode.configure(cursor = "@cursor.cur")
    
    #lol
    btn_Open_lol = ctk.CTkButton(app, 
                                 text= "" ,
                                 image=img_lol,
                                 width=20, height=100,
                                 bg_color="black",
                                 fg_color="black",          
    command=lambda: open_app(r"C:\Users\NGAIVINH\Desktop\Game\League of Legends.lnk"))
    btn_Open_lol.grid(row=1, column=2, padx=20, pady=20)
    btn_Open_lol.configure(cursor = "@cursor.cur")
    
    #coccoc
    btn_Open_coccoc = ctk.CTkButton(app, 
                                    text="", 
                                    image=img_coccoc,
                                    width=200, height=100,
                                    bg_color="black",
                                    fg_color="black",
    command=lambda: open_app(r"C:\Users\NGAIVINH\Desktop\Apps\Cốc Cốc.lnk"))
    btn_Open_coccoc.grid(row=1, column=3, padx=20, pady=20)
    btn_Open_coccoc.configure(cursor = "@cursor.cur")
    
    #word
    btn_Open_word = ctk.CTkButton(app, 
                                  text="",
                                  image=img_word,
                                  width=200, height=100,
                                  bg_color="black",
                                  fg_color="black",
    command=lambda: open_app(r"C:\Users\NGAIVINH\Desktop\Offices\Word.lnk"))
    btn_Open_word.grid(row=1, column=4, padx=20, pady=20)
    btn_Open_word.configure(cursor = "@cursor.cur")
    
    #youtube
    btn_Open_youtube = ctk.CTkButton(app, 
                                     text="", 
                                     image=img_youtube,
                                     width=200, height=100,
                                     bg_color="black",
                                     fg_color="black",
    command=lambda: open_app(r"C:\Users\NGAIVINH\Desktop\Apps\Youtube.lnk"))
    btn_Open_youtube.grid(row=2, column=1, padx=20, pady=20)
    btn_Open_youtube.configure(cursor = "@cursor.cur")
    
    #poe
    btn_Open_poe = ctk.CTkButton(app, 
                                 text="", 
                                 image=img_poe,
                                 width=200, height=100,
                                 bg_color="black",
                                 fg_color="black",
    command=lambda: open_app(r"C:\Users\NGAIVINH\Desktop\Apps\Poe.lnk"))
    btn_Open_poe.grid(row=2, column=2, padx=20, pady=20)
    btn_Open_poe.configure(cursor = "@cursor.cur")
    
    #discord
    btn_Open_discord = ctk.CTkButton(app, 
                                     text="", 
                                     image=img_discord,
                                     width=200, 
                                     height=100,
                                     bg_color="black",
                                     fg_color="black",
    command=lambda: open_app(r"C:\Users\NGAIVINH\Desktop\Game\Discord.lnk"))
    btn_Open_discord.grid(row=2, column=3, padx=20, pady=20)
    btn_Open_discord.configure(cursor = "@cursor.cur")
    
    #game
    btn_Open_GAME = ctk.CTkButton(app,
                                  text="",
                                  image=img_game,
                                  width=200, height=100,
                                  bg_color="black",
                                  fg_color="black",
    command=lambda: open_app(r"C:\Users\NGAIVINH\Desktop\Game"))
    btn_Open_GAME.grid(row=2, column=4, padx=20, pady=20)
    btn_Open_GAME.configure(cursor = "@cursor.cur")
    
if __name__ == "__main__":
    run_on_startup()
    app_init()
    app.mainloop()