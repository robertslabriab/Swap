import swapInput,swapper,key,swappingWithKeys
def swapping():
	positiveAnswer=["yes","y"]
	negativeAnswer=["no","n"]
	haveKey=input("Do you have a key?\n")
	if haveKey.lower() in positiveAnswer:
		recieveKey=input("Did you recieve the key?\n")
		if recieveKey.lower() in positiveAnswer:
			swappedMessage=swappingWithKeys.unswap()
		else:
			swappedMessage=swappingWithKeys.swapUsingKey()
	else:
		swappedMessage=swapper.swapper(swapInput.swapLetters(),swapInput.swapMessage())
	print(swappedMessage)