def worstFit( weight, n, c):
 
    res = 0
 
    bin_rem = [0 for i in range(n)]
     
   
    for i in range(n):
     
        mx,wi = -1,0
 
        for j in range(res):
            if (bin_rem[j] >= weight[i] and bin_rem[j] - weight[i] > mx):
                wi = j
                mx = bin_rem[j] - weight[i]
             
 
        if (mx == -1):
            bin_rem[res] = c - weight[i]
            res += 1
         
        else: 
            bin_rem[wi] -= weight[i]
     
    return res
 
