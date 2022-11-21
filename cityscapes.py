
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n10008918
#    Student name: Jaewon Seo
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  CITYSCAPES
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and efficiently repeating multiple actions in
#  order to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "build_city".
#  You are required to complete this function so that when the
#  program is run it draws a city whose plan is determined by
#  randomly-generated data stored in a list which specifies what
#  style of building to erect on particular sites.  See the
#  instruction sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single Python 3 file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must not rely on any non-standard Python
# modules that need to be installed separately, because the markers
# may not have access to such modules.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

canvas_height = 700 # pixels
canvas_width = 1100 # pixels
grass_depth = 95 # vertical depth of the "grass", in pixels
half_width = canvas_width // 2 # maximum x coordinate in either direction
grid_font = ('Arial', 10, 'normal') # font for drawing the grid
grid_size = 50 # gradations for the x and y scales shown on the screen
offset = 5 # offset of the x-y coordinates from the screen's edge, in pixels
max_height = canvas_height - grass_depth # maximum positive y coordinate
max_building_height = 575 # city ordinance maximum building height
site_width = 240 # maximum width of a building site

# Define the locations of building sites approved by the
# city council (arranged from back to front)
sites = [['Site 1', [-225, 0]],
         ['Site 2', [25, 0]],
         ['Site 3', [275, 0]],
         ['Site 4', [-375, -25]],
         ['Site 5', [-125, -25]],
         ['Site 6', [125, -25]],
         ['Site 7', [375, -25]],
         ['Site 8', [-275, -50]],
         ['Site 9', [-25, -50]],
         ['Site 10', [225, -50]]]

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image.
# By default the drawing grid is displayed - call the function
# with False as the argument to prevent this.
def create_drawing_canvas(show_grid = True):

    # Set up the drawing canvas with coordinate (0, 0) in the
    # "grass" area
    setup(canvas_width, canvas_height)
    setworldcoordinates(-half_width, -grass_depth, half_width, max_height)

    # Draw as fast as possible
    tracer(False)

    # Make the sky blue
    bgcolor('sky blue')

    # Draw the "grass" as a big green rectangle (overlapping the
    # edge of the drawing canvas slightly)
    overlap = 25 # pixels
    penup()
    goto(-(half_width + overlap), -(grass_depth + overlap)) # bottom-left
    fillcolor('pale green')
    begin_fill()
    setheading(90) # face north
    forward(grass_depth + overlap * 2)
    right(90) # face east
    forward(canvas_width + overlap * 2)
    right(90) # face south
    forward(grass_depth + overlap * 2)
    end_fill()

    # Draw a nice warm sun peeking into the image at the top left
    penup()
    goto(-canvas_width // 2, canvas_height - grass_depth)
    pencolor('yellow')
    dot(350)

    # Draw a big fluffy white cloud in the sky
    goto(canvas_width // 3, canvas_height - grass_depth - 100)
    pencolor('white')
    dot(200)
    setheading(200)
    forward(100)
    dot(180)
    setheading(0)
    forward(200)
    dot(160)

    # Optionally draw x coordinates along the bottom of the
    # screen (to aid debugging and marking)
    pencolor('black')
    if show_grid:
        for x_coord in range(-half_width + grid_size, half_width, grid_size):
            goto(x_coord, -grass_depth + offset)
            write('| ' + str(x_coord), font = grid_font)

    # Optionally draw y coordinates on the left-hand edge of
    # the screen (to aid debugging and marking)
    if show_grid:
        for y_coord in range(-grid_size, max_height, grid_size):
            goto(-half_width + offset, y_coord - offset)
            write(y_coord, font = grid_font)
        goto(-half_width + offset, max_building_height - 5)
        write('Maximum allowed building height', font = grid_font)

    # Optionally mark each of the building sites approved by
    # the city council
    if show_grid:
        for site_name, location in sites:
            goto(location)
            dot(5)
            goto(location[0] - (site_width // 2), location[1])
            setheading(0)
            pendown()
            forward(site_width)
            penup()
            goto(location[0] - 40, location[1] - 17)
            write(site_name + ': ' + str(location), font = grid_font)
     
    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas.
# By default the cursor (turtle) is hidden when the program
# ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any drawing in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the build_city function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the random_plan function appearing below.  Your
# program must work correctly for any data set generated by the
# random_plan function.
#
# Each of the data sets below is a list specifying a set of
# buildings to be erected.  Each specification consists of the
# following parts:
#
# a) The site on which to erect the building, from Site 1 to 10.
# b) The style of building to be erected, from style 'A' to 'D'.
# c) The number of floors to be constructed, from 1 to 10.
# d) An extra value, either 'X' or 'O', whose purpose will be
#    revealed only in Part B of the assignment.  You should
#    ignore it while completing Part A.
#

# Each of these data sets draws just one building in each of the
# four styles
fixed_plan_1 = [[1, 'A', 6, 'O']]
fixed_plan_2 = [[2, 'B', 7, 'O']]
fixed_plan_3 = [[3, 'C', 5, 'O']]
fixed_plan_4 = [[4, 'D', 4, 'O']]
fixed_plan_5 = [[1, 'A', 9, 'X']]
fixed_plan_6 = [[2, 'B', 2, 'X']]
fixed_plan_7 = [[3, 'C', 3, 'X']]
fixed_plan_8 = [[4, 'D', 6, 'X']]

# Each of the following data sets draws just one style of
# building but at three different sizes, including the maximum
# (so that you can check your building's maximum height against
# the height limit imposed by the city council)
fixed_plan_9 = [[1, 'A', 10, 'O'], [2, 'A', 5, 'O'], [3, 'A', 1, 'O']]
fixed_plan_10 = [[1, 'B', 10, 'O'], [2, 'B', 5, 'O'], [3, 'B', 1, 'O']]
fixed_plan_11 = [[1, 'C', 10, 'O'], [2, 'C', 5, 'O'], [3, 'C', 1, 'O']]
fixed_plan_12 = [[1, 'D', 10, 'O'], [2, 'D', 5, 'O'], [3, 'D', 1, 'O']]
fixed_plan_13 = [[1, 'A', 10, 'X'], [2, 'A', 5, 'X'], [3, 'A', 1, 'X']]
fixed_plan_14 = [[1, 'B', 10, 'X'], [2, 'B', 5, 'X'], [3, 'B', 1, 'X']]
fixed_plan_15 = [[1, 'C', 10, 'X'], [2, 'C', 5, 'X'], [3, 'C', 1, 'X']]
fixed_plan_16 = [[1, 'D', 10, 'X'], [2, 'D', 5, 'X'], [3, 'D', 1, 'X']]

# Each of the following data sets draws a complete cityscape
# involving each style of building at least once. There is
# no pattern to them, they are simply specific examples of the
# kind of data returned by the random_plan function which will be
# used to assess your solution. Your program must work for any value
# that can be returned by the random_plan function, not just these
# fixed data sets.
fixed_plan_17 = \
         [[1, 'D', 2, 'O'],
          [2, 'B', 7, 'O'],
          [5, 'C', 6, 'O'],
          [6, 'A', 4, 'O']]
fixed_plan_18 = \
         [[1, 'D', 6, 'O'],
          [3, 'C', 5, 'O'],
          [4, 'B', 3, 'O'],
          [9, 'A', 9, 'O'],
          [10, 'D', 2, 'O']]
fixed_plan_19 = \
         [[5, 'C', 6, 'O'],
          [6, 'B', 9, 'O'],
          [7, 'A', 5, 'O'],
          [8, 'A', 7, 'O'],
          [9, 'D', 4, 'O']]
fixed_plan_20 = \
         [[1, 'A', 4, 'O'],
          [2, 'B', 4, 'O'],
          [3, 'A', 5, 'O'],
          [4, 'D', 7, 'O'],
          [10, 'B', 10, 'O']]
fixed_plan_21 = \
         [[1, 'B', 6, 'O'],
          [3, 'A', 4, 'O'],
          [4, 'C', 4, 'O'],
          [6, 'A', 8, 'O'],
          [8, 'C', 7, 'O'],
          [9, 'B', 5, 'O'],
          [10, 'D', 3, 'O']]
fixed_plan_22 = \
         [[1, 'A', 10, 'O'],
          [2, 'A', 9, 'O'],
          [3, 'C', 10, 'O'],
          [4, 'B', 5, 'O'],
          [5, 'B', 7, 'O'],
          [6, 'B', 9, 'O'],
          [7, 'C', 2, 'O'],
          [8, 'C', 4, 'O'],
          [9, 'A', 6, 'O'],
          [10, 'D', 7, 'O']]
fixed_plan_23 = \
         [[3, 'A', 8, 'O'],
          [4, 'C', 8, 'O'],
          [5, 'B', 4, 'O'],
          [6, 'D', 5, 'O'],
          [7, 'C', 5, 'X'],
          [8, 'A', 3, 'X'],
          [9, 'D', 2, 'X']]
fixed_plan_24 = \
         [[2, 'C', 3, 'O'],
          [3, 'B', 1, 'O'],
          [4, 'C', 3, 'X'],
          [5, 'C', 1, 'O'],
          [6, 'D', 2, 'O'],
          [7, 'B', 1, 'O'],
          [8, 'D', 2, 'O'],
          [9, 'C', 7, 'O'],
          [10, 'A', 1, 'X']]
fixed_plan_25 = \
         [[1, 'B', 7, 'X'],
          [3, 'C', 1, 'O'],
          [6, 'D', 3, 'O'],
          [7, 'A', 7, 'O'],
          [8, 'D', 3, 'X'],
          [9, 'C', 7, 'O'],
          [10, 'C', 9, 'X']]
fixed_plan_26 = \
         [[1, 'A', 6, 'O'],
          [2, 'A', 2, 'O'],
          [3, 'A', 9, 'X'],
          [4, 'D', 1, 'X'],
          [5, 'C', 7, 'O'],
          [6, 'D', 6, 'O'],
          [7, 'B', 5, 'O'],
          [8, 'A', 1, 'O'],
          [9, 'D', 10, 'X'],
          [10, 'A', 6, 'O']]
 
#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to mark your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a city
# to be built.  Your program must work for any data set returned by
# this function.  The results returned by calling this function will
# be used as the argument to your build_city function during marking.
# For convenience during code development and marking this function
# also prints the plan for the city to be built to the shell window.
#

def random_plan(print_plan = True):
    building_probability = 70 # percent
    option_probability = 20 # percent
    from random import randint, choice
    # Create a random list of building instructions
    city_plan = []
    for site in range(1, len(sites) + 1): # consider each building site
        if randint(1, 100) <= building_probability: # decide whether to build here
            style = choice(['A', 'B', 'C', 'D']) # choose building style
            num_floors = randint(1, 10) # choose number of floors
            if randint(1, 100) <= option_probability: # decide on option's value
                option = 'X'
            else:
                option = 'O'
            city_plan.append([site, style, num_floors, option])
    # Optionally print the result to the shell window
    if print_plan:
        print('\nBuildings to be constructed\n' +
              '(site, style, no. floors, option):\n\n',
              str(city_plan).replace('],', '],\n '))
    # Return the result to the student's build_city function
    return city_plan

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "build_city" function.
#

# Erect buildings as per the provided city plan
def build_city(dummy_parameter):
    for each_item in dummy_parameter:   # for every items in the list created by random_plan function
        def first_item (dummy_parameter, n):   # very first item in the list dummy_parameter with the parameterized variable called n (variable n is the nth item in the list random_plan function)
            # put values into the variables of the function definition construct_building
            # and draw certain type of building in certain position if the list from the random_plan function calls one of them
            construct_building (n, 1, 'A', -225, 0) # construct certain building (building style A, at site 1)
            construct_building (n, 1, 'B', -225, 0) # construct following building (building style B, at site 1)
            construct_building (n, 1, 'C', -225, 0) # construct following  building (building style C, at site 1)
            construct_building (n, 1, 'D', -225, 0) # construct following  building (building style D, at site 1)

            # construct following building at site 2
            construct_building (n, 2, 'A', 25, 0) 
            construct_building (n, 2, 'B', 25, 0) 
            construct_building (n, 2, 'C', 25, 0)
            construct_building (n, 2, 'D', 25, 0)
            
            # construct following building at site 3
            construct_building (n, 3, 'A', 275, 0) 
            construct_building (n, 3, 'B', 275, 0) 
            construct_building (n, 3, 'C', 275, 0)
            construct_building (n, 3, 'D', 275, 0)

            # construct following building at site 4
            construct_building (n, 4, 'A', -375, -25) 
            construct_building (n, 4, 'B', -375, -25) 
            construct_building (n, 4, 'C', -375, -25)
            construct_building (n, 4, 'D', -375, -25)

            # construct following building at site 5
            construct_building (n, 5, 'A', -125, -25) 
            construct_building (n, 5, 'B', -125, -25) 
            construct_building (n, 5, 'C', -125, -25)
            construct_building (n, 5, 'D', -125, -25)

            # construct following building at site 6
            construct_building (n, 6, 'A', 125, -25) 
            construct_building (n, 6, 'B', 125, -25) 
            construct_building (n, 6, 'C', 125, -25)
            construct_building (n, 6, 'D', 125, -25)

            # construct following building at site 7
            construct_building (n, 7, 'A', 375, -25) 
            construct_building (n, 7, 'B', 375, -25) 
            construct_building (n, 7, 'C', 375, -25)
            construct_building (n, 7, 'D', 375, -25)

            # construct following building at site 8
            construct_building (n, 8, 'A', -275, -50) 
            construct_building (n, 8, 'B', -275, -50) 
            construct_building (n, 8, 'C', -275, -50)
            construct_building (n, 8, 'D', -275, -50)

            # construct following building at site 9
            construct_building (n, 9, 'A', -25, -50) 
            construct_building (n, 9, 'B', -25, -50) 
            construct_building (n, 9, 'C', -25, -50)
            construct_building (n, 9, 'D', -25, -50)

            # construct following building at site 10
            construct_building (n, 10, 'A', 225, -50) 
            construct_building (n, 10, 'B', 225, -50) 
            construct_building (n, 10, 'C', 225, -50)
            construct_building (n, 10, 'D', 225, -50)
            

        def second_item (dummy_parameter, n):   # defining second item in dummy_parameter
            first_item(dummy_parameter, n)  # calling the function definitioon first_item with the parameterized variable n
            

        def third_item (dummy_parameter, n):    # defining third item in dummy_parameter
            first_item(dummy_parameter, n)  # calling the function definitioon first_item with the parameterized variable n


        def fourth_item (dummy_parameter, n):   # defining fourth item in dummy_parameter
            first_item(dummy_parameter, n)  # calling the function definitioon first_item with the parameterized variable n


        def fifth_item (dummy_parameter, n):    # defining fifth item in dummy_parameter
            first_item(dummy_parameter, n)  # calling the function definitioon first_item with the parameterized variable n


        def sixth_item (dummy_parameter, n):    # defining sixth item in dummy_parameter
            first_item(dummy_parameter, n)  # calling the function definitioon first_item with the parameterized variable n


        def seventh_item (dummy_parameter, n):  # defining seventh item in dummy_parameter
            first_item(dummy_parameter, n)  # calling the function definitioon first_item with the parameterized variable n


        def eighth_item (dummy_parameter, n):    # defining eighth item in dummy_parameter
            first_item(dummy_parameter, n)  # calling the function definitioon first_item with the parameterized variable n


        def ninth_item (dummy_parameter, n):    # defining ninth item in dummy_parameter
            first_item(dummy_parameter, n)  # calling the function definitioon first_item with the parameterized variable n


        def tenth_item (dummy_parameter, n):    # defining tenth item in dummy_parameter
            first_item(dummy_parameter, n)  # calling the function definitioon first_item with the parameterized variable n

            
##  Function definition of construct_building with variables in the bracket 
## The variables are:
## nth item in the bracket(list) of random_plan funciton
## position of the building to be constructed
## style of the building to be constructed
## x_coordinate: position where x axis of building/ roof will be constructed
## y_cordinate: position where y axis of building/roof will be constructed
    def construct_building (n, position_number, building_style, x_cord, y_cord):  # function definition construct_building with 5 variables
        if dummy_parameter [n][0] == position_number:   # if the first item in the list (name is dummy_parameter) created by random_plan function is equal to certain variable called position_number, run the following code
            if dummy_parameter [n][1] == building_style:    # if the second item in the list dummy_parameter is equal to certain variable called building_style, run the following code
                if dummy_parameter [n][3] == 'O':   # if third item in the list dummy_parameter is equal to 'O' run the following code
                    if building_style == 'A':   # if variable in the building_style is equal to building style 'A' run the following code
                        # run the following if-elif-else statement if the certain number is in the third item of the list dummy_parameter, construct the certain type of the floor and caps it with the certain type of the roof
                        if dummy_parameter [n][2] == 1: # if the third item in the list dummy-parameter is equal to 1 execute following code (certain number in the third item tell you how many floors you have to draw on the canvas at a certain position)
                            building_A_floor_1 (x_cord, y_cord) # draw floor 1 of the building style 1 at a certain position, parameterized the position of the building to be drawn, x axis as the variable x_cord and y axis as the variable y_cord
                            building_A_roof (x_cord, y_cord + 40)   # draw building style A's roof which caps the first floor of the building style A
                        elif dummy_parameter [n][2] == 2:
                            building_A_floor_2 (x_cord, y_cord)
                            building_A_roof (x_cord, y_cord + 80)
                        elif dummy_parameter [n][2] == 3:
                            building_A_floor_3 (x_cord, y_cord)
                            building_A_roof (x_cord, y_cord + 120)
                        elif dummy_parameter [n][2] == 4:
                            building_A_floor_4 (x_cord, y_cord)
                            building_A_roof (x_cord, y_cord + 160)
                        elif dummy_parameter [n][2] == 5:
                            building_A_floor_5 (x_cord, y_cord)
                            building_A_roof (x_cord, y_cord + 200)
                        elif dummy_parameter [n][2] == 6:
                            building_A_floor_6 (x_cord, y_cord)
                            building_A_roof (x_cord, y_cord + 240)
                        elif dummy_parameter [n][2] == 7:
                            building_A_floor_7 (x_cord, y_cord)
                            building_A_roof (x_cord, y_cord + 280)
                        elif dummy_parameter [n][2] == 8:
                            building_A_floor_8 (x_cord, y_cord)
                            building_A_roof (x_cord, y_cord + 320)
                        elif dummy_parameter [n][2] == 9:
                            building_A_floor_9 (x_cord, y_cord)
                            building_A_roof (x_cord, y_cord + 360)
                        elif dummy_parameter [n][2] == 10:
                            building_A_floor_10 (x_cord, y_cord)
                            building_A_roof (x_cord, y_cord + 400)                    
                        else:
                            pass

                    # run the following if-elif-else statement if the certain number is in the third item of the list dummy_parameter, construct the certain type of the floor and caps it with the certain type of the roof
                    elif building_style == 'B': # if variable in the building_style is equal to building style 'B' run the following code
                        if dummy_parameter [n][2] == 1:
                            building_B_floor_1 (x_cord, y_cord)
                            building_B_roof (x_cord, y_cord + 40)
                        elif dummy_parameter [n][2] == 2:
                            building_B_floor_2 (x_cord, y_cord)
                            building_B_roof (x_cord, y_cord + 80)
                        elif dummy_parameter [n][2] == 3:
                            building_B_floor_3 (x_cord, y_cord)
                            building_B_roof (x_cord, y_cord + 120)
                        elif dummy_parameter [n][2] == 4:
                            building_B_floor_4 (x_cord, y_cord)
                            building_B_roof (x_cord, y_cord + 160)
                        elif dummy_parameter [n][2] == 5:
                            building_B_floor_5 (x_cord, y_cord)
                            building_B_roof (x_cord, y_cord + 200)
                        elif dummy_parameter [n][2] == 6:
                            building_B_floor_6 (x_cord, y_cord)
                            building_B_roof (x_cord, y_cord + 240)
                        elif dummy_parameter [n][2] == 7:
                            building_B_floor_7 (x_cord, y_cord)
                            building_B_roof (x_cord, y_cord + 280)
                        elif dummy_parameter [n][2] == 8:
                            building_B_floor_8 (x_cord, y_cord)
                            building_B_roof (x_cord, y_cord + 320)
                        elif dummy_parameter [n][2] == 9:
                            building_B_floor_9 (x_cord, y_cord)
                            building_B_roof (x_cord, y_cord + 360)
                        elif dummy_parameter [n][2] == 10:
                            building_B_floor_10 (x_cord, y_cord)
                            building_B_roof (x_cord, y_cord + 400)                    
                        else:
                            pass

                    # run the following if-elif-else statement if the certain number is in the third item of the list dummy_parameter, construct the certain type of the floor and caps it with the certain type of the roof
                    elif building_style == 'C': # if variable in the building_style is equal to building style 'C' run the following code
                        if dummy_parameter [n][2] == 1:
                            building_C_floor_1 (x_cord, y_cord)
                            building_C_roof (x_cord, y_cord + 40)
                        elif dummy_parameter [n][2] == 2:
                            building_C_floor_2 (x_cord, y_cord)
                            building_C_roof (x_cord, y_cord + 80)
                        elif dummy_parameter [n][2] == 3:
                            building_C_floor_3 (x_cord, y_cord)
                            building_C_roof (x_cord, y_cord + 120)
                        elif dummy_parameter [n][2] == 4:
                            building_C_floor_4 (x_cord, y_cord)
                            building_C_roof (x_cord, y_cord + 160)
                        elif dummy_parameter [n][2] == 5:
                            building_C_floor_5 (x_cord, y_cord)
                            building_C_roof (x_cord, y_cord + 200)
                        elif dummy_parameter [n][2] == 6:
                            building_C_floor_6 (x_cord, y_cord)
                            building_C_roof (x_cord, y_cord + 240)
                        elif dummy_parameter [n][2] == 7:
                            building_C_floor_7 (x_cord, y_cord)
                            building_C_roof (x_cord, y_cord + 280)
                        elif dummy_parameter [n][2] == 8:
                            building_C_floor_8 (x_cord, y_cord)
                            building_C_roof (x_cord, y_cord + 320)
                        elif dummy_parameter [n][2] == 9:
                            building_C_floor_9 (x_cord, y_cord)
                            building_C_roof (x_cord, y_cord + 360)
                        elif dummy_parameter [n][2] == 10:
                            building_C_floor_10 (x_cord, y_cord)
                            building_C_roof (x_cord, y_cord + 400)                    
                        else:
                            pass

                    # run the following if-elif-else statement if the certain number is in the third item of the list dummy_parameter, construct the certain type of the floor and caps it with the certain type of the roof
                    elif building_style == 'D': # if variable in the building_style is equal to building style 'D' run the following code
                        if dummy_parameter [n][2] == 1:
                            building_D_floor_1 (x_cord, y_cord)
                            building_D_roof (x_cord, y_cord + 40)
                        elif dummy_parameter [n][2] == 2:
                            building_D_floor_2 (x_cord, y_cord)
                            building_D_roof (x_cord, y_cord + 80)
                        elif dummy_parameter [n][2] == 3:
                            building_D_floor_3 (x_cord, y_cord)
                            building_D_roof (x_cord, y_cord + 120)
                        elif dummy_parameter [n][2] == 4:
                            building_D_floor_4 (x_cord, y_cord)
                            building_D_roof (x_cord, y_cord + 160)
                        elif dummy_parameter [n][2] == 5:
                            building_D_floor_5 (x_cord, y_cord)
                            building_D_roof (x_cord, y_cord + 200)
                        elif dummy_parameter [n][2] == 6:
                            building_D_floor_6 (x_cord, y_cord)
                            building_D_roof (x_cord, y_cord + 240)
                        elif dummy_parameter [n][2] == 7:
                            building_D_floor_7 (x_cord, y_cord)
                            building_D_roof (x_cord, y_cord + 280)
                        elif dummy_parameter [n][2] == 8:
                            building_D_floor_8 (x_cord, y_cord)
                            building_D_roof (x_cord, y_cord + 320)
                        elif dummy_parameter [n][2] == 9:
                            building_D_floor_9 (x_cord, y_cord)
                            building_D_roof (x_cord, y_cord + 360)
                        elif dummy_parameter [n][2] == 10:
                            building_D_floor_10 (x_cord, y_cord)
                            building_D_roof (x_cord, y_cord + 400)                    
                        else:
                            pass


                elif dummy_parameter [n][3] == 'X': # else if third item in the list dummy_parameter is equal to 'X' run the following code to draw buildings that are yet to be completed in your cityscapes
                    if building_style == 'A':   # if variable in the building_style is equal to building style 'A' run the following code
                    # run the following if-elif-else statement if the certain number is in the third item of the list dummy_parameter, construct the certain type of the floor and caps it with the building crane
                        if dummy_parameter [n][2] == 1: # if the third item in the list dummy-parameter is equal to 1 execute following code (certain number in the third item tell you how many floors you have to draw on the canvas at a certain position)
                            building_A_floor_1 (x_cord, y_cord) # draw floor 1 of the building style 1 at a certain position, parameterized the position of the building to be drawn, x axis as the variable x_cord and y axis as the variable y_cord
                            building_crane (x_cord, y_cord + 40)   # draw building crane which caps the first floor of the building style A
                        elif dummy_parameter [n][2] == 2:
                            building_A_floor_2 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 80)
                        elif dummy_parameter [n][2] == 3:
                            building_A_floor_3 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 120)
                        elif dummy_parameter [n][2] == 4:
                            building_A_floor_4 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 160)
                        elif dummy_parameter [n][2] == 5:
                            building_A_floor_5 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 200)
                        elif dummy_parameter [n][2] == 6:
                            building_A_floor_6 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 240)
                        elif dummy_parameter [n][2] == 7:
                            building_A_floor_7 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 280)
                        elif dummy_parameter [n][2] == 8:
                            building_A_floor_8 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 320)
                        elif dummy_parameter [n][2] == 9:
                            building_A_floor_9 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 360)
                        elif dummy_parameter [n][2] == 10:
                            building_A_floor_10 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 400)                    
                        else:
                            pass

                    # run the following if-elif-else statement if the certain number is in the third item of the list dummy_parameter, construct the certain type of the floor and caps it with the building crane
                    elif building_style == 'B': # if variable in the building_style is equal to building style 'B' run the following code
                        if dummy_parameter [n][2] == 1:
                            building_B_floor_1 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 40)
                        elif dummy_parameter [n][2] == 2:
                            building_B_floor_2 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 80)
                        elif dummy_parameter [n][2] == 3:
                            building_B_floor_3 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 120)
                        elif dummy_parameter [n][2] == 4:
                            building_B_floor_4 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 160)
                        elif dummy_parameter [n][2] == 5:
                            building_B_floor_5 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 200)
                        elif dummy_parameter [n][2] == 6:
                            building_B_floor_6 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 240)
                        elif dummy_parameter [n][2] == 7:
                            building_B_floor_7 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 280)
                        elif dummy_parameter [n][2] == 8:
                            building_B_floor_8 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 320)
                        elif dummy_parameter [n][2] == 9:
                            building_B_floor_9 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 360)
                        elif dummy_parameter [n][2] == 10:
                            building_B_floor_10 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 400)                    
                        else:
                            pass

                    # run the following if-elif-else statement if the certain number is in the third item of the list dummy_parameter, construct the certain type of the floor and caps it with the building crane
                    elif building_style == 'C': # if variable in the building_style is equal to building style 'C' run the following code
                        if dummy_parameter [n][2] == 1:
                            building_C_floor_1 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 40)
                        elif dummy_parameter [n][2] == 2:
                            building_C_floor_2 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 80)
                        elif dummy_parameter [n][2] == 3:
                            building_C_floor_3 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 120)
                        elif dummy_parameter [n][2] == 4:
                            building_C_floor_4 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 160)
                        elif dummy_parameter [n][2] == 5:
                            building_C_floor_5 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 200)
                        elif dummy_parameter [n][2] == 6:
                            building_C_floor_6 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 240)
                        elif dummy_parameter [n][2] == 7:
                            building_C_floor_7 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 280)
                        elif dummy_parameter [n][2] == 8:
                            building_C_floor_8 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 320)
                        elif dummy_parameter [n][2] == 9:
                            building_C_floor_9 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 360)
                        elif dummy_parameter [n][2] == 10:
                            building_C_floor_10 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 400)                    
                        else:
                            pass

                    # run the following if-elif-else statement if the certain number is in the third item of the list dummy_parameter, construct the certain type of the floor and caps it with the building crane
                    elif building_style == 'D': # if variable in the building_style is equal to building style 'D' run the following code
                        if dummy_parameter [n][2] == 1:
                            building_D_floor_1 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 40)
                        elif dummy_parameter [n][2] == 2:
                            building_D_floor_2 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 80)
                        elif dummy_parameter [n][2] == 3:
                            building_D_floor_3 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 120)
                        elif dummy_parameter [n][2] == 4:
                            building_D_floor_4 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 160)
                        elif dummy_parameter [n][2] == 5:
                            building_D_floor_5 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 200)
                        elif dummy_parameter [n][2] == 6:
                            building_D_floor_6 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 240)
                        elif dummy_parameter [n][2] == 7:
                            building_D_floor_7 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 280)
                        elif dummy_parameter [n][2] == 8:
                            building_D_floor_8 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 320)
                        elif dummy_parameter [n][2] == 9:
                            building_D_floor_9 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 360)
                        elif dummy_parameter [n][2] == 10:
                            building_D_floor_10 (x_cord, y_cord)
                            building_crane (x_cord, y_cord + 400)                    
                        else:
                            pass
                    else:
                        pass
                else:
                    pass

            

