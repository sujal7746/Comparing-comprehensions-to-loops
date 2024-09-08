#dictionary with integer data
populations = {'city1':1000, 'city2':2000, 'city3': 3000 }
print(populations)

#dictionary using loops
total = 0
for value in populations.values():
    total += value
print({'all cities ': total})

#dictionary using list comprehension
total_population = {'all cities': sum([people for people in populations.values()])}
print(total_population)

#dictionary with list data
populations_two = {'city1 and city2 ': [1000,2000], 'city3, city4 and city5': [3000,4000,5000]}
print(populations_two)

summed_population = {cities : sum(people) for cities, people in populations_two.items()}
print(summed_population)