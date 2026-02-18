import numpy as np
import pandas as pd

def discmass(filename,Mdisc):
    """
    """
    file = np.loadtxt(filename) 
    mass_acc1 = file[:,20]
    mass_acc2 = file[:,21]
    initialmass = np.full(mass_acc1.shape, Mdisc)
    totalmass = initialmass - mass_acc1 - mass_acc2 
    return totalmass

def percentagemass(filename,Mdisc):
    """
    """
    file = np.loadtxt(filename)
    mass_acc1 = file[:,20]
    mass_acc2 = file[:,21]
    finalmacc1 = mass_acc1[len(mass_acc1)-1:]
    finalmacc2 = mass_acc2[len(mass_acc2)-1:]
    totalmass = discmass(filename,Mdisc)[len(mass_acc1)-1:]
    return str(finalmacc1), str(finalmacc2), str(totalmass)

percentmacc1 = percentagemass("C:/Users/tomsh/OneDrive - University of Leeds/year 4/Accretion disc/Semester 2/Week4/Cer_resol500thous/gwdisc01_cer500.ev",1)[0]

percentmacc2 = percentagemass("C:/Users/tomsh/OneDrive - University of Leeds/year 4/Accretion disc/Semester 2/Week4/Cer_resol500thous/gwdisc01_cer500.ev",1)[1]
percentdisc = percentagemass("C:/Users/tomsh/OneDrive - University of Leeds/year 4/Accretion disc/Semester 2/Week4/Cer_resol500thous/gwdisc01_cer500.ev",1)[2]



dataset = {
    "Primary Mass acc (%)" : percentmacc1,
    "Secondary Mass acc (%)" : percentmacc2,
    "Final mass of disc (%)" : percentdisc
    }

pd.DataFrame(dataset, index = ['values'])

    
   


