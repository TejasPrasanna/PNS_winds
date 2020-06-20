import h5py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn-pastel')



n="/home/tejas/mhd-winds-helm-eos/helm.out1.00025.athdf"
n2="/home/tejas/helm_eos/helm.out1.00025.athdf"

f = h5py.File(n,"r")
f2=h5py.File(n2,"r")
        
x1 = f['x1v']
x1s=f2['x1v']
    
x1v=(np.array(x1.value)[0])
x1vs=(np.array(x1s.value)[0])
    

prim=f['prim']
prims=f2['prim']
    
pr=(np.array(prim.value))[1][0][0][0]
    
rho=(np.array(prim.value))[0][0][0][0]
    
v1=(np.array(prim.value))[2][0][0][0]
    
v2=(np.array(prim.value))[3][0][0][0]
    
v3=(np.array(prim.value))[4][0][0][0]

prs=(np.array(prims.value))[1][0][0][0]
    
rhos=(np.array(prims.value))[0][0][0][0]
    
v1s=(np.array(prims.value))[2][0][0][0]
    
v2s=(np.array(prims.value))[3][0][0][0]
    
v3s=(np.array(prims.value))[4][0][0][0]

plt.plot(x1v,pr,color='blue',label="Without source function")
plt.plot(x1vs,prs,color='red',label="With source function")
plt.legend()
plt.xlabel('x')
plt.ylabel(r"$P/10^{16} \ (g \ cm^{-1} \ s^{-2})$")
plt.show()
