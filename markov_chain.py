#import 
import numpy as np
import matplotlib.pyplot as plt
def fkpp(n,N):
    """[summary]        

    Args:
        n (int): [description]
        N ([int): [description]

    Returns:
        oyeah: norm of p-p_stationary, where p_stationary is the eigenvector of P transpose
    """
    #generate random n vector
    p=np.random.rand(n,n)
    #adjust the ratio/scale such that the sum of the values is 1
    p=p/np.sum(p)
    #generate random matrix of size n by n 
    P=np.random.rand(n,n)
    #scale P
    P=P/P.sum(axis=1)[:,None]
    print(P)
    #calculate the eigenvector of the matrix transpose
    w,v=np.linalg.eig(np.transpose(P))
    #scale the entries such that the sum is 1, then rename it
    diao=w/np.sum(w)
    p_stationary=diao
    #for loop function to compute the norm of p-p_stationary
    #rescale the matrix P
    for r in range(n):
        P[r]=P[r]/np.sum(P[r])
    #define the output oyeah and begin with zeros as entries
    oyeah=np.zeros(N)
    for i in range(N):
        p=np.matmul(np.transpose(P),p)
        oyeah[i]=np.linalg.norm(p-p_stationary)
       
    return oyeah
#input n and N to run the function
fks=(fkpp(5,50))
#plot the values against i(plotting the function)
plt.plot(fks)
plt.show()    
