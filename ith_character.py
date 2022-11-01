#python code to demonstrate
#method to remove ith character
#using join() + list comprehension
#Initializing string 
test_str = "GeeksForGeeks"
print("The original string is : " + test_str)
#removing charecter at pos 3
#using join() + list comprehension
new_str = ''.join([test_str[i] for i in range(len(test_str)) if i != 2])
#printing string after removal
#removes ele. at 3rd index
print("The string after removal of ith character: " + new_str)	