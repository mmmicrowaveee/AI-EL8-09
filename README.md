

<div align="center">

  <!-- Header Banner / Badges -->
  <img src="https://img.shields.io/badge/Artificial_Intelligence-Expert_System-0A66C2?style=for-the-badge&logo=python&logoColor=white" alt="AI Expert System" />
  <img src="https://img.shields.io/badge/Control_System-Fuzzy_Logic_Mamdani-008080?style=for-the-badge" alt="Fuzzy Control" />
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=yellow" alt="Python" />
  <img src="https://img.shields.io/badge/Library-Scikit--Fuzzy-orange?style=for-the-badge" alt="Scikit-Fuzzy" />
  <img src="https://img.shields.io/badge/Platform-Windows_11_(Local_Run)-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows" />

  <h1>🧠 Expert System for Autonomous Braking Control</h1>
  <p><b>Implementasi Sistem Pakar Berbasis Logika Fuzzy (Metode Mamdani) pada Sistem Kendali Pengereman Otomatis</b></p>

  <p>
    <a href="#-identitas--spesifikasi-environment-lokal">Identitas & Environment</a> •
    <a href="#-arsitektur-expert-system--sistem-kendali">Arsitektur Sistem</a> •
    <a href="#-langkah-instalasi--eksekusi-lokal">Cara Running</a> •
    <a href="#-hasil-pengujian--analisis-input-output">Hasil & Analisis</a> •
    <a href="#-log-troubleshooting-eksekusi-lokal">Troubleshooting</a>
  </p>
</div>

---

## 📌 Ikhtisar Proyek (Project Overview)

Repository ini merupakan bagian dari pemenuhan tugas mata kuliah **Artificial Intelligence (AI)** dengan topik fokus **Expert System (Sistem Pakar)** yang diterapkan pada domain **Sistem Kendali Otomatis (*Closed-Loop Actuator Control*)**.

Program ini mengimplementasikan *Knowledge-Based Fuzzy Inference System* (Metode Mamdani) untuk menentukan besaran persentase gaya pengereman aktuator (`braking_force`) secara otomatis berdasarkan pembacaan dua sensor utama: **Kecepatan Kendaraan (`speed`)** dan **Jarak Terhadap Objek (`distance`)**.

