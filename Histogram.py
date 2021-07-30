import numpy as np
import matplotlib.pyplot as plt
ages=[]
people=[]
for i in range(0,75,5):
    ages.append(i)

people=np.random.randint(0,70,size=55)
print(people)
print(ages)
plt.hist(people,ages,label="Ages",color="#100000") # Bins should be given and only second value. here we have given ages
plt.xlabel("Ages")
plt.ylabel("People")
plt.show()