import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

a=np.linspace(0,4*np.pi,201)
b1=np.sin(a)
b2=np.cos(a)
b3=b1+b2

# opening a figure()
plt.figure()


# plot-1-sin curve
# plt.subplot(311)
plt.subplot(3,1,1)    # for plotting subplot we have to give the axis which is followed by (rows,columns,position)
plt.plot(a,b1,color="Red",label="sin",linestyle="--")
plt.title("Sin Curve")
plt.xlabel("Angle")
plt.ylabel("Magntitude")
plt.grid()
plt.legend()    



# plot-2-cosin curve
#plt.subplot(312)
plt.subplot(3,1,2)    # for plotting subplot we have to give the axis which is followed by (rows,columns,position)
plt.plot(a,b2,color="Blue",label="cosin",linestyle="-")
plt.title("Cos Curve")
plt.xlabel("Angle")
plt.ylabel("Magntitude")
plt.grid()
plt.legend()

plt.subplot(3,1,3)
plt.plot(a,b3,color="Green",label="Mixture",Marker="o")
plt.title("Sin + Cos Curve")
plt.xlabel("Angle")
plt.ylabel("Magntitude")
plt.grid()
plt.legend()

#To make layout good with space
plt.tight_layout()

plt.show() # this should be used only once.