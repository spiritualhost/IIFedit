#Acting on the IIF

df = pd.read_csv("SIcash12092024.iif", sep='\\s+')
myIIF = pd.DataFrame(df)

#For specific cell reference
#print(myIIF["NAME"][2], "\n")

#Print entire iif
print(myIIF)

#Print headers as list
headers = list(myIIF)
#print(headers)

#Print number of columns (i.e., the actual amount of the items in the top row)
numColumns = len(myIIF.loc[0])
#print(f"There are {numColumns} columns in the IIF.")

#Print number of rows (i.e., the actual amount of items in the first column, which should be the longest column)
numRows = myIIF.shape[0] + 1
#print(f"There are {numRows} rows in the IIF.")

#Dictionary of IIF data
iifIndexed = {}
for names in headers:
	temp = []
	for items in myIIF[names]:
		temp.append(items)
	iifIndexed[names] = temp
print(iifIndexed)
