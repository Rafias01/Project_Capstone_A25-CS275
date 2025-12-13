# Customer Segmentation using RFM & K-Means Clustering

## Deskripsi Proyek

Proyek ini bertujuan untuk melakukan **segmentasi pelanggan e-commerce** menggunakan pendekatan **RFM (Recency, Frequency, Monetary)** dan algoritma **K-Means Clustering**. Segmentasi pelanggan dilakukan untuk memahami pola perilaku belanja, nilai pelanggan, serta karakteristik demografis sehingga dapat digunakan sebagai dasar **strategi pemasaran berbasis data**.

Aplikasi dikembangkan dalam bentuk **dashboard interaktif berbasis Streamlit** yang memungkinkan pengguna melakukan eksplorasi data, evaluasi clustering, serta visualisasi hasil segmentasi secara end-to-end. Proyek ini bersifat **empiris**, **reproducible**, dan mengikuti praktik umum dalam analisis data dan data mining pemasaran.

---

## Tujuan Penelitian / Proyek

1. Mengidentifikasi segmen pelanggan berdasarkan perilaku transaksi menggunakan RFM.
2. Menentukan jumlah cluster optimal menggunakan **Elbow Method** dan **Silhouette Score**.
3. Menganalisis karakteristik tiap cluster dari sisi nilai bisnis, demografi, dan perilaku belanja.
4. Menyediakan rekomendasi strategi pemasaran untuk setiap segmen pelanggan.

---

## Dataset

Dataset yang digunakan adalah **ecommerce_sales_dataset.csv** dengan atribut utama sebagai berikut:

* `customer_id`
* `order_id`
* `order_date`
* `quantity`
* `price`
* `discount`
* `shipping_cost`
* `category`
* `payment_method`
* `customer_gender`
* `customer_age`

Dataset diproses untuk membentuk fitur RFM pada level pelanggan.

---

## Metodologi

Pendekatan yang digunakan mengikuti alur analisis data kuantitatif sistematis:

1. **Data Loading & Overview**

   * Memuat dataset CSV
   * Menampilkan ringkasan dan preview data

2. **Exploratory Data Analysis (EDA)**

   * Analisis korelasi numerik (heatmap)
   * Distribusi variabel numerik

3. **Feature Engineering (RFM)**

   * Recency: selisih hari sejak transaksi terakhir
   * Frequency: jumlah transaksi unik
   * Monetary: total nilai belanja pelanggan

4. **Normalisasi Data**

   * StandardScaler digunakan untuk menghindari bias skala fitur

5. **Clustering (K-Means)**

   * Uji jumlah cluster dari k = 2 hingga 10
   * Evaluasi menggunakan Elbow Method dan Silhouette Score
   * Pemilihan cluster terbaik berdasarkan nilai Silhouette tertinggi

6. **Visualisasi & Interpretasi Cluster**

   * Scatter plot antar dimensi RFM
   * Radar chart profil cluster
   * Analisis demografi dan perilaku belanja

7. **Business Insight & Strategy Mapping**

   * Penamaan cluster
   * Rekomendasi strategi pemasaran

---

## Struktur Proyek

```
📁 Project-Capstone
│── app.py                          # Aplikasi Streamlit (dashboard utama)
│── Project_Capstone_A25_CS275.ipynb # Notebook analisis eksploratif & eksperimen
│── ecommerce_sales_dataset.csv     # Dataset utama
│── README.md                       # Dokumentasi proyek
│── requirements.txt                # requirements atau library yang diperlukan
```

---

## Cara Replikasi Proyek

Langkah-langkah berikut memungkinkan peneliti atau praktisi lain untuk mereplikasi hasil proyek ini.

### 1. Persiapan Lingkungan

Buat virtual environment (opsional namun disarankan).

```bash
python -m venv venv
venv\Scripts\activate     
```

### 2. Instalasi Dependensi

Instal library yang dibutuhkan:

```bash
pip install streamlit pandas numpy matplotlib seaborn scikit-learn
```

### 3. Menyiapkan Dataset

* Pastikan file `ecommerce_sales_dataset.csv` berada dalam satu direktori dengan `app.py`
* Pastikan struktur kolom sesuai dengan deskripsi dataset

### 4. Menjalankan Aplikasi Dashboard

```bash
streamlit run app.py
```

Aplikasi akan berjalan secara lokal dan dapat diakses melalui browser.

### 5. Replikasi Analisis Notebook 

