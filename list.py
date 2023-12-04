a = ['a1', 'a2', 'a3']
b = ['b1', 'b2', 'b3']
for x, y in zip(a, b):
    print(x, y)

#________________________________________________________

a = ['a1', 'a2', 'a3']
b = ['b1', 'b2', 'b3']
result = [x + y for x, y in zip(a, b)]
print(result)

#________________________________________________________

import itertools
 
a = ['a1', 'a2', 'a3']
b = ['b1', 'b2']
 
for x, y in itertools.zip_longest(a, b):
    print(x, y)
#________________________________________________________

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
 
for sublist in nested_list:
    for item in sublist:
        print(item)
#________________________________________________________

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for sublist in nested_list:
    print(*sublist, sep=",")
#________________________________________________________

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = [item for sublist in nested_list for item in sublist]

#________________________________________________________

import pprint
 
pokemon_list = ['Pikachu', 'Abra', 'Charmander']
pprint.pprint(pokemon_list)
#________________________________________________________

import json
 
pokemon_list = ['Pikachu', 'Abra', 'Charmander']
print(json.dumps(pokemon_list))
#________________________________________________________
#________________________________________________________