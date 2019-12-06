
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 14:23:26 2019
CS2300 Project 2 - This project is designed to read lines & target box values from a file, then p.ot them using matplotlib.pyplot
@author: jonathanzeas
"""

import matplotlib.pyplot as plt
import numpy as np
  
file_num = 0


#for each file
for file_name in ("line1-1.txt","line2.txt","line3.txt","line4.txt","line5.txt"):

    file_num+=1
    
    #create a new figure
    plt.figure()
    
    #open the file
    file = open(file_name, "r")


    #for each line in the file (should only be 1)
    for line in file:
        #split the line into an array by spaces
        line_array = line.split(" ")
        
    #print the array
    print("\n\nFile "+str(file_num)+" - "+str(line_array))
    
    file.close()
    
    # t axis values for square
    x = [int(line_array[0]),int(line_array[2])+int(line_array[0]),int(line_array[2])+int(line_array[0]),int(line_array[0]),int(line_array[0])] 
    # corresponding l(t) axis values 
    y = [int(line_array[1]),int(line_array[1]),int(line_array[2])+int(line_array[1]),int(line_array[2])+int(line_array[1]),int(line_array[1])] 
      
    #Draw the square
    plt.plot(x,y)
    
    
    #Unless vector has undefined slope (x = 0), goes through try
    try:
        #rise/run
        slope = int(line_array[6])/int(line_array[5])
        #calculated from vector's parametric form
        scalar = -int(line_array[3])/int(line_array[5])
        #calculate the y intercept so it can be used by our graphing library
        y_intercept = int(line_array[4])+(scalar*int(line_array[6]))
        
        
        #spots in target box
        max_x_tb = int(line_array[2])+int(line_array[0])
        min_x_tb = int(line_array[0])
        
        #define the line as infinite points between the min and max x values of the target box
        a = np.linspace(min_x_tb,max_x_tb)
        #define the equation for y in slope intercept form
        b = slope * a + y_intercept
        #draw the line
        plt.plot(a,b)
        
    #if vector has uundefined slope (x = 0), prints a straight vertical line through the target box & given point
    except:
        #gets values in tb
        max_y_tb = int(line_array[2])+int(line_array[1])
        min_y_tb = int(line_array[1])
        
        #define the x values as being at the x value of the point
        a = [int(line_array[3]),int(line_array[3])]
        #define the y values as being inside the target box
        b = [min_y_tb, max_y_tb]
        #plot the line
        plt.plot(a,b)
    
    #Calculate implicit form
    imp_a1 = -int(line_array[6])
    imp_a2 = int(line_array[5])
    
    p1 = int(line_array[3])
    p2 = int(line_array[4])
    
    c = -(imp_a1*p1)-(imp_a2*p2)
    
    #Print the implicit form
    print("Implicit Form of Line: "+str(imp_a1)+"x + "+str(imp_a2)+"y + "+str(c)+" = 0")
    
    #show the graph
    plt.show()



    







