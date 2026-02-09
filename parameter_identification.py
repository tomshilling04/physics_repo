
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#Input Parameters all in code units
#In all outputs, assume G and c are equal to 1

def massratio(M_1,M_2):
    """
    Finds the mass ratio between the two black holes in the merger.
    """
    q = M_2/M_1
    return q
#Mass ratio between the black holes in simulation
def outerdisc(M_1,M_2,a):
    """
    q = mass ratio 
    a = separation between the two black holes
    output = a fraction of the Roche lobe radius in order to find the outer radius of the accretion disc.
    """
    q = massratio(M_1,M_2)
    x = 0.6*q**(2/3) + np.log(1 + q**(1/3))
    r_L = (0.49*q**(2/3))/(x)
    R_out = 0.9*r_L*a
    return R_out
def decoupling(q,HoverR,M_1,alphass):
    """
    q = mass ratio
    HR = aspect ratio (H/R)
    M_1 = Mass of the primary
    alphass = Shakura Sunyaev viscocity parameter
    The output is the decoupling separation in the system where the decay rate becomes GW driven and not accretion driven
    """
    x = ((M_1**(5/2))/(alphass))**(2/5)
    y = (q*(1+q))**(2/5)
    a_0 = ((512/15)**(2/5))*x*y*(HoverR**(-4/5))
    return a_0
def kepler_angmom(M,R):
    """
    M = mass of the object matter orbits
    R = radius of the separation between central object and orbiting object
    """
    omega = (M/(R**3))**(1/2)
    return omega
def kepler_orbit(M,R):
    """
    M : mass of the object
    R : radius of the object
    returns the time period of the orbit
    """
    P = 2*(np.pi)/kepler_angmom(M,R)
    return P
def visc_timescale(alphass, HoverR,M,R):
    """
    alphass = Shakura and Sunyaev viscosity parameter
    HR = disc aspect ratio H/R
    P = the time period for the outer disc to orbit
    """
    t_vis = (2/3)*(1/alphass)*HoverR**(-2)*(1/kepler_angmom(M,R))
    return t_vis
def GW_timescale(a,mass,q):
    """
    mass is the mass of the primary black hole
    a is the separation between primary and secondary
    q is the mass ratio between the two masses of the primary and secondary black hole
    output: 
    tau : the gravitational wave timsecale of the system
    """
    x = (mass**3)*q*(1+q)
    tau = (5/256)*((a**4)/x)
    return tau
M1 = 1
M2 = 10**(-3)
HR = 0.01
alpha = 0.001
a = 4.75 #code units for seperation
R_p_in = 3*M1
R_s_in = 3*M2


dataset = {
    'Mass ratio, q' : massratio(M1,M2),
    'Decoupling separation' : decoupling(massratio(M1,M2),HR, M1, alpha),
    'R_p,out' : outerdisc(M1,M2,a),
    'R_s,out' : outerdisc(M2,M1,a)
}
table = pd.DataFrame(dataset, index = ['values'])

timescaledataset = {
    'Secondary Timescales' : [visc_timescale(alpha,HR,M2,outerdisc(M2,M1,a)),GW_timescale(a,M2,massratio(M2,M1))],
    'Primary Timescales' : [visc_timescale(alpha,HR,M1, outerdisc(M1,M2,a)),GW_timescale(a,M1,massratio(M1,M2))]
}
index_labels = ['Viscous Timescale','Grav Wave Timescale']
df = pd.DataFrame(timescaledataset, index = index_labels)
print(df)

print(table)

sep = np.arange(1,200)


plt.plot(sep, visc_timescale(alpha, HR,M1,sep) ,color='red',label = 'Viscous timescale')
plt.plot(sep, GW_timescale(sep,M1,massratio(M1,M2)), color = 'green', label = 'GW timescale')
plt.xlim(200,20)
plt.ylabel("timescale")
plt.xlabel("seperation (GM/$c^2$)")
plt.legend()
plt.savefig("Decoupling_Sep.png")
plt.show()