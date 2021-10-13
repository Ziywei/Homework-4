#import relevant files
from numba.core.types.scalars import Boolean
import numpy as np
import numba
import scipy
import matplotlib.pyplot as plt
#setting the variables as given in the homework file
N_max=50
threshold=50
#define a function called mandelbrot, explained belowed
def mandelbrot(N_max,threshold,n):
    """[summary]

    Args:
        N_max (int): number of iterations
        threshold (int): the limit of the z value/complex number
        n (tuple of (nx,ny)): the resolution of the result

    Returns:
        2D boolean array: the sets that are in range
    """
    #define n
    (nx,ny)=n
    #generate x and y with even nx and ny space within the interval/range
    x=np.linspace(-2,1,nx)
    y=np.linspace(-1.5,1.5,ny)
    #begin with zeros and count with for loop
    mandelbrot_set=np.zeros((nx,ny), dtype=bool)
    for j in range(ny):
        for i in range(nx):
            #used the codes given in the pdf file, definition of complex number and the settings of z
            c=x[i]+1j*y[j]
            z=0
            for k in range(N_max):
                z=z**2+c
                #counting by if statement
            if (abs(z)<=threshold):
                mandelbrot_set[i][j]=True
                

    return mandelbrot_set
#rename the output as Mask, a 2D boolean array
Mask=mandelbrot(50, 50, (601, 401))
#plot and save the mandelbrot set generated from the function
plt.imshow(Mask.T,extent=[-2,1,-1.5,1.5])
plt.gray()
plt.savefig('mandelbrot.png')