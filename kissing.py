import math

def setSphere(dimention, radius):
    endSphere = []
    for i in range(dimention):
        endSphere.append(0)
    endSphere.append(radius)
    return endSphere


#Volume of n = Cn*pi^(n/2)*R^n
#math.comb(7,5)

#Need an iterative formula
def calculateSurfaceArea(sphere, dimention):
    if dimention == 2:
        return 2*math.pi*sphere[dimention]
    if dimention == 3:
        return 4*math.pi*sphere[dimention]**2
    if dimention == 4:
        return 2*math.pi**2*sphere[dimention]**3
    if dimention == 5:
        return 8/3*math.pi**2*sphere[dimention]**4

def calculateVolume(sphere, dimention):
    if (dimention == 2):
        return math.pi*sphere[dimention]**2
    if (dimention == 3):
        return 4/3*math.pi*sphere[dimention]**3
    if (dimention == 4):
        return 1/2*math.pi**2*sphere[dimention]**4
    if (dimention == 5):
        return 8/15*math.pi**2*sphere[dimention]**5


sphere2d = setSphere(2, 1)
sphere3d = setSphere(3, 1)
auxSphere3d = setSphere(3, 2)
sphere4d = setSphere(4, 1)
auxSphere4d = setSphere(4, 2)
sphere5d = setSphere(5, 1)
auxSphere5d = setSphere(5, 2)
sphere6d = setSphere(6, 1)
auxSphere6d = setSphere(6, 2)
sphere7d = setSphere(7, 1)
auxSphere7d = setSphere(7, 2)
sphere8d = setSphere(8, 1)
auxSphere8d = setSphere(8, 2)
sphere9d = setSphere(9, 1)
auxSphere9d = setSphere(9, 2)
sphere10d = setSphere(10, 1)
auxSphere10d = setSphere(10, 2)

#print(calculateVolume(Sphere3d, 3))

#print(calculateSurfaceArea(auxSphere, 3))

#3d
# x1**2 + x2**2 + x3**2 = 1
#cos(theta) = x1*y1+ x2*y2 + x3*y3 <= 1/2
# k^2 <= S(theta) < 13

#No caso 3d podemos simplesmente preencher uma superficie 2d tirada a partir da superficie de uma esfera 3d usando 2*raio

print("Max number of 3d spheres around a 3d sphere: ", calculateSurfaceArea(auxSphere3d, 3)/calculateVolume(sphere2d, 2))

#4d
print("Max number of 4d spheres around a 4d sphere: ", calculateSurfaceArea(auxSphere4d, 4)/calculateVolume(sphere3d, 3))

#5d
print("Max number of 5d spheres around a 5d sphere: ", calculateSurfaceArea(auxSphere5d, 5)/calculateVolume(sphere4d, 4))

# x1**2 + x2**2 + x3**2 + x4**2 = 1 // This is the representation of all points at the edge of the sphere
# Distancia entre 2 pontos no espaço-
#   sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
#
# No caso da nossa esfera precisamos que esta equação iguale a 2 para todos os pares sph0-sphn
# Precisamos tambem que todos os pares sphn-sphm tenham uma distância superior a 2
# Se (xn-xm)**2 > 4 ou y ou z ja verficamos a condição (eficiência)
# Podemos também tentar fazer verificações mais locais a cada esfera por causa de eficiência.
# All generated spheres must be contained in a square of 6r, or 6 units:
#   - This can be done simply by making sure all coordinates are in between -3 and 3
#   - After spawning a sphere anywhere in the cube, we shall then reduce or increase all coordinates proporcinally until
#     we have a distance of 2 to the main sphere (sph0):
#       - This is done with an approximation algorythm until a desired precision.
#       
# There is a problem with the current approach. Assigning random values will result in a lot of free space
# We should try to avoid a weird distance between two spheres avoiding distances like 3.8 which barely allows for a sphere to fit there.
# We should follow some sort of curve or function to maximize proximity between spheres