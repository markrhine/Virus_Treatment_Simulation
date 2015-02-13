# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    
    results = []
    gutresults = []
    for a in range(300):
        results.append([])
        gutresults.append([])
    for b in range(numTrials):
        viruses = []
        for c in range(10000):
            resistances = {'guttagonol': False}
            vir = ResistantVirus(.1, .05, resistances, .005)
            viruses.append(vir)
        
        Mark = TreatedPatient(viruses, 1000)
        
        for d in range(150):
            pop = Mark.update()
            results[d].append(pop)
            gutpop = Mark.getResistPop(['guttagonol'])
            gutresults[d].append(gutpop)
        
        Mark.addPrescription('guttagonol')
        
        for e in range(150, 300):
            newpop = Mark.update()
            results[e].append(newpop)
            newgutpop = Mark.getResistPop(['guttagonol'])
            gutresults[e].append(newgutpop)
        
    FinalResults = results[299]
    print len(FinalResults)
    
    
    
    pylab.figure(5)
    pylab.hist(FinalResults, bins = 10)
    pylab.title('Simulation with Drugs - Frequency')
    pylab.xlabel('Virus Population')
    pylab.ylabel('Number of Trials with Population') 
    pylab.legend()
    pylab.show()






#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    results = []
    gutresults = []
    
    for a in range(375):
        results.append([])
        gutresults.append([])
    
    for b in range(numTrials):
        viruses = []
        for c in range(100):
            resistances = {'guttagonol': False, 'grimpex': False}
            vir = ResistantVirus(.1, .05, resistances, .02)
            viruses.append(vir)
        
        Mark = TreatedPatient(viruses, 1000)
        
        for d in range(150):
            pop = Mark.update()
            results[d].append(pop)
            gutpop = Mark.getResistPop(['guttagonol'])
            gutresults[d].append(gutpop)
        
        Mark.addPrescription('guttagonol')
        
        for e in range(150, 225):
            newpop = Mark.update()
            results[e].append(newpop)
            newgutpop = Mark.getResistPop(['guttagonol'])
            gutresults[e].append(newgutpop)
        
        Mark.addPrescription('grimpex')
        
        for f in range(225, 375):
            newpop = Mark.update()
            results[f].append(newpop)
            
        
    FinalResults = results[374]
    print len(FinalResults)
    
      
    pylab.figure(6)
    pylab.hist(FinalResults, bins = 10)
    pylab.title('300 day delay')
    pylab.xlabel('Virus Population')
    pylab.ylabel('Number of Trials with Population') 
    pylab.show()


simulationTwoDrugsDelayedTreatment(110)

