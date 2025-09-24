# The Celestial Pitch
Basically I was tasked to make Football Shop related website so might as well make it about game powerups and parkour techs.

## Note About Branches
I only realized I could do this after finishing the second assignment lol.
- main: Where development happens, maybe I will use dev or something later but idk maybe not.
- master: A dummy branch for merging whenever I want to deploy.

## Quick Links
- [Tugas Individu 4](#tugas-individu-4)
- [Tugas Individu 3](#tugas-individu-3)
- [Tugas Individu 2](#tugas-individu-2)
- [PWS Deployment](http://muhammad-fahri41-thecelestialpitch.pbp.cs.ui.ac.id)

## Tugas Individu 4
### Step by Step Implementation Checklist
#### 1. Mengimplementasikan login, logout, dan register
- Buat routing untuk masing-masing fungsionalitas
- Gunakan `UserCreationForm` dari contrib django untuk membuat registrasi user sederhana, penggunaannya mirip dengan form lain
- Gunakan `AuthenticatonForm` untuk data login, dan gunakan fungsi `login` untuk menginisialisasi session user
- Fungsi login menggunakan django sessions untuk menyimpan data session user
- Gunakan `logout` dari contrib django untuk logout
- Tambahkan `@login_required(login_url='/login')` untuk rute yang memerlukan autentikasi

### Membuat 2 Akun Pengguna dengan Masing-Masing 3 Dummy Data
- Buat akun melalui laman registrasi
- Login akun
- Daftarkan produk

### Menghubungkan Model Product dengan User
- Tambahkan field `admin` (di sini hanya user biasa) untuk menandakan admin yang menambah katalog produk
- Gunakan `User` dari contrib django dan `models.ForeignKey` untuk menambahkan sebuah relasi pada model lain.
- Untuk `models.ForeignKey`, wajib menambahkan opsi `on_delete` dikarenakan Foreign Key tidak boleh dangling jika reference dihapus
- Di sini saya gunakan `models.SET_NULL` agar jika akun admin dihapus, katalog tetap ada tetapiadmin pembuatnya tidak lagi direferensi (menjadi NULL)

### Menampilkan Detail Informasi Pengguna Yang Sedang Logged In
- Gunakan `request.get_user()` untuk mendapatkan `User` object
- Akses atribut seperti `username` dengan `user.username`, lalu terapkan akses ini ke dalam template
- Perhatikan bahwa atribut `password` tidaklah menyimpan password sebenarnya, melainkan password yang sudah di hash dengan salt, dan pada SQLite yang saya coba menggunakan pbkdf2.

### Menggunakan dan Menampilkan Cookie
- Gunakan `response.set_cookie` untuk men-set value-parameter pair pada cookie
- Gunakan `request.COOKIES.get` untuk mengambil nilai dari cookie
- Cookie pada dasarnya adalah dictionary biasa disimpan dalam plaintext

## Django AuthenticationForm, Kelebihan, dan Kekurangannya
Django `AuthenticationForm` adalah salah satu `Form` builtin django yang dapat digunakan untuk quick startup model autentikasi. Kelebihannya adalah sangat cepat dan mudah untuk di-setup, terintegrasi langsung dengan `authenticate` backend, dan cukup informatif. Kekurangannya adalah fleksibilitas yang kecil (hanya sebagai quick startup) dibanginkan form yang lebih kompleks misal penambahan captcha atau penggunaan login option lain (seperti SSO, mail, google, dll., tetapi harus didukung backend).

## Apa Perbedaan Autentikasi dan Otorisasi serta Cara Django Mengimplementasikannya
Autentikasi menjamin bahwa user adalah user yang valid (bukan orang lain) dengan standar yang wajar (user diwajibkan menjaga passwordnya sendiri). Otorisasi menjamin bahwa user yang melakukan suatu aksi memiliki izin untuk melakukan aksi tersebut. Pada django, otorisasi terikat dengan `User` class (atau dapat juga di extend), di mana pemberian otorisasi mirip ACL (Access control list). Setiap user diberi akses untuk aksi-aksi tertentu, termasuk akses untuk menggunakan akses yang disediakan suatu grup-grup tertentu. Dengan model ini, akses dapat ditentukan secara individual melalui user maupun secara massal melalui grup.

## Apa Saja Kelebihan dan Kekurangan Session dan Cookies Dalam Menyimpan State Dalam Web
Session artinya server melacak data-data yang berkaitan sebuah session identifier (umumnya disimpan pada cookie), sehingga server dapat mengingat detail user yang sedang log in tanpa memberi kewenangan bagi client untuk mendikte apa yang dapat ia lakukan. Cookie adalah storage yang disimpan oleh browser, berupa key-value pair, dikirimkan kembali ke server setiap request, dan isinya beragam tergantung keperluan dari server. Kelebihan session adalah server dapat menentukan data apa saja yang bersangkutan dengan session id tertentu, misalnya akses kontrol yang diperbolehkan untuk suatu user. Kekurangannya adalah server harus mengetahui data yang berkaitan dengan session id sehingga parallelisme dapat terbatas. Cookie lebih generik, kelebihannya dapat digunakan untuk apa saja dan selalu diberikan oleh browser sehingga dapat menyimpan data non-sensifit seperti opsi darkmode dan setting. Kekurangannya adalah cookie dapat dirubah oleh user sehingga tidak dapat diandalkan untuk hal-hal sensitif.

## Apakah Penggunaan Cookies Aman Secara Default, Bagaimana Django Menanggapinya
Cookies memiliki beberapa bahaya seperti penyimpanan plaintext yang dapat dimanipulasi oleh user. Selain itu karena cookie secara otomatis di-attach oleh browser untuk setiap request pada domain tertentu, maka website malicious dapat memanfaatkan cookie yang tersimpan untuk berpura-pura sebagai user yang log in. Django menangani ini dengan menggunakan session cookie yang hanya sebagai penanda session dan tidak bisa dibruteforce, serta penerapan csrf untuk menghindari cookie digunakan sebagai alat autentikasi tanpa consent pengguna.

## Tugas Individu 3
### Step by Step Implementation Checklist
#### 1. Menambahkan Fungsi views Baru untuk Melihat Semua Object dan Object by ID Dalam Bentuk XML dan JSON
- Import `Product` dari `main.models` serta method-method lain yang digunakan
- Ambil keseluruhan product dengan `Product.objects.all()`, di sini `Product.objects` mengimplementasikan `QuerySet` dan `.all()` mengembalikan semua objek
- Jika diminta id tertentu, dapat menggunakan `get_object_or_404(Product, pk=id)`, tetapi di sini saya gunakan `Product.objects.get(pk=id)` untuk mengembalikan satu elemen yang cocok
- Gunakan `serializers.serialize('xml', product_list)` untuk mengubah data menjadi string xml, ubah menjadi json jika diminta dalam bentuk json, dan wrap dalam list jika hanya satu object
- Return `HttpResponse` dengan `content_type='application/xml'` untuk xml dan `content_type='application/json'` untuk json

#### 2. Menambahkan Routing URL untuk Masing-Masing views
- Tambahkan URL baru untuk setiap views seperti URL routing yang lain
- Untuk query yang menggunakan id, dapat menggunakan `<uuid:id>` dalam URL path
- id merujuk pada nama parameter pada fungsi views

#### 3. Membuat Halaman Data Objek Model
- Adaptasi dari tutorial 2
- Ubah `news_list` menjadi `product_list`, 'news' menjadi 'product', `News` menjadi `Product`, hilangkan `is_news_hot`, serta rename beberapa field seperti `title` menjadi `name`
- Template di sini menggunakan tag `if`, `else`, `for` untuk mengintegrasikan dengan data dari django
- Tombol `add` dan `detail` menggunakan tag `url` dan diisi reverse url dengan `app_name=<app>` serta `path(url, name=<func_name>)` dinyatakan sebagai `<app>:<func_name>`

#### 4. Membuat Halaman Form untuk Menambahkan Objek
- Adaptasi dari tutorial 2
- Hampir persis sama kecuali dua nama display

#### 5. Membuat Halaman yang Menampilkan Detail dari Objek
- Adaptasi dari tutorial 2
- Ubah 'news' menjadi 'product'
- Hilangkan field yang tidak ada (is_news_hot)
- Rename field yang direpresentasikan dengan nama berbeda (title menjadi nama, thumbnail menjadi icon, content menjadi description)
- Tambahkan field yang belum ada (base_price)
- Tombol "Back to Product List" menggunakan tag `url` yang juga menggunakan reverse url django]

### Mengapa Diperlukan Data Delivery dalam Implementasi Platform
Data delivery artinya transfer data antara satu tempat ke tempat yang lain, umumnya dengan platform/framework yang berbeda.
Contohnya adalah django dengan javascript, atau django dengan external tools.
Tanpa data delivery, platform/framework yang berbeda tidak dapat berkomunikasi satu sama lain.
Tentu saja tanpa data yang lengkap, komputasi tidak dapat dilakukan, sehingga data delivery (misal json data melalui HTTP) diperlukan.

### Perbandingan XML dan JSON
Menurut saya XML dan JSON memiliki kegunaannya sendiri tergantung konteks.
Untuk game modding atau konfigurasi ekstensif XML umumnya lebih ekspresif.
Di sisi lain JSON lebih mudah dicerna, serta terintegrasi dengan javascript.
Integrasi langsung dengan javascript adalah alasan utama JSON lebih umum ditemukan dalam ekosistem web.
Untuk ekosistem selain web, kepopuleran JSON dikarenakan umumnya dan sederhananya JSON.
Meskipun begitu terdapat juga menggunakan XML, TOML, atau bahkan penyimpanan custom seperti line by line atau key-value pair.

### Fungsi dari Method is\_valid()
Fungsi ini mengecek form yang diisi sudah sesuai dengan ketentuan.
Pertama dicek apakah data dapat diubah menjadi python type (karena jika menggunakan external tools, misal `curl`, dapat saja data tidak valid).
Lalu data dicek terhadap aturan untuk field tersebut, mungkin terhadap kategori, terhadap `uuid`, atau cek custom.
Setelahnya, jika ada, semua field akan digabungkan dan dicek validitasnya sebagai suatu entitas utuh.
Jika ada data yang tidak seharusnya, maka fungsi ini akan bernilai `False` dan error akan disimpan pada `form.errors`.
Tanpa validasi sebelum `.save`, maka data akan langsung disimpan di database.
Hal ini berbahaya karena database bisa saja tidak menerapkan constraint dengan benar atau terdapat constraint tambahan pada form yang melewati cek yang seharusnya.

### Mengapa CSRF Token Dibutuhkan
`csrf_token` digunakan untuk mencegah CSRF (Cross-Site Request Forgery) di mana website malicious menggunakan cookies dari user untuk mencoba melakukan request yang tidak seharusnya.
Misalnya saja dapat membuat user yang sedang logged in memesan barang tertentu tanpa sepengetahuan user.
Hal ini terjadi karena cookie dapat dikirimkan oleh browser untuk suatu domain tujuan, terlepas dari origin yang melakukan request.
Dengan CSRF token (setiap form dan setiap user berbeda), malicious website ini tidak bisa menebak `csrf_token` yang benar.
Dengan CORS yang benar (`Access-Control-Allow-Origin` bukan `*`, by default sudah benar), browser tidak memperbolehkan website malicious membaca response (termasuk `csrf_token`) dari website asli.
Tanpa CSRF token yang benar, server akan menolak request dari malicious website tersebut.
By default, jika tidak menerapkan `csrf_token` pada Django, form akan selalu ditolak oleh server.
Selain `csrf_token`, Django juga menggunakan `CSRF_TRUSTED_ORIGINS` untuk memastikan request bukan CSRF.

### Screenshot POSTMAN
![XML Product List](https://i.imgur.com/LQXFteM.png)
![JSON Product List](https://i.imgur.com/jJSrtWE.png)
![XML Product by ID](https://i.imgur.com/8Lsjsty.png)
![JSON Product by ID](https://i.imgur.com/L1UHiat.png)

## Tugas Individu 2
### Step by Step Implementation Checklist
#### 1. Membuat Sebuah Proyek Django Baru
- Copy-paste dulu `requirements.txt` dan file-file environment dari tutorial-0
- Jangan lupa buat virtual environment dengan `python3 -m venv env` dan nyalakan dengan `source env/bin/activate.fish` (kalau tidak menggunakan fish shell, cari sendiri cara aktivasinya)
- Jalankan `django-admin startproject the_celestial_pitch .`
- Di sini `the_celestial_pitch` adalah nama proyeknya dan `.` artinya buat pada directory yang sama

#### 2. Membuat Aplikasi Main Pada Proyek Tersebut
- Jalankan `./manage.py startapp main`
- Command tersebut membuat aplikasi baru bernama main
- Jangan lupa tambahkan `main` pada list `INSTALLED_APPS` pada `the_celestial_pitch/settings.py`

#### 3. Melakukan Routing Pada Proyek Agar Dapat Menjalankan Aplikasi Main
- Tambahkan `from django.urls import path, include` pada `the_celestial_pitch/urls.py`
- Lalu, tambahkan `path('', include('main.urls')),` pada list urlpatterns pada file `the_celestial_pitch/urls.py`
- Hal ini akan me-redirect semua request yang bukan berawalan admin ke pada main

#### 4. Membuat Model Pada Aplikasi Main
- Dalam `main/models.py` tambahkan class `Product(models.Model)`, lalu tambahkan atribut sesuai kebutuhan dan optional parameter sesuai kebutuhan
- Jika menggunakan optional parameter `choices`, dapat diberikan iterable dengan masing masing 2 elemen yang merepresentasikan internal representation dan human readable format
- Kebanyakan dari opsi-opsi optional parameter sudah ditunjukkan pada tutorial-1

#### 5. Membuat Fungsi Pada views.py Untuk Menampilkan Template
- Dalam `main/views.py`, cukup buat sebuah fungsi (di sini `show_index`) yang menerima sebuah request dan me-return sebuah HttpResponse.
- Untuk template sederhana cukup gunakan hardcoded dictionary sebagai context, lalu berikan pada fungsi `render`
- `show_index` sekarang akan me-return `render(request, 'index.html', context)`
- Jangan lupa untuk membuat template file html pada `main/templates/index.html`, dan masukkan `{{ var_name }}` sebagai nilai yang butuh diganti oleh templating libary django

#### 6. Membuat Sebuah Routing Pada urls.py Untuk Memetakan views.py
- Buatlah file `main/urls.py`, dan tambahkan `app_name = 'main'` serta `url_patterns = [path('', views.show_index, name='index']`
- Jangan lupa untuk mengimport file dan module yang dibutuhkan, `from django.urls import path` dan `import main.views as views`
- `app_name` akan men-setting namespace menjadi `main` untuk reverse url (whatever that is)
- `path` menambahkan sebuah entry pada routing di mana `/` (no path) akan menampilkan `index.html`
- Jika pada `the_celestial_pitch/urls.py` sebelumnya include main menggunakan path lain, maka path lain itulah yang menjadi url `index.html`

#### 7. Melakukan Deployment Pada PWS
- Buat sebuah project pada PWS lalu simpan password projectnya dan setup environment variable
- Pastikan `the_celestial_pitch/settings.py` siap untuk deployment (DATABASES, DEBUG, INSTALLED_APPS, ALLOWED_HOSTS, dan lainnya), mengacu pada setup tutorial-0
- Push branch master pada PWS
- Pray

### Bagan Request Client
![Bagan](https://i.imgur.com/HGT0xXh.png)

### Peran settings.py Pada Django
Peran `settings.py` pada umumnya untuk mensetting variabel-variabel global yang digunakan oleh engine Django secara keseluruhan.
Hal-hal seperti debug mode, database url, url-url template dan static, allowed hosts, dan berbagai macam miscellaneous lainnya.
Variabel seperti allowed hosts mencegah miskonfigurasi host header processing dari meretas sistem.
Debug mode memudahkan untuk debugging permsalahan saat development tapi dapat digunakan sebagai oracle untuk hacker pada deployment.

### Cara Kerja Migration di Django
Migration adalah proses perubahan schema pada sebuah database.
Untuk migration yang tidak menambahkan non nullable field, column akan ditambahkan secara normal.
Jika table belum ada maka table akan dibuat.
Untuk migration yang lebih kompleks, berkemungkinan membutuhkan aturan migrasi yang dibuat manual.
Untuk migration automatis cukup jalankan `./manage.py makemigrations && ./manage.py migrate`.

### Mengapa Django Dijadikan Permulaan Pengembangan Perangkat Lunak
Django merupakan framework yang memiliki banyak sekali tools yang disertakan by default.
Tidak perlu menggunakan SQL query secara manual karena terdapat Django models.
Tidak perlu menambahkan logika parsing dan response HTTP rumit karena kebanyakan sudah di handle oleh Django.
Tidak perlu menambahkan logika templating sendiri karena templating engine sudah disertakan oleh Django.
Ditulis menggunakan bahasa python yang sangat mudah dibaca.

