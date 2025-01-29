# ResuMe (Resume Classification)

## Deskripsi Proyek

ResuMe adalah aplikasi berbasis web yang dikembangkan sebagai proyek akhir dalam program Magang dan Studi Independen Bersertifikat (MSIB) "Artificial Intelligence 4 Jobs" di Orbit Future Academy. Aplikasi ini menggunakan algoritma Naïve Bayes untuk mengklasifikasikan resume berdasarkan divisi tertentu guna membantu tim Human Resource (HR) dalam proses seleksi kandidat.

## Tujuan

- Mengembangkan keterampilan dalam bidang Artificial Intelligence (AI) dengan penerapan praktis.
- Mengimplementasikan model klasifikasi resume menggunakan pendekatan AI.
- Meningkatkan efisiensi dan akurasi dalam seleksi kandidat kerja.

## Teknologi yang Digunakan

- **Python**: Digunakan sebagai bahasa pemrograman utama.
- **Flask**: Framework web untuk membangun aplikasi berbasis web.
- **Naïve Bayes**: Algoritma utama dalam klasifikasi resume.
- **NLTK**: Untuk preprocessing teks.
- **TF-IDF**: Untuk ekstraksi fitur dari teks.
- **Ngrok**: Untuk mengakses aplikasi melalui jaringan publik.

## Fitur Utama

- **Upload Resume**: Pengguna dapat mengunggah resume dalam format PDF.
- **Klasifikasi Otomatis**: Resume dikategorikan ke dalam enam divisi:
  - Accounting
  - Business Development
  - Digital Media
  - Engineering
  - Human Resource
  - Sales
- **Evaluasi Model**: Menggunakan Confusion Matrix, Precision, Recall, dan F1-Score.
- **Web-Based Interface**: Antarmuka berbasis web menggunakan Flask.

## Instalasi dan Penggunaan

1. **Clone Repository**
   ```bash
   git clone https://github.com/username/resume-classification.git
   cd resume-classification
   ```
2. **Instalasi Dependensi**
   ```bash
   pip install -r requirements.txt
   ```
3. **Menjalankan Aplikasi**
   ```bash
   python app.py
   ```
4. **Menggunakan Ngrok untuk Akses Publik**
   ```bash
   ngrok http 5000
   ```
5. **Akses Aplikasi** Buka browser dan akses `http://127.0.0.1:5000` atau gunakan URL yang diberikan oleh Ngrok.

## Dataset

Dataset yang digunakan berasal dari Kaggle dengan total 677 entri yang mencakup enam kategori resume.

## Evaluasi Model

- **Akurasi Model**: 83%
- **Confusion Matrix**: Digunakan untuk mengevaluasi performa klasifikasi.
- **Metode Evaluasi**: Precision, Recall, dan F1-Score.

## Pengembang

**Ahmad Muyaqi**\
Magang & Studi Independen Bersertifikat - Orbit Future Academy\
Universitas Negeri Semarang


## Kontak

Jika ada pertanyaan atau saran, silakan hubungi melalui email: (muyaqiahmad@gmail.com) atau kunjungi LinkedIn: https://www.linkedin.com/in/ahmadmuyaqi/.

