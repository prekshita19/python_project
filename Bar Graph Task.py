import matplotlib.pyplot as plt
print("Bar Graph")
a1=[1,2,3,4,5]
a2=[55,65,50,62,65]
a3=[15,5,10,25,19]
plt.bar(a1,a2,label="Total Students",color="#2396AB")
plt.bar(a1,a3,label="Absent Students",color="#AB1234")
plt.legend()
plt.title("Students in Respective class")
plt.xlabel("Class")
plt.ylabel("Students")
plt.show()