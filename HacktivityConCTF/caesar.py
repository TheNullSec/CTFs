#!/usr/bin/python3

import sys

mapping = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

offset = 13

if(len(sys.argv) > 2):
	offset = int(sys.argv[2])

new_string = ""


def get_key(val): 
    for key, value in mapping.items(): 
         if val == value: 
             return key 


with open(sys.argv[1], 'r') as caesar_file:

	caesar_text = caesar_file.read().upper()
	#print(caesar_text)
	x = 0
	while(x < len(caesar_text)):
		if(caesar_text[x] in mapping.keys()):
			initial_number = mapping[caesar_text[x]]
			if(initial_number <= offset):
				initial_number = initial_number + 26
			final_number = initial_number - offset
			new_string = new_string + get_key(final_number)

		else:
			new_string = new_string + caesar_text[x]
		
		x = x + 1
		

print(new_string)
