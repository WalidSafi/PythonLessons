# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is unordered, changeable and does not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values:

walid_dict = {
    "name": "Walid",
    "last_name": "Safi",
    "age": 25,
    "country": "Canada",
    "is_married": False,
}

kulsoom_dict = {
    "name": "Kulsoom",
    "last_name": "Jafri",
    "age": 26,
    "country": "Canada",
    "is_married": False,
}


advanced_dict = {
    "name": "Walid",
    "last_name": "Safi",
    "age": 25,
    "country": "Canada",
    "is_married": False,
    "friends": ["Kulsoom", "Hassan", "Hussain"],
    "skills": ["Python", "Java", "C++"],
    "address": {
        "street": "1234 Main St",
        "city": "Toronto",
        "state": "ON",
        "zip": "M1M1M1"
    }
}

# Practice ONE: #Using the walid_dict print the following: Walid Safi is 25 years old and lives in Canada
# HINT: Access the values using the keys in the dictionary (walid_dict['name'] = 'Walid')

# Practice TWO: 
# #Using the walid_dict and kulsoom_dict print the following: 
# Walid Safi is 25 years and can do a flip reset, Kulsoom Jafri is 26 years old and can do a backflip 

# Practice THREE: USING the DICTONARY METHODS, create an array of the walid_dict and kulsoom_dict

# Practice FOUR: USING the DICTONARY METHODS, using get() method, print the value of the "name" of walid_dict

# Practice FIVE: USING the DICTONARY METHODS, using keys() method, print all the keys of advanced_dict

# Practice SEVEN: USING the DICTONARY METHODS, using items() method, print all the items of advanced_dict

# DICTIOARY METHODS
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary


