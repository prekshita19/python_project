"""
There are various types  of methods in line chart
1. .title("")           To declare the title
2. .xlabel("")          To declare the name of x-axis
3. .ylabel("")          To declare the name of y-axis
4. .show()              Display the output
5. .Legend()            To display the information
6. .grid(color="")      To specify color as in the background grids
7. .subplot()           To declare a new plot under a plot.
"""

print("plot is only used for line chart.")
import matplotlib.pyplot as plt
a1=[0,3,5,6,8]
a2=[0,10,8,15,25]
plt.plot(a1,a2,label="Demo",color="Violet",linewidth=5)
plt.title("Line Chart")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid(color="Red")
plt.legend()
plt.show()