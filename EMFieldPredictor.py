## Nick Cudd
## Phys 122 7686 Spring 2022
## Electric Field Force Predictor

import math

## Charge object can be (+) or (-), position is a list of form [x, y, z] coordinates
class pointCharge:
    def __init__(self, charge, position):
        self.charge = charge
        self.position = position
        
## Uses position list (vector) elements a[x, y, z] and b[x, y, z] to determine distance between two arbitrary points in 3d space
def pointDistance (a, b):
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2 + (b[2] - a[2])**2)

## For determining electric field between source charge and field location --> b = field location, a = source charge location
def electricField(Q, a, b): 
    k = 8.99e9
    return (k * Q) / pointDistance(a, b)**2

## Defines a cube of arbitrary dimensions n meters comprised of equally distributed and equally charged particles of charge C coulombs
def cubeMaker(Q, n):
    cube = []
    for x in range(0, n + 1):
        for y in range(0, n + 1):
            for z in range(0, n + 1):
                piece = pointCharge(Q, [x, y, z]) ## "Filling up" each dimension with charges inside the cube
                cube.append(piece)
    return cube

## Defines a field generated by a cube of equally charged/distanced particles
## The total field vector at some location is a combination or superposition of all vectors pointing from each field charge to the field location
def superposition(fieldLocation, sourceCharge, fieldDimensions):
    field = cubeMaker(sourceCharge, fieldDimensions)
    total = 0
    for point in field: ## Each point is a vector (list in the form [x, y, z]) that points to a constituent particle in the cube of charges
        total += electricField(sourceCharge, point.position, fieldLocation) ## Adding up the effect of each individual particle on the field location
    return total

print("The electric field generated by a charge at a location in space is defined by the force it would exert on a positive test charge at that location. By the principle of superposition, the electric " 
      + "field of a group of charges on a point is defined by the combination of each individual charge's electric field on that point. " 
      + "This program creates a cube with n meter sides with a uniform charge distribution of Q coulombs per square meter to calculate the cumulative electric field at a given coordinate position. " 
      + "By combining the resultant vectors from each cube particle's effect on some location in the field using [kQ / r^2], we can calculate the net electric field at that location.")

print("\nExample: A 1m x 1m x 1m (unit) cube is comprised of 8 equally charged and equally distributed particles with charges of 1 coulomb. To determine the overall electric field at point "
      + "(2, 2, 2,), we need to combine the effects of each constituent particle on that location in space. This program iterates over each particle's electric field with respect to (2, 2, 2) and "
      + "sums their vectors using the principle of superposition, resulting in " + str("{:.1e}".format((superposition([2,2,2], 1, 1)))) + " N/C. Because of the definition of the electric field, " 
      + "it is consistent that this result is positive as the cube is comprised of positive charges, meaning that a positive test charge would be repelled. If the cube were comprised of the same charge "
      + "but negative, this vector would be the same in magnitude but opposite in direction.")