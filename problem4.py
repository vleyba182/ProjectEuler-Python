############################################################################################################
#	Project Euler: Problem #4
#
#	Developed with Python 2.7.6
#
#	A palindromic number reads the same both ways. The largest palindrome made from the product of two
#	2 digit numbers is 9009 = 91 * 99.
#
#	Find the largest palindrome made from the product of two 3-digit numbers.
#
############################################################################################################

#Declare variables needed for program
number_1 = range(100, 1000)
number_2 = range(100, 1000)
max_palindrome = 0

#for ever 3 digit number find all possible products
for n1 in number_1:
	for n2 in number_2:
		product = n1 * n2

		#check if product is palindrome
		if product == int(str(product)[::-1]):	#

			#keep track of largest palidrome fund
			if product > max_palindrome:		
				max_palindrome = product 	
					
#print the max palidrome product found			
print max_palindrome 				

