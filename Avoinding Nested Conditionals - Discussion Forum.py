"""
@Author:Victor Hugo de Barros
"""
#Example of avoinding, Nested Conditionals.
#[...]Instead as mentioned before, we can simply inputting some relational operators,
#[...]Boolean Expression and logical operators in one branch, instead creating many.

def nested_function(y, x, g):                                                                       #Nested Functional
    gender = y
    weight = x
    height = g
    if gender == "male":
        if height >= 1.60 and height <= 1.70:
            if weight >= 50 and weight <= 60:
                print("You are in good shape.")
    else:
        print("you need make better. Keep it up.")


print(nested_function("male",  60, 1.70))


# Above with Nested Conditional. ↑
#---------------------//--------------------------
# Bellow avoinding Nested Conditionals. ↓                                                           #Avoinding Nested Conditionals
                                                                                            #Here some of the all Logical Operators, Relational Operators,
                                                                                            #[...] and Bolean Expressions

#Avoiding Nested Conditionals:
def avoid_conditionals(y, x, g):
    gender = y
    weight = x
    height = g
    if gender == "male" and height >= 1.60 and height <= 1.70 and weight >= 50 and weight <= 60: # <<<-------Equivalent single conditional.
        print("You are in good shape.")
    else:
        print("you need make better. Keep it up.")


print(avoid_conditionals("male",  60, 1.70))
