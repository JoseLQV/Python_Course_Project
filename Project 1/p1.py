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
    
    
    #-------- Code Here Task 2: -------------
    elif Option == 2:
        
        # Verification of float input
        valid = False
        while valid != True:   
            try:
                num = float(input("Enter a float number: "))
                
                if type(num) != float:
                    continue
                else:
                    break
            
            except:
                # If the input cannot be converted to an integer, prompt the user again
                print("Invalid input. Please enter a valid input.")
                        

            
        Conversion_Menu = int(input(
            "\nChoose the unit to convert:\n"
            "(1) Pressure units\n"
            "(2) Wind Speed units\n"))
        
        if Conversion_Menu == 1:
            Pressure_Menu = int(input(
            "\nSelect Original Pressure Unit and Value:\n"
            "(1) Pascal (Pa)\n"
            "(2) Atmosphere (atm)\n"
            "(3) Bar (bar)\n"))
            
            Convert_menu = int(input(
            "\nConvert Pressure Unit too:\n"
            "(1) Pascal (Pa)\n"
            "(2) Atmosphere (atm)\n"
            "(3) Bar (bar)\n"))
            
            if Pressure_Menu == 1 and Convert_menu == 2: # Pascal -> Atm
                # 1 pascal = 9.8692 * 10 ** -6 (atm)
                convert = num * (9.8692 * (10**-6))
                print("Pascal -> Atm",convert)
            elif Pressure_Menu == 1 and Convert_menu == 3: # Pascal -> Bar
                # 1 pascal = 0.00001 (bar)
                convert = num * (0.00001)
                print("Pascal -> Bar",convert)
            elif Pressure_Menu == 2 and Convert_menu == 1: # Atm -> Pascal
                # 1 atm = 101325 pa
                convert = num * (101325)
                print("Atm -> Pascal",convert)
            elif Pressure_Menu == 2 and Convert_menu == 3: # Atm -> Bar
                # 1 Atm = 1.01325
                convert = num * (1.01325)
                print("Atm -> Bar",convert)
            elif Pressure_Menu == 3 and Convert_menu == 1: # Bar -> Pascal
                # 1 pascal = 100000(bar)
                convert = num * (100000)
                print("Bar -> Pascal",convert)
            elif Pressure_Menu == 3 and Convert_menu == 2: # Bar -> Atm
                # 1 pascal = 0.98692 (bar)
                convert = num * (0.98692)
                print("Bar -> Atm",convert)
            elif Pressure_Menu == Convert_menu:
                print("Base Conversion are the same:",num)
            else:
                print("Invalid Option")
            
            
        elif Conversion_Menu == 2:
            Wind_speed_units = int(input(
            "\nEnter the original wind speed unit:\n"
            "(m/s) Meters per second \n"
            "(km/h) Kilometers per hour\n"
            "(mph) Miles per hour\n"))
            
            Convert_menu = int(input(
            "\nConvert wind speed unit too:\n"
            "(m/s) Meters per second \n"
            "(km/h) Kilometers per hour\n"
            "(mph) Miles per hour\n"))
            
            if Wind_speed_units == 1 and Convert_menu == 2: # m/s -> km/h
                # 1 m/s = 3.6 km/h
                convert = num * (3.6)
                print("Pascal -> Atm",convert)
            elif  Wind_speed_units == 1 and Convert_menu == 3:#m/s ->mph
                # 1 m/s = 2.23694 mph
                convert = num * (2.23694)
                print("Pascal -> Bar",convert)
            elif  Wind_speed_units == 2 and Convert_menu == 1: #km/h -> m/s
                # 1 km/h = 0.277778 m/s
                convert = num * (0.277778)
                print("Atm -> Pascal",convert)
            elif  Wind_speed_units == 2 and Convert_menu == 3: #km/h -> mph
                # 1 km/h = 0.621371
                convert = num * (0.621371)
                print("Atm -> Bar",convert)
            elif  Wind_speed_units == 3 and Convert_menu == 1: # mph -> m/s
                # 1 mph = 0.44704 m/s
                convert = num * (0.44704)
                print("Pascal -> Bar",convert)
            elif  Wind_speed_units == 3 and Convert_menu == 2: # mph -> km/h
                # 1 mph = 1.60934
                convert = num * (1.60934)
                print("Pascal -> Bar",convert)
            elif  Wind_speed_units == Convert_menu:
                print("Base Conversion are the same:",num)
            else:
                print("Invalid Option")
            
        else:
            print("Invalid Input")
        

        
            
        
            
        
        print("You chose option 2")
    elif Option == 3:
        print("You chose option 3")
    elif Option == 0:
        print("Exiting the program...")
        Exit = True
    else:
        print("Invalid option")
        
        
        
    # --------- Task 2 Step by Step: ------------
    # Task 2A
    #-> Return too Main Menu (Done)
    #-> Valid Inputs in Menu (Done)
    #-> Option 2 input must be Float, else try again input 
    
    
    
    
    