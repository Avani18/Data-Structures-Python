#Implement all methods of string in Python

#Initialise the strings
str1 = "The leaves are green. The leaves are beautiful."
str2 = "leaves"

#Function find('substring', beg, end) Returns first occurrence of the substring
print ("str2 occurs in str1 at: ", str1.find(str2))

#Function rfind('substring', beg, end) Returns last occurrence of the substring
print ("Last occurrence of str2 in str1 is at: ", str1.rfind(str2))

#Function startswith('substring', beg, end) Returns true if string begins with substring
if (str1.startswith("The")):
	print ("str1 begins with 'The'")
else:
	print ("str1 does not begin with 'The'")
	
#Function endswith('substring', beg, end) Returns true if string ends with substring
if (str1.endswith("dul.")):
	print ("str1 ends with 'dul.'")
else:
	print ("str1 does not end with 'dul.'")
	
#Function islower('string') Returns true if the string is all lower case
if (str1.islower()):
	print ("All characters in str1 are lower case.")
if (str2.islower()):
	print ("All characters in str2 are lower case.")
	
#Function isupper('string') Returns true if the string is all upper case
if (str1.isupper()):
	print ("All characters in str1 are upper case.")
if (str2.isupper()):
	print ("All characters in str2 are upper case.")	
	
#Function lower() Returns a new string with all lower case
print ("Lower case of str1 is: ", str1.lower())

#Function upper() Returns a new string with all upper case
print ("Upper case of str2 is: ", str2.upper())

#Function swapcase() Returns a new string with the swapped case of each character
print ("Swapped case of str1 is: ", str1.swapcase())	

#Function title() Returns a new string with first capital letter of each word
print ("Title case of str1 is: ", str1.title())



#Function len() Returns length of the string
print ("The length of str1 is: ", len(str1))

#Function count('substring', beg, end) Returns count of substring in string
print ("str2 occurs in str1 {} times.".format(str1.count(str2)))

#Function center(length, 'joinstring') Returns a new string of length 'length' with string centered by joinstring
print ("str2 centered with '-' is: ", str2.center(15, '-'))

#Function ljust(length, 'joinstring') Returns a new string of length 'length' with string on left and adjusted by joinstring
print ("str2 left shifted with '-' is: ", str2.ljust(20, '-'))

#Function rjust(length, 'joinstring') Returns a new string of length 'length' with string on right and adjusted by joinstring
print ("str2 right shifted with '-' is: ", str2.rjust(20, '-'))

#Function isaplha() Returns true if all characters are alphabets
if (str1.isalpha()):
	print ("All characters in str1 are alphabets.")
else:
	print ("All characters in str1 are not alphabets.")
	
if (str2.isalpha()):
	print ("All characters in str2 are alphabets.")
else:
	print ("All characters in str2 are not alphabets.")

#Function isalnum() Returns true if all characters are combination of numbers and alphabets	
if ("abc123".isalnum()):
	print ("All characters in string are a combination of numbers and alphabets only.")
else:
	print ("All characters in string are not a combination of numbers and alphabets only.")
	
#Function isspace() Returns true if all characters are spaces
if ("	".isspace()):
	print ("All characters in string are spaces.")
else:
	print ("All characters in string are not spaces.")
	
#Function join(tuple) Returns a new string of tuple joined by string
str3 = ('The', 'leaves', 'are', 'green')
print ("str3 after joining with '-' is: ", '-'.join(str3))


str4 = "----leaves----"

#Function strip('string') Returns a new string with 'string' stripped from the left and right of a string 
print ("str4 after stripping is: ", str4.strip('-'))

#Function lstrip('string') Returns a new string with 'string' stripped from the left of a string 
print ("str4 after left stripping is: ", str4.lstrip('-'))

#Function rstrip('string') Returns a new string with 'string' stripped from the right of a string 
print ("str4 after right stripping is: ", str4.rstrip('-'))

#Function min('string') Returns the smallest character in the 'string'
print ("Smallest character in str2 is: ", min(str2))

#Function max('string') Returns the largest character in the 'string'
print ("Largest character in str2 is: :", max(str2))

str5 = "flowers"

#Function replace('string_to_replace', 'new_string', max) Returns a new string with 'string_to_replace' replaced by 'new_string' max number of times
print ("str1 after replacing 1 value of leaves with flowers is: ", str1.replace(str2, str5, 1))

str6 = "The\tleaves\tare\tgreen"

#Function expandtabs(size) Returns a new string with tabs extended by a given size of spaces, default = 8
print ("Exapnded tabs for str6 are: ", str6.expandtabs())
print ("Expanded tabs for str6 with size 3 are: ", str6.expandtabs(3))
