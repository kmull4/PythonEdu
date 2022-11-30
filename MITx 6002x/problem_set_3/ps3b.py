# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics 

import random
import pylab
from ps3b_precompiled_39 import * # for Python version 3.9

''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''


#
# PROBLEM 1
#
class SimpleVirus(object):
    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        return self.maxBirthProb

    def getClearProb(self):
        """
        Returns the clear probability.
        """
        return self.clearProb

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """
        if random.random() > self.getClearProb():
            return False
        else:
            return True

    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         
        
        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """
        reproduceProb = self.maxBirthProb * (1 - popDensity)
        if random.random() > reproduceProb:
            raise NoChildException # did not reproduce
        else: # return new instance of SimpleVirus
            return SimpleVirus(self.maxBirthProb, self.clearProb)

class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        """
        self.viruses = viruses
        self.maxPop = maxPop

    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """
        return self.viruses

    def getMaxPop(self):
        """
        Returns the max population.
        """
        return self.maxPop

    def getTotalPop(self):
        """
        Gets the size of the current total virus population. 
        returns: The total virus population (an integer)
        """
        return len(self.viruses)

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        
        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.                    
          
        popDensity is defined as the ratio of the current virus population to
        the maximum virus population for a patient and should be calculated in
        the update method of the Patient class.
        
        returns: The total virus population at the end of the update (an
        integer)
        """
        for v in self.viruses:
            # see if virus has cleared naturally
            if v.doesClear():
                self.viruses.remove(v)
                continue
        # calc new population density (popDensity, float)
        popDensity = len(self.viruses)/self.maxPop
        # determine how many produce with new popDensity
        for v in self.viruses[0:len(self.viruses)]: # index to stop and no new ones added
            try:
                self.viruses.append(v.reproduce(popDensity))
            except NoChildException: # did not make a child virus
                continue
        return len(self.viruses)


#
# PROBLEM 2
#
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    # timesteps and graph values
    timesteps = 300
    yVals, results, finalY = list(), list(), list()
    
    # run simulation numTrials times
    for i in range(numTrials):
        viruses = [] # new list of viruses
        for j in range(numViruses): # add virus instances
            viruses.append(SimpleVirus(maxBirthProb, clearProb))
        # create instance of Patient
        mypatient = Patient(viruses, maxPop)
        # run simulation on mypatient
        for k in range(timesteps):
            yVals.append(mypatient.update())
        # add list of yVals to results
        results.append(yVals)
    
    # average out results
    for i in range(timesteps):
        avg = [] # blank list
        for l in results:
            avg.append(l[i]) # add the value for each list at index i
        finalY.append(sum(avg) / len(avg))
    
    # plot
    pylab.plot(finalY, label = "SimpleVirus")
    pylab.title("SimpleVirus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend(loc = "best")
    pylab.show()

#
# PROBLEM 3
#
class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)       

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """
        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self.resistances = resistances
        self.mutProb = mutProb

    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        return self.resistances

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        return self.mutProb

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.       

        drug: The drug (a string)

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        try:
            return self.resistances[drug]
        except KeyError:
            return False

    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.

        A virus particle will only reproduce if it is resistant to ALL the drugs
        in the activeDrugs list. For example, if there are 2 drugs in the
        activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        then it will NOT reproduce.

        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:      

        self.maxBirthProb * (1 - popDensity).                       

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.       

        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mutProb is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population       

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """
        # check to see if resistant to all drugs
        for drug in activeDrugs:
            if self.isResistantTo(drug) == False:
                raise NoChildException # not resistant to at least one drug
        
        # similar to SimpleVirus chance to reproduce
        reproduceProb = self.maxBirthProb * (1 - popDensity)
        if random.random() > reproduceProb:
            raise NoChildException # did not reproduce naturally
        
        # calculate mutations for offspring
        newResistances = self.resistances.copy()
        for drug in self.resistances:
            if self.resistances[drug] == True:
                # mutProb chance to lose resistance
                if random.random() < self.mutProb:
                    newResistances[drug] = False
            
            elif self.resistances[drug] == False:
                # 1-mutProb chance to gain resistance
                if random.random() > (1 - self.mutProb):
                    newResistances[drug] = True
        
        return ResistantVirus(self.maxBirthProb, self.clearProb,\
                              newResistances, self.mutProb)

#
# PROBLEM 4
#
class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).              

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        """
        Patient.__init__(self, viruses, maxPop)
        self.prescriptions = []

    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """
        if newDrug not in self.prescriptions:
            self.prescriptions.append(newDrug)

    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """
        return self.prescriptions

    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        population = 0
        # loop through viruses
        for v in self.viruses:
            resistAll = True
            # loop through drugResist
            for d in drugResist:
                try:
                    if v.resistances[d] == False:
                        resistAll = False
                except KeyError:
                    resistAll = False
            if resistAll == True:
                population += 1
        return population

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        """
        for v in self.viruses:
            # see if virus has cleared naturally
            if v.doesClear():
                self.viruses.remove(v)
                continue
        # calc new population density (popDensity, float)
        popDensity = len(self.viruses)/self.maxPop
        # determine how many produce with new popDensity
        for v in self.viruses[0:len(self.viruses)]: # index to stop and no new ones added
            try:
                self.viruses.append(v.reproduce(popDensity, self.prescriptions))
            except NoChildException: # returned a NoChildException
                continue
        return len(self.viruses)

#
# PROBLEM 5
#
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """
    # timesteps and graph values
    timesteps = 150
    resultsTotal, resultsResistant, finalYTotal, finalYResistant = list(), list(), list(), list()
    # remember that "resultsX" are a list of lists of the data so far
    
    # begin trials
    for i in range(numTrials):
        # run simulation per instructions
        viruses, yValsTotal, yValsResistant = [], [], [] # new lists
        for j in range(numViruses): # add virus instances
            viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
        # create new instance of Patient
        mypatient = TreatedPatient(viruses, maxPop)
        
        # begin time
        for k in range(timesteps):
            yValsTotal.append(mypatient.update()) # core update() method
            yValsResistant.append(mypatient.getResistPop(['guttagonol']))
        # add treatment halfway through
        mypatient.addPrescription('guttagonol')
        # continue simulation on mypatient for the same amount of timesteps
        for k in range(timesteps):
            yValsTotal.append(mypatient.update()) # core update() method
            yValsResistant.append(mypatient.getResistPop(['guttagonol']))
        
        # add data to results
        resultsTotal.append(yValsTotal)
        resultsResistant.append(yValsResistant)
        
    
    # trials done, now average out resultsTotal
    for i in range(timesteps*2): # remember how timesteps was used earlier
        avg = [] # new list
        for l in resultsTotal:
            avg.append(l[i]) # add the value for each list at index i
        finalYTotal.append(sum(avg) / len(avg))
    # resultsResistant
    for i in range(timesteps*2): # remember how timesteps was used earlier
        avg = [] # new list
        for l in resultsResistant:
            avg.append(l[i]) # add the value for each list at index i
        finalYResistant.append(sum(avg) / len(avg))
    
    # plot
    pylab.plot(finalYTotal, label = "Virus Total Count")
    pylab.plot(finalYResistant, label = "Virus Resistant Count")
    pylab.title("ResistantVirus simulation")
    pylab.xlabel("Time Step")
    pylab.ylabel("# viruses")
    pylab.legend(loc = "best")
    pylab.show()


if __name__ == "__main__":
    #simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, 100)
    simulationWithDrug(75, 100, .8, 0.1, {"guttagonol": True}, 0.8, 10)