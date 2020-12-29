# basic lists, arrays, tuples
# 'list' is the same as an array in Python

empty_list = []
students = ['bernice', 'aaron', 'cody']

# strings can be manipulated as lists
word = list("cats")
del word[1]
print(word)

# list comprehensions: tldr, a dummy amount can be done in a single line.
full_names = [student.title() + " Smith" for student in students]
print(full_names)
squares = [number**2 for number in range(1, 11)]
print("The first 3 squares are %d, %d, and %d" % (squares[0], squares[1], squares[2]))

# 'range' returns all numbers within it.
numbers = list(range(0, 10, 2))
print(numbers)

# accessing a specific element
print(students[0].title())

# find number of elements
elementCount = len(students)

# -1 is the location of the LAST item on the list
# only loops into negatives once: -4, nor 4 exists.
print(students[-1].title())

# iterating through a list
for student in students:
    print("Hello, " + student.title() + "!")

# enumerating allows you to access the index while iterating
for number, student in enumerate(students):
    # this next line shows type conversions
    num = str(number)
    print(num + ' ' + student.title())

# lists are searchable, and return a ValueError if not found. The 'in' keyword returns true or false if
# the value is/isn't in the list.
print("Aaron is at index " + str(students.index('aaron')))
print("Aaron" in students)

# "append" adds an element to the end, or "insert" adds it to the specified index
students.append("edward")
students.insert(1, "harry")

# 'del' removes at the selected index, 'remove' removes the chosen value/element
del students[1]
students.remove('edward')

# 'pop' removes the element at the last index, and returns it
print(students.pop())

# can be reversed
students.reverse()

# pull subset of list:
first_batch = students[0:2]

# also sortable. "Sort" permanently alters the list, while "Sorted" creates a temp copy to print from
# while still preserving the original order.
students.sort()
students.sort(reverse=True)

# 'min', 'max', and 'sum' are usable on numerical lists
print(max(numbers))


# TUPLES
# tuples are immutable lists. Define them with parenthesis instead of brackets. Similar functionality.
example_tuple = (1, 2, 3)

