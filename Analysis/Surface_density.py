import numpy as np
import matplotlib.pyplot as plt


def Sigma_0(R_out,R_in,p,Mdisc):
    """
    Inputs:
        R_out: This is the outer radius of my accretion disc
        R_in: This is the inner radius of my accretion disc
        p: The power law of surface density profile
        Mdisc: the mass of the disc 
    
    Outputs:
        sigma0: returns the reference surface density that is used for later calculations
        This value is in kgm**-3 so differs to .discparam file
        Reference radius = inner radius
    """
    x = (2-p)*Mdisc
    radiusdiff = (R_out**(2-p))-(R_in**(2-p))
    sigma0 = x/(2*(np.pi)*radiusdiff*(R_in**p))
    return sigma0

Mdisc = 2*10**(30)
SchwaR = (6.67*10**(-11)*Mdisc)/((3*10**(8))**2)
sigma0 = Sigma_0(4.1*SchwaR,2*SchwaR,1.5,2*10**30) 

def seperation(M1,M2,a0,t):
    """
    

    Parameters
    ----------
    M1 : The mass of the primary SMBH
    M2 : The mass of the secondary SMBH
    a0 : The initial seperation of M1 and M2
    t  : The time from beginning of simulation
        
        
    Returns
    -------
    a  : This is the seperation at time t of the simulation. The seperation is 
        approximately equal to the outer radius.
        
    Used to calculate the surface density across radius as reference surface dens. 
    changes.

    """
    #c = 3*10**8
    c = G =1
    #G = 6.67*(10**(-11))
    beta = (64/5)*(((G**3)*M1*M2*(M1+M2))/(c**5))
    a = (a0**4 - (4*beta*t))**(1/4)
      
    
    return a
  

def SurfaceDensity(filename,M1, M2,initial_R_out, a0, R_in, N, Mdisc):
    """

    Parameters
    ----------
    filename : the file that has all the data available
    M1 : The mass of the primary
    M2 : The mass of the secondary
    initial_R_out : This is the value of the outer rarius initially before the secondary interferes
    a0 : The initial seperation, dependent on sim
    R_in : the inner radius. Also considered R_ref
    N : Float at a specific data point within the data file
    Mdisc : The mass of the accretion disc. In the sim = M1 and also 1 solar mass
    Returns
    -------
    R : Te radius within the disc between R_in and R_out
    SurfDens : The surface density at the specific radius

    """
    
    
    file = np.loadtxt(filename)
    totmacc = file[:,22]
    time = file[:,0]
    a = seperation(M1,M2,a0,time[N])
    R = np.arange(R_in,a0, 0.1)
    if  a > initial_R_out:
        
        refsigma = Sigma_0(initial_R_out,R_in,1.5,Mdisc - totmacc[N])
        SurfDens = refsigma*((R/R_in)**(-1.5))
        return SurfDens, R
    elif a<= initial_R_out:
        
        refsigma = Sigma_0(a, R_in,1.5,Mdisc - totmacc[N])
        SurfDens = refsigma*((R/R_in)**1.5)
        return SurfDens, R
    
def TimePoint(filename, N):
    """
    Inputs: 
        filename : Reading this file in order to find the time point I am using
    """
    file = np.loadtxt(filename)
    time = file[:,0]
    return time[N]

file = "C:/Users/tomsh/OneDrive - University of Leeds/year 4/Accretion disc/Semester 2/Week4/Retrograde_resol2mill/gwdisc01_ret2mill.ev"

SurfDens, R = SurfaceDensity(file, 1, 0.001, 4.1, 4.75, 2, 400, 1)
  
def kepler_angmom(M,R):
    """
    M = mass of the object matter orbits
    R = radius of the separation between central object and orbiting object
    """
    omega = (M/(R**3))**(1/2)
    return omega   
    
def Height(R,HoverR):
    """
    """
    H = R * HoverR
    return H

def kinematic_visc(R,M,HoverR,alpha):
    """
    """
    H = Height(R, HoverR)
    Omega = kepler_angmom(M, R)
    v = alpha*H*Omega
    return v

    
