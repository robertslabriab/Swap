import swapInput,swapper,key
def swapping():

	positiveAnswer=["yes","y"]
	negativeAnswer=["no","n"]
	haveKey=input("Do you have a key?\n")
	if haveKey.lower() in positiveAnswer:
		keyList=key.keyFob()
		tracker=0
		while tracker<len(keyList):
			if tracker==0:
				swappedMessage=swapper.swapper(keyList[tracker],swapInput.swapMessage())
			else:
				swappedMessage=swapper.swapper(keyList[tracker],swappedMessage)
			tracker+=1
	else:
		swappedMessage=swapper.swapper(swapInput.swapLetters(),swapInput.swapMessage())
	print(swappedMessage)