#!/usr/bin/python3

import socket
import time


def split(word): 
	return [char for char in word]


x = 0
y = 1

letters = "abcdefghijklmnopqrstuvwxyz"

letterList = split(letters)
print(letterList)



table = {" " : "0"}



while(y < 27):

	table[letters[y - 1]] = str(y)
	y = y + 1


while(x <= 100):

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("jh2i.com",50034))



	msg = s.recv(1024)
	msg = msg.decode("utf-8")
	
	letterComp1 = msg[0]
	

	s.send(bytes("send back this line exactly. no flag here, just filler.", "utf-8"))
	msg = s.recv(1024)
	msg = str(msg)
	msg = msg.replace("b\'","")
	msg = msg.replace("b\"", "")
	msg = msg.replace("\\n\'", "")
	msg = msg.replace("\\n\"", "")



	letterComp2 = msg[0]
	
	
	
	if(0 <= (int(table.get(letterComp1)) - int(table.get(letterComp2)))):
		degree = int(table.get(letterComp1)) - int(table.get(letterComp2))

	else:
		degree = int(table.get(letterComp1)) + abs(int(table.get(letterComp1)) - int(table.get(letterComp2)))


	splitter = msg.split(". ");
	msg = splitter[1]


	x = x + 1

	s.close()


	z = 0

	result = ""

	while(z<=len(msg) - 1):

	
		subjectLetter = msg[z]
	
		if(subjectLetter == " "):
			result = result + subjectLetter

		elif(subjectLetter in letterList):
			subjectNumber = int(table.get(subjectLetter, subjectLetter))
			#print(subjectNumber)
			if((subjectNumber + degree) > 26):

				subjectCalc = (subjectNumber + degree) 

				resultNumber = subjectCalc - 26
				#print(resultNumber)
			else:
				resultNumber = subjectNumber + degree
				#print(resultNumber)

			for letterie, numberie in table.items():
				if int(numberie) == int(resultNumber):
					#print(letterie)
					result = result + letterie

		else:
			result = result + subjectLetter
		
		z = z + 1

	print(result)




