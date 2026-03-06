#Week 7, Program 4 - Coordinates
#Caiden Heinrichs
#03/06/26

import math


#Finds the distance between two points using the formula
def distanceBetweenPoints(point1, point2):
    distance = math.sqrt(((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2))
    return round(distance, 4)


def main():
    #Collects user input for coordinates
    try:
        coordinateX = float(input("Enter the x coordinate for the first point: "))
        coordinateY = float(input("Enter the y coordinate for the first point: "))
        coordinateZ = float(input("Enter the z coordinate for the first point: "))
    except:
        print("Please enter valid input.")

    #Builds the 1st point from the coordinates
    point1 = (coordinateX, coordinateY, coordinateZ)

    #Reassigns coordinates to new input
    try:
        coordinateX = float(input("Enter the x coordinate for the second point: "))
        coordinateY = float(input("Enter the y coordinate for the second point: "))
        coordinateZ = float(input("Enter the z coordinate for the second point: "))
    except:
        print("Please enter valid input.")

    #Builds the 2nd point from new coordinates
    point2 = (coordinateX, coordinateY, coordinateZ)

    #Calculates the distance and prints it
    distance = distanceBetweenPoints(point1, point2)
    print(f'The distance between the two points is about {distance}')


if __name__ == '__main__':
    main()
