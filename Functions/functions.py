# Functions are peices of code that can be called from other parts of the program
# They are used to reduce code duplication and make the code more readable
# Functions are defined using the def keyword

def print_hello():
    print("Hello")

print_hello()

#PRACTICE, create a function that prints "Hello World"



# Functions can take parameters, which are values (Can be hard-coded, or a variable) that are passed to the function

# Example, create a function that takes a name as a parameter, and prints "Hello <name>"
def print_name(name): # name is a parameter!
    print("Hello", name)

# To call the function, you must pass a value to the parameter
print_name("Walid") # Walid is an argument!

name = "Safi"
print_name(name) # Safi is an argument!

#PRACTICE, You can pass multiple parameters to a function

def print_many(name, occupation):
    print("Hello", name, "You are a", occupation)

print_many("Walid", "Programmer")

#PRACTICE, create a function that takes a name and a description as parameters, and prints "<name> is a <description>"


#PRACTICE, create a function that takes a name and a description as parameters, and prints "<name> is a <description>", but only if the name is Walid


#PRACTICE create a function that does something with the names array. Loop through the array and call the function with each name

names = ['Walid', 'Safi', 'Ahmad', 'Al-Abdul-Walid']



# Functions can return values, which are values that are returned from the function
def add_two_numbers(num1, num2):
    return num1 + num2 # return is a keyword that returns a value from the function

answer = add_two_numbers(5, 10)
print(answer)

#PRACTICE, create a function that takes two numbers as parameters, and returns the remainder of the two numbers


# Functions can be called from other functions

# Create two functions called get_name and get_occupation
# get_name should return a name
# get_name should call get_occupation 