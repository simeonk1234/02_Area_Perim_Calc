# functions go here

# checks input is a number more than zero

def num_check(question):
    valid = False
    while not valid:

        error = "Please enter a number that is more than zero"

        try:

            response = float(input(question))

            if response > 0:
                return response

            else: 
                print(error)
                print()

        
        except ValueError:  
                print(error)




# main routine goes here

keep_going = ""
while keep_going == "":

    width = num_check("Width: ")
    height = num_check("Height: ")


    area = width * height

    perimeter = 2 * (width + height)

    print("Perimeter: {} units".format(perimeter))
    print("Area: {} square units".format(area))
    print()

    keep_going = input("Press <enter> to keep going or any key to quit")

print()
print("Thanks for using the area / perimeter calculator")