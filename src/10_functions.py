# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even():
    # Read a number from the keyboard
    num = input("Enter a number: ")
    num = int(num)

    # Print out "Even!" if the number is even. Otherwise print "Odd"
    if(num%2==0): 
        print("Even!")
        return True
    else: 
        print("Odd!")
        return False

# YOUR CODE HERE
is_even()
