## Nick Cudd
## Phys 122 7686 Spring 2022
## Electric Field Force Predictor
## Distance assumed to be in meters (m), charge assumed to be in coulombs (C), origin is defined at [0, 0, 0]

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

## Defines a cube of arbitrary dimensions (m) comprised of equally distributed and equally charged particles (C)
def cubeMaker(Q, n):
    cube = []
    for x in range(0, n):
        for y in range(0, n):
            for z in range(0, n):
                piece = pointCharge(Q, [x, y, z]) ## "Filling up" each dimension with charges
                cube.append(piece)
    return cube

## Defines a field generated by a cube of equally charged/distanced particles
## The total field vector at some location is a combination or superposition of all vectors pointing from each field charge to the field location
def superposition(fieldLocation, sourceCharge, fieldDimensions):
    field = cubeMaker(sourceCharge, fieldDimensions)
    total = 0
    for i in field: ## Each i is a vector that points to a constituent particle in the cube of charges
        total += electricField(sourceCharge, i.position, fieldLocation) ## Adding up the effect of each individual particle on the field location
    return total

print("Example: The electric field at (3, 3, 3) for a 2m x 2m x 2m solid cube with 1 C per m^2 would result in a vector with magnitude \n" 
      + str("{:.1e}".format((superposition([3,3,3], 1, 2)))) + " N/C, assuming positive to be away from the cube and negative to be towards the cube.")

print("\nSimilarly, the electric field at (3, 3, 3) for a 2m x 2m x 2m solid cube with -1 C per m^2 would result in a vector with magnitude \n" 
      + str("{:.1e}".format((superposition([3,3,3], -1, 2)))) + " N/C, opposite to the direction of 1 C per m^2")