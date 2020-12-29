# Basic string formatting
# single or double quotes
# Note: Python style uses no capital letters and underscores for spaces in variables

# whitespace removal
name = ' \teric\t '

print('My name is %s.' % name.strip().title())
print('-' + name.lstrip() + '-')
print('-' + name.rstrip() + '-')
print('-' + name.strip() + '-')

# changing capitalization
print(name)
print(name.title())
print(name.upper())

# concatenating strings
first_name = 'ada'
last_name = "lovelace"

full_name = first_name + ' ' + last_name

# manipulating strings
full_name = full_name.replace('love', 'shoe')
print(full_name)

names = full_name.split(' ')
print(names)

# SEARCHING strings
# 'find' returns STARTING index of FIRST instance of searched element. 'rfind' finds the last (reverse find)
# both return -1 if not found
print(full_name.find('shoe'))
print(full_name.count('e'))

