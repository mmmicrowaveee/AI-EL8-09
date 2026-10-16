\# Expert System for Autonomous Braking Control (Fuzzy Logic Knowledge-Based System)



Repository ini merupakan bagian dari pemenuhan tugas mata kuliah \*\*Artificial Intelligence (AI)\*\* dengan fokus topik \*\*Expert System pada Sistem Kendali\*\*. Program ini mengimplementasikan \*Rule-Based Fuzzy Logic Expert System\* untuk mengendalikan gaya pengereman otomatis (\*Autonomous Braking Control\*) berdasarkan pengetahuan pakar.



\- \*\*Sumber Repository Referensi:\*\* \[aidanjgriffiths/Fuzzy-Logic-System-Jupyter](https://github.com/aidanjgriffiths/Fuzzy-Logic-System-Jupyter)

\- \*\*Topik AI:\*\* Expert System (Knowledge-Based Fuzzy Inference System)

\- \*\*Domain Aplikasi:\*\* Sistem Kendali Otomatis (\*Closed-Loop Actuator Control\*)



\---



\## 1. Identitas \& Spesifikasi Environment Lokal



Program ini telah diuji dan dijalankan secara lokal (\*local execution\*) pada spesifikasi perangkat berikut:



\* \*\*Nama:\*\* Ariel Davison Lucius

\* \*\*NIM:\*\* 101022430006

\* \*\*Program Studi:\*\* S1 Teknik Elektro

\* \*\*Perangkat:\*\* Laptop Acer Nitro 7

\* \*\*Sistem Operasi:\*\* Windows 10 / 11 (64-bit)

\* \*\*Versi Python:\*\* Python 3.x (via Virtual Environment)

\* \*\*IDE:\*\* Visual Studio Code (dengan ekstensi Jupyter Notebook)

\* \*\*Library Utama:\*\* `scikit-fuzzy`, `numpy`, `scipy`, `matplotlib`, `networkx`



\---



\## 2. Deskripsi Sistem \& Arsitektur Expert System



Dalam sistem kendali, pendekatan \*\*Expert System berbasis Fuzzy Logic (Metode Mamdani)\*\* digunakan untuk menerjemahkan keputusan operator/pakar manusia ke dalam aturan kendali otomatis (\*IF-THEN Rules\*) tanpa memerlukan pemodelan persamaan diferensial non-linier yang kompleks.



\### Komponen Utama:

1\. \*\*Crisp Inputs (Sensor):\*\*

&#x20;  \* `Speed` (Kecepatan kendaraan: rentang 0 – 100 km/jam) -> Himpunan Fuzzy: \*Very Slow, Slow, Fast, Very Fast\*.

&#x20;  \* `Distance` (Jarak terhadap objek/halangan: rentang 0 – 100 meter) -> Himpunan Fuzzy: \*Very Close, Close, Far, Very Far\*.

2\. \*\*Knowledge Base \& Inference Engine:\*\*

&#x20;  \* Menggunakan basis aturan (\*Rule Base\*) kombinasi kondisi kecepatan dan jarak untuk menentukan aksi aktuator (contoh: `IF Speed is Very Fast AND Distance is Very Close THEN Braking Force is Very Heavy`).

3\. \*\*Defuzzification (Crisp Output Aktuator):\*\*

&#x20;  \* `Braking Force` (Persentase gaya pengereman: rentang 0 – 100%) -> Himpunan Fuzzy: \*Very Light, Light, Heavy, Very Heavy\*.



\---



\## 3. Langkah Instalasi \& Cara Running Lokal



Berikut adalah langkah-langkah untuk mereproduksi dan menjalankan program ini di komputer lokal:



\### a. Clone Repository

```bash

git clone \[https://github.com/aidanjgriffiths/Fuzzy-Logic-System-Jupyter.git](https://github.com/aidanjgriffiths/Fuzzy-Logic-System-Jupyter.git)

cd Fuzzy-Logic-System-Jupyter

