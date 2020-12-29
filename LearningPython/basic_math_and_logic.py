# MATH
# ** is the notations for "to the power of"
print(2**3)

# LOGIC
a = 1
b = 2
if a == b:
    print("A = B")
elif a > b:
    print("A > B")
else:
    print("B > A")

# true/false values:
# Empty strings evaluate to false. 0 evaluates to false. All other numbers and strings are true.
# None is a special python value (similar to void) and evaluates to false.

if False:
    print("This is the false keyword, not the string, so this won't print.")

if 'FALSE':
    print("This statement will still evaluate to true.")

if None:
    print("This statement won't print though.")

# GETTING INPUT
user_input = None
while user_input != 'exit':
    user_input = input("Please type something, or 'quit' to exit loop.\n")
    print(user_input)
