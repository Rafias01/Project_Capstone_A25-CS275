import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

st.set_page_config(page_title='RFM Segmentation Dashboard', layout='wide')

st.title("Customer Segmentation — RFM & K-Means")

# ============================
# LOAD DATA OTOMATIS
# ============================
df = pd.read_csv("ecommerce_sales_dataset.csv")

# ============================
# BUAT TABS / SECTION
# ============================
tabs = st.tabs([
    "📊 Data Overview",
    "🔥 Korelasi & Distribusi",
    "📈 Analisis RFM",
    "🎯 Evaluasi Clustering",
    "🧩 Visualisasi Cluster",
    "👥 Demografi",
    "🛒 Perilaku Belanja"
])

# =========================================================
# 📊 1. DATA OVERVIEW
# =========================================================
with tabs[0]:
    st.header("📊 Data Overview")
    st.subheader("Preview Dataset")
    st.dataframe(df.head())

# =========================================================
# 🔥 2. KORELASI & DISTRIBUSI
# =========================================================
with tabs[1]:
    st.header("🔥 Korelasi & Distribusi Numerik")

    st.subheader("Heatmap Korelasi Numerik")
    num = df.select_dtypes(include=['float64', 'int64'])

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.heatmap(num.corr(), annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

    st.subheader("Distribusi Semua Kolom Numerik")
    num_cols = num.columns
    rows = (len(num_cols) // 3) + 1

    fig, axes = plt.subplots(rows, 3, figsize=(15, 5 * rows))
    axes = axes.flatten()

    for i, col in enumerate(num_cols):
        sns.histplot(df[col], kde=True, bins=30, ax=axes[i])
        axes[i].set_title(f"Distribusi {col}")

    st.pyplot(fig)

# =========================================================
# 📈 3. ANALISIS RFM
# =========================================================
with tabs[2]:
    st.header("📈 Analisis RFM")

    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    df['total_amount'] = (df['quantity'] * df['price'] *
                          (1 - df['discount'])) + df['shipping_cost']

    min_date = df['order_date'].min()
    df['order_date_filled'] = df['order_date'].fillna(min_date)
    snapshot = df['order_date_filled'].max() + pd.Timedelta(days=1)

    rfm = df.groupby('customer_id').agg({
        'order_date_filled': 'max',
        'order_id': 'nunique',
        'total_amount': 'sum'
    }).reset_index()

    rfm.columns = ['customer_id', 'last_purchase', 'Frequency', 'Monetary']
    rfm['Recency'] = (snapshot - rfm['last_purchase']).dt.days

    st.subheader("Boxplot RFM")
    fig, ax = plt.subplots(figsize=(14, 6))
    sns.boxplot(data=rfm[['Recency', 'Frequency', 'Monetary']], orient='h', ax=ax)
    st.pyplot(fig)

# =========================================================
# 🎯 4. EVALUASI CLUSTERING
# =========================================================
with tabs[3]:
    st.header("🎯 Evaluasi Clustering (Elbow & Silhouette)")

    X = rfm[['Recency', 'Frequency', 'Monetary']]
    scaler = StandardScaler().fit(X)
    X_scaled = scaler.transform(X)

    cluster_range = range(2, 11)
    inertia = []
    silhouette_scores = []

    for k in cluster_range:
        model = KMeans(n_clusters=k, random_state=42).fit(X_scaled)
        inertia.append(model.inertia_)
        silhouette_scores.append(silhouette_score(X_scaled, model.labels_))

    fig, ax = plt.subplots(1, 2, figsize=(14, 4))

    ax[0].plot(cluster_range, inertia, marker='o')
    ax[0].set_title("Elbow Method")

    ax[1].plot(cluster_range, silhouette_scores, marker='o', color='orange')
    ax[1].set_title("Silhouette Score")

    st.pyplot(fig)

    best_k = cluster_range[int(np.argmax(silhouette_scores))]
    st.success(f"Jumlah cluster terbaik = {best_k}")

# =========================================================
# 🧩 5. VISUALISASI CLUSTER
# =========================================================
with tabs[4]:
    st.header("🧩 Visualisasi Cluster")

    kmeans_final = KMeans(n_clusters=best_k, random_state=42)
    rfm['Cluster'] = kmeans_final.fit_predict(X_scaled)
    centroids = kmeans_final.cluster_centers_

    st.subheader("Recency vs Monetary")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=rfm, x='Recency', y='Monetary', hue='Cluster', s=70, ax=ax)
    ax.scatter(centroids[:, 0], centroids[:, 2], c='black', s=250, marker='X')
    st.pyplot(fig)

    st.subheader("Frequency vs Monetary")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=rfm, x='Frequency', y='Monetary', hue='Cluster', s=70, ax=ax)
    ax.scatter(centroids[:, 1], centroids[:, 2], c='black', s=250, marker='X')
    st.pyplot(fig)

    st.subheader("Recency vs Frequency")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=rfm, x='Recency', y='Frequency', hue='Cluster', s=70, ax=ax)
    ax.scatter(centroids[:, 0], centroids[:, 1], c='black', s=250, marker='X')
    st.pyplot(fig)

    st.subheader("Radar Chart — Profil RFM per Cluster")
    rfm_mean = rfm.groupby('Cluster')[['Recency', 'Frequency', 'Monetary']].mean()
    norm = (rfm_mean - rfm_mean.min()) / (rfm_mean.max() - rfm_mean.min())

    labels = norm.columns
    theta = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)

    fig = plt.figure(figsize=(8, 6))
    ax = plt.subplot(111, polar=True)

    for idx, row in norm.iterrows():
        values = row.values.tolist()
        values += values[:1]
        ax.plot(np.append(theta, theta[0]), values, marker='o', label=f"Cluster {idx}")

    ax.set_xticks(theta)
    ax.set_xticklabels(labels)
    plt.legend(loc='upper right')
    st.pyplot(fig)

