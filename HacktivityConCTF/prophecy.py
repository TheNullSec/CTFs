#!/usr/bin/python3

import pexpect
import time

program_complete = False

last_iteration = 0

current_iteration = 1

number_list = []


def Process_Output(output):
	
	output = output.decode("utf-8")
	output.replace('\r\n \r\n', '')
	print(output)

	
	if(any(char.isdigit() for char in output)):
		split_output = output.split()
		print(split_output[-1])
		return split_output[-1]


	else:
		print("Program Finished!")
		program_complete = True
		return 0





while(program_complete == False):
	current_iteration = 1
	process = pexpect.spawn('nc jh2i.com 50012')
	process_alive = True
	print(number_list)

	while(process_alive == True and last_iteration >= current_iteration):

		process.expect('>')

		process.sendline(number_list[current_iteration - 1])

		current_iteration = current_iteration + 1

	process.expect('>')

	process.sendline('1')

	process.expect('\S .*')

	last_iteration += 1

	#print(process.after)

	number_list.append(Process_Output(process.after))

	#time.sleep(1)







