**Inline CSS**

Inline CSS adalah kode CSS yang ditulis langsung pada atribut elemen HTML. Setiap elemen HTML memiliki atribut style.

Manfaat

1. Sangat membantu ketika hanya ingin menguji dan melihat perubahan pada satu elemen.
2. Berguna untuk memperbaiki kode dengan cepat.
3. Proses permintaan HTTP yang lebih kecil dan proses load website akan lebih cepat.

Kekurangan

1. Proses permintaan HTTP yang lebih kecil dan proses load website akan lebih cepat.

**Internal CSS**

Internal CSS adalah kode CSS yang ditulis di dalam tag <style> dan kode HTML dituliskan di bagian atas (header) file HTML. Internal CSS dapat digunakan untuk membuat tampilan pada satu halaman website dan tidak digunakan pada halaman website yang lain.

Manfaat
  
1. Perubahan pada Internal CSS hanya berlaku pada satu halaman saja.
2. Class dan ID bisa digunakan oleh internal stylesheet.
3. Tidak perlu melakukan upload beberapa file karena HTML dan CSS berada dalam satu file.
  
Kekurangan
1. Tidak efisien apabila Anda ingin menggunakan CSS yang sama dalam beberapa file.
2. Membuat performa website lebih lemot. Sebab, CSS yang berbeda-beda akan mengakibatkan loading ulang setiap kali Anda ganti halaman website.

**External CSS**
  
Eksternal CSS adalah kode CSS yang ditulis terpisah dengan kode HTML Eksternal CSS ditulis di sebuah file khusus yang berekstensi .css. File eksternal CSS biasanya diletakkan setelah bagian <head> pada halaman.

Manfaat
1. Ukuran file HTML akan menjadi lebih kecil dan struktur dari kode HTML jadi lebih rapi.
2. Loading website menjadi lebih cepat.
3. File CSS dapat digunakan di beberapa halaman website sekaligus.

Kekurangan
1. Halaman akan menjadi berantakan, ketika file CSS gagal dipanggil oleh file HTML. Hal ini terjadi disebabkan karena koneksi internet yang lambat.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

HTML5 TAG

  
![image](https://user-images.githubusercontent.com/87772747/194213788-c6ff2c6f-4f2c-43dd-8604-622e68bf826c.png)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

CSS SELECTOR

**1. Selektor Tag**
  
Selektor Tag disbut juga Type Selector. Selektor ini akan memilih elemen berdasarkan nama tag.
  
  
**2. Selektor Class**
  
Selektor class adalah selektor yang memilih elemen berdasarkan nama class yang diberikan. Selektor class dibuat dengan tanda titik di depannya.
  
  
**3. Selektor ID**
  
Selektor ID hampir sama dengan class. Bedanya, ID bersifat unik. Hanya boleh digunakan oleh satu elemen saja.
  
  
**4. Selektor Atribut**
  
Selektor atribut adalah selektor yang memilik elemen berdasarkan atribut. Selektor ini hampir sama seperti selektor Tag.
  
  
**5. Selektor Universal**
  
Selektor universal adalah selektor yang digunakan untuk menyeleksi semua elemen pada jangkaua (scope) tertentu.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1. Menambahkan style.css pada folder static sebagai external css
2. Memanggil fungsi agar style.css dapat digunakan pada base.html
3. Mendesain todolist, login, register, dan create-task.
 
