#!/bin/python3

dictionary = {}

character1 = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"

numbers = list(range(1,27))

#keys = []
#values = []

keys = character1.split()

values = numbers

print(values)

x = 0

while(x < len(keys)):
	dictionary[keys[x]] = values[x]
	x = x + 1
print(dictionary)
