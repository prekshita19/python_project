import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

read=pd.read_csv("C:/Users/Fly-Emirates/Dropbox/Tops/machine Learning/Clustering/Mall_Customers.csv")
x=read.iloc[:,[3,4]].values

from sklearn.cluster import KMeans
wcss=[]
for i in range(1,11):
    k=KMeans(n_clusters=i,n_init=10,init="k-means++",max_iter=300,random_state=0)
    k.fit(x)
    wcss.append(k.inertia_)

plt.plot(range(1,11),wcss)
plt.show()

km=KMeans(n_clusters=5,n_init=10,init="k-means++",max_iter=300,random_state=0)
store=km.fit_predict(x)
#scatter_matrix(pd.DataFrame(store))
plt.scatter(x[store == 0, 0], x[store == 0, 1], s=100, c='red', label='Careful')
plt.scatter(x[store == 1, 0], x[store == 1, 1], s=100, c='blue', label='Standard')
plt.scatter(x[store == 2, 0], x[store == 2, 1], s=100, c='green', label='Target')
plt.scatter(x[store == 3, 0], x[store == 3, 1], s=100, c='cyan', label='Careless')
plt.scatter(x[store == 4, 0], x[store == 4, 1], s=100, c='magenta', label='Sensible')
plt.scatter(k.cluster_centers_[:, 0], k.cluster_centers_[:, 1], s=300, c='yellow', label='Centroids')
plt.title('Clusters of clients')
plt.xlabel('Annual Income(k$)')
plt.ylabel('Spending Score(1-100)')
plt.legend()
plt.show()