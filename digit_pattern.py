def pattern(n):
	#traverse through the elements
	#in n assuming it as a string
	for i in n:
		#print | for every line 
		print("|", end = "")
		#print i number of * S in 
		#each line 
		print("*" * int(i))
#get the input string
n = "41325"
pattern(n)