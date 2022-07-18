def firstFit(weight, n, c):
     
    res = 0
     
    bin_rem = [0]*n
     
    for i in range(n):
       
        j = 0
        while( j < res):
            if (bin_rem[j] >= weight[i]):
                bin_rem[j] = bin_rem[j] - weight[i]
                break
            j+=1
             
        if (j == res):
            bin_rem[res] = c - weight[i]
            res= res+1
    return res
     
