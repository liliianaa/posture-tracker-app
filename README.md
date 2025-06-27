🧍‍♂️Human Posture Tracking Web App




Aplikasi web interaktif berbasis Streamlit untuk mendeteksi dan melacak postur duduk/berdiri manusia dari video menggunakan YOLOv8 dan Deep SORT. Aplikasi ini mampu menghitung durasi setiap postur per individu dan memungkinkan pengguna mengunduh hasilnya dalam bentuk video dan file CSV.

🌟 Fitur Utama
Deteksi & Tracking Cerdas: Deteksi duduk/berdiri menggunakan YOLOv8 dan pelacakan ID unik dengan Deep SORT

Visualisasi Real-Time: Tampilkan video dengan kotak deteksi dan label ID+durasi

Timer Otomatis: Hitung waktu duduk dan berdiri untuk tiap orang dalam video

Ekspor CSV & Video: Unduh video hasil analisis dan rekapitulasi waktu dalam bentuk CSV

100% Berbasis Web: Tidak perlu instalasi lokal, dapat dijalankan di Streamlit Cloud

📂 Format Input yang Didukung
🎥 Format video: .mp4

📏 Resolusi: Fleksibel (otomatis disesuaikan)

👥 Dukungan multi-orang dengan ID unik

🚀 Cara Cepat Menjalankan Aplikasi
Prasyarat
Python 3.10+

(Opsional) GPU dengan CUDA untuk inferensi lebih cepat

Langkah Instalasi
Clone repository

bash
Copy code
git clone https://github.com/username/posture-tracking-streamlit.git
cd posture-tracking-streamlit
Buat virtual environment

bash
Copy code
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
Instalasi dependensi

bash
Copy code
pip install -r requirements.txt
Letakkan model YOLO
Simpan file best.pt (hasil training model deteksi postur) di direktori proyek.

Jalankan aplikasi

bash
Copy code
streamlit run app.py
🧠 Cara Kerja Aplikasi
Pengguna mengunggah video .mp4

Setiap frame diproses dengan YOLOv8 untuk deteksi manusia dan klasifikasi postur

Deep SORT melacak posisi orang dari frame ke frame, memberi ID unik

Sistem menghitung durasi waktu duduk dan berdiri untuk setiap ID

Hasil dapat diunduh sebagai:

📥 Video hasil (output_posture.mp4)

📄 File CSV (output_posture.csv)

📊 Contoh Output CSV
csv
Copy code
ID,Sit Duration (s),Stand Duration (s)
1,75,32
2,10,98
3,0,140
📁 Struktur Folder Proyek
bash
Copy code
.
├── app.py                # Script utama Streamlit
├── best.pt               # Model deteksi postur (YOLOv8)
├── requirements.txt      # Daftar dependensi Python
├── runtime.txt           # Versi Python untuk Streamlit Cloud
└── ...
🔧 Daftar Dependensi
txt
Copy code
streamlit                # Antarmuka web interaktif
ultralytics              # Library YOLOv8 untuk deteksi objek
deep_sort_realtime       # Pelacakan objek real-time
opencv-python-headless   # Pemrosesan video (tanpa GUI)
Pillow                   # Manipulasi gambar
torch                    # Framework deep learning
Semua dependensi terdaftar di file requirements.txt.

☁️ Deployment di Streamlit Cloud
Upload proyek ke GitHub

Pastikan app.py, requirements.txt, dan runtime.txt tersedia

Kunjungi https://streamlit.io/cloud

Klik New App → Pilih repo GitHub → Klik Deploy

Model best.pt dapat diunggah ke root repo atau ditautkan dari URL

⚠️ Catatan: Streamlit Cloud tidak mendukung GPU, jadi disarankan menggunakan video pendek untuk performa optimal.

📈 Rencana Pengembangan
🔴 Dukungan real-time dari webcam

🧍 Deteksi lebih banyak postur (contoh: membungkuk, tidur)

⏰ Peringatan waktu duduk terlalu lama

🌐 Integrasi API untuk pemantauan kantor/sekolah

🤝 Kontribusi
Kami terbuka untuk kontribusi komunitas! Kamu bisa:

Melaporkan bug

Menambahkan fitur baru

Memperbaiki dokumentasi

Langkah Kontribusi
bash
Copy code
# 1. Buat cabang baru
git checkout -b fitur/postur-lain

# 2. Lakukan perubahan dan commit
git commit -m "feat: menambahkan deteksi jongkok"

# 3. Push ke GitHub dan buat Pull Request
git push origin fitur/postur-lain
🙌 Ucapan Terima Kasih
YOLOv8 dari Ultralytics

Deep SORT dari nwojke/deep_sort

Streamlit sebagai framework pembuatan UI Python

⭐ Dukung Proyek Ini
Jika aplikasi ini bermanfaat:

🌟 Beri bintang pada repo

🍴 Fork dan kembangkan lebih lanjut

🔗 Bagikan ke teman/kolega

💬 Beri masukan dan feedback

