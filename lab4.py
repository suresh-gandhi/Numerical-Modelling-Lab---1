#### ASSIGNMENT - 4 
#### @author - SURESH GANDHI (14MI31024)

MAX_LOG_RATE = 1e3
BASE_TOL = 1e-12
irrMaxInterations = 70
irrAccuracy = .00000001
irrInitialGuess = 0
import pandas as pd
import numpy 
import math 
import numpy as np

## Function to calculate the NPV
def NPV(array,r):
    N = 0
    for i in range(len(array)):
        N = N + array[i]/math.pow(1+r,i)
    return N
  
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
 
## Function to calculate the IRR
def IRR(values):
    s = 0
    r = numpy.arange(len(values))
    if len(values) == 0:
        return s

    x0 = 0
    x1 = 0
    for i in range(0, irrMaxInterations):
        fValue = 0
        fDerivative = 0
        for k in r:
            fValue = fValue + values[k] / math.pow(1.0 + x0, k)

            fDerivative = round(fDerivative - k * values[k] / math.pow(1.0 + x0, k + 1.0), 3)

        x1 = x0 - round(fValue / fDerivative, 4)
        if abs(x1 - x0) > irrAccuracy:
            s = x1
            break
        else:
            x0 = x1

    return s
       
## The main driver function
def main():
    
    data_pa  = pd.read_csv('cf_Panihati.csv', header = None, index_col = 0)
    array_pa = data_process(data_pa)
    npv_pa = NPV(array_pa[5], array_pa[7][0]/100)
    irr_pa = IRR(array_pa[5])
    
    data_ek  = pd.read_csv('cf_Ekchakra.csv', header = None, index_col = 0)
    array_ek = data_process(data_ek)
    npv_ek = NPV(array_ek[5], array_ek[7][0]/100) 
    irr_ek = IRR(array_ek[5])
    
    data_re  = pd.read_csv('cf_Remuna.csv', header = None, index_col = 0)
    array_re = data_process(data_re)
    npv_re = NPV(array_re[5], array_re[7][0]/100)   
    irr_re = IRR(array_re[5])


    data_bh  = pd.read_csv('cf_Bhadrani.csv', header = None, index_col = 0)
    array_bh = data_process(data_bh)
    npv_bh = NPV(array_bh[5], array_bh[7][0]/100) 
    irr_bh = IRR(array_bh[5])

    print("IF WE CONSIDER THE NPV FOR THE PROJECT DECISION: ")
    print("MR GOPINATH SHOULD GO WITH THE BHANDARI PROJECT AS ITS NPV IN CR IS ")
    print(npv_bh) 
    
    print("IF WE CONSIDER THE IRR FOR THE PROJECT DECISION")
    print("MR GOPINATH SHOULD GO WITH THE BHANDARI PROJECT AS ITS IRR IS ")
    print(irr_bh) 
        
if __name__ == "__main__": main()
    


