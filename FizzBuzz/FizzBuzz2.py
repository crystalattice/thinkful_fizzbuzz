#    Have a hard-coded upper line, n.
#    Print "Fizz buzz counting up to n", substituting in the number we'll be counting up to.
#    Print out each number from 1 to n, replacing with Fizzes and Buzzes as appropriate.
#    Print the digits rather than the text representation of the number (i.e. print 13 rather than thirteen).
#    Each number should be printed on a new line.

#    If the user supplies a value at the command line when script runs, we'll use that value.
#    Otherwise, we'll use the input() function to get a value from the user.

import sys

if len(sys.argv) > 1:
    entered_value = int((sys.argv[1]))
else:
    entered_value = int(input("Please enter a value: "))

top_value = entered_value

print ("Fizz buzz counting up to {0}".format(top_value))
entry = 1
while entry <= top_value:
    if entry % 3 == 0 and entry % 5 == 0:
        outry = "FizzBuzz"
    elif entry % 3 == 0:
        outry = "Fizz"
    elif entry % 5 == 0:
        outry = "Buzz"
    else: outry = entry
    print (outry)
    entry += 1