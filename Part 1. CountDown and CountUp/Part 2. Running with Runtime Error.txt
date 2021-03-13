def my_function(y, x):
# Age permitted is above 16.
# Hight permitted is above 1.60.
# Supervisor is called when: age equal 11 and hight is equal
#[...] or greater than 1.50.
# Supervisor is called when: age is equal or greater than 11 and
#[...] hight equal or less than 1.60.
# Age equal 11, is considerable acceptable if hight sastify
#[...]the supervisor anaylsis.
# Hight between 1.50 to 1.59, is considerable acceptable if the
#[...] minimum age of 11, but dependes od suspervisor decisions (analysis).

	age = y
	h = x
	if age <= 10 or h <= 1.49:
		print(age, h)
		print("disapproved")
	if age == 11 and h >= 1.50:
	if age >= 11 and h <= 1.60:
            print("Supervisor")
	if age >= 12 and h >= 1.60:
		print(age, h)
		print("approved")

print(my_function(12, 1.50))