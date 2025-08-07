from terminal_coef import term
import matplotlib.pyplot as plt
import numpy as np

Tstop = 10 #terminal time

#generating coefficients
Coefs = term([0,0,0],[1,0,0],Tstop) 

#using numpy polinomial function to model results
poly_function = np.poly1d(np.flip(Coefs))

#plotting the result
t = np.arange(0,Tstop,0.1)
plt.plot(t, poly_function(t), color='red', linewidth=1, markersize=1) 
plt.grid()
plt.xlim(0, Tstop)
plt.tick_params(axis='both', which='major', pad=15)
plt.show()