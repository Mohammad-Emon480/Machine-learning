import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Read Excel file
df = pd.read_excel(r"C:\PCA data analysis\PCA_Data1.xlsx")  # Update path if needed

# Select columns for clustering, e.g., 'Bond' and 'Angle'
x = df['Bond']
y = df['Angle']

data = list(zip(x, y))
inertias = []

for i in range(10, 49):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)

plt.plot(range(10, 49), inertias, marker='o')
plt.title('Elbow method')
plt.xlabel('Bond')
plt.ylabel('Angle')
plt.show()