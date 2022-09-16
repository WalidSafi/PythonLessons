# For loops are used when you know how many times you want to repeat a block of code

# range() is a built in function that creates a list of numbers from 0 to the number you pass in
# range(10) will create a list of numbers from 0 to 9
# range(1,10) will create a list of numbers from 1 to 9
# range(1,10,2) will create a list of numbers from 1 to 9, but only print the odd numbers

# range(start, stop, step) if you only pass in one number, it will be the stop, if you pass in two numbers, it will be start and stop
# range(-20, 20) will create a list of numbers from -20 to 19, the size of the list will be 40

ran = range(-50, 50)

for i in ran:
    print(i)

#PRACTICE, create a for loop that prints the numbers 1-100

#PRACTICE, create a for loop that from numbers 1-100, but only print the even numbers

#PRACTICE, create a for loop that from numbers 1-100, but only print numbers divisible by 7

# You can loop through a string, and print each character

for i in 'Hello World':
    print(i)

#PRACTICE, create a for loop that prints only the 'o' in the string 'Hello World'

#PRACTICE, create a for loop that loops from 1 to 100, and create two variables, one that stores the sum of all the numbers 