import warnings
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score


df = pd.read_csv(r'E:/World/Code/Python/BTL/bai1/file/result.csv', header=[0, 1, 2])

# Tiền xử lý: Xử lý các giá trị thiếu nếu có
numeric_columns = df.select_dtypes(include=[np.number]).columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

# Chuẩn hóa dữ liệu số
numerical_data = df.select_dtypes(include=[float, int])
scaler = StandardScaler()
X = scaler.fit_transform(numerical_data)

# Tìm số lượng cụm tối ưu
sse = []
silhouette_scores = []
for k in range(2, 10):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    sse.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X, kmeans.labels_))

plt.figure(figsize=(12, 5))

# Phương pháp Elbow để xác định SSE
plt.subplot(1, 2, 1)
plt.plot(range(2, 10), sse, marker='o')
plt.xlabel("Number of Clusters")
plt.ylabel("SSE")
plt.title("Elbow Method")

# Đánh giá Silhouette Score
plt.subplot(1, 2, 2)
plt.plot(range(2, 10), silhouette_scores, marker='o')
plt.xlabel("Number of Clusters")
plt.ylabel("Silhouette Score")
plt.title("Silhouette Score")
plt.show()

# Sử dụng số cụm = 4 dựa trên kết quả từ đồ thị
optimal_k = 4
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)


# Kết quả phân cụm
print("Phân cụm thành công. Kết quả phân cụm:")
print(df[['name', 'nation', 'team']].head())

# Kiểm tra số lượng cầu thủ trong mỗi cụm
print("Số lượng cầu thủ trong mỗi cụm:")
print(df['Cluster'].value_counts())

# Trực quan hóa các cụm
plt.figure(figsize=(10, 7))
sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=df['Cluster'], palette='viridis', s=100, alpha=0.7)
plt.title('Clusters of Players')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend(title='Cluster')
plt.show()
