import random

# FOR FINAL QUESTION IGNORE FOR NOW
dictone = {
    "name": "Mufasa",
    "marks": 91,
}

dicttwo = {
    "name": "Scar",
    "marks": 61,
}

dictthree = {
    "name": "Simba",
    "marks": 75.53,
}

dictfour = {
    "name": "Nala",
    "marks": 43,
} 

# Example:
# Generate a random number between 1 and 2
num = random.randint(1,2)

if num == 1:
    name = 'Walid'
else:
    name = 'Kulsoom'

if name == 'Walid':
    print('Hello Walid')
elif name == 'Kulsoom':
    print('Hello Kulsoom')

# Practice ONE:
# Using the random module, generate a random number between 1 and 10
# If the number is greater than 5, print 'Greater than 5'
# If the number is less than 5, print 'Less than 5'

# Practice TWO: FIND THE BUGS AND FIX THEM. There are 4 bugs in this code

# num = random.randint(1,9999)
#if num % 2 > 0?
#    print('This is ODD')
#elseif num % 2 = 0:
#    print{'this is EVEN'}
#

# Practice THREE: create a random number between 1 and 4
# IF the mark is less than 50, print 'Fail'
# IF the mark is between 50 and less than 70, print 'Ds and Cs get degrees'
# IF the mark is between 70-80, print 'Bs get better degrees'
# IF the mark is greater than 80, print ' fking nerd'
# IF no mark is found, print 'No mark found'
# And print the mark and name of the student

# CREATE NUMBER HERE, This number will act as the index for the mark array

marks = [dictone, dicttwo, dictthree, dictfour]