######################################################################
#################  Executing All the Function Definitions #######################
######################################################################    
    if len(dummy_parameter) == 1:   ## if there is only one list in dummy_parameter created by random_plan function, run the following code
        first_item(dummy_parameter, 0) # run the function definition called first_item for the certain list created by random_plan function and the list is parameterized as the name dummy_parameter 
    
    elif len(dummy_parameter) == 2: ## else if there are two lists in dummy_parameter created by random_plan function, run the following code
        first_item(dummy_parameter, 0) # run the function definition called first_item
        second_item(dummy_parameter, 1)    # run the function definition called second_ item

    elif len(dummy_parameter) == 3: ## else if there are three lists in dummy_parameter, run the following code
        first_item(dummy_parameter, 0) # run the function definition called first_item
        second_item(dummy_parameter, 1)    # run the function definition called second_item
        third_item(dummy_parameter, 2) # run the function definition called third_item

    elif len(dummy_parameter) == 4: ## else if there are four lists in dummy_parameter, run the following code
        first_item(dummy_parameter, 0) # run the function definition called first_item
        second_item(dummy_parameter, 1)    # run the function definition called second_item
        third_item(dummy_parameter, 2) # run the function definition called third_item
        fourth_item(dummy_parameter, 3)    # run the function definition called fourth_item

    elif len(dummy_parameter) == 5: ## else if there are five lists in dummy_parameter, run the following code
        first_item(dummy_parameter, 0) # run the function definition called first_item
        second_item(dummy_parameter, 1)    # run the function definition called second_item
        third_item(dummy_parameter, 2) # run the function definition called third_item
        fourth_item(dummy_parameter, 3)    # run the function definition called fourth_item
        fifth_item(dummy_parameter, 4) # run the function definition called fifth_item
                                
    elif len(dummy_parameter) == 6: ## else if there are six lists in dummy_parameter, run the following code
        first_item(dummy_parameter, 0) # run the function definition called first_item
        second_item(dummy_parameter, 1)    # run the function definition called second_item
        third_item(dummy_parameter, 2) # run the function definition called third_item
        fourth_item(dummy_parameter, 3)    # run the function definition called fourth_item
        fifth_item(dummy_parameter, 4) # run the function definition called fifth_item
        sixth_item(dummy_parameter, 5) # run the function definition called sixth_item

    elif len(dummy_parameter) == 7: ## else if there are seven lists in dummy_parameter, run the following code
        first_item(dummy_parameter, 0) # run the function definition called first_item
        second_item(dummy_parameter, 1)    # run the function definition called second_item
        third_item(dummy_parameter, 2) # run the function definition called third_item
        fourth_item(dummy_parameter, 3)    # run the function definition called fourth_item
        fifth_item(dummy_parameter, 4) # run the function definition called fifth_item                          
        sixth_item(dummy_parameter, 5) # run the function definition called sixth_item
        seventh_item(dummy_parameter, 6)   # run the function definition called seventh_item

    elif len(dummy_parameter) == 8: ## else if there are eight lists in dummy_parameter, run the following code
        first_item(dummy_parameter, 0) # run the function definition called first_item
        second_item(dummy_parameter, 1)    # run the function definition called second_item
        third_item(dummy_parameter, 2) # run the function definition called third_item
        fourth_item(dummy_parameter, 3)    # run the function definition called fourth_item
        fifth_item(dummy_parameter, 4)      # run the function definition called fifith_item                                  
        sixth_item(dummy_parameter, 5) # run the function definition called sixth_item
        seventh_item(dummy_parameter, 6)   # run the function definition called seventh_item 
        eighth_item(dummy_parameter, 7)    # run the function definition called eighth_item,

    elif len(dummy_parameter) == 9: ## else if there are nine lists in dummy_parameter, run the following code
        # run the following function definitions 
        first_item(dummy_parameter, 0) 
        second_item(dummy_parameter, 1)  
        third_item(dummy_parameter, 2) 
        fourth_item(dummy_parameter, 3)   
        fifth_item(dummy_parameter, 4)                                  
        sixth_item(dummy_parameter, 5) 
        seventh_item(dummy_parameter, 6)   
        eighth_item(dummy_parameter, 7)
        ninth_item(dummy_parameter, 8)

    elif len(dummy_parameter) == 10:    ## else if there are ten lists in dummy_parameter, run the following code
        # run the following function definitions 
        first_item(dummy_parameter, 0) 
        second_item(dummy_parameter, 1)  
        third_item(dummy_parameter, 2) 
        fourth_item(dummy_parameter, 3)   
        fifth_item(dummy_parameter, 4)                                  
        sixth_item(dummy_parameter, 5) 
        seventh_item(dummy_parameter, 6)   
        eighth_item(dummy_parameter, 7)
        ninth_item(dummy_parameter, 8)
        tenth_item(dummy_parameter, 9)

    else:   ## else if there are no lists in dummy_parameter, run the following code
        pass ## do nothing



