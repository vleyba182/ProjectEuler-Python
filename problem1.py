############################################################################################################
#	Project Euler: Problem # 1
#
#	Developed with Python 2.7.6
#
# 	If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
#	The sum of these multiples is 23.
#
# 	Find the sum of all the multiples of 3 or 5 below 1000.
#
############################################################################################################

count = 0
totalsum = 0

while (count < 1000):
	if count % 3 == 0 or count % 5 == 0:
		totalsum = totalsum + count
	count = count + 1
print(totalsum)