import swapInput,swapper,key
def unswap():
	keyList=swapInput.swapKey()
	tracker=0
	while tracker<len(keyList):
		if tracker==0:
			swappedMessage=swapper.swapper(keyList[tracker],swapInput.swapMessage())
		else:
			swappedMessage=swapper.swapper(keyList[tracker],swappedMessage)
		tracker+=1
	return swappedMessage
	
def swapUsingKey():
	keyList=key.keyFob()
	tracker=0
	while tracker<len(keyList):
		if tracker==0:
			swappedMessage=swapper.swapper(keyList[tracker],swapInput.swapMessage())
		else:
			swappedMessage=swapper.swapper(keyList[tracker],swappedMessage)
		tracker+=1
	return swappedMessage