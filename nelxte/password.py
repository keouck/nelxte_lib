#--- Metadata ---#

__author__ = "Amay Agarwal"
__license__ = "MIT License"
__version__ = "1.0"
__maintainer__ = "Amay Agarwal"
__email__ = "amayagarwal428@gmail.com"
__status__ = "Production"

import re #--- Import the regex library ---#

spec_chars = re.compile('[@`_!#$%^&*()<>?=+/|}{~:]') #--- Compile a list of special characters ---#
l_alphabets = re.compile('[a-z]') #--- Compile a list of lower case alphabets ---#
u_alphabets = re.compile('[A-Z]') #--- Compile a list of upper case alphabets ---#
nums = re.compile('[0-9]') #--- Compile a list of numbers ---#

def detect_character(pass_string, character_set): #--- Define a function to search strings for a given list of characters ---#
	if(character_set.search(pass_string) == None): #--- If the character isn't in the string, return false ---#
		res = False
	else: #--- If the character is in the string, return false ---#
		res = True
	return(res)

def check(password, min_length=8, max_length= 200, special_chars=True, numbers=True, upper_case=True, lower_case=True, common_password=True):
	
	#--- Check whether the data entered by user is in correct format, else raise a type error ---#

	if type(password) != str:
		raise TypeError('argument password must be str')
	elif type(min_length) != int:
		raise TypeError('argument min_length must be int')
	elif type(max_length) != int:
		raise TypeError('argument max_length must be int')
	elif type(special_chars) != bool:
		raise TypeError('argument special_chars must be bool')
	elif type(numbers) != bool:
		raise TypeError('argument numbers must be bool')
	elif type(upper_case) != bool:
		raise TypeError('argument upper_case must be bool')
	elif type(lower_case) != bool:
		raise TypeError('argument lower_case must be bool')
	elif type(common_password) != bool:
		raise TypeError('argument common_password must be bool')



	if len(password) < min_length or len(password) > max_length: #--- Check if the length of the password matches the criteria set ---#
		return 'password must be shorter than {} characters and longer than {} characters.'.format(max_length, min_length) #--- if not, then return the criteria ---#

	#--- Check for special characters if the parameter is true ---#

	if special_chars == True:
		output = detect_character(password, character_set=spec_chars)

		if output == True:
			pass
		else:
			return 'Password must contain atleast one special character.' #--- Else, return error statement ---#
	else:
		pass

	#--- Check for numbers if the parameter is true ---#	

	if numbers == True:
		output = detect_character(password, character_set=nums)

		if output == True:
			pass
		else:
			return 'Password must contain atleast one number.' #--- Else, return error statement ---#
	else:
		pass

	#--- Check for lower case alphabets if the parameter is true ---#

	if lower_case == True:
		output = detect_character(password, character_set=l_alphabets)

		if output == True:
			pass
		else:
			return 'Password must contain atleast one lower case alphabet.' #--- Else, return error statement ---#
	else:
		pass

	#--- Check for upper case alphabets if the parameter is true ---#

	if upper_case == True:
		output = detect_character(password, character_set=u_alphabets)

		if output == True:
			pass
		else:
			return 'Password must contain atleast one upper case letter.' #--- Else, return error statement ---#
	else:
		pass

	if common_password == True:
		f = open('passwords.txt')
		f = f.read()
		f = f.split('\n')
		for i in f:
			if i == password:
				return 'This password is very common. Please use something stronger.'
			else:
				pass
	else:
		pass

	return 'OK' #--- Return, 'OK' if the password is fine ---#