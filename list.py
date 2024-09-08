#----------Lists--------------


number_list = [1,2,3,4]   #list use square brackets for creation
letter_list = ['a', 'b', 'c', 'd']
mixed_list = [1, 'a', 2, 'b', 3, 'c', [88,99]] #can also nest  lists within lists

print(number_list)
print(letter_list)
print(mixed_list)

print(type(number_list))

original_value = number_list[0]     #save the value in index 0
number_list[0] = 9                   #lists are mutable, can change items once assigned
print(number_list)

number_list[0] = original_value     #reassign original value
print(number_list)

number_list.append(5)  #add value in list via append
print(number_list)

number_list += [6]     #add item in list via operator
print(number_list)

new_number_list = number_list[:]  #copy entire list via slicing
print(new_number_list)
print(id(number_list))
print(id(new_number_list))  #different id
print()

other_number_list = number_list   #create second reference to same list objects
print(id(number_list))            # same ids
print(id(other_number_list))       # pointing to the same object

number_list.append(99)      #append to first list
print(other_number_list)    #print other number list this also show new value

print(number_list[:])
print(number_list[1:3])
print(number_list[3:])