### For all the function definitons of constructing buildings' roofs and floors (all the floors and roofs of the four different types of building), 
### we have to make the turtle start constructing them from one point.
### Therefore, even though we change the site (starting position) of the building to be constructed,
### with the parameterized starting point, we can start constructing them at any position we want
##################### Function Definition - BUILDING A ######################

# Defining the roof of the building style A
def building_A_roof (x_cord , y_cord):
    penup()
    goto(x_cord, y_cord)    # goto parameterized position x_axis and y_axis

    #   draw lighting rode as a roof of the building style A
    pendown()   
    pensize(2)
    begin_fill()
    fillcolor("black")
    forward(75.7)
    left(90)
    forward(10)
    left(90)
    forward(150)
    left(90)
    forward(10)
    left(90)
    forward(75)

    penup()
    forward(75.7)
    left(90)
    forward(10)
    left(90)
    forward(52)
    end_fill()
    
    begin_fill()
    fillcolor("black")
    pendown()
    setheading(0)
    left(90)
    forward(15)
    setheading(0)
    left(150)
    forward(15)
    
    setheading(0)   
    left(90)
    forward(15)
    setheading(0)
    left(150)
    forward(10)

    ## drawing lighting rod
    setheading(0) 
    left(90)
    forward(45)
    setheading(0)
    left(147)
    forward(5)
    setheading(0)
    right(90)
    forward(47.5)

    right(60)
    forward(10)
    setheading(0)
    right(90)
    forward(14)

    right(60)
    forward(15)
    setheading(0)
    right(90)
    forward(16)
    end_fill()

    # end by moving the turtle back to the point where it started
    penup() # pen up before moving to parameterized position x_axis and y_axis
    goto(x_cord, y_cord)    # goto parameterized position x_axis and y_axis
    setheading(0) # end with setting the orientation of the turtle to angle 0
    
    
