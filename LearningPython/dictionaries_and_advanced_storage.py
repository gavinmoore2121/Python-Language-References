# Dictionaries
# Dictionaries store key-value pairs, similar to hashmaps in Java
# Any data structure, including a list, tuple, or another dictionary, can be stored as the value.
# They are not ordered: pairs will be returned in random orders. Using sorted(sample_dictionary)
# can be used to solve this.

sample_dictionary = {'sample1': 1, 'sample2': 2, 'sample3': 3}
print(sample_dictionary)
print("sample 1's value is: %d" % sample_dictionary['sample1'])

del sample_dictionary['sample2']
sample_dictionary['sample3'] = 2

# dictionary.items() pulls all key/value pairs into a list of tuples and returns it
print('Example of behavior in loops:')
for key, value in sample_dictionary.items():
    print(key)
    print(value)
