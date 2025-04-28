# customer-churn-analytics

Tentu! Aku akan buatkan README versi **lebih menarik dan profesional**, lengkap dengan ide **penempatan gambar** 📸 supaya mentor kamu makin paham dan terkesan.

Kamu bisa tambahkan gambar-gambar berikut:
- **EDA Visualization** (contoh: churn distribution, contract type vs churn)
- **Model Evaluation** (contoh: confusion matrix atau ROC curve)
- **Tampilan Streamlit App** (screenshot aplikasi saat live)

Berikut contoh **README.md** dengan format markdown + gambar:

---

# 📊 Telco Customer Churn Prediction Project

<div align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Customer_Churn.svg/1024px-Customer_Churn.svg.png" width="400"/>
</div>

---

## 📋 Overview
Dalam industri telekomunikasi, **kehilangan pelanggan (churn)** adalah tantangan serius yang dapat mengurangi pendapatan dan pertumbuhan perusahaan.

Melalui project ini, saya:
- Melakukan **data cleaning** dan **data integration** dari beberapa sumber.
- Melakukan **analisis eksplorasi data (EDA)** untuk memahami perilaku pelanggan.
- Membangun **model prediksi churn** menggunakan **Machine Learning**.
- Mengembangkan **aplikasi Streamlit interaktif** untuk menampilkan hasil prediksi.

---

## 🧩 Dataset Description
Dataset terdiri dari 7043 pelanggan Telco di California dan dikompilasi dari beberapa file:
- Customer Information
- Location Data
- Online Services
- Payment Information
- Service Options
- Status Analysis

**Target:**  
`Churn Value` (1 = Churn, 0 = Stay)

---

## ⚙️ Project Flow
<div align="center">
  <img src="https://miro.medium.com/v2/resize:fit:828/format:webp/1*t9rPZP6MBbkg6xVvnvC6VA.png" width="700"/>
</div>

1. **Data Preparation**
   - Merge seluruh dataset menggunakan `CustomerID`.
   - Cek dan tangani missing values serta data duplikat.

2. **Exploratory Data Analysis (EDA)**
   - Analisis demografi, jenis layanan, metode pembayaran, hingga satisfaction score.
   - Visualisasi faktor-faktor yang mempengaruhi churn.

   📈 Contoh EDA:
   ![EDA Example](https://user-images.githubusercontent.com/67491980/151698267-830dd78f-41ff-4b3d-9f5d-9f42a309e25f.png)

3. **Model Building**
   - Machine Learning models: **Logistic Regression**, **Random Forest**, **XGBoost**.
   - Tuning hyperparameter untuk optimasi.
   - Evaluasi performa model dengan:
     - Accuracy
     - Precision & Recall
     - F1 Score
     - ROC-AUC

   🧠 Contoh Model Evaluation:
   ![Confusion Matrix Example](https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Confusion_matrix.svg/640px-Confusion_matrix.svg.png)

4. **Deployment with Streamlit**
   - Bangun aplikasi prediksi churn berbasis web.
   - User dapat input karakteristik pelanggan → Prediksi churn/non-churn.

   🚀 Contoh Tampilan App:
   ![Streamlit App Example](https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png)

---

## 📈 Tools Used
- **Python 3.11**
- **Pandas, Numpy** - Data manipulation
- **Matplotlib, Seaborn** - Visualization
- **Scikit-learn** - ML Modeling
- **XGBoost** - Gradient Boosting Model
- **Streamlit** - Deployment aplikasi web

---

## 🏆 Project Goals
- Membantu perusahaan mengidentifikasi pelanggan berisiko churn lebih awal.
- Memberikan insights berbasis data untuk memperbaiki strategi retensi.
- Mengembangkan pengalaman membuat **end-to-end machine learning pipeline** dan **aplikasi produk** nyata.

---

## 🚀 How to Run Locally
1. Clone repository ini:
   ```bash
   git clone https://github.com/yourusername/telco-customer-churn-prediction.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Jalankan aplikasi:
   ```bash
   streamlit run app.py
   ```

---

## 🙌 Acknowledgements
- Dataset bersifat fiktif dan dibuat untuk keperluan pembelajaran dan pengembangan model prediktif churn pelanggan.
- Project ini dibuat dalam rangka meningkatkan kemampuan Data Science, Machine Learning, dan Deployment.

---

> ✨ Terima kasih telah mengunjungi project ini! Feedback dan saran sangat dihargai!

---

Kalau kamu mau, aku juga bisa buatkan **struktur file/folder** + contoh isi **requirements.txt** supaya repo kamu langsung **siap rilis** di GitHub!  
Mau sekalian dibuatin? 🚀🚀🚀