# funciton defining the process of building the first floor of building A
def building_A_floor_1 (x_cord, y_cord):
    penup()
    goto(x_cord, y_cord)    # goto parameterized position x_axis and y_axis

    #   draw first floor of the building
    pendown()
    pensize(3)
    begin_fill()
    fillcolor("Blue")
    forward(75)
    left(90)
    forward(40)
    left(90)
    forward(150)
    left(90)
    forward(40)
    left(90)
    forward(75)
    end_fill()

    #   draw window
    penup()
    goto(x_cord, y_cord)
    setheading(0)
    pendown()
    forward(15)
    left(90)
    forward(40)
    right(90)
    forward(30)
    right(90)
    forward(40)
    left(90)
    forward(30)
    left(90)
    forward(40)

    penup()
    goto(x_cord, y_cord)
    setheading(0)
    pendown()
    right(180)
    forward(15)
    right(90)
    forward(40)
    left(90)
    forward(30)
    left(90)
    forward(40)
    right(90)
    forward(30)

    # end by moving the turtle back to the point where it started
    penup() # pen up before moving to parameterized position x_axis and y_axis
    goto(x_cord, y_cord)    # goto parameterized position x_axis and y_axis
    setheading(0)   # end with setting the orientation of the turtle to angle 0

    
# function defining the process of building second floor of building A (first floor + first floor of building A, total two floors)
def building_A_floor_2 (x_cord, y_cord):
    building_A_floor_1(x_cord, y_cord)  ## calling the first floor (**always construct the new floor on the previous floor/ floors**)
    building_A_floor_1(x_cord, y_cord + 40) # calling the first floor but this time add 40 pixels to the y coordinate so turtle can draw one more floor on the top of first floor