# =========================================================
# 👥 6. DEMOGRAFI
# =========================================================
with tabs[5]:
    st.header("👥 Demografi Pelanggan")

    st.subheader("Distribusi Gender")
    fig, ax = plt.subplots(figsize=(6, 6))
    df['customer_gender'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax)
    ax.set_ylabel("")
    st.pyplot(fig)

    st.subheader("Gender per Cluster")
    fig, ax = plt.subplots(figsize=(10, 5))
    merged = rfm.merge(df[['customer_id', 'customer_gender']], on='customer_id')
    sns.countplot(data=merged, x='Cluster', hue='customer_gender', ax=ax)
    st.pyplot(fig)

    st.subheader("Density Usia per Gender")
    fig, ax = plt.subplots(figsize=(9, 5))
    sns.kdeplot(data=df, x='customer_age', hue='customer_gender', fill=True, ax=ax)
    st.pyplot(fig)

    st.subheader("Heatmap Kelompok Usia per Cluster")

    def age_group(age):
        if age < 25:
            return "Youth (<25)"
        elif age <= 40:
            return "Adult (25-40)"
        elif age <= 60:
            return "Middle Age (41-60)"
        else:
            return "Senior (>60)"

    df['age_group'] = df['customer_age'].apply(age_group)
    demo = df[['customer_id', 'age_group']].drop_duplicates()
    rfm_demo = rfm.merge(demo, on='customer_id', how='left')

    heat = rfm_demo.groupby(['Cluster', 'age_group']).size().unstack(fill_value=0)

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(heat, annot=True, cmap='YlGnBu', ax=ax)
    st.pyplot(fig)

# =========================================================
# 🛒 7. PERILAKU BELANJA + PENJELASAN CLUSTER
# =========================================================
with tabs[6]:
    st.header("🛒 Perilaku Belanja Pelanggan")

    # Penjelasan Cluster
    st.markdown("""
## **1. Cluster 0 — Low-Value Hibernating Customers**
### RFM Insight:
- Recency: 100.60  
- Frequency: 3.98  
- Monetary: 486.45  

### Profil Singkat:
Segmen ini terdiri dari pelanggan bernilai rendah dengan aktivitas belanja menurun. Meski frekuensi tidak terlalu kecil, tetapi Recency tinggi menandakan sudah lama tidak bertransaksi. Pembelian biasanya terjadi hanya saat promo.

### Strategi:
- Promo ringan (voucher 10–20%, gratis ongkir)
- Reminder produk & rekomendasi
- Urgency promo
- Bundle hemat

---

## **2. Cluster 1 — New or Dormant Low Spenders**
### RFM Insight:
- Recency: 389.14  
- Frequency: 2.58  
- Monetary: 400.73  

### Profil Singkat:
Pelanggan baru atau yang tidak aktif. Nilai belanja rendah dan masih dalam tahap eksplorasi platform.

### Strategi:
- Onboarding campaign
- Upsell ringan
- Promo kategori populer
- Program loyalitas sederhana

---

## **3. Cluster 2 — Premium Loyal Buyers**
### RFM Insight:
- Recency: 90.15  
- Frequency: 6.80  
- Monetary: 1730.52  

### Profil Singkat:
Segmen paling bernilai: sering belanja, nilai transaksi besar, dan loyal.

### Strategi:
- Akses eksklusif
- Loyalty program premium
- Personalized recommendation
- Premium customer care
- Bundle premium
""")

    st.subheader("Kategori Barang Paling Banyak Dibeli per Cluster")
    df_cl = df.merge(rfm[['customer_id', 'Cluster']], on='customer_id')
    cat = df_cl.groupby(['Cluster', 'category'])['quantity'].sum().reset_index()

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=cat, x='Cluster', y='quantity', hue='category', ax=ax)
    st.pyplot(fig)

    st.subheader("Persentase Metode Pembayaran")
    fig, ax = plt.subplots(figsize=(7, 7))
    df['payment_method'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax)
    ax.set_ylabel("")
    st.pyplot(fig)