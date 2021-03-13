"""
@Author:Victor Hugo de Barros
"""
def my_function(y, x):
# Age permitted is above 16.
# Hight permitted is above 1.60.
# Supervisor is called when: age equal 11 and hight is equal or greater than 1.50.
# Supervisor is called when: age is equal or greater than 11 and hight equal or less than 1.60.
# Age equal 11, is considerable acceptable if hight sastify the supervisor anaylsis.
# Hight between 1.50 to 1.59, is considerable acceptable if the minimum age of 11, but dependes od suspervisor decisions (analysis).

	age = y                                                                                        #Chained Conditional
	h = x                                                                        #This is an example of chained conditional because it
	if age <= 10 or h <= 1.49:                                                   #[...] it involves more than a branch: "if, elif, else".
		print("disapproved")                                                     #[...] but the function carries out the if on the same indent.
	if age == 11 and h >= 1.50:
            print("Supervisor")
	if age >= 11 and h <= 1.60:
            print("Supervisor")
	if age >= 12 and h >= 1.60:
		print(age, h)
		print("approved")

print(my_function(12, 1.50))

#Nested Conditional
def my_function(y, x, t):                                                                       #Nested Conditional
	eating = t                                                                   #The function shows a nested conditional on the left-side:
	age = y                                                                      #[...] it consists in one or more conditional nesting other conditionals. For
	h = x                                                                        #[...] instance, as you can observe, there is a ''IF'', and the underneath more
	if eating == 'no':
		if age <= 10 or h <= 1.49:
			print("disapproved")
		if age == 11 and h >= 1.50:
			print("Supervisor")
		if age >= 11 and h <= 1.60:
			print("Supervisor")
		if age >= 12 and h >= 1.60:
			print(age, h)
			print("approved")
	else:
		if eating == 'yes':
			print("Unfortunately, you can't get in here eating. Kindly finish it first.")


print(my_function(12, 1.50, 'no'))