# function defining the process of building third floor of building A (second floor + first floor of building A, total three floors)
def building_A_floor_3 (x_cord, y_cord):
    building_A_floor_2(x_cord, y_cord) ## calling the second floor (first floor + second floor) (**always construct the new floor on the previous floor/ floors**)
    building_A_floor_1(x_cord, y_cord + 80) # calling the first floor and add 80 pixels to the y axis so it can draw one more floor on the top of second floor

# defining fourth floor of building style A
def building_A_floor_4 (x_cord, y_cord):
    building_A_floor_3 (x_cord, y_cord)
    building_A_floor_1 (x_cord, y_cord + 120)

# defining fifth floor of building style A
def building_A_floor_5 (x_cord, y_cord):
    building_A_floor_4 (x_cord, y_cord)
    building_A_floor_1 (x_cord, y_cord + 160)

# defining sixth floor of building style A
def building_A_floor_6 (x_cord, y_cord):
    building_A_floor_5 (x_cord, y_cord)
    building_A_floor_1 (x_cord, y_cord + 200)

# defining seventh floor of building style A
def building_A_floor_7 (x_cord, y_cord):
    building_A_floor_6 (x_cord, y_cord)
    building_A_floor_1 (x_cord, y_cord + 240)

# defining eighth floor of building style A
def building_A_floor_8 (x_cord, y_cord):
    building_A_floor_7 (x_cord, y_cord)
    building_A_floor_1 (x_cord, y_cord + 280)

# defining ninth floor of building style A
def building_A_floor_9 (x_cord, y_cord):
    building_A_floor_8 (x_cord, y_cord)
    building_A_floor_1 (x_cord, y_cord + 320)

# defining tenth floor of building style A
def building_A_floor_10 (x_cord, y_cord):
    building_A_floor_9 (x_cord, y_cord)
    building_A_floor_1 (x_cord, y_cord + 360)



##################### Function Definition - BUILDING B ######################

