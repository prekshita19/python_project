import matplotlib.pyplot as plt
a1=['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']
a2=[15000,12000,250000,25000,300000,900000,80000,65555,78942,100000,690000,326512]
a3=[0,100000,25000,60000,85002,69523,142222,789131,561322,545613,798456,456321]
plt.plot(a1,a2,label="P1.Expense",color="Red",linewidth=1)
plt.plot(a1,a3,label="P2.Expense",color="Blue",linewidth=1)
plt.title("Expense Chart in USD")
plt.legend()
plt.show()