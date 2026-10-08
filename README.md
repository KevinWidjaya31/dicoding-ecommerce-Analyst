# Brazilian E-Commerce Data Analysis

## 📌 Project Overview

Project ini merupakan analisis data Brazilian E-Commerce Public Dataset by Olist untuk memahami performa penjualan, kontribusi kategori produk, serta hubungan antara ketepatan waktu pengiriman dengan kepuasan pelanggan.

Analisis dilakukan menggunakan Python melalui proses **data gathering, data assessing, data cleaning, exploratory data analysis (EDA), dan business analysis**. Hasil analisis juga divisualisasikan dalam bentuk dashboard interaktif menggunakan Streamlit.

---

## 🎯 Business Questions

Project ini berfokus pada dua pertanyaan bisnis utama:

### Business Question 1

**Bagaimana perkembangan total revenue dan jumlah order Olist secara bulanan selama periode September 2016 hingga Oktober 2018, dan kategori produk apa yang memberikan kontribusi revenue terbesar?**

Analisis ini bertujuan untuk mengetahui perkembangan performa penjualan serta mengidentifikasi kategori produk yang memberikan kontribusi revenue terbesar.

### Business Question 2

**Seberapa besar perbedaan rata-rata review score antara pesanan yang dikirim tepat waktu dan pesanan yang terlambat selama periode 2017–2018?**

Analisis ini bertujuan untuk mengetahui hubungan antara ketepatan waktu pengiriman dengan kepuasan pelanggan berdasarkan review score.

---

## 📂 Dataset

Dataset yang digunakan adalah:

**Brazilian E-Commerce Public Dataset by Olist**

Dataset berisi informasi mengenai transaksi e-commerce di Brazil, termasuk data order, customer, product, payment, review, dan seller.

Dataset utama yang digunakan dalam analisis:

* `olist_orders_dataset.csv`
* `olist_order_items_dataset.csv`
* `olist_products_dataset.csv`
* `olist_order_reviews_dataset.csv`
* `olist_customers_dataset.csv`
* `product_category_name_translation.csv`

Dataset tidak disertakan dalam repository karena ukuran file dan ketentuan distribusi dataset. Dataset dapat diperoleh melalui platform Kaggle.

---

## 🔎 Data Analysis Process

Analisis dilakukan melalui beberapa tahapan berikut.

### 1. Data Gathering

Mengumpulkan dataset yang diperlukan dari Brazilian E-Commerce Public Dataset by Olist.

### 2. Data Assessing

Melakukan pemeriksaan terhadap:

* Struktur dan ukuran dataset
* Tipe data
* Missing values
* Duplicate data
* Duplicate identifier
* Invalid values
* Outliers
* Konsistensi data

### 3. Data Cleaning

Beberapa tindakan yang dilakukan antara lain:

* Mengubah kolom tanggal menjadi tipe datetime.
* Menangani missing values sesuai kebutuhan analisis.
* Menghapus atau menyaring nilai transaksi yang tidak valid.
* Memastikan review score berada pada rentang 1–5.
* Menangani data yang diperlukan untuk analisis pengiriman.
* Menggabungkan beberapa dataset berdasarkan identifier yang sesuai.

### 4. Feature Engineering

Beberapa fitur baru dibuat untuk mendukung analisis, antara lain:

* `order_month`
* `order_year`
* `revenue`
* `order_value`
* `delivery_difference_days`
* `delivery_status`

`delivery_status` digunakan untuk membedakan pesanan yang dikirim tepat waktu dan pesanan yang terlambat.

### 5. Exploratory Data Analysis

EDA dilakukan untuk menjawab business questions melalui analisis:

* Perkembangan revenue secara bulanan
* Jumlah order secara bulanan
* Revenue berdasarkan kategori produk
* Kontribusi revenue setiap kategori
* Perbandingan review score berdasarkan status pengiriman

---

## 📊 Key Findings

### Business Question 1

Revenue tertinggi terjadi pada **November 2017** dengan total revenue sebesar:

**R$ 1,010,271.37**

Kategori produk dengan kontribusi revenue terbesar adalah:

**Health Beauty**

dengan total revenue sebesar:

**R$ 1,258,681.34**

atau sekitar:

**9.26% dari keseluruhan revenue.**

Hasil tersebut menunjukkan bahwa kategori Health Beauty memiliki kontribusi yang cukup penting terhadap performa penjualan.

### Business Question 2

Terdapat perbedaan yang cukup besar antara rata-rata review score pesanan yang dikirim tepat waktu dan pesanan yang terlambat.

| Delivery Status | Average Review Score |
| --------------- | -------------------: |
| On Time         |                 4.21 |
| Late            |                 2.55 |

Terdapat selisih sebesar **1.66 poin**.

Hasil ini menunjukkan bahwa keterlambatan pengiriman berkaitan dengan penurunan kepuasan pelanggan. Oleh karena itu, ketepatan waktu pengiriman merupakan salah satu aspek penting dalam meningkatkan customer experience.

---

## 💡 Recommendations

Berdasarkan hasil analisis, beberapa rekomendasi yang dapat diberikan adalah:

1. **Memprioritaskan kategori Health Beauty** dengan melakukan evaluasi stok, promosi, dan strategi pemasaran untuk mempertahankan kontribusinya terhadap revenue.

2. **Meningkatkan ketepatan waktu pengiriman** dengan memantau seller, wilayah, dan proses logistik yang memiliki tingkat keterlambatan tinggi.

3. **Menggunakan review score sebagai indikator customer experience** untuk mengevaluasi dampak permasalahan pengiriman terhadap kepuasan pelanggan.

---

## 📈 Streamlit Dashboard

Project ini dilengkapi dengan dashboard interaktif menggunakan Streamlit.

Dashboard menyediakan beberapa informasi utama:

* Total Revenue
* Total Orders
* Monthly Revenue Trend
* Revenue by Product Category
* Delivery Status
* Average Review Score
* Delivery Performance
* Key Business Findings

### Dashboard Preview

Dashboard dapat dijalankan secara lokal menggunakan:

```bash
streamlit run dashboard.py
```

Kemudian buka URL yang diberikan oleh Streamlit, biasanya:

```text
http://localhost:8501
```

---

## 📁 Project Structure

```text
Submission Kevin Widjaya/
│
├── Olist_Final_Project.ipynb
├── dashboard.py
├── requirements.txt
├── README.md
│
├── dashboard_data/
│   ├── dashboard_data.csv
│   ├── monthly_sales.csv
│   ├── category_sales.csv
│   ├── delivery_review.csv
│   └── delivery_summary.csv
│
└── data/
    └── orders_dataset.csv
        order_items_dataset.csv
        products_dataset.csv
        order_reviews_dataset.csv
        customers_dataset.csv
        product_category_name_translation.csv
```

---

## 🛠️ Technologies

Project ini menggunakan beberapa tools dan library berikut:

* **Python**
* **Pandas** — data manipulation and analysis
* **NumPy** — numerical computation
* **Matplotlib** — data visualization
* **Seaborn** — statistical visualization
* **Plotly** — interactive visualization
* **Streamlit** — interactive dashboard
* **Jupyter Notebook / Google Colab** — data analysis

---

## ▶️ How to Run

### 1. Clone atau download repository

Pastikan seluruh file project berada dalam satu folder.

### 2. Install dependencies

Jalankan:

```bash
pip install -r requirements.txt
```

### 3. Jalankan notebook

Buka:

```text
Olist_Final_Project.ipynb
```

Notebook dapat dijalankan menggunakan Jupyter Notebook, JupyterLab, atau Google Colab.

### 4. Jalankan Streamlit Dashboard

Pastikan terminal berada di folder yang berisi `dashboard.py`, kemudian jalankan:

```bash
streamlit run dashboard.py
```

Dashboard dapat diakses melalui:

```text
http://localhost:8501
```

---

## 📌 Notes

Dataset mentah tidak disertakan secara langsung dalam repository. Pastikan dataset ditempatkan pada folder yang sesuai sebelum menjalankan notebook.

File pada folder `dashboard_data` merupakan hasil pengolahan data yang digunakan oleh Streamlit Dashboard.

---

## 👤 Author

**Kevin Widjaya**

**Areas of Interest:**

* Data Analytics
* Artificial Intelligence
* Machine Learning
* Computer Vision
