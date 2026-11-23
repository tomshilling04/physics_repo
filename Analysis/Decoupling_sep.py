import numpy as np
import matplotlib.pyplot as plt


G = 6.67e-11
c = 3e8
solarM = 2e30
def massratio(M_1,M_2):
    """
    Finds the mass ratio between the two black holes in the merger.
    """
    q = M_2/M_1
    return q

def decoupling_sep(M_1,M_2,alphaSS,HoverR):
    """
    """
    a = ((512/15)**0.4)*(((massratio(M_1, M_2)*((G*M_1)**2.5))/(alphaSS*c**5))**0.4)*HoverR**(-0.8)
    return a

def decoupl_newunits(M_1,M_2,alphaSS,HoverR):
    """
    """
    a = decoupling_sep(M_1, M_2, alphaSS, HoverR)*c**2 
    b = a/(G*M_1)
    return b

def GW_timescale(a,M_1,M_2):
    """
    mass is the mass of the primary black hole
    a is the separation between primary and secondary
    q is the mass ratio between the two masses of the primary and secondary black hole
    output: 
    tau : the gravitational wave timsecale of the system
    """
    x = (M_1**3)*massratio(M_1,M_2)*(1+massratio(M_1, M_2))
    tau = (5/256)*((a**4)/x)*(c**5/G**3)
    return tau


def kepler_angmom(M,R):
    """
    M = mass of the object matter orbits
    R = radius of the separation between central object and orbiting object
    """
    omega = (G*M/(R**3))**0.5
    return omega

def visc_timescale(alphass, HoverR,M,a):
    """
    alphass = Shakura and Sunyaev viscosity parameter
    HR = disc aspect ratio H/R
    P = the time period for the outer disc to orbit
    """
    t_vis = (2/3)*(1/alphass)*HoverR**(-2)*(1/kepler_angmom(M,a))
    return t_vis

def Schw_radius(M_1):
    """
    """
    r = (G*M_1)/(c**2)
    return r  
    
# parameters
M1 = 1e8*solarM
M2 = 1e5*solarM
HR = 0.01
alpha = 0.01
R = Schw_radius(M1)
a_val_rg = np.arange(1,100,0.1) #in GM/c^2
a_val_m = a_val_rg*Schw_radius(M1) #in m

plt.plot(a_val_rg, visc_timescale(alpha, HR, M1, a_val_m), label='Viscous Timescale',color='red')
plt.plot(a_val_rg,GW_timescale(a_val_m, M1, M2), label='GW Timescale',color='green')
plt.xlabel(r'separation $(GM/c^2)$')
plt.ylabel('timescale (s)')
plt.gca().invert_xaxis()
plt.legend()

plt.show()
#print(decoupl_newunits(M1, M2, alpha, HR))


