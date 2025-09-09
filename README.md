# The Celestial Pitch
Basically I was tasked to make Football Shop related website so might as well make it about game powerups and parkour techs.

## Note About Branches
I only realized I could do this after finishing the second assignment lol.
- main: Where development happens, maybe I will use dev or something later but idk maybe not.
- master: A dummy branch for merging whenever I want to deploy.

## Quick Links
- [Tugas Individu 2](#tugas-individu-2)
- [PWS Deployment](http://muhammad-fahri41-thecelestialpitch.pbp.cs.ui.ac.id)

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

