
# Indefinite Arguments (**kwargs) Practice #1
# Create a function called number_attributes that counts the number of parameters that are passed, and returns that number as the result.

def number_attributes(*args):
    return len(args)
print(number_attributes(1, 2, 3))   # returns 3
print(number_attributes("a"))       # returns 1
print(number_attributes())          # returns 0








# Indefinite Arguments (**kwargs) Practice #2
# Create a function called list_attributes that returns in the form of a list the values of the attributes given in the form of keywords. The function must expect to receive any number of arguments of this type.

def list_attributes(*args):
    return len(args)
print(keywords_attributes(what, six, elite)) #returns elite
print(keywords_attributes("b"))              #returns six
print(number_attributes())









# Indefinite Arguments (**kwargs) Practice #3
# Create a function called describe_person, which takes his name as parameters and then an indeterminate number of arguments. This function should display on the screen:

# Characteristics of {name}:
# {argument_name}: {argument_value}
# {argument_name}: {argument_value}
# etc...
# For example:

# describe_person("Ash", eye_color="brown", hair_color="black")

# Will print to the screen:

# Characteristics of Ash:
# eye_color: brown
# hair_color: black

def describe_person(Ash, eye_color, hair_color):
    print(describe_person("Ash", eye_color="brown", hair_color="black"))