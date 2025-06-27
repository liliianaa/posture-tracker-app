# 🧍‍♂️ Human Posture Tracking Web App

Aplikasi web interaktif berbasis **Streamlit** untuk mendeteksi dan melacak **postur duduk/berdiri manusia** dari video menggunakan **YOLOv8** dan **Deep SORT**. Aplikasi ini mampu menghitung durasi setiap postur per individu dan memungkinkan pengguna mengunduh hasilnya dalam bentuk video dan file CSV.

---

## 🌟 Fitur Utama

* 🎯 **Deteksi & Pelacakan Cerdas**
  Deteksi postur duduk/berdiri dengan YOLOv8 dan pelacakan ID unik menggunakan Deep SORT.

* 🎥 **Visualisasi Real-Time**
  Tampilkan kotak deteksi dan label durasi langsung di atas video.

* ⏱️ **Timer Otomatis**
  Hitung durasi duduk dan berdiri secara terpisah untuk tiap orang.

* 📁 **Ekspor CSV & Video**
  Unduh hasil deteksi berupa video dan data waktu dalam format CSV.

* 🌐 **100% Berbasis Web**
  Tidak perlu instalasi tambahan, dapat dijalankan langsung di Streamlit Cloud.

---

## 📂 Format Input yang Didukung

* 🎞️ Format video: `.mp4`
* 📏 Resolusi: Bebas (otomatis disesuaikan)
* 👥 Mendukung banyak orang (multi-ID) dalam satu video

---

## 🚀 Cara Cepat Menjalankan Aplikasi

### ⚖️ Prasyarat

* Python **3.10+**
* (Opsional) GPU dengan CUDA untuk mempercepat proses deteksi

### 🛠️ Instalasi

1. **Clone repository**

   ```bash
   git clone https://github.com/username/posture-tracking-streamlit.git
   cd posture-tracking-streamlit
   ```

2. **Buat virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate     # Windows: venv\Scripts\activate
   ```

3. **Instalasi dependensi**

   ```bash
   pip install -r requirements.txt
   ```

4. **Letakkan model YOLOv8**
   Simpan file `best.pt` (model deteksi postur) di direktori utama proyek.

5. **Jalankan aplikasi**

   ```bash
   streamlit run app.py
   ```

---

## 🧠 Cara Kerja Aplikasi

1. Pengguna mengunggah video `.mp4` melalui web interface.
2. Setiap frame dianalisis oleh **YOLOv8** untuk mendeteksi dan mengklasifikasi postur manusia (duduk atau berdiri).
3. **Deep SORT** melacak objek yang terdeteksi dan memberi **ID unik** untuk tiap orang.
4. Timer menghitung durasi **duduk** dan **berdiri** secara otomatis berdasarkan ID.
5. Setelah video selesai diproses, pengguna dapat:

   * 👅 Mengunduh **video hasil deteksi**
   * 📄 Mengunduh **CSV ringkasan waktu postur**

---

## 📊 Contoh Output CSV

```csv
ID,Sit Duration (s),Stand Duration (s)
1,75,32
2,10,98
3,0,140
```

---

## 📁 Struktur Folder Proyek

```bash
.
├── app.py              # Script utama aplikasi Streamlit
├── best.pt             # Model YOLOv8 untuk deteksi postur
├── requirements.txt    # Daftar pustaka Python
├── runtime.txt         # Versi Python untuk deployment Streamlit Cloud
└── ...
```

---

## 🔧 Daftar Dependensi (requirements.txt)

```txt
streamlit                # Framework UI berbasis web
ultralytics              # YOLOv8 untuk deteksi postur
deep_sort_realtime       # Pelacakan objek multi-ID
opencv-python-headless   # Pengolahan video
Pillow                   # Manipulasi gambar
torch                    # Framework machine learning (PyTorch)
```

---

## ☁️ Deployment di Streamlit Cloud

1. Upload proyek ke GitHub.
2. Pastikan file `app.py`, `requirements.txt`, dan `runtime.txt` tersedia.
3. Buka [https://streamlit.io/cloud](https://streamlit.io/cloud).
4. Klik **"New App"** → Pilih repository → Klik **"Deploy"**.
5. Pastikan file `best.pt` tersedia di root repository.

> ⚠️ **Catatan:** Streamlit Cloud tidak mendukung GPU, jadi sebaiknya gunakan video berdurasi pendek agar proses berjalan optimal.

---

## 📈 Rencana Pengembangan

* 🎥 Dukungan deteksi dari webcam secara real-time
* 🢎 Tambahan postur lain seperti membungkuk, jongkok, tidur
* ⏰ Fitur peringatan jika duduk terlalu lama
* 📡 Integrasi API untuk pemantauan ruang publik / sekolah / kantor

---

## 🤝 Kontribusi

Kami menyambut kontribusi dari siapa pun!

### Cara Berkontribusi:

```bash
# 1. Buat cabang baru
git checkout -b fitur/postur-lain

# 2. Lakukan perubahan dan commit
git commit -m "feat: menambahkan deteksi jongkok"

# 3. Push ke GitHub dan buat Pull Request
git push origin fitur/postur-lain
```

---

## 🙌 Ucapan Terima Kasih

* **Ultralytics YOLOv8**: [https://github.com/ultralytics/ultralytics](https://github.com/ultralytics/ultralytics)
* **Deep SORT Tracking**: [https://github.com/nwojke/deep\_sort](https://github.com/nwojke/deep_sort)
* **Streamlit**: Untuk framework web berbasis Python yang sangat mudah digunakan

---

## ⭐ Dukung Proyek Ini

Jika aplikasi ini membantu Anda:

* 🌟 Berikan bintang di GitHub
* 🍟 Fork dan kembangkan sendiri
* 🔗 Bagikan ke rekan/komunitas Anda
* 💬 Beri masukan agar kami bisa terus meningkatkan aplikasi ini
