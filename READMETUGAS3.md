Nama: Abdillah Assajjad
NPM: 2106653571

JSON
+ JSON adalah (Notasi Objek JavaScript) Adalah standar terbuka berbasis teks untuk pertukaran data.
+ JSON adalah bahasa meta.
+ JSON sederhana dan mudah dibaca.
+ JSON berorientasi pada data.
+ JSON mendukung array.	
+ File JSON diakhiri dengan ekstensi .json.

XML
+ XML (bahasa markup eXtensible) adalah format independen perangkat lunak-perangkat keras untuk pertukaran data.
+ XML adalah bahasa markup.
+ XML lebih rumit.
+ XML berorientasi pada dokumen.
+ XML tidak mendukung array.
+ File XML diakhiri dengan ekstensi .xml.

HTML
+ HTML adalah singkatan dari Hypertext Markup Language.
+ HTML difokuskan pada penyajian data.
+ HTML didorong oleh format.
+ HTML Case Insensitive.
+ HTML tidak menyediakan dukungan namespaces.
+ HTML tidak strict.
+ HTML memiliki tag yang telah ditentukan sebelumnya.

2. Data delivery sangat penting untuk memungkinkan pertukaran data antara browser dan server tanpa adanya proses pemuatan ulang sebuah halaman. Dari segi pengguna, hal ini memungkinkan Anda untuk mengakses suatu informasi tanpa harus menavigasi kebanyak halaman website.

Cara implementasi:
1. membuat django-app bernama mywatchlist dengan python manage.py startapp wishlist
2. mendaftarkan mywatchlist ke intsalled app
3. membuat skema models untuk perpindahan data
4. mempersiapkan migrasi skema model ke dalam database Django lokal dengan python manage.py makemigrations
5. menerapkan skema model yang telah dibuat ke dalam database Django lokal dengan python manage.py migrate.
6. Menambahkan 10 data untuk objek MyWatchList pada folder fixtures.
7. memasukkan data tersebut ke dalam database Django lokal dengan python manage.py loaddata initial_wishlist_data.json
8. Membuat fungsi yang mengembalikkan mywatchlist.html dan html-html yang lainnya pada views.py
9. pada poin 8, kita juga menambahkan fungsi yang mengembalikkan data dalam bentuk XML dan JSON menggunakan rumus yang telah disediakan pada lab 2.
10. Membuat template mywatchlist dengan ekstensi .html
11. melakukan routing terhadap fungsi views pada urls.py
12. Mendaftarkan juga aplikasi mywatchlist ke dalam urls.py yang ada pada folder project_django dengan menambahkan potongan kode berikut pada variabel urlpatterns
13. 