# Defining the roof of the building style B
def building_B_roof (x_cord, y_cord):
    penup()
    goto(x_cord, y_cord)    # goto parameterized position x_axis and y_axis

    # draw roof floor of the building style B with fill colour white
    begin_fill()
    fillcolor("white")
    forward(100)
    pendown()
    pensize(1.5)
    left(90)
    forward(40)
    left(90)
    forward(200)
    left(90)
    forward(40)
    penup()
    left(90)
    forward(100)
    end_fill()

    # draw red hospital cross mark at the middle of the roof floor
    penup()
    goto(x_cord, y_cord)
    left(90)
    forward(5)
    pendown()
    begin_fill()
    fillcolor("red")
    right(90)
    forward(5)
    left(90)
    forward(10)
    right(90)
    forward(10)
    left(90)
    forward(10)
    left(90)
    forward(10)
    right(90)
    forward(10)
    left(90)
    forward(10)
    left(90)
    forward(10)
    right(90)
    forward(10)
    left(90)
    forward(10)
    left(90)
    forward(10)
    right(90)
    forward(10)
    left(90)
    forward(5)
    end_fill()

    # end by moving the turtle back to the point where it started
    penup() # pen up before moving to parameterized position x_axis and y_axis
    goto(x_cord, y_cord)     # goto parameterized position x_axis and y_axis
    setheading(0)   # end with setting the orientation of the turtle to angle 0


# funciton defining the process of building the first floor of building style B
def building_B_floor_1 (x_cord, y_cord):
    penup()
    goto(x_cord, y_cord)    # goto parameterized position x_axis and y_axis

    # draw the first floor with fill colour white    
    pendown()
    pensize(1.5)
    begin_fill()
    fillcolor("white")
    forward(100)
    left(90)
    forward(40)
    left(90)
    penup()
    forward(200)
    pendown()
    left(90)
    forward(40)
    left(90)
    forward(100)
    end_fill()

    # draw nine windows on the first floor
    penup()
    goto(x_cord - 93, y_cord + 27)
    setheading(0)
    pendown()
    begin_fill()
    fillcolor("DeepSkyBlue")
    forward(15)
    right(90)
    forward(16)
    right(90)
    forward(15)
    right(90)
    forward(17)
    end_fill()

    penup()
    goto(x_cord - 71, y_cord + 27)
    setheading(0)
    pendown()
    begin_fill()
    fillcolor("DeepSkyBlue")
    forward(15)
    right(90)
    forward(16)
    right(90)
    forward(15)
    right(90)
    forward(17)
    end_fill()

    penup()
    goto(x_cord - 50, y_cord + 27)
    setheading(0)
    pendown()
    begin_fill()
    fillcolor("DeepSkyBlue")
    forward(15)
    right(90)
    forward(16)
    right(90)
    forward(15)
    right(90)
    forward(17)
    end_fill()

    penup()
    goto(x_cord - 29, y_cord + 27)
    setheading(0)
    pendown()
    begin_fill()
    fillcolor("DeepSkyBlue")
    forward(15)
    right(90)
    forward(16)
    right(90)
    forward(15)
    right(90)
    forward(17)
    end_fill()

    penup()
    goto(x_cord - 8.5, y_cord + 27)
    setheading(0)
    pendown()
    begin_fill()
    fillcolor("DeepSkyBlue")
    forward(15)
    right(90)
    forward(16)
    right(90)
    forward(15)
    right(90)
    forward(17)
    end_fill()
    penup()

    penup()
    goto(x_cord + 12.5, y_cord + 27)
    setheading(0)
    pendown()
    begin_fill()
    fillcolor("DeepSkyBlue")
    forward(15)
    right(90)
    forward(16)
    right(90)
    forward(15)
    right(90)
    forward(17)
    end_fill()
    penup()

    penup()
    goto(x_cord + 34, y_cord + 27)
    setheading(0)
    pendown()
    begin_fill()
    fillcolor("DeepSkyBlue")
    forward(15)
    right(90)
    forward(16)
    right(90)
    forward(15)
    right(90)
    forward(17)
    end_fill()
    penup()

    penup()
    goto(x_cord + 56, y_cord + 27)
    setheading(0)
    pendown()
    begin_fill()
    fillcolor("DeepSkyBlue")
    forward(15)
    right(90)
    forward(16)
    right(90)
    forward(15)
    right(90)
    forward(17)
    end_fill()
    penup()

    penup()
    goto(x_cord + 78, y_cord + 27)
    setheading(0)
    pendown()
    begin_fill()
    fillcolor("DeepSkyBlue")
    forward(15)
    right(90)
    forward(16)
    right(90)
    forward(15)
    right(90)
    forward(17)
    end_fill()
    penup()

    goto(x_cord, y_cord)    # goto parameterized position x_axis and y_axis
    setheading(0)   # end with setting the orientation of the turtle to angle 0

# defining middle floor which will be constructed on the bottom floor, middle section (floor those are not touching the ground)  when it/ they is/are called
def building_B_floor_middle (x_cord, y_cord):
    penup()
    goto(x_cord, y_cord)
    
    pensize(1.5)
    begin_fill()
    fillcolor("white")
    forward(100)
    left(90)
    pendown()
    forward(40)
    left(90)
    penup()
    forward(200)
    pendown()
    left(90)
    forward(40)
    left(90)
    penup()
    forward(100)
    end_fill()

    penup()
    goto(x_cord - 93, y_cord + 27)
    setheading(0)
    pendown()
    begin_fill()
    fillcolor("DeepSkyBlue")
    forward(15)
    right(90)
    forward(16)
    right(90)
    forward(15)
    right(90)
    forward(17)
    end_fill()

    penup()
    goto(x_cord - 71, y_cord + 27)
    setheading(0)
    pendown()
    begin_fill()
    fillcolor("DeepSkyBlue")
    forward(15)
    right(90)
    forward(16)
    right(90)
    forward(15)
    right(90)
    forward(17)
    end_fill()

    penup()
    goto(x_cord - 50, y_cord + 27)
    setheading(0)
    pendown()
    begin_fill()
    fillcolor("DeepSkyBlue")
    forward(15)
    right(90)
    forward(16)
    right(90)
    forward(15)
    right(90)
    forward(17)
    end_fill()

    penup()
    goto(x_cord - 29, y_cord + 27)
    setheading(0)
    pendown()
    begin_fill()
    fillcolor("DeepSkyBlue")
    forward(15)
    right(90)
    forward(16)
    right(90)
    forward(15)
    right(90)
    forward(17)
    end_fill()

    penup()
    goto(x_cord - 8.5, y_cord + 27)
    setheading(0)
    pendown()
    begin_fill()
    fillcolor("DeepSkyBlue")
    forward(15)
    right(90)
    forward(16)
    right(90)
    forward(15)
    right(90)
    forward(17)
    end_fill()
    penup()

    penup()
    goto(x_cord + 12.5, y_cord + 27)
    setheading(0)
    pendown()
    begin_fill()
    fillcolor("DeepSkyBlue")
    forward(15)
    right(90)
    forward(16)
    right(90)
    forward(15)
    right(90)
    forward(17)
    end_fill()
    penup()

    penup()
    goto(x_cord + 34, y_cord + 27)
    setheading(0)
    pendown()
    begin_fill()
    fillcolor("DeepSkyBlue")
    forward(15)
    right(90)
    forward(16)
    right(90)
    forward(15)
    right(90)
    forward(17)
    end_fill()
    penup()

    penup()
    goto(x_cord + 56, y_cord + 27)
    setheading(0)
    pendown()
    begin_fill()
    fillcolor("DeepSkyBlue")
    forward(15)
    right(90)
    forward(16)
    right(90)
    forward(15)
    right(90)
    forward(17)
    end_fill()
    penup()

    penup()
    goto(x_cord + 78, y_cord + 27)
    setheading(0)
    pendown()
    begin_fill()
    fillcolor("DeepSkyBlue")
    forward(15)
    right(90)
    forward(16)
    right(90)
    forward(15)
    right(90)
    forward(17)
    end_fill()
    penup()
    
    goto(x_cord, y_cord)
    setheading(0)


# function defining the process of building second floor of building B (first floor + middle floor of building B, total two floors)
def building_B_floor_2 (x_cord, y_cord):
    building_B_floor_1 (x_cord, y_cord)
    building_B_floor_middle (x_cord, y_cord + 40)
    
# defining third floor of building style B
def building_B_floor_3 (x_cord, y_cord):
    building_B_floor_2 (x_cord, y_cord)
    building_B_floor_middle (x_cord, y_cord + 80)

# defining fourth floor of building style B
def building_B_floor_4 (x_cord, y_cord):
    building_B_floor_3 (x_cord, y_cord)
    building_B_floor_middle (x_cord, y_cord + 120)

# defining fifth floor of building style B
def building_B_floor_5 (x_cord, y_cord):
    building_B_floor_4 (x_cord, y_cord)
    building_B_floor_middle (x_cord, y_cord + 160)
    
# defining sixth floor of building style B
def building_B_floor_6 (x_cord, y_cord):
    building_B_floor_5 (x_cord, y_cord)
    building_B_floor_middle (x_cord, y_cord + 200)

# defining seventh floor of building style B
def building_B_floor_7 (x_cord, y_cord):
    building_B_floor_6 (x_cord, y_cord)
    building_B_floor_middle (x_cord, y_cord + 240)

# defining eighth floor of building style B
def building_B_floor_8 (x_cord, y_cord):
    building_B_floor_7 (x_cord, y_cord)
    building_B_floor_middle (x_cord, y_cord + 280)
    
# defining ninth floor of building style B
def building_B_floor_9 (x_cord, y_cord):
    building_B_floor_8 (x_cord, y_cord)
    building_B_floor_middle (x_cord, y_cord + 320)

# defining tenth floor of building style B
def building_B_floor_10 (x_cord, y_cord):
    building_B_floor_9 (x_cord, y_cord)
    building_B_floor_middle (x_cord, y_cord + 360)


##################### Function Definition - BUILDING C ######################

# Defining the roof of the building style C
def building_C_roof (x_cord, y_cord):
    penup()
    goto(x_cord, y_cord)    # goto parameterized position x_axis and y_axis

    # draw roof of the building style C
    pendown()
    begin_fill()
    fillcolor("DarkRed")
    pensize(2)
    forward(100)
    left(140)
    forward(126)
    left(80)
    forward(126)
    setheading(0)
    forward(100)
    end_fill()

    # draw chimney
    penup()
    left(180)
    forward(100)
    right(140)
    forward(80)
    setheading(0)
    pendown()
    left(90)
    begin_fill()
    fillcolor("grey")
    forward(30)
    right(90)
    forward(2.5)
    left(90)
    forward(11.8)
    left(90)
    forward(30)
    left(90)
    forward(11.8)
    left(90)
    forward(30)
    left(180)
    forward(27.5)
    left(90)
    forward(49)
    end_fill()

    # end by moving the turtle back to the point where it started
    penup() # pen up before moving to parameterized position x_axis and y_axis
    goto(x_cord, y_cord)    # goto parameterized position x_axis and y_axis
    setheading(0)   # end with setting the orientation of the turtle to angle 0


# funciton defining the process of building the first floor of building C
def building_C_floor_1 (x_cord, y_cord):
    penup()
    goto(x_cord, y_cord)    # goto parameterized position x_axis and y_axis

    # draw first floor of the building
    pendown()
    pensize(2)
    begin_fill()
    fillcolor("FireBrick")
    forward(75)
    left(90)
    forward(40)
    left(90)
    forward(150)
    left(90)
    forward(40)
    left(90)
    forward(75)
    end_fill()

    # draw window
    penup()
    goto(x_cord, y_cord)
    setheading(0)
    left(90)
    forward(5)
    pendown()
    pensize(3.5)
    pencolor("LightGrey")
    begin_fill()
    fillcolor("DarkBlue")
    right(90)
    forward(20)
    left(90)
    forward(30)
    left(90)
    forward(40)
    left(90)
    forward(30)
    left(90)
    forward(20)
    end_fill()
    
    pensize(3)
    left(90)
    forward(30)
    right(90)
    forward(20)
    right(90)
    forward(14.9)
    right(90)
    forward(40)
    
    pensize(2)
    pencolor("black")

    # end by moving the turtle back to the point where it started
    penup() # pen up before moving to parameterized position x_axis and y_axis
    goto(x_cord, y_cord)    # goto parameterized position x_axis and y_axis
    setheading(0)   # end with setting the orientation of the turtle to angle 0


# function defining the process of building second floor of building C (first floor + first floor of building C, total two floors)
def building_C_floor_2 (x_cord, y_cord):
    building_C_floor_1 (x_cord, y_cord) ## calling the first floor (**always construct the new floor on the previous floor/ floors**)
    building_C_floor_1 (x_cord, y_cord + 40)    # calling the first floor but this time add 40 pixels to the y coordinate so turtle can draw one more floor on the top of first floor

# defining third floor of building style C
def building_C_floor_3 (x_cord, y_cord):
    building_C_floor_2 (x_cord, y_cord)
    building_C_floor_1 (x_cord, y_cord + 80)

# defining fourth floor of building style C
def building_C_floor_4 (x_cord, y_cord):
    building_C_floor_3 (x_cord, y_cord)
    building_C_floor_1 (x_cord, y_cord + 120)

# defining fifth floor of building style C
def building_C_floor_5 (x_cord, y_cord):
    building_C_floor_4 (x_cord, y_cord)
    building_C_floor_1 (x_cord, y_cord + 160)

# defining sixth floor of building style C
def building_C_floor_6 (x_cord, y_cord):
    building_C_floor_5 (x_cord, y_cord)
    building_C_floor_1 (x_cord, y_cord + 200)

# defining seventh floor of building style C
def building_C_floor_7 (x_cord, y_cord):
    building_C_floor_6 (x_cord, y_cord)
    building_C_floor_1 (x_cord, y_cord + 240)

# defining eighth floor of building style C
def building_C_floor_8 (x_cord, y_cord):
    building_C_floor_7 (x_cord, y_cord)
    building_C_floor_1 (x_cord, y_cord + 280)

# defining ninth floor of building style C
def building_C_floor_9 (x_cord, y_cord):
    building_C_floor_8 (x_cord, y_cord)
    building_C_floor_1 (x_cord, y_cord + 320)

# defining tenth floor of building style C
def building_C_floor_10 (x_cord, y_cord):
    building_C_floor_9 (x_cord, y_cord)
    building_C_floor_1 (x_cord, y_cord + 360)



##################### Function Definition - BUILDING D ######################

# Defining the roof of the building style D
def building_D_roof (x_cord, y_cord):
    penup()
    goto(x_cord, y_cord)    # goto parameterized position x_axis and y_axis

    # draw roof floor
    pendown()
    pensize(2)
    begin_fill()
    fillcolor("Cornsilk")
    forward(75)
    left(90)
    forward(40)
    left(90)
    forward(150)
    left(90)
    forward(40)
    left(90)
    forward(75)
    end_fill()

    forward(75)
    left(180)
    forward(15)
    right(90)

    # draw window
    begin_fill()
    fillcolor("DeepSkyBlue")
    forward(20)
    left(90)
    forward(30)
    left(90)
    forward(20)
    left(90)
    forward(30)
    left(180)
    end_fill()

    forward(45)
    right(90)

    # draw window
    begin_fill()
    fillcolor("DeepSkyBlue")
    forward(20)
    left(90)
    forward(30)
    left(90)
    forward(20)
    left(90)
    forward(30)
    left(180)
    end_fill()

    forward(45)
    right(90)

    # draw window
    begin_fill()
    fillcolor("DeepSkyBlue")
    forward(20)
    left(90)
    forward(30)
    left(90)
    forward(20)
    left(90)
    forward(30)
    end_fill()

    penup()
    goto(x_cord, y_cord)
    pendown()
    forward(75)
    left(90)
    forward(40)
    right(90)

    # draw roof
    begin_fill()
    fillcolor("Cornsilk")
    forward(10)
    left(45)
    forward(10)
    setheading(0)
    left(180)
    forward(185)
    setheading(0)
    right(45)
    forward(10)
    setheading(0)
    forward(160)
    end_fill()

    forward(10)
    left(45)
    forward(10)
    setheading(0)

    begin_fill()
    fillcolor("Cornsilk")
    left(45)
    forward(10)
    setheading(0)
    left(180)
    forward(198)
    setheading(0)
    right(45)
    forward(10)
    setheading(0)
    forward(185)
    end_fill()

    # end by moving the turtle back to the point where it started
    penup() # pen up before moving to parameterized position x_axis and y_axis
    goto(x_cord, y_cord)    # goto parameterized position x_axis and y_axis
    setheading(0)   # end with setting the orientation of the turtle to angle 0
    

