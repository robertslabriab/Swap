def swapper(letters,message):
	letterOne=letters[0].lower()
	letterTwo=letters[1].lower()
	msg=list(message)
	for x in range(len(msg)):
		if msg[x].lower()==letterOne:
			msg[x]=letterTwo
		elif msg[x].lower()==letterTwo:
			msg[x]=letterOne
	msg="".join(msg)
	return msg
