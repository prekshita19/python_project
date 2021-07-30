import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

read=pd.read_csv("C:/Users/Fly-Emirates/Dropbox/Tops/machine Learning/Clustering/Mall_Customers.csv")
x=read.iloc[:,[3,4]].values

dendogram=sch.dendrogram(sch.linkage(x,method="ward"))
plt.title("Dendogram")
plt.xlabel("Customers")
plt.ylabel("Euclidean Distance")
plt.show()

hc=AgglomerativeClustering(n_clusters=5,affinity="euclidean")
y_hc=hc.fit_predict(x)

plt.scatter(x[y_hc==0,0],x[y_hc==0,1],s=100,c="red",label="Careful")
plt.scatter(x[y_hc==1,0],x[y_hc==1,1],s=100,c="blue",label="Standard")
plt.scatter(x[y_hc==2,0],x[y_hc==2,1],s=100,c="green",label="Target")
plt.scatter(x[y_hc==3,0],x[y_hc==3,1],s=100,c="cyan",label="Careless")
plt.scatter(x[y_hc==4,0],x[y_hc==4,1],s=100,c="magenta",label="Sensible")
plt.title("Clusters of clients")
plt.xlabel("Annual Income(k$)")
plt.ylabel("spending Score(1-100)")
plt.legend()
plt.show()