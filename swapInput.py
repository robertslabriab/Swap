def swapLetters():
	letters=input("What two letters would you like to swap?\n")
	letterOne=letters[0].lower()
	letterTwo=letters[1].lower()
	
	while len(letters)!=2 or letterOne.isnumeric()==True or letterTwo.isnumeric()==True or letterOne==letterTwo:
		letters=input("Please enter two different letters.\n")
		letterOne=letters[0].lower()
		letterTwo=letters[1].lower()
		
		#make sure to delete in final form
		if letters=="break":
			break
	return letters

def swapMessage():
	message=input("What message would you like to swap?\n")
	return message

#cd\Portfolio\swap
#swapInput.py