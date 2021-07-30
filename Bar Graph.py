import matplotlib.pyplot as plt
print("Bar Graph")
a1=[1,2,3,4,5]
a2=[55,65,50,62,65]
plt.bar(a1,a2,label="Students",color="#2396AB")
plt.title("Students in Respective class")
plt.xlabel("Class")
plt.ylabel("Students")
plt.show()