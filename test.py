#Fill json file
import json
from tkinter import filedialog
buttons = []
for row in range(1, 4):
    for column in range(1, 7):
        button_info = {
            'file_path': r"C:\Users\NGAIVINH\Desktop\AppDIY\IP to PC.exe",
            'icon_path': None,
            'row': row,
            'column': column
        }
        buttons.append(button_info)

with open(r"./bin/saved_buttons.json", 'w') as f:
    json.dump(buttons, f, indent=4)
    
'''
    {
        "file_path": "C:\\Users\\NGAIVINH\\Desktop\\AppDIY\\IP to PC.exe",
        "icon_path": null,
        "row": 3,
        "column": 6
    }
'''
def open_file_dialog():
    file_path = filedialog.askopenfilename(
        title="Select a Shortcut",
        filetypes=[("Shortcut files", "*.lnk"), ("All files", "*.*")]
    )
    
    if file_path:
        # Chắc chắn rằng file_path là đường dẫn đến file .lnk
        if file_path.lower().endswith('.lnk'):
            print(f"Selected shortcut: {file_path}")  # Đường dẫn đến shortcut
        else:
            print(f"Selected file: {file_path}")
        
if __name__ == '__main__':
    open_file_dialog()
    text = "example.file.txt"

    if text != None:
        text = text.rsplit(".", 1)[0]

    print(text)