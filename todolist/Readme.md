Link: https://tugas-2-pbp-abdi.herokuapp.com/todolist/login/


**Apa kegunaan {% csrf_token %} pada elemen form? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen form? **

agar elemen form terlindung dari ancaman dalam bentuk CSRF. CSRF adalah serangan yang membuat user tanpa sadar mengirimkan request bukan ke form tujuan melainkan ke form yang lain yang user mungkin saja tidak ketahui. Form tersebut dapat dimasukkan melalui injeksi kode. Dengan adanya csrf_token maka program akan mengecek token terlebih dahulu sebelum mengirimkannya ke server untuk diproses, diproses atau tidaknya form tersebut tergantung dari validnya token. Jika csrf_token tidak ada maka input user akan rawan diketahui oleh hacker karena bisa jadi inputan merekan masuk ke form yang di injeksi oleh hacker.


**Apakah kita dapat membuat elemen form secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat form secara manual.**

Ya, kita dapat membuat elemen form secara manual tanpa menggunakan generator seperti {{ form.as_table }}.Untuk membuat elemen form secara manual ini dapat menggunakan CSS di mana kita akan mengakses tiap section satu-satu pada atribut-atribut models.

**Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML. **

User akan menulis alamat dari web yang kemudian HTTP request akan digenerate di browser lalu dikirimkan ke server. Server akan menerima request tadi dan akan mencari fungsi views.py mana yang akan menghandle path. Setelah itu halaman form akan dikembalikan ke user dan ditampilkan lewat browser. User akan mengisi form kemudian browser akan generate HTTP request, method, dan arguments ke URL destination dan mengirimkannya ke server. Server menerima request berupa form yang sudah diisi kemudian server akan mengecek dan mencari views.py mana yang akan menghandle atau memprosesnya. Setelah itu, akan digenerate halama HTML yang kemudian akan di display ke user.

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**

1. membuat django-app bernama mywatchlist dengan python manage.py startapp todolist
2. mendaftarkan todolist ke installed app serta mendaftarkan url-nya di prodject_django agar bisa diakses. melakukan routing terhadap fungsi views pada urls.py
3. membuat skema models untuk perpindahan data.
4. mempersiapkan migrasi skema model ke dalam database Django lokal dengan python manage.py makemigrations.
5. menerapkan skema model yang telah dibuat ke dalam database Django lokal dengan python manage.py migrate.
6. Membuat fungsi yang mengembalikkan todolist.html dan html-html yang lainnya pada views.py.
7. Fungsi2 tersebut ada 5 fungsi yakni show_todolist, register, login_user, logout_user, add_task
8. Membuat template todolist dengan ekstensi .html serta template untuk form registrasi, login, dan add_task agar pengguna dapat menggunakan todolist dengan baik.
9. Deploy ke Heroku serta mendaftarkan 2 akun dan setiap akun menambahkan 3 task.
