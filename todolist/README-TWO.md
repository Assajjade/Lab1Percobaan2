## Asynchronus Programming dan Synchronus programming
- Asynchronus programming: Proses jalannya program bisa dilakukan secara bersamaan tanpa harus menunggu proses antrian. Pada dasarnya semua Bahasa pemrograman menggunakan Asynchronouse.
- Synchronus programming: Proses jalannya program secara sequential , disini yang dimaksud sequential ada berdasarkan antrian ekseskusi program. 
## Paradigma Event-Driven Programming
Event-Driven Programming adalah salah satu teknik pemogramman yang konsep kerjanya tergantung dari kejadian atau event tertentu. misalnya ketika tombol A diklik maka nilai label 2 ditambah nilai label 3 dibagi nilai label4.tapi jika tombol A diklik dan ternyata label satu berisikan penjumlahan. makaprogram yang dijalankan label 2 ditambah label 3.

## Asynchronus Programming pada AJAX
AJAX adalah sebuah teknik yang dapat membuat laman website ter-*update* secara asinkronus. Artinya browser tidak perlu *reload* seluruh laman website ketika hanya ada perubahan data yang kecil. AJAX akan mengirimkan request ke server, dan melanjutkan eksekusi tanpa menunggu balasan dari server terlebih dahulu.

## Implementasi checklist
1. Membuat fungsi views yang mengembalikan data json
2. Mendaftarkan url dari views tersebut
3. Membuat script untuk mengambil data json dari views yang sudah dibuat lalu data yang telah diambil ditampilkan pada html
4. Mengubah tombol Add task sebagai tombol yang akan mengaktifkan pop up modal
5. Membuat modal berdasarkan dokumentasi bootsrap yang didalmnya berisi form untuk menambah task
6. Membuat fungsi views yang menerima data lalu menyimpan data tersebut jika valid
7. Mendaftarkan url dari views tersebut.
8. Membuat script yang aktif ketika tombol submit form diklik lalu script tersebut akan mengambil data dari form lalu mengirimkan ke views yang sudah dibuat
