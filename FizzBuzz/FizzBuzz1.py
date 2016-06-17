#    Have a hard-coded upper line, n.
#    Print "Fizz buzz counting up to n", substituting in the number we'll be counting up to.
#    Print out each number from 1 to n, replacing with Fizzes and Buzzes as appropriate.
#    Print the digits rather than the text representation of the number (i.e. print 13 rather than thirteen).
#    Each number should be printed on a new line.

top_value = 100
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