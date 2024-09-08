loop_numbers = [] #create an empty list
for number in range(1,101): #use for loop
    loop_numbers.append(number)   #append 100 numbers to list
print(loop_numbers)

#list comprehension
comp_number = [number for number in range(1,100)] #crate a new list
print(comp_number)

#list comprehension with added condition
comp_number_three = [number for number in range(1,100) if number % 3 == 0] #multiple of 3
print(comp_number_three)