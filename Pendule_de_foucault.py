
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from scipy.integrate import odeint 
from mpl_toolkits.mplot3d import Axes3D

# Constantes physique--------------------
L=25
g=9.81
omega_terre=7
lat=np.radians(48.85)
omega_0=np.sqrt(g/L)

#Pas de temps-----------------------
t=np.linspace(0,20,200)

#graduation des axes-----------------
x=np.linspace(-10,10,200)
y=np.linspace(-10,10,200)


def systeme(z,t,omega_0):
    x,y,v_y,v_x=z
    dxdt=v_x
    dydt=v_y
    dv_xdt= 2* (omega_terre)*v_x*(np.sin(lat))-(omega_0*x)
    dv_ydt=2* (omega_terre)*v_y*(np.sin(lat))-(omega_0*y)
   
    return [dxdt,dv_xdt,dydt,dv_ydt]

 
#conditions initiales -----------------------
x_0=0
y_0=0
v_x0=0
v_y0=3
z_0=[x_0,y_0,v_x0,v_y0]
Z0=17

#solution-------------------------------------
sol=odeint(systeme,z_0,t, args=(omega_0,))

#extraction des résultats----------------------
pos_x=sol[:,0]
pos_y=sol[:,3]


pos_Z= Z0-np.sqrt(L**2 -pos_x**2-pos_y**2)
#animation du système--------------------------
def update(i):
    line.set_data(pos_x[:i],pos_y[:i])
    line.set_3d_properties(pos_Z[:i])
    
    
    point.set_data(pos_x[:i],pos_y[:i])
    point.set_3d_properties(pos_Z[:i])
    return line, point

fig=plt.figure(figsize=(9,7))
ax=fig.add_subplot(111,projection='3d')
point, = ax.plot([], [],[], 'ro')
line, = ax.plot([], [],[], 'b-', alpha=0.5)



X,Y=np.meshgrid(x,y)
#Z=np.zeros_like(pos_x)

traj=ax.plot3D(pos_x,pos_y,pos_Z)
#plt.plot(pos_x,pos_y)
ani=animation.FuncAnimation(fig,update,frames=500,interval=20,blit=False, repeat=False)
plt.show()
