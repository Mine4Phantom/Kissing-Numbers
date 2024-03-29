import math
import random

point1a = []
point2a = []
dimention = 2

# Euclidean distance of points

def euclideanDistance(point1, point2):
    if (len(point1) != len(point2)):
        return False
    distance = 0
    for i in range(len(point1)):
        distance += (point1[i] - point2[i])**2
    return math.sqrt(distance)


# Check if distance is more than 2

def isDistanceGT2(point1, point2):
    if (euclideanDistance(point1, point2) >= 2):
        return True
    return False

# Generating spheres in a square, cube, tesseract...

def sphereGenerator():
    sphere = []
    for i in range(dimention):
        sphere.append(round(random.uniform(-3,3), 3))
    return sphere


# Define how much to move the sphere

def moverCalc(sphere, auxsphere):
    distance = 2 - euclideanDistance(sphere, auxsphere)
    return math.exp(distance/7)

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
    cnt = 1000
    while(cnt > 0):
        if (distance > 2): # This is an attempt to approximate the values, there are better algorithms
            for i in range(dimention):
                sphere[i] = sphere[i]*moverCalc(sphere, auxsphere)
        elif (distance < 2):
            for j in range(dimention):
                sphere[j] = sphere[j]*moverCalc(sphere, auxsphere)
        
        if round(euclideanDistance(sphere, auxsphere),4) == 2:
            return sphere
        cnt -= 1

# Saves the results to a text file

def saveResults(results_list):
    f = open("results.txt", "a") # Maybe change this to create a new file each time
    f.write("\n Obtained %s results for a %s dimentional sphere:\n\n" % (len(results_list)-1, len(results_list[0])))
    for i in range(len(results_list)):
        f.write(str(results_list[i]))
        f.write("\n")
    f.close()



def main():
    initial = [0,0]
    results = [initial]
    for i in range(10000):
        sphere = sphereGenerator()
        sphere = sphereMover(sphere)
        for i in range(len(results)):
            if(sphere is None):
                continue
            if (not isDistanceGT2(results[i], sphere)):
                break
            if i == len(results) - 1:
                results.append(sphere)
    saveResults(results)

main()