## Nick Cudd
## Phys 122 7686 Spring 2022
## Electric Field Predictor

import math

E_x = []
E_y = []
E_z = []
E_xyz = []

# charge object can be (+) or (-), position is a vector of form [x, y, z] coordinates
class pointCharge:
    def __init__(self, charge, position):
        self.charge = charge
        self.position = position

# to calculate distance between two points in [x, y, z] form
def distance(v1, v2):
    return [v2[0] - v1[0], v2[1] - v1[1], v2[2] - v1[2]]

# to calculate magnitude of a vector [x, y, z]
def mag(v):
    return math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)

# returns unit vector with x, y, and z components to determine direction 
def unit_v(v): 
    magnitude = mag(v)
    unit = [v[0] / magnitude, v[1] / magnitude, v[2] / magnitude]
    return unit

def field_vector(charge, charge_position, field_location):
    source = pointCharge(charge, charge_position)
    location = field_location

    # Calculating field magnitude from the electric field equation E = kq / r^2 
    k = 8.99e9
    r = mag((distance(source.position, location)))
    q = charge
    field_magnitude = (k * q) / r**2

    # Finding the seperation unit vector between the source charge and the location in the field, and then scaling by the magnitude of the electric field
    r_hat = unit_v(distance(source.position, location))
    field_v = [component * field_magnitude for component in r_hat]
    return field_v

# Constructing a plane of dimensions n x n meters for a total of n^2 evenly spaced charges of q coulombs each
def plane(q, n):
    points = []
    for x in range(0, n):
        for y in range(0, n):
            charge = pointCharge(q, [x, y, 0])
            points.append(charge)
    return points

test_location = [1, 1, 1] 
source_charge = -0.0000000001
charged_plane = plane(source_charge, 3)

# Creates lists of the x, y, and z components of the electric field at a location respectively 
for point in charged_plane:
    E_x.append(field_vector(point.charge, point.position, test_location)[0]) # List of x-components of each point charge's effect on field
    E_y.append(field_vector(point.charge, point.position, test_location)[1]) # List of y-components of each point charge's effect on field
    E_z.append(field_vector(point.charge, point.position, test_location)[2]) # List of z-components of each point charge's effect on field

# Superposition of all electric field components per axis
E_xyz.append(sum(E_x)) # total x-component of electric field
E_xyz.append(sum(E_y)) # total y-component of electric field
E_xyz.append(sum(E_z)) # total z-component of electric field

# E_xyz has the format (|E|*x-hat, |E|*y-hat,|E|*z-hat), and then finds the magnitude of this vector to determine total resultant electric field vector
print("The electric field at " + str(test_location) + " for plane with dimensions 2 x 2 meters has a magnitude of " + str((E_xyz[0])) + " N/C in the x-direction, a magnitude of " + str((E_xyz[1])) + 
      " N/C in the y-direction, and a magnitude of " + str("{0:.2f}".format(E_xyz[2])) + " N/C in the z-direction.")

# Sign convention: electric fields point away from positive charges and towards negative charges assuming a positive test charge
if source_charge > 0: 
    # when plane points are all positively charged (field points AWAY from plane)
    print("The total electric field vector points away from the plane with magnitude " + str("{0:.2f}".format(mag(E_xyz)))  + " N/C.") 
else:
    # when plane points are all negatively charged (field points TOWARDS plane)
    print("The total electric field vector points towards from the plane with magnitude " + str("{0:.2f}".format(-mag(E_xyz))) + " N/C.")