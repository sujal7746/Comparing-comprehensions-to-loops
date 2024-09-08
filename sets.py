from tuples import number_tuple

number_set = {1,2,3,4}   #sets use curly braces for creation
letter_set = {'a', 'b', 'c', 'd'}
mixed_set = {1, 'a', 2, 'b', 3, 'c', (88, 99)}  #types must be "hashable", i.e, immutable
empty_set = set()                       #have to use the set() function, cannot use = {}

print(number_set)
print(letter_set)
print(mixed_set)
print(empty_set)

print(type(number_set))

number_set_unique = {1,1,1,2222,444,444} #sets only store unique values
print(number_set_unique)

number_set.add(5)
print(number_set)

number_set.remove(2)
print(number_set)

try:
    number_set.remove(98)  #if the item is not in the set
except Exception as e:
    print("caught Exception" , e)  #key error 98

print(98 in number_set) #false
print(3 in number_set)  #true