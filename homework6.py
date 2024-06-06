my_dict = {'Voronezh': 438, 'Vladimir': 1034}
print(my_dict)
print(my_dict['Voronezh'])
print(my_dict.get('Moscow'))
my_dict.update({'Kazan': 1019, 'Sochi': 186})
print(my_dict.get('Kazan'))
del(my_dict['Kazan'])
print(my_dict)

my_set = {1, 2, 3, 4, True, 2, 3, 4, 'String', True, (1, 2, 3)}
print(my_set)
my_set.add(8)
my_set.add('Integer')
my_set.discard(2)
print(my_set)