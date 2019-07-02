def swapper(letters,message):
	letterOne=letters[0].lower()
	letterTwo=letters[1].lower()
	msg=list(message)
	for x in range(len(msg)):
		if msg[x].lower()==letterOne:
			if msg[x]==letterOne.upper():
				msg[x]=letterTwo.upper()
			else:
				msg[x]=letterTwo
		elif msg[x].lower()==letterTwo:
			if msg[x]==letterTwo.upper():
				msg[x]=letterOne.upper()
			else:
				msg[x]=letterOne
	msg="".join(msg)
	return msg