* **Referensi Utama Repository:** [aidanjgriffiths/Fuzzy-Logic-System-Jupyter](https://github.com/aidanjgriffiths/Fuzzy-Logic-System-Jupyter)
* **File Eksekusi Utama:** `fuzzy_control.py`

---

## 💻 Identitas & Spesifikasi Environment Lokal

Sesuai dengan kriteria penugasan, seluruh kode program pada repository ini telah dikonfigurasi, diuji, dan dijalankan secara lokal (*local execution*) pada spesifikasi perangkat berikut:

| Parameter | Spesifikasi Detail |
| :--- | :--- |
| **Nama Mahasiswa** | **Ariel Davison Lucius** |
| **NIM / Kelas** | **101022430006** / **EL4809** |
| **Program Studi** | S1 Teknik Elektro |
| **Perangkat Keras** | Laptop Acer (Windows x64 Architecture) |
| **Sistem Operasi** | Microsoft Windows 10/11 64-bit |
| **Direktori Kerja Lokal** | `E:\01-Expert-System-Control\01-Expert-System-Control` |
| **Environment Python** | Python Virtual Environment (`venv`) via Windows PowerShell |
| **Dependensi Library** | `numpy`, `scipy`, `matplotlib`, `scikit-fuzzy`, `networkx` |

---

## ⚙️ Arsitektur Expert System & Sistem Kendali

Sistem pakar ini menggantikan pemodelan matematis diferensial non-linier menggunakan pendekatan **Aturan Linguistik Pakar (*IF-THEN Rules*)**.

```text
+-------------------+       +-----------------------------------------------+       +------------------------+
|   CRISP INPUTS    |       |             EXPERT SYSTEM ENGINE              |       |      CRISP OUTPUT      |
|  (Sensor Daerah)  |       |                                               |       |   (Aktuator Kendali)   |
|                   |       |  +---------------+     +-------------------+  |       |                        |
| - Speed (km/h)    | ----> |  | Fuzzification | --> |  Inference Engine |  | ----> | - Braking Force (%)    |
| - Distance (m)    |       |  +---------------+     |  (Mamdani Rules)  |  |       |   [Defuzzification:    |
|                   |       |                        +-------------------+  |       |    Centroid Method]    |
+-------------------+       +-----------------------------------------------+       +------------------------+
```

### 1. Variabel Linguistik & Himpunan Fuzzy (*Membership Functions*)
* **Input 1 — Kecepatan (`speed`):** Semesta pembicaraan [0, 100]\text{ km/h}
  * *Very Slow* (Trapesium: [0, 0, 20, 35])
  * *Slow* (Segitiga: [20, 40, 60])
  * *Fast* (Segitiga: [45, 65, 85])
  * *Very Fast* (Trapesium: [70, 85, 100, 100])
* **Input 2 — Jarak Objek (`distance`):** Semesta pembicaraan [0, 100]\text{ m}
  * *Very Close* (Trapesium: [0, 0, 15, 30])
  * *Close* (Segitiga: [15, 35, 55])
  * *Far* (Segitiga: [40, 65, 85])
  * *Very Far* (Trapesium: [70, 85, 100, 100])
* **Output — Gaya Pengereman (`braking_force`):** Semesta pembicaraan [0, 100]\%
  * *Very Light* ([0, 0, 15, 30]), *Light* ([15, 35, 55]), *Heavy* ([45, 65, 85]), *Very Heavy* ([70, 85, 100, 100])

### 2. Basis Pengetahuan (*Knowledge Base / Rule Base*)
Mesin inferensi mengevaluasi 8 aturan pakar (*Rule 1 – Rule 8*) berikut:

| Kode Aturan | Kondisi Sensor 1 (`Speed`) | Operator | Kondisi Sensor 2 (`Distance`) | Keputusan Aktuator (`Braking Force`) |
| :---: | :---: | :---: | :---: | :---: |
| **R1** | `very_fast` | `AND` | `very_close` | **`very_heavy`** |
| **R2** | `fast` | `AND` | `very_close` | **`very_heavy`** |
| **R3** | `fast` | `AND` | `close` | **`heavy`** |
| **R4** | `slow` | `AND` | `close` | **`light`** |
| **R5** | `slow` | `AND` | `far` | **`very_light`** |
| **R6** | `very_slow` | `OR` | `very_far` | **`very_light`** |
| **R7** | `very_fast` | `AND` | `close` | **`very_heavy`** |
| **R8** | `very_fast` | `AND` | `far` | **`heavy`** |

---

## 🚀 Langkah Instalasi & Eksekusi Lokal

Berikut adalah prosedur langkah demi langkah untuk mereproduksi dan menjalankan program ini di komputer lokal menggunakan **Windows PowerShell**:

### 1. Persiapan Direktori Kerja
```powershell
mkdir 01-Expert-System-Control
cd 01-Expert-System-Control
```

### 2. Pembuatan & Aktivasi Virtual Environment (`venv`)
```powershell
python -m venv venv
Set-ExecutionPolicy Unrestricted -Scope Process
.\venv\Scripts\Activate.ps1
```

### 3. Instalasi Dependensi Library
Pastikan indikator `(venv)` sudah aktif di sebelah kiri terminal, lalu jalankan:
```powershell
pip install numpy scipy matplotlib scikit-fuzzy networkx
```

### 4. Eksekusi Program Sistem Pakar
```powershell
python fuzzy_control.py
```

---

## 📊 Hasil Pengujian & Analisis Input-Output

Pada pengujian eksekusi lokal menggunakan skrip `fuzzy_control.py`, diberikan skenario pengujian darurat (*high-speed close-proximity test*) dengan parameter *crisp input* sebagai berikut:

* **Input Sensor Kecepatan (`speed`):** $78\text{ km/h}$ *(terpetakan pada derajat keanggotaan Fast dan Very Fast)*
* **Input Sensor Jarak (`distance`):** $18\text{ m}$ *(terpetakan pada derajat keanggotaan Very Close dan Close)*

### Output Terminal PowerShell:
```text
====================================================
   EXPERT SYSTEM: FUZZY AUTONOMOUS BRAKING CONTROL  
====================================================
Input Sensor Kecepatan (Speed)   : 78 km/h
Input Sensor Jarak (Distance)    : 18 m
Output Aktuator Pengereman       : 84.52 %
====================================================
```

### Analisis Sistem Kendali:
Dengan kecepatan tinggi ($78\text{ km/h}$) dan jarak halangan yang sudah sangat dekat ($18\text{ m}$), mesin inferensi mengaktifkan **Rule 1**, **Rule 2**, **Rule 3**, dan **Rule 7** secara simultan. Proses *defuzzification* menggunakan metode *Centroid (Center of Gravity)* menghasilkan sinyal kendali pengereman sebesar **$84.52\%$** (kategori **Very Heavy Braking**) untuk menghentikan laju kendaraan dengan aman.

### Bukti Screenshot Running Lokal:
> *(Catatan: Pastikan kamu meng-upload gambar screenshot ke folder `screenshots` atau sesuaikan nama filenya di bawah ini)*

![Bukti Running Lokal](screenshots/local_run_output.png)

---

## 🛠️ Log Troubleshooting Eksekusi Lokal

Selama proses konfigurasi dan pengujian di perangkat lokal, terdapat beberapa kendala teknis yang ditemukan dan berhasil diselesaikan:

1. **Konflik Lingkungan *Build* PlatformIO di VS Code:**
   * **Masalah:** Antarmuka default VS Code terikat pada *environment* PlatformIO (`penv`) untuk mikrokontroler sehingga mengganggu inisialisasi kernel Python standar.
   * **Solusi:** Membuka sesi kerja terpisah melalui Windows PowerShell secara langsung pada direktori `E:\01-Expert-System-Control\01-Expert-System-Control` dan mengeksekusi kode sebagai skrip mandiri (`fuzzy_control.py`).
2. **Kegagalan Penyalinan `venvlauncher.exe` Lintas Partisi Drive (`D:\` ke `E:\`):**
   * **Masalah:** Muncul pesan `Unable to copy 'D:\Lib\venv\scripts\nt\venvlauncher.exe'` akibat interupsi proses pada pembuatan `venv` pertama yang menyebabkan file terkunci.
   * **Solusi:** Menghapus direktori `venv` yang korup dengan perintah `Remove-Item -Recurse -Force venv` dan membangun ulang *virtual environment* secara bersih.
3. **Pemanggilan Aktivasi `venv` pada Windows PowerShell:**
   * **Masalah:** Menjalankan perintah `venv\Scripts\activate` tanpa awalan relative path memicu error `The module 'venv' could not be loaded`.
   * **Solusi:** Menggunakan sintaks eksplisit PowerShell `.\venv\Scripts\Activate.ps1`.
4. **Dependensi Graf `networkx` pada Modul `skfuzzy.control`:**
   * **Masalah:** Saat mengeksekusi `from skfuzzy import control as ctrl`, muncul `ModuleNotFoundError: No module named 'networkx'` karena `scikit-fuzzy` tidak menginstal `networkx` secara otomatis.
   * **Solusi:** Menambahkan instalasi paket `pip install networkx` di dalam `(venv)` sehingga grafik simulasi *defuzzification* berhasil ditampilkan melalui `matplotlib`.

---

<div align="center">
  <sub>Disusun untuk Tugas Mata Kuliah Artificial Intelligence — Program Studi S1 Teknik Elektro</sub>
</div>
