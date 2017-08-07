import math
# useful constants
Newtons_universal_gravitational_constant = 6.673*(10**(-11))
mass_of_the_Earth = 5.97 * (10**24)
mass_of_a_person = 100.0
radius_of_the_Earth = 6.37*(10**6)

# variables of useful constants
M_p = mass_of_a_person
M_E = mass_of_the_Earth
R_E = radius_of_the_Earth
G = Newtons_universal_gravitational_constant

# Gravitational potential energy function
def gravitational_potential_energy(mass1,mass2,distance):
    E_grav = (-G * mass1 * mass2)/(distance)
    return E_grav
E = gravitational_potential_energy(M_E,M_p,R_E)


# Gravitational force function
def gravitational_force(mass1,mass2,distance):
    F_grav = (-G * mass1 * mass2)/(distance)**2
    return F_grav
F = gravitational_force(M_E,M_p,R_E)



print ('gravitational potential energy in Joule is: ')
print (E)
print ('gravitational force in Newton is:')
print (F)

print (math.pi)