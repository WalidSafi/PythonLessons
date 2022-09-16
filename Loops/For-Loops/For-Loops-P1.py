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