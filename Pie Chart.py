import matplotlib.pyplot as plt
expense=[2000,1000,2500,500]
categories=["Petrol","Food","rent","electricity"]
plt.pie(expense,labels=categories,colors=["Red","Yellow","Green","Orange"],autopct="%.1f%%",shadow=True)#,explode=(0.1,0.5,0.3,0.1))
plt.show()