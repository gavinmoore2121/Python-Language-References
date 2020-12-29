# DECLARATION
# Functions are highly similar to methods in Java. General format:
# def function_name(argument_1, argument_2):
#
# Notably, a return type is not required. Variable types are also not needed
# in the arguments. The return statement will still cause
# the function to return the element and exit.
#
# The function ends when the next line isn't tabbed over. Style guide suggests
# two blank lines after a function definition, and for functions to be declared above
# any 'main' code.

def square(number):
    return number**2


# Functions can handle an arbitrary amount of data. Parameters prefaced with an asterisk are optional, and
# will pass any number of data within them as a tuple.
def sum_function(num_1, num_2, *num_3):
    number_sum = num_1 + num_2
    for value in num_3:
        number_sum += value
    return number_sum


def example_function(string='default'):
    print("This is an example. Your message is '%s'" % string)


# This is the syntax for accepting arbitrary numbers of keyword/value pairs. It's implemented as a dictionary,
# and therefore can utilized as a group or be looped though.
def example_arb_keywords(arg_1, arg_2, **kwargs):
    print('\narg_1:', arg_1)
    print('arg_2:', arg_2)
    print('arg_3:', kwargs)
    for key, value in kwargs.items():
        print(key + ': ' + value)


def describe_person(first_name, last_name, age):
    print("First name: %s" % first_name.title())
    print("Last name: %s" % last_name.title())
    print("Age: %d\n" % age)


print(square(4))
example_function()
# Parameters can be passed in any order, as long as they are labeled. Otherwise, they are added based on order.
describe_person(age=71, first_name='brian', last_name='kernighan')
describe_person(age=70, first_name='ken', last_name='thompson')
describe_person('adele', 'goldberg', 69)
print(sum_function(1, 2))
print(sum_function(1, 2, 3, 4, 5))
example_arb_keywords('a', 'b', value_3='c', value_4='d', value_5='e')
