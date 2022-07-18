import time
import random
from NP_worst import worstFit
from NP_first import firstFit
from NP_best import BestFit


for i in range(5):
    
    weight = [2, 5, 4, 7, 1, 3, 8]
    c = 10
    n = len(weight)
    
    
    start = time.perf_counter()
    firstFit(weight, n, c)
    end = time.perf_counter()
    
    print("Number of bins required in First Fit : ",firstFit(weight, n, c))
    print("Time consumed for First fit Programming: ",end - start)
    
    start = time.perf_counter()
    BestFit(weight, n, c)
    end = time.perf_counter()
    
    print("Number of bins required in Best Fit : ",BestFit(weight, n, c))
    print("Time consumed for Best fit Programming: ",end - start)
    
    start = time.perf_counter()
    worstFit(weight, n, c)
    end = time.perf_counter()
    
    print(f"Number of bins required in Worst Fit : {worstFit(weight, n, c)}")
    print("Time consumed for Worst Fit Programming: ",end - start)
