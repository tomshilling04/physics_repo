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
    c = 3*10**8
    G = 6.67*(10**(-11))
    beta = (64/5)*(((G**3)*M1*M2*(M1+M2))/(c**5))
    a = (a0 - (4*beta*t))**(1/4)
    return a
    
    

def SurfaceDensity(filename,M1, M2,initial_R_out, a0, R_in, N, Mdisc):
    """

    Parameters
    ----------
    filename : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    
    
    file = np.loadtxt(filename)
    totmacc = file[:,22]
    time = file[:,0]
    a = seperation(M1,M2,a0,time[N])
    R = np.arange(R_in,a0)
    if  a > initial_R_out:
        
        refsigma = Sigma_0(initial_R_out,R_in,1.5,Mdisc - totmacc[N])
        SurfDens = refsigma*((R/R_in)**1.5)
        return R, SurfDens
    elif a<= initial_R_out:
        
        refsigma = Sigma_0(a, R_in,1.5,Mdisc - totmacc[N])
        SurfDens = refsigma*((R/R_in)**1.5)
        return R, SurfDens
    
def TimePoint(filename, N):
    """
    """
    file = np.loadtxt(filename)
    time = file[:,0]
    return time[N]


plt.plot(SurfaceDensity("C:/Users/tomsh/OneDrive - University of Leeds/year 4/Accretion disc/Semester 2/Week4/Ret_resol1mill/gwdisc01_ret1mill.ev", 1*Mdisc, 0.001*Mdisc, 4.1*SchwaR, 4.75*SchwaR, 2*SchwaR, 100, 1*Mdisc))
        
    
    
    
    
    
    
