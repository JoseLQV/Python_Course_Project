#NAME: Jose Luis Quinones Velez  843-18-5449
#Code: Task 1 + Task 2
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
        
            
        Conversion_Menu = int(input(
            "\nChoose the unit to convert:\n"
            "(1) Pressure units\n"
            "(2) Wind Speed units\n"))
        
        
        # Verification of float input
        valid = False
        while valid != True:   
            try:
                num = float(input("Enter unit value: "))
                
                if type(num) != float:
                    continue
                else:
                    break
            
            except:
                # If the input cannot be converted to an integer, prompt the user again
                print("\nInvalid input. Please enter a valid input.\n")
        
        if Conversion_Menu == 1:
            Pressure_Menu = str(input(
            "\nEnter initial units:\n"
            "(Pa) Pacal\n"
            "(atm) Atmosphere\n"
            "(bar) Bar\n"))
            
            if Pressure_Menu == "Pa":
                atm =  num * (9.8692 * (10**-6))
                bar = num * (0.00001)
                
                print(f"\n{num} Pa is equivalent to {round(atm,3)} atm and {round(bar,3)} bar\n")
            elif Pressure_Menu == "atm":
                pa = num * (101325)
                bar = num * (1.01325)
                
                print(f"\n{num} atm is equivalent to {round(pa,3)} pa and {round(bar,3)} bar\n")
            elif Pressure_Menu == "bar":
                pa = num * (100000)
                atm = num * (0.98692)
                
                print(f"\n{num} bar is equivalent to {round(pa,3)} pa and {round(atm,3)} atm\n")
            else:
                print("\nwrong input\n")
                     
            
        elif Conversion_Menu == 2:
            Wind_speed_units = str(input(
            "\nEnter the original wind speed unit:\n"
            "(m/s) Meters per second \n"
            "(km/h) Kilometers per hour\n"
            "(mph) Miles per hour\n"))
            
            if Wind_speed_units == 'm/s' : 
                # m/s -> km/h      1 m/s = 3.6 km/h
                km_h = num * (3.6)
                #m/s ->mph         1 m/s = 2.23694 mph
                mph = num * (2.23694)
                print(f"{num} m/s is equivalent to {round(km_h,3)} km/h and {round(mph,3)} mph.")
                
            elif  Wind_speed_units == 'km/h': 
                #km/h -> m/s        1 km/h = 0.277778 m/s
                m_s = num * (0.277778)
                #km/h -> mph        1 km/h = 0.621371
                mph = num * (0.621371)
                print(f"{num} km/h is equivalent to {round(m_s,3)} m/s and {round(mph,3)} mph.")
                
            elif  Wind_speed_units == 'mph':
                # mph -> m/s        1 mph = 0.44704 m/s
                m_s = num * (0.44704)
                # mph -> km/h       1 mph = 1.60934 km/h
                km_h = num * (1.60934)
                print(f"{num} mph is equivalent to {round(m_s,3)} m/s and {round(km_h,3)} km/h.")
                
            else:
                print("Invalid Option")
            
        else:
            print("Invalid Input")

    elif Option == 3:
        valid = False
        while valid == False:
            hexadecimal = str(input("Enter a hexadecimal number: "))
            length_hex = len(hexadecimal) -1
            # No hashmap I assume
            # allowed = ["0", '1', '2', '3', '4', '5', '6', '7', '8', '9', "A", "B", "C", "D", "E", "F",'a','b','c','d','f']
        
            result = 0
            for j in hexadecimal:
                valid = True
                if j == '0':
                    result += (0 * 16**(length_hex))
                elif j == '1':
                    result += (1 * 16**(length_hex))   
                elif j == '2':
                    result += (2 * 16**(length_hex))  
                elif j == '3':
                    result += (3 * 16**(length_hex))   
                elif j == '4':
                    result += (4 * 16**(length_hex))
                elif j == '5':
                    result += (5 * 16**(length_hex))
                elif j == '6':
                    result += (6 * 16**(length_hex))
                elif j == '7':
                    result += (7 * 16**(length_hex))
                elif j == '8':
                    result += (8 * 16**(length_hex))
                elif j == '9':
                    result += (9 * 16**(length_hex))
                elif j == 'A' or j == 'a':
                    result += (10 * 16**(length_hex))
                elif j == 'B' or j == 'b':
                    result += (11 * 16**(length_hex))
                elif j == 'C' or j == 'c':
                    result += (12 * 16**(length_hex))
                elif j == 'D' or j == 'd':
                    result += (13 * 16**(length_hex))
                elif j == 'E' or j == 'e':
                    result += (14 * 16**(length_hex))
                elif j == 'F' or j == 'f':
                    result += (15 * 16**(length_hex))

                else:
                    #Not found 
                    valid = False
                    break
                  
                length_hex -= 1
                    
            
            if valid == True:
                # Valid Hexadecimal
                print("Hexadecimal -> Decimal :",result)
                break
            else:
                print("Try again , invalid hexadecimal input") 
        
    elif Option == 0:
        print("Exiting the program...")
        Exit = True
    else:
        print("Invalid option")
        
        
        
    