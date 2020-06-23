


import h5py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn-pastel')



fig = plt.figure()

ax = plt.axes(xlim=(-0.6,0.6), ylim=(0,1.1),xlabel="x",ylabel=r"$P/10^{16} \ (g \ cm^{-1} \ s^{-2})$")
line1, = ax.plot([], [], lw=3,label="Without source")
line2,=ax.plot([], [], lw=3)
def init():
    line1.set_data([],[])
    return line1,
def animate(i):
    
    
    if(i<10):
        n="/home/tejas/mhd-winds-helm-eos/helm.out1.0000"+str(i)+".athdf"
        n2="/home/tejas/helm_eos/helm.out1.0000"+str(i)+".athdf"
    if(i>=10):
        n="/home/tejas/mhd-winds-helm-eos/helm.out1.000"+str(i)+".athdf"
        n2="/home/tejas/helm_eos/helm.out1.000"+str(i)+".athdf"
    f = h5py.File(n,"r")
    f2=h5py.File(n2,"r")
    a=list(f.keys())
    #print(a)
    
    x1 = f['x1v']
    x1s=f2['x1v']
    
    x1v=(np.array(x1.value)[0])
    x1vs=(np.array(x1s.value)[0])
    #print(x1v)

    prim=f['prim']
    prims=f2['prim']
    #print(prim.value)
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

    line1.set_data(x1v,pr)
    return line1,

anim = FuncAnimation(fig, animate, init_func=init,
                               frames=25, interval=200, blit=True)


anim.save('pressure.gif', writer='imagemagick')

