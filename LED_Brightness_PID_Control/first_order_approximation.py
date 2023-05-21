from matplotlib import pyplot as plt
import numpy as np  
from scipy.optimize import curve_fit

# load a file names data_truncated.txt with delimiter next line and unpack it into x and y
i,y = np.loadtxt('data_truncated.txt', delimiter=',', unpack=True)

# define x consisting of integers starting from 0 and equal to the length of y
x = np.arange(len(y))

# fitting function is y = (1003 - a*exp(b*x)
def fitting_function(x, a, b):
    return (1003 - a*np.exp(b*x))

plt.plot(i[0:60], y[0:60], 'bo',label='Experimental Data')
plt.xlabel('Time (10ms)')
plt.ylabel('Sensor value (0-1024)')
plt.title('Time vs Sensor Value ')
plt.legend()

# initial guess for a and b
a = -0.832 # Gain
b = 0.004 # 1 ms

# Perform the curve fitting
popt, pcov = curve_fit(fitting_function, x, y, p0=[a, b])
print(popt)

# print the fitted parameters
print('a = ', popt[0], 'b = ', popt[1])

# Plot fitted function
plt.plot(x, fitting_function(x, *popt), 'r-', label='Fitted function')
plt.show()