Notebook `Project_Capstone_A25_CS275.ipynb` digunakan untuk:

* Eksplorasi awal data
* Eksperimen clustering
* Validasi pendekatan

Notebook dapat dijalankan menggunakan Jupyter Notebook atau JupyterLab.

---

## Output Utama

* Segmentasi pelanggan berbasis RFM
* Nilai Silhouette Score sebagai indikator kualitas cluster
* Visualisasi:

  * Heatmap korelasi
  * Scatter plot cluster
  * Radar chart profil cluster
  * Distribusi demografi
  * Pola kategori belanja & metode pembayaran

---

## Interpretasi Hasil Clustering Pelanggan (RFM – K-Means)

Segmentasi pelanggan dilakukan menggunakan pendekatan **Recency, Frequency, dan Monetary (RFM)** yang dikombinasikan dengan algoritma **K-Means Clustering**. Berdasarkan evaluasi kualitas model menggunakan *Silhouette Score*, jumlah cluster optimal yang terbentuk adalah **3 cluster**. Setiap cluster merepresentasikan pola perilaku pelanggan yang berbeda secara signifikan dan memiliki implikasi strategis yang berbeda bagi bisnis.

---

## Cluster 0 (Low-Value Hibernating Customers)

### Karakteristik RFM
- **Recency: Tinggi**  
  Pelanggan sudah lama tidak melakukan transaksi.
- **Frequency: Rendah–Menengah**  
  Frekuensi pembelian terbatas dan tidak konsisten.
- **Monetary: Rendah**  
  Total nilai belanja relatif kecil.

### Interpretasi Perilaku
Cluster ini menggambarkan pelanggan dengan tingkat keterlibatan yang menurun. Meskipun sebagian pelanggan pernah melakukan beberapa transaksi, jarak waktu sejak pembelian terakhir cukup lama sehingga mengindikasikan **pelanggan pasif atau berisiko churn**. Pola belanja cenderung tidak berkelanjutan dan sangat bergantung pada promo.

### Implikasi Bisnis
Nilai ekonomi dari segmen ini relatif rendah sehingga tidak menjadi prioritas utama untuk investasi pemasaran jangka panjang. Namun, segmen ini masih memiliki potensi untuk diaktifkan kembali dengan biaya yang relatif rendah.

---

## Cluster 1 (New or Dormant Low Spenders)

### Karakteristik RFM
- **Recency: Sangat Tinggi**  
  Sebagian besar pelanggan sudah lama tidak aktif atau hanya pernah melakukan satu transaksi.
- **Frequency: Rendah**  
  Jumlah transaksi sangat sedikit.
- **Monetary: Rendah**  
  Nilai transaksi kecil.

### Interpretasi Perilaku
Cluster ini terdiri dari pelanggan baru yang belum berkembang atau pelanggan lama yang gagal bertransformasi menjadi pelanggan aktif. Secara perilaku, pelanggan masih berada pada tahap eksplorasi dan belum menunjukkan keterikatan terhadap platform atau merek.

### Implikasi Bisnis
Segmen ini memiliki kontribusi pendapatan yang rendah, tetapi penting dalam konteks **pertumbuhan basis pelanggan**. Risiko churn pada cluster ini cukup tinggi apabila tidak dilakukan intervensi yang tepat.

---

## Cluster 2 (Premium Loyal Buyers)

### Karakteristik RFM
- **Recency: Rendah**  
  Pelanggan melakukan transaksi dalam waktu dekat.
- **Frequency: Tinggi**  
  Frekuensi pembelian tinggi dan konsisten.
- **Monetary: Tinggi**  
  Total nilai belanja sangat besar.

### Interpretasi Perilaku
Cluster ini merupakan segmen pelanggan paling bernilai. Pelanggan menunjukkan loyalitas tinggi, keterlibatan jangka panjang, serta kontribusi signifikan terhadap pendapatan. Sensitivitas terhadap harga relatif rendah dan kepercayaan terhadap platform sudah terbentuk.

### Implikasi Bisnis
Segmen ini adalah **aset strategis utama** perusahaan. Kehilangan pelanggan dalam cluster ini akan berdampak langsung pada performa keuangan bisnis.



---

## Kontribusi & Pengembangan Lanjutan

Proyek ini dapat dikembangkan lebih lanjut dengan:

* Integrasi model prediktif (Customer Lifetime Value)
* Segmentasi berbasis waktu (temporal clustering)
* Deployment ke cloud
* Integrasi data real-time