# funciton defining the process of building the first floor of building D
def building_D_floor_1 (x_cord, y_cord):
    penup()
    goto(x_cord, y_cord)    # goto parameterized position x_axis and y_axis

    # draw floor
    pendown()
    pensize(2)
    begin_fill()
    fillcolor("Cornsilk")
    forward(75)
    left(90)
    forward(40)
    left(90)
    forward(150)
    left(90)
    forward(40)
    left(90)
    forward(75)
    end_fill()

    # drawing pillar
    setheading(0)
    forward(75)
    right(180)
    forward(15)
    right(90)
    forward(40)
    left(90)

    # draw window
    begin_fill()
    fillcolor("DeepSkyBlue")
    forward(30)
    left(90)
    forward(40)
    left(90)
    forward(30)
    left(90)
    forward(40)
    end_fill()

    left(90)
    penup()
    forward(45)
    pendown()

    # draw pillar
    left(90)
    forward(40)
    right(90)

    # draw window
    begin_fill()
    fillcolor("DeepSky Blue")
    forward(30)
    right(90)
    forward(40)
    right(90)
    forward(30)
    right(90)
    forward(40)
    right(90)
    end_fill()

    penup()
    forward(45)
    pendown()

    # draw pillar
    right(90)
    forward(40)
    left(90)

    # draw window
    begin_fill()
    fillcolor("DeepSkyBlue")
    forward(30)
    left(90)
    forward(40)
    left(90)
    forward(30)
    left(90)
    forward(40)
    end_fill()
    
    # end by moving the turtle back to the point where it started
    penup() # pen up before moving to parameterized position x_axis and y_axis
    goto(x_cord, y_cord)    # goto parameterized position x_axis and y_axis
    setheading(0)   # end with setting the orientation of the turtle to angle 0

# function defining the process of building second floor of building D (first floor + first floor of building D, total two floors)
def building_D_floor_2 (x_cord, y_cord):
    building_D_floor_1 (x_cord, y_cord) ## calling the first floor (**always construct the new floor on the previous floor/ floors**)
    building_D_floor_1 (x_cord, y_cord + 40)    # calling the first floor but this time add 40 pixels to the y coordinate so turtle can draw one more floor on the top of first floor

# defining third floor of building style D
def building_D_floor_3 (x_cord, y_cord):
    building_D_floor_2 (x_cord, y_cord)
    building_D_floor_1 (x_cord, y_cord + 80)

# defining fourth floor of building style D
def building_D_floor_4 (x_cord, y_cord):
    building_D_floor_3 (x_cord, y_cord)
    building_D_floor_1 (x_cord, y_cord + 120)

# defining fifth floor of building style D
def building_D_floor_5 (x_cord, y_cord):
    building_D_floor_4 (x_cord, y_cord)
    building_D_floor_1 (x_cord, y_cord + 160)

# defining sixth floor of building style D
def building_D_floor_6 (x_cord, y_cord):
    building_D_floor_5 (x_cord, y_cord)
    building_D_floor_1 (x_cord, y_cord + 200)

# defining seventh floor of building style D
def building_D_floor_7 (x_cord, y_cord):
    building_D_floor_6 (x_cord, y_cord)
    building_D_floor_1 (x_cord, y_cord + 240)

# defining eighth floor of building style D
def building_D_floor_8 (x_cord, y_cord):
    building_D_floor_7 (x_cord, y_cord)
    building_D_floor_1 (x_cord, y_cord + 280)

# defining ninth floor of building style D
def building_D_floor_9 (x_cord, y_cord):
    building_D_floor_8 (x_cord, y_cord)
    building_D_floor_1 (x_cord, y_cord + 320)

# defining tenth floor of building style D
def building_D_floor_10 (x_cord, y_cord):
    building_D_floor_9 (x_cord, y_cord)
    building_D_floor_1 (x_cord, y_cord + 360)



######## Assignment 1 Part B: building incompleted building  ######################

# Defining the building crane
def building_crane (x_cord, y_cord):
    penup()
    goto(x_cord, y_cord)    # goto parameterized position x_axis and y_axis

    # draw building crane
    forward(27.5)
    pendown()
    pensize(3)
    left(90)
    forward(25)
    right(90)
    forward(25)
    right(90)
    forward(25)
    right(90)
    forward(25)
    setheading(0)
    left(45)
    forward(35.36)
    setheading(0)
    left(180)
    forward(25)
    left(135)
    forward(35.36)
    setheading(0)

    left(180)
    forward(25)
    right(90)
    forward(25)
    forward(25)
    right(90)
    forward(25)
    right(90)
    forward(25)
    right(90)
    forward(25)
    setheading(0)
    left(45)
    forward(35.36)
    setheading(0)
    left(180)
    forward(25)
    left(135)
    forward(35.36)
    setheading(0)

    left(180)
    forward(25)
    right(90)
    forward(25)
    forward(25)
    right(90)
    forward(25)
    right(90)
    forward(25)
    right(90)
    forward(25)
    setheading(0)
    left(45)
    forward(35.36)
    setheading(0)
    left(180)
    forward(25)
    left(135)
    forward(35.36)
    setheading(0)

    left(90)
    forward(25)
    right(90)
    forward(25)
    right(90)
    forward(25)
    right(90)
    forward(25)
    setheading(0)
    left(45)
    forward(35.36)
    setheading(0)
    left(180)
    forward(25)
    left(135)
    forward(35.36)
    setheading(0)

    left(180)
    forward(25)
    right(90)
    forward(25)
    forward(40)
    setheading(0)
    right(122)
    forward(47.17)
    setheading(0)
    forward(25)
    left(90)
    forward(13)
    left(90)
    forward(17)
    setheading(0)
    forward(17)
    left(90)
    forward(11)
    left(90)
    forward(10)

    setheading(0)
    forward(10)
    right(90)
    forward(49)
    left(90)
    forward(25)
    right(90)

    begin_fill()
    fillcolor("black")
    forward(5)
    left(90)
    forward(35)
    left(90)
    forward(35)
    left(90)
    forward(35)
    left(90)
    forward(30)
    end_fill()

    right(90)
    forward(50)
    right(45)
    forward(140)
    setheading(0)
    left(15)
    forward(20)
    setheading(0)
    right(45)
    forward(112)
    right(90)
    forward(18)
    right(90)
    forward(18)
    setheading(0)
    forward(22)
    left(180)
    forward(22)
    setheading(0)
    left(45)
    forward(18)
    setheading(0)
    right(180)
    forward(25)
    setheading(0)
    left(45)
    forward(18)
    setheading(0)
    right(180)
    forward(25)
    setheading(0)
    left(45)
    forward(18)
    setheading(0)
    right(180)
    forward(25)
    setheading(0)
    left(45)
    forward(18)
    setheading(0)
    right(180)
    forward(25)
    setheading(0)
    left(45)
    forward(17)
    setheading(0)
    right(180)
    forward(25)
    setheading(0)
    left(45)
    forward(18)

    left(180)
    forward(18)
    setheading(0)
    left(135)
    forward(15)
    setheading(0)
    right(90)
    forward(85)
    dot(10)
    forward(10)
    right(35)
    forward(5)
    circle(5, 190)

    # end by moving the turtle back to the point where it started
    penup() # pen up before moving to parameterized position x_axis and y_axis
    goto(x_cord, y_cord)    # goto parameterized position x_axis and y_axis
    setheading(0)   # end with setting the orientation of the turtle to angle 0



#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# building your city.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
# ***** Change the default argument to False if you don't want to
# ***** display the coordinates and building sites
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(True)

# Give the drawing canvas a title
# ***** Replace this title with your name and/or a description of
# ***** your city
title("Jaewon Seo's SIMCITY: The Random City Plan")

### Call the student's function to build the city
### ***** While developing your program you can call the build_city
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_plan()" as the
### ***** argument to the build_city function.  Your program must
### ***** work for any data set that can be returned by the
### ***** random_plan function.
##build_city(fixed_plan_1) # <-- used for code development only, not marking
build_city(random_plan()) # <-- used for assessment

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()

#
#--------------------------------------------------------------------#

