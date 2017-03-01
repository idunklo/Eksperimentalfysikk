import numpy as np
import matplotlib.pyplot as plt

def I(V_L, R_L):
    I = V_L/R_L
    return I

VL = np.array([-77.890, -152.60, -286.77, -378.46, -442.01, -475.65, -497.65, -500.25, -502.62]) *1E-3
RL = np.array([0.5, 1, 2, 3, 5,  10, 50, 100, 1000]) 
V = np.array([86.372, 160.57, 294.64, 385.37, 447.24, 478.24, 498.29, 500.52, 502.73]) *1E-3

I = I(VL, RL)

plt.plot(V, I, "*-")
plt.show() 
