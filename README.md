#  Hand Tracking Mouse Control 

Proyek ini menggunakan OpenCV dan MediaPipe untuk melacak gerakan tangan dan mengontrol kursor mouse pada layar. Dengan menggunakan kamera, sistem dapat mendeteksi jari telunjuk dan jari tengah untuk menggerakkan kursor serta melakukan klik.

## ✨ Fitur
- 🖥️ **Pelacakan tangan real-time** menggunakan OpenCV dan MediaPipe.
- 🎯 **Kontrol kursor mouse** dengan gerakan tangan.
- 👆 **Klik otomatis** dengan jari telunjuk dan tengah.
- 🔄 **Filter eksponensial** untuk pergerakan yang lebih halus.
- 🚫 **Zona mati (dead zone)** untuk menghindari gerakan kecil yang tidak diinginkan.
- 🎮 **Tampilan FPS** untuk pemantauan performa.

## ⚙️ Persyaratan
Sebelum menjalankan proyek ini, pastikan Anda telah menginstal pustaka yang diperlukan:
```bash
pip install opencv-python mediapipe numpy pyautogui
```

## 🚀 Cara Menjalankan
1. 📷 Pastikan kamera Anda berfungsi.
2. ▶️ Jalankan skrip dengan perintah berikut:
```bash
python main.py
```
3. 🏹 Gunakan jari telunjuk dan Jari tengah untuk menggerakkan kursor.
4. 🖱️ Jari telunjuk yang terbuka akan melakukan hold klik kiri.
5. ❌ Tekan tombol **'q'** untuk keluar dari program.

## 🔧 Konfigurasi Tambahan
- 🎥 **Resolusi Kamera:** Dikurangi menjadi **320x240** untuk meningkatkan performa.
- 🔄 **Filter Eksponensial:** Digunakan untuk mengurangi getaran pada pergerakan kursor.
- 🚫 **Zona Mati:** Ditetapkan pada **5 piksel** untuk menghindari pergerakan yang terlalu sensitif.

## 🏆 Penggunaan
- 🖥️ **Mengontrol PC tanpa mouse fisik.**
- 🏗️ **Eksperimen dalam interaksi komputer berbasis gerakan.**
- 🤖 **Dapat dikembangkan lebih lanjut untuk sistem kontrol berbasis gesture lainnya.**

## 📜 Lisensi
Proyek ini bersifat open-source, Anda dapat menggunakannya dan memodifikasinya sesuai kebutuhan. 🚀

