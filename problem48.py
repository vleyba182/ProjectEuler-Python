############################################################################################################
#	Project Euler: Problem # 1
#
#	Developed with Python 2.7.6
#
#	2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
#	What is the sum of the digits of the number 21000?
#
############################################################################################################

number = range(1,1001)
sum = 0

for n in number:	
	product = n ** n
	sum += product

sumstring = str(sum)
print sumstring[-10:]