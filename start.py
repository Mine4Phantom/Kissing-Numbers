import math
import random

point1a = []
point2a = [] 

# Euclidean distance of points

def euclideanDistance(point1, point2):
    if (len(point1) != len(point2)):
        return False
    distance = 0
    for i in range(len(point1)):
        distance += (point1[i] - point2[i])**2
    return math.sqrt(distance)


# Generating spheres in a square, cube, tesseract...

def sphereGenerator(dimention):
    sphere = []
    for i in range(dimention):
        sphere.append(random.randrange(-3,3, 0.1))
    return sphere


# Move the sphere to distance 2 of the main sphere

def sphereMover(sphere):
    dimention = len(sphere)
    auxsphere = []
    for i in range (dimention):
        auxsphere.append(0)

    distance = euclideanDistance(sphere, auxsphere)

    if (not distance):
        print("Something went wrong")
        return False
    
    if (distance == 0):
        print(" We got a 0 spawn")

    while(True):
        if (distance > 2): # This is an attempt to approximate the values, there are better algorithms
            for i in range(dimention):
                sphere[i] = sphere[i]*0.99
        elif (distance < 2):
            for j in range(dimention):
                sphere[j] = sphere[j]*1.01
        
        if math.round(euclideanDistance(sphere, auxsphere),3) == 2:
            return sphere

