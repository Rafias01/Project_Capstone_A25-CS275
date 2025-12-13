# Customer Segmentation with RFM & K-Means

## 📌 Deskripsi Proyek
Proyek ini merupakan bagian dari *Capstone Project Kelompok A25-CS275* dengan use case *AC-06: Customer Segmentation for Personalized Retail Marketing*.

Judul proyek:
*Implementasi Customer Segmentation dengan Pendekatan RFM dan K-Means untuk Strategi Retensi Pelanggan pada Bisnis E-Commerce*

Tujuan utama proyek ini adalah mengelompokkan pelanggan e-commerce berdasarkan perilaku transaksi menggunakan metode *RFM (Recency, Frequency, Monetary)* dan *K-Means Clustering*, sehingga perusahaan dapat merancang strategi pemasaran dan retensi pelanggan yang lebih efektif dan tepat sasaran.

---

## 👥 Tim Pengembang
- *Rafi Ananda Subekti* — M891D5Y1608  
- *Jonathan Regan* — M891D5Y0910  
- *Stevano Pratama Ichwan* — M891D5Y1869

---

## 🧠 Business Understanding
Dalam industri e-commerce, memahami perilaku pelanggan merupakan faktor krusial untuk meningkatkan pendapatan dan loyalitas. Dengan segmentasi pelanggan, bisnis dapat:
- Mengidentifikasi pelanggan bernilai tinggi (premium)
- Menentukan pelanggan yang mulai tidak aktif (hibernating)
- Mengoptimalkan strategi promosi dan anggaran pemasaran

Metode *RFM* digunakan untuk menilai pelanggan berdasarkan:
- *Recency*: Jarak waktu sejak transaksi terakhir
- *Frequency*: Frekuensi transaksi
- *Monetary*: Total nilai transaksi

Hasil RFM kemudian dikelompokkan menggunakan *K-Means* untuk mendapatkan segmentasi pelanggan yang lebih terstruktur.

---

## 📂 Dataset
Dataset yang digunakan adalah data transaksi e-commerce dengan atribut utama seperti:
* `order_id`
* `customer_id`
* `category`
* `price`
* `discount`
* `quantity`
* `payment_method`
* `order_date`
* `delivery_time_days`
* `region`
* `returned`
* `total_amount`
* `shipping_cost`
* `customer_age`
* `customer_gender`

Dataset dimuat dari file:

ecommerce_sales_dataset.csv


---

## 🔧 Tools & Library
Proyek ini dikembangkan menggunakan Python dengan library utama berikut:
- pandas, numpy
- matplotlib, seaborn
- scikit-learn
- scipy
- yellowbrick

---

## 🛠 Tahapan Proyek

### 1. Data Understanding
- Eksplorasi dataset
- Cek missing value dan duplikasi
- Visualisasi distribusi dan korelasi data numerik

### 2. Data Preparation
- Menghapus kolom tidak relevan
- Konversi tipe data tanggal
- Membuat kolom total_amount
- Agregasi data per customer

### 3. RFM Analysis
- Perhitungan Recency, Frequency, Monetary
- RFM Scoring menggunakan quantile
- Visualisasi boxplot RFM

### 4. Modelling (Clustering)
- Standardisasi data (StandardScaler)
- Penentuan jumlah cluster optimal dengan:
  - Silhouette Score
  - Elbow Method
- Training model K-Means

### 5. Evaluation & Visualization
- Visualisasi cluster (2D scatter plot)
- Radar chart profil RFM per cluster
- Distribusi customer per cluster
- Analisis demografi (usia & gender)
- Analisis kategori produk dan metode pembayaran

---

## 📊 Hasil Segmentasi
Model menghasilkan *3 cluster utama*:

### 🔹 Cluster 0 — Low-Value Hibernating Customers
- Recency tinggi (lama tidak transaksi)
- Monetary rendah–menengah
- Cocok untuk reactivation campaign

### 🔹 Cluster 1 — New or Dormant Low Spenders
- Pelanggan baru atau pasif
- Frekuensi dan nilai transaksi rendah
- Potensial untuk onboarding dan upselling ringan

### 🔹 Cluster 2 — Premium Loyal Buyers
- Pelanggan paling aktif dan bernilai tinggi
- Kontributor utama revenue
- Prioritas utama untuk retensi dan loyalty program

---

## 🎯 Rekomendasi Strategi Bisnis
- *Cluster 0*: Promo reaktivasi, reminder, bundle hemat
- *Cluster 1*: Onboarding campaign, promo kategori populer
- *Cluster 2*: Loyalty program premium, personalized recommendation, eksklusivitas

---

## ▶ Cara Menjalankan
1. Pastikan Python dan library yang dibutuhkan telah terinstal
2. Letakkan dataset ecommerce_sales_dataset.csv pada direktori yang sama
3. Jalankan file notebook / script Python

---

## 📌 Catatan
- Proyek ini bersifat analisis dan eksploratif
- Model dapat dikembangkan lebih lanjut dengan:
  - Integrasi dashboard (Streamlit)
  - Model prediktif churn
  - Automasi deployment (MLOps)

---