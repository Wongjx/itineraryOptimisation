import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets.samples_generator import make_blobs
from processKML import parseKMLforKmeans
from sklearn.cluster import KMeans


# placemarks = parseKML("doc.KML")
nameList,comList = parseKMLforKmeans("doc.KML")
comListArray = np.array(comList)

# X, y_true = make_blobs(n_samples=50, centers=4,cluster_std=0.60, random_state=0)
# plt.scatter(X[:, 0], X[:, 1], s=50)

kmeans = KMeans(n_clusters=4)
kmeans.fit(comListArray)
y_kmeans = kmeans.predict(comListArray)
centers = kmeans.cluster_centers_

# plt.scatter(comListArray[:, 0], comListArray[:, 1], c=y_kmeans, s=50, cmap='viridis')
# plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5);
# plt.show()

print(y_kmeans)
print(y_kmeans.shape)
with open("output.csv",'w',encoding='utf8') as csvfile:
    for i in range(len(nameList)):
        line = nameList[i]+","+str(y_kmeans[i])+'\n'
        # csvfile.write(line.encode('utf8'))
        csvfile.write(line)



