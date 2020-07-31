#!/usr/bin/python

import hashlib
import sys
import pexpect


answered = False

#hex_match = sys.argv[1]


def Process_Output(output):

	output = output.decode("utf-8")
	output.replace('\r\n \r\n', '')
	print(output)


	split_output = output.split()
	print(split_output[-1])
	return split_output[-1]





def computeMD5hash(my_string):

	m = hashlib.md5()
	m.update(my_string.encode('utf-8'))
	return m.hexdigest()

def searchFile(hex_match):

	with open("/usr/share/wordlists/rockyou.txt") as infile:

		try:
			for line in infile:

				md5_hash = computeMD5hash(line.rstrip())

				if (md5_hash.startswith(hex_match)):
					print(md5_hash + "  " + line)
					return line
		except:
			pass

		send = "end"
		return send

while(answered == False):

	process = pexpect.spawn('nc jh2i.com 50005')

	process.expect('\S .*')

	prefix = Process_Output(process.after)

	send = searchFile(prefix)

	print(str(send).strip())

	if(send != "end"):
		
		

		process.sendline(str(send).strip())

		process.expect('\S .*')

		answer = process.after

		print (answer)

		answered = True
