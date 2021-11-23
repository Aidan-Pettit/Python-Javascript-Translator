# This will turn into "console.log"
print('Welcome!')

# And these variables will be prefixed with "let"
num1 = 1
num2 = 2

# Arithmetic operations are basically the same
sum = num1 + num2

# Brackets are added around if statements
if sum == 3:
    print('The sum is 3!')

# Have you noticed that the comments changed too?
# "#" turned into "//"

# Additionally, some other keywords are different
# True -> true
True
# False -> false
False
# None -> null
None
# and -> &&
num1 < num2 and sum == 3
# or -> ||
num1 < num2 or sum == 3

# Finally, loops and functions (as well as if statements) have curly
# braces placed around them.

list = [1, 2, 3]

for item in list:
    print(item)

counter = 0

while counter <= 10:
    print(counter)
    counter += 1


def greet(name):
    print('Hello, my name is ', name)


# And that's it! Thank you for looking at this transator!
print('Thank you so much!')

# Don't forget to try running the new file with node!
