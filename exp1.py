import math #import pi
def goto(linenum):  #create goto function
    global line
    line = linenum
line = 1
while True:
    if line == 1:
        choice = input("Enter 1 to find the volume of a cube.\nEnter 2 to find the volume of  a cylinder.\nEnter 3 to find the volume of a cone.\nEnter 4 to find the volume of a sphere.\n:")  #choice of what object to find the volume of
        if choice == '1':
            cube_edge = input("Edge: ")
            a1 = float(cube_edge)
            v1 = a1 * a1 * a1   #formula for volume of cube (a^3)
            print("The volume for the cube is: ",v1)
            goto(2) #jump to prompt
        if choice == '2':
            cylinder_rad = input("Radius: ")
            cylinder_height = input("Height: ")
            b1 = float(cylinder_rad)
            b2 = float(cylinder_height)
            v2 = math.pi * b1 * b1 * b2 #formula for volume of cylinder (pi*r^2*h)
            print("The volume for the cylinder is: ",v2)
            goto(2)
        if choice == '3':
            cone_rad = input("Radius: ")
            cone_height = input("Height: ")
            c1 = float(cone_rad)
            c2 = float(cone_height)
            v3 = math.pi * c1 * c1 * c2 #formula for volume of cone (pi*r^2*h / 3)
            v3 = v3 / 3
            print("The volume for the cone is: ",v3)
            goto(2)
        if choice == '4':
            sphere_rad = input("Radius: ")
            d1 = float(sphere_rad)
            v4 = math.pi * d1 * d1 * d1 * 4 #formula for volume of sphere (pi*r^3 * 4/3)
            v4 = v4 / 3
            print("The volume for the sphere is: ",v4)
            goto(2)
    elif line == 2:
            user_input = input("Would you like to find the volume of another object? (yes/no): ")   #prompt if user wants to find the volume of another object
            yes_choices = ['yes', 'y', 'ye']    #list for similar words to yes
            no_choices = ['no', 'n', 'on']      #list for similar words to no
            if user_input.lower() in yes_choices:
                goto(1)
            else:
                print("Thank you!")
                break