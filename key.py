import swapInput
def keyFob():
	numOfKeys=input("How many keys would you like?\n")
	keys=[]
	flag=False
	tracker=0
	if numOfKeys.isnumeric()==True:
		flag=True
	while numOfKeys.isnumeric()==False:
		numOfKeys=input("Please input a number.\n")
		if numOfKeys.isnumeric()==True:
			flag=True
	while tracker<int(numOfKeys) and flag==True:
		newKey=swapInput.swapLetters()
		keys.append(newKey)
		tracker+=1
	return keys