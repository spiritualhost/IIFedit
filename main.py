from tkinter import filedialog 
from tkinter import *

if __name__ == "__main__":
    print("test")
    root = Tk()

    #Setup
    root.geometry("640x320")
    root.minsize(320,160)
    root.resizable(1, 1)
    root.configure(background="blanched almond")
    root.title("PDF Module")
    
    #Buttons
	
    newIIF = Button(root, text="Create new IIF", command=lambda: print("Test: newIIF"))


    quitApp = Button(root, text="Quit", command=root.destroy)
    quitApp.pack(pady=10)

    #Main loop
    root.mainloop()


