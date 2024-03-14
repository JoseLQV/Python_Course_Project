#NAME: Jose Luis Quinones Velez  843-18-5449
#Code: 
#Program: VS code , python

import math #We will learn more about the math library later. no need to modifiy this line.

BORDER_COUNT = 25
STAR_BORDER = "*" * BORDER_COUNT
Exit = False
print("\n" + STAR_BORDER + "\nPROJECT I\n" + STAR_BORDER)# this line only print a lint of asterisks
# do not delete the following block of instructions

while Exit == False:
    Option = int(input(
        "\nSelect option:\n"
        "(1) Area of figures\n"
        "(2) Units conversion\n"
        "(3) Base conversion\n"
        "(0) Exit\n"))  
    #Add the code needed to display the following menu and to complete the task 1a
    if Option == 1:
        Area_calculation = int(input(
            "\nSelect option:\n"
            "(1) Area of a SQUARE\n"
            "(2) Area of a RECTANGLE\n"
            "(3) Area of a CIRCLE\n"
            "(4) Area of a TRIANGLE\n"))

        if 1<=Area_calculation<=4:#in [1,2,3,4]: #  ASSUME THE INPUTS ARE INTEGER NUMBERS.
            #IN THIS PHASE YOU DON'T NEED TO VERIFY IF THE INPUT IS AN INTEGER OR A NUMERIC VALUE 
            #Add your code to complete the tasks
            
            if Area_calculation == 1: #Area of a Square (area = x*x)
                length_side = int(input(" Enter the length of the side: "))
                area = length_side * length_side
                
            elif Area_calculation == 2: #Area of a Rectangle (area = b*h)
                base = int(input(" Enter the base magnitude: "))
                height = int(input(" Enter the height magnitude: "))
                area = base*height
            
            elif Area_calculation == 3: #Area of a Circle (area = pi * radius)
                radius = int(input(" Enter the magnitude of the radius:"))
                area = math.pi * (radius*radius)
                
            elif Area_calculation == 4: #Area of a Triangle (area = 1/2(b*h))
                base = int(input(" Enter the base magnitude: "))
                height = int(input(" Enter the height magnitude: "))
                area = (1/2)*(base*height)
                
            #------- Small Figures -----------
            fit = str(input("You want to check how many small figures will fit in the initial figure? (y or n) "))
            
    #         ● If yes, the program will ask for the area of the small figure.
    #               ○ Then it will print the number of times the small figure will fit in the first figure. 
            if fit == "y":
                small_area = int(input("Enter area of small figure: "))
                if small_area <= area: # small area not bigger than initial figure
                    count = math.floor(area/small_area)
                    print(f"Small figure count: {count}")
                
                else: #Small figure is bigger than the initial area
                    print(f"Small figure count: {0}")


    #         ● If not, the program will show the area of the first figure. 
            elif fit == 'n':
                print("Area:",area)
                
                
            else:
                print("Invalid input")
            
                
        else:
            print("Invalid input")
    
    elif Option == 2:
        print("You chose option 2")
    elif Option == 3:
        print("You chose option 3")
    elif Option == 0:
        print("Exiting the program...")
        Exit = True
    else:
        print("Invalid option")