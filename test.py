#Fill json file
import json
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