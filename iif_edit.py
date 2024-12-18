import pandas as pd
from tkinter import *
import os
from iif_import import *


#Current working directory
cwd = os.getcwd()

#Current working file path
cwfp = ""


#*****************************************************************************************************************

#Tkinter grid window setup
editIIF = Tk()
editIIF.title(f"Edit IIF")
editIIF.geometry("1040x600")
editIIF.configure(background="blanched almond")

#Test label - Remove
#dimensions = Label(editIIF, text=f"The IIF is {numColumns} columns long by {numRows} rows wide.").pack(pady=10) 

#Hashed entry widgets for user manipulation and writing to original iif
#Formed as keys being tuple of coordinates (x, y) and values being the entry widgets themselves
entryWidgets = {}



#Functions to open IIF editor window and edit the contents, export,etc.

#Function to fill the screen with labels
#!!!!Needs to be made better but fine for now!!!!

def iifFill(window, myIIF):

	#ISSUE
	#Headers are still remaining past new headers if file chosen second has less of them than file chosen previously
	
	for widget in entryWidgets.values():
		widget.destroy()
	entryWidgets.clear()
	

	#Need to alter dictionary to capture all headers in key
	#Dictionary of IIF data
	iifHash = {}
	headers = list(myIIF)
	for names in headers:
		temp = []
		for items in myIIF[names]:
			temp.append(items)
		iifHash[names] = temp
	print(iifHash)

	i = 1 #x-coordinate in grid
	j = 0 #y-coordinate in grid

	for keys in list(iifHash.keys()):
		header = Label(window, text=f"{keys}", width=15)
		header.grid(row=j, column=i, padx=10, pady=10)
		j+=1

		for values in iifHash[keys]:
			cells = Entry(window, width=15)
			cells.grid(row=j, column=i, padx=10, pady=10)
			cells.insert(0, values)  # Pre-fill with data
			entryWidgets[(j, i)] = cells #Creating hash map of grid coordinates for entry widgets
			j+=1
		j = 0
		i+=1
	



#Function to select IIF, update on-screen label, and toss path to iifFill() to fill entry widgets
def updateFileLabel(cwfp):
	cwfp = selectIIF()
	chosenIIF.config(text=f"{os.path.basename(cwfp)} selected")

	df = pd.read_csv(str(cwfp), sep='\t')
	#df = pd.read_csv(str(cwfp), sep='\\s+', engine='python')
	myIIF = pd.DataFrame(df)

	return iifFill(editIIF, myIIF)


#Function to save updated IIF
#NEEDS WORK
def SaveData():
	pass
	return 0




		
#************************************************************************************************************	

#Screen elements

#Fills screen with entry widgets for editing the iif
selectFile = Button(editIIF, text="Select an IIF...", command=lambda: updateFileLabel(cwfp))
selectFile.grid(row=0, column=0, padx=10, pady=10)

#Shows chosen IIF on screen
chosenIIF = Label(editIIF, text="No file selected...")
chosenIIF.grid(row=1, column=0, padx=10, pady=10)

#Button to save updated data
saveButton = Button(editIIF, text="Save altered IIF as...", command=lambda: print("test save"))
saveButton.grid(row=2, column=0, padx=10, pady=10)

#Button to quit program
quitter = Button(editIIF, text="Quit", command=editIIF.destroy)
quitter.grid(row=3, column=0, padx=10, pady=10)
 
#*************************************************************************************************************

#Main body
if __name__ == "__main__":
	#Start the GUI	
	editIIF.mainloop()





