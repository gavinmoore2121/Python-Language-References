# Each individual file is a module. The syntax 'from module_name import ClassName1, ClassName2'
# can be used to import classes. Any number of classes can be written in a single module. The syntax
# 'from module_name import *' will import all classes and functions from a module, but this is non-standard.

# You can also use 'import module_name as my_module_name' to change the name in your code to something more convenient.

import example_class as space_station


my_rocket = space_station.Rocket()
print("Rocket altitude:", my_rocket.y)
my_rocket.move_up()
print("Rocket altitude:", my_rocket.y)

