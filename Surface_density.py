import numpy as np
import matplotlib.pyplot as plt


def Sigma_0(R_out,R_in,p,Mdisc):
    """
    
    """
    x = (2-p)*Mdisc
    radiusdiff = R_out**(2-p)-R_in**(2-p)
    sigma0 = x/(2*(np.pi)*radiusdiff)
    return sigma0

MSMBH = 2*10**(38)
SchwaR = (6.67*10**(-11)*MSMBH)/((3*10**(8))**2)
sigma0 = Sigma_0(4.1*SchwaR,2*SchwaR,1.5,0.01*MSMBH)
    
    