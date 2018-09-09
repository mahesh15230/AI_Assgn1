import numpy as np
import math
import matplotlib.pyplot as plt
import pdb

#Holder table
pop_size = 15
gens = 30
cross_prob = .8
K = .5
F = 0
limitsHolder = [-10,10]
limitsEgg = [-1,1]
delta = 100
stopgen_limit = .001
#genfitvals = []
bestsol = []

def criteria_check(sol,mode="Holder"):
    if mode!="Holder":
        return np.abs(sol[0]) >= limitsEgg[0] and np.abs(sol[1]) <= limitsEgg[1]
    else:
        return np.abs(sol[0]) >= limitsHolder[0] and np.abs(sol[1]) <= limitsHolder[1]

def fitfunc(sol, mode="Egg", objfnmode=None):#Egg,None for egg holder
    if objfnmode == None:
        if mode=="Egg":
            return math.sqrt((sol[0]-1)**2+(sol[1]-0.7895154296875)**2)
        else:
            return math.sqrt((sol[0]-8.05502)**2 + (sol[1]-9.66549)**2)
    else:
        if mode == None:
            return -(512*sol[1]+47)*math.sin(math.sqrt(np.abs((sol[0]*256)+sol[1]*512+47)))-sol[0]*512*math.sin(math.sqrt(np.abs(sol[0]*512-sol[1]*512-47)))
        else:
            return -np.abs(*math.sin(sol[0])*math.cos(sol[1])*np.exp(np.abs(1-(math.sqrt(sol[0]**2+sol[1]**2)/math.pi))))

def iscross():
    return np.random.uniform(0,1) < cross_prob

#Initialize population
def gencandidate(mode):
    if mode=='Holder':
        candidates = [list(np.random.uniform(-10,10,2)) for i in range(pop_size)]
    else:
        candidates = [np.random.uniform(-1,1,2) for i in range(pop_size)]
    return candidates
        
candidates = gencandidate('Egg')
#pdb.set_trace()

for j in range(gens):
    print('gens')
    if delta <= stopgen_limit:
        break
    F = np.random.uniform(-2,2) # Same F value for the current gen
    print('Traversing all candidates')
    for i in range(pop_size):
        check = False
        temp = []
        while not check:        
            #Mutation
            print("Mutation")
            xr1 = candidates[np.random.randint(0,pop_size)]
            xr2 = candidates[np.random.randint(0,pop_size)]
            xr3 = candidates[np.random.randint(0,pop_size)]
            temp = candidates[i]
            candidates[i][0] += K*(xr1[0] - candidates[i][0]) + F*(xr2[0] - xr3[0])
            candidates[i][1] += K*(xr1[1] - candidates[i][1]) + F*(xr2[1] - xr3[1])
            #CrossOver
            if iscross():
                index1 = int(np.random.uniform(0,2))%2
                if not index1:
                    (candidates[i][0],temp[0]) = (temp[0],candidates[i][0])
                    (candidates[i][1],temp[1]) = (temp[1],candidates[i][1])
                else:
                    (candidates[i][1],temp[1]) = (temp[1],candidates[i][1])
            print("CrossOver")
            #Check Criteria
            check = criteria_check(candidates[i],'Egg')
            print('check is ',check)
            print('temp : ',temp)
            print('candidates : ',candidates[i])
            #print("Check Criteria")
        #Perform Selection
        if fitfunc(temp,"Egg") < fitfunc(candidates[i],"Egg"):
            candidates[i] = temp
        print('selection')
        print('delta value ',delta)
        if delta > fitfunc(candidates[i],"Egg"):
            delta = fitfunc(candidates[i],"Egg")
        bestsol.append(delta)


plt.plot(bestsol)
plt.ylabel("Best solution generation-wise")
print('whew')
print("last best sol is ",delta)
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            