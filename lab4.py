## Lab - 4, @author - Suresh Gandhi

import pandas as pd
import numpy as np
import math 

## Function to calculate the NPV
def NPV(array,r):
    N = 0;
    for i in range(len(array)):
        N = N + array[i]/math.pow(1+r,i)
    return N;
  
## Function for data processing
def data_process(data):
    data.fillna(0, inplace  = True)
    array = np.array(data)
    for i in range(array.shape[1]):
        array[4][i] = array[3][i]-array[2][i]-array[1][i]
        
        if(array[4][i] <= 0):
            array[5][i] = array[4][i]
        else:
            array[5][i] = array[4][i]*(1-array[6][0]/100)
    
    return array
 
## Function to calculate the irr based on Newton Raphson method
def irr_newton(stream):
    rate_0 = 0.0
    n = 0
    d = 0
    s=0
    r = np.arange(len(stream))
    for steps in range(50):
        # print (steps)

        for i in range(len(r)):
            n = n + stream[i] / (math.pow(1 + rate_0, i + 1))

        for i in range(len(r)):
            d = d + (i + 1) * stream[i] / (math.pow(1 + rate_0, i + 2))
        # print (d)
        rate_1 = rate_0 + n / d
        if (abs(rate_1 - rate_0) > 0.0001):
            s=rate_1
            break
        else: rate_0 = rate_1
    return s

def irr_bro(stream):
    rate = 0.0
    for steps in range(50):
        r = np.arange(len(stream))
        # Factor exp(m) out of the numerator & denominator for numerical stability
        m = max(-rate * r)
        f = np.exp(-rate * r - m)
        t = np.dot(f, stream)
        if abs(t) < 0.0001 * math.exp(-m):
            break
        u = np.dot(f * r, stream)
        # Clip the update to avoid jumping into some numerically unstable place
        rate = rate + np.clip(t / u, -1.0, 1.0)

    return math.exp(rate) - 1
  
## Driver function      
def main():
    
    data_pa  = pd.read_csv('cf_Panihati.csv', header = None, index_col = 0)
    array_pa = data_process(data_pa)
    npv_pa = NPV(array_pa[5], array_pa[7][0]/100)
    irr_pa = irr_bro(array_pa[5])
    print("NPV for Panihati coal block is:", npv_pa)
    print("IRR for Panihati coal block is:", irr_pa*100)
    
    data_ek  = pd.read_csv('cf_Ekchakra.csv', header = None, index_col = 0)
    array_ek = data_process(data_ek)
    npv_ek = NPV(array_ek[5], array_ek[7][0]/100) 
    irr_ek = irr_bro(array_ek[5])
    print("\nNPV for Ekchakra coal block is:", npv_ek)
    print("IRR for Ekchakra coal block is:", irr_ek*100)
    
    data_re  = pd.read_csv('cf_Remuna.csv', header = None, index_col = 0)
    array_re = data_process(data_re)
    npv_re = NPV(array_re[5], array_re[7][0]/100)   
    irr_re = irr_bro(array_re[5])
    print("\nNPV for Remuna coal block is:", npv_re)
    print("IRR for Remuna coal block is:", irr_re*100)


    data_bh  = pd.read_csv('cf_Bhadrani.csv', header = None, index_col = 0)
    array_bh = data_process(data_bh)
    npv_bh = NPV(array_bh[5], array_bh[7][0]/100) 
    irr_bh = irr_bro(array_bh[5])

    
    print("\nMaximum value of NPV is for Bhadrani coal block:",npv_bh)
    
    print("Maximum value of IRR is for Bhadrani coal block:",irr_bh*100)

        
if __name__ == "__main__": main()

