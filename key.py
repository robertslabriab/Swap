import swapInput
def keyFob():
	keys=input("How many keys would you like?\n")
	numOfKeys=[]
	flag=False
	tracker=0
	
	if keys.isnumeric()==True:
		flag=True
	
	while keys.isnumeric()==False:
		keys=input("Please input a number.\n")
		if keys.isnumeric()==True:
			flag=True
	while tracker<int(keys) and flag==True:
		newKey=swapInput.swapLetters()
		numOfKeys.append(newKey)
		tracker+=1
	return numOfKeys
