import numpy as np
import matplotlib.pyplot as plt

def I(V_L, R_L):
    I = (V_L/R_L)
    return I 

VL_pos = np.array([4.4210, 4.4641, 4.4755,  4.5005, 4.5057, 4.5232, 4.5297, 4.5352])  #[V]
RL_pos = np.array([10, 20, 25, 30, 50, 100, 200, 500])     #[Ohm]
V_pos = np.array([ 607.38, 564.63, 553.72, 536.94, 526.31, 510.63, 503.48, 497.97])*1E-3   #[V]

VL_neg = np.array([-0.16911, -1.6012, -3.1097, -3.8311, -4.5477, -5.4397, -5.4968, -5.5137, -5.5226, -5.3743]) 
RL_neg =  np.array([1, 10, 20, 25, 30, 50, 100, 200, 500, 40])  
V_neg = np.array([-4.8625, -3.4391, -1.9362, -1.2036, -0.44821, 0.41011, 0.46735, 0.48343, 0.49197, 0.34817])  

I_pos = I(VL_pos, RL_pos)
I_neg = I(VL_neg, RL_neg)


plt.plot(V_pos, I_pos, "*")
plt.plot(V_neg, I_neg, "x") 
plt.show()


