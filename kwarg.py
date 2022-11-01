#def printKwargs(**kwargs):
#	print(kwargs)

#driver code
#if __name__ == "__main__":
#	printKwargs(Argument_1='gfg', Argument_2='GFG')
def concatenate(**arguments):
	#initialising empty string
	final_str = ""
	#Iterating over the python kwargs
	#dictionary
	for elements in arguments.values():
		final_str += elements
	return final_str

	#driver code 
if __name__ == '__main__':
	print(concatenate(a="g", b="F", c="g"))