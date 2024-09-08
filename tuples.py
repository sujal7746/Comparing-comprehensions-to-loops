#----------tuples------------
number_tuple = (1,2,3,4)   #tuples use parentheses for creation
letter_tuple = ('a', 'b', 'c', 'd')
mixed_tuple = (1, 'a', 2, 'b', 3, 'c', [88,99]) #can mix different types

print(number_tuple)
print(letter_tuple)
print(mixed_tuple)

print(type(number_tuple))      #<class 'tuple'>

try:
    number_tuple[0] = 9     #tuples are immutable, cant change item once assigned
except Exception as e:
    print(' Caught Exception  ', e) #typeerror: 'tuple' object does not support item assigned

try:
    new_number_tuple = number_tuple + (5) #try to add item to tuples by creating a tuple
except Exception as e:                      #typeerror: can only concatenate tuple (not "int") to tuple
    print(' Caught Exception  ', e)

new_number_tuple = number_tuple + (5, )  #have to add a comma to make it a tuple
print(new_number_tuple)

number_tuple = number_tuple + (5,)
print(number_tuple)
print(id(number_tuple))

number_tuple = number_tuple + (6,)
print(id(number_tuple))

print(number_tuple[:])           # slice operator - entire tuple
print(number_tuple[1:3])
print(number_tuple[3:])