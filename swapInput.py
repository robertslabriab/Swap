import key
def swapLetters():
	letters=input("What two letters/numbers would you like to swap?\n")
	while len(letters)!=2 or letters[0].lower()==letters[1].lower():
		letters=input("Please enter two different letters/numbers.\n")
	return letters

def swapMessage():
	message=input("What message would you like to swap?\n")
	return message
	
def swapKey():
	keys=key.keyFob()
	newKeys=list(reversed(keys))
	return newKeys
	