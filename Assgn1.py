import numpy as np
import math
import matplotlib.pyplot as plt                                                                                                                                                                                                                                                                                                                                                                                                                                                          
#import pdb                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
#Holder table
pop_size = 50
gens = 100
cross_prob = .8
K = .5                                                                                                                                                                                                                                                                                                                                                                                                                                                          
F = 0
limitsHolder = [-10,10]
limitsEgg = [-1,1]
bestsol = []                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                                                                                                                          
def criteria_check(sol,mode="Holder"):
    x = sol[0]
    y = sol[1]
    if mode!="Holder":
        return limitsEgg[0] <= x <= limitsEgg[1] and limitsEgg[0] <= y <= limitsEgg[1]                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    else:
        return limitsHolder[0] <= x <= limitsHolder[1] and limitsHolder[0] <= y <= limitsHolder[1]
def fitfunc(sol, mode):
    x = sol[0]
    y = sol[1]
    if mode=="Egg":
        return -(512*y+47)*math.sin(math.sqrt(np.abs((x*256)+y*512+47)))-x*512*math.sin(math.sqrt(np.abs(x*512-y*512-47)))
    else:
        return -np.abs(math.sin(x)*math.cos(y)*np.exp(np.abs(1-(math.sqrt(x**2+y**2)/math.pi))))                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
def iscross():
    return np.random.uniform(0,1) > cross_prob                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                                                                                                                          
#Initialize population                                                                                                                                                                                                                                                        
def gencandidate(mode):                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    if mode=='Holder':                                                                                                                                                                                                                                                                                                                                                                                                                                                          
        candidates = [list(np.random.uniform(-10,10,2)) for i in range(pop_size)]                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    else:                                                                                                                                                                                                                                                                                                                                                                                                                                                          
        candidates = [list(np.random.uniform(-1,1,2)) for i in range(pop_size)]                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    return candidates
                                                                                                                                                                                                                                                                                                                                                                                                                                                          
def runDE(function):
    if function=="Egg" or function=="Holder":                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
        candidates = gencandidate(function)                                                                                                                                                                                                                                                                                                                                                                                                                                                          
        #pdb.set_trace()                                                                                                                                                                                                                                                                                                                                                                                                                                                          
        best_sol_gen = 10000
        for j in range(gens):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
            F = np.random.uniform(-2,2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
            for i in range(pop_size):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                check = False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                temp = []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
                while not check:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                    #Mutation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                    xr1 = candidates[np.random.randint(0,pop_size)]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                    xr2 = candidates[np.random.randint(0,pop_size)]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                    xr3 = candidates[np.random.randint(0,pop_size)]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                    temp = candidates[i]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                    candidates[i][0] += K*(xr1[0] - candidates[i][0]) + F*(xr2[0] - xr3[0])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                    candidates[i][1] += K*(xr1[1] - candidates[i][1]) + F*(xr2[1] - xr3[1])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                    #CrossOver                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                    if iscross():                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                        candidates[i][0] = temp[0]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                    if iscross():                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                        candidates[i][1] = temp[1]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                    #Check Criteria                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                    check = criteria_check(candidates[i],function)            
                parent_val = fitfunc(temp, function)
                trial_val = fitfunc(candidates[i], function)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                if parent_val < trial_val:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                    candidates[i] = temp[:]
                    if parent_val < best_sol_gen:
                        best_sol_gen = parent_val
                else:
                    if trial_val < best_sol_gen:
                        best_sol_gen = trial_val
                        
            bestsol.append(best_sol_gen)
        return bestsol
de1 = runDE("Egg")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
x = [i for i in range(gens)]
plt.plot(x, bestsol)
print('last best sol : ',bestsol[-1])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
plt.ylabel("Best solution generation-wise")