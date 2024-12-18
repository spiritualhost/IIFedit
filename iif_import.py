#Getting IIF files into the program

from tkinter import filedialog

def selectIIF():
    #Window gui to select IIF
    file_path = filedialog.askopenfilename(
            title = "Select IIF", 
            filetypes=[("IIF Files", "*.iif")]
            )
    print(file_path)
    return file_path

