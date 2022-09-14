link: https://tugas-2-pbp-abdi.herokuapp.com/

![image](https://user-images.githubusercontent.com/87772747/190173028-3c193c1f-e53c-4818-9278-6e7a05fef80f.png)
Penjelasan:
User melakukan request ke internet yang diteruksan ke server django, Request yang masuk akan diolah oleh urls.py kemudian diteruskan ke views.py berdasarkan keinginan dari pengguna. views.py akan mengecek apakah perlu mengakses database atau tidak. jika dibutuhkan, maka views.py akan mengirim query pada models.py lalu database akan mengirimkan query yang sesuai ke views.py melalu models.py. query-query tersebut akan ditampilkan melalui template html yang telah disediakan. html tersebut akan dikembalikan ke user sebaga web page yang akan ditampilkan pada layar komputer/laptop.

Virtual environtment dibutuhkan agar sistem yang dijalankan terisolasi. Sehingga command command yang diberikan pada cmd tidak akan merubah configuration dari system operasi yang terpakai. Kita tetap bisa menjalankan web tanpa menggunakan virtual environtment akan tetapi bakal rawan terjadi configuration pada sistem operasi.

Cara Implementasi Tugas 2:
1. Setelah cloning repositori yang disediakan, maka langsung saja mebuat fungsi yang menerima parameter request dan mengembalikan render(request, "katalog.html", context), karena app katalog juga sudah tersedia.
2. Membuat routing pada urls.py sehingga halaman html dapat ditampilkan pada browser serta mendaftarkan aplikasi katalog pada folder prodject_django agar bisa diakses nantinya.
3. Pada views.py, masukkan fungsi yang memanggil query ke model database dan menyimpan hasil query tersebut ke dalam sebuah variabel seperti list_katalog, nama, npm dll
4. Lalu, masuk ke template html yang disediakan mengubah variabel-variabel yang nantinya akan ditampilkan seperti nama, npm dll. Pada template juga memasukkan program looping yang akan mengakses method-method yang ada pada models.py seperti atribut item_name, item_price, dll.
5. Setelah melakukan migrasi, loaddata .json yang sudah disediakan lalu melakukan push ke repositori github.
6. Setelah itu, buat aplikasi pada web heroku lalu copy API KEY dan nama aplikasi tersebut.
7. Ke github bagian settings, cari secrets dan pilih actions,Create new secret repository (2 secret repo), yang satu HEROKU_API_KEY isinya api key yang bisa dilihat di account settings heroku. Satunya lagi HEROKU_APP_NAME isinya nama aplikasi yang dibuat di Heroku, pergi ke actions di repo github klik yang masih failed, trus re-run all jobs, Tunggu aja sampai ada centang hijau, trus buka aplikasi lu lewat link https://tugas-2-pbp-abdi.herokuapp.com/
