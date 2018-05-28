import numpy as np
import matplotlib.pyplot as plt
def squareWave(x,n):
    f = np.zeros((x.shape[0],))
    
    k = 1
    while k <= n:
        f = f + (8*np.sin((2*k-1)*x)/((2*k-1)*np.pi))
        k = k + 1
        
        return f

x = np.linspace(0.0,2*np.pi,100)
y = squareWave(x, 80)

plt.plot(x,y)
plt.show()


