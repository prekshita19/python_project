import matplotlib.pyplot as plt
speed=[]
for i in range(0,100,10):
    speed.append(i)
distance=[]
for i in range(0,50,5):
    distance.append(i)
plt.scatter(distance,speed)
plt.title("Speed and distance Scatter Chart")
plt.xlabel("Distance")
plt.ylabel("Speed")
plt.grid()
plt.show()