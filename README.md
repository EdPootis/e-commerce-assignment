<b>Edmond Christian / 2306208363 / PBP D </b>

<br></br>
<b>Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step</b>

1. Membuat folder dengan nama project saya di komputer dan menyambungkannya dengan git.
2. Membuat repository kosong di github.
3. Melakukan commit dan push folder komputer ke dalam github untuk menyambungkan kedua git.
4. Membuat dan mengaktifkan virtual environment dengan 'python -m venv env' kemudian 'env\Scripts\activate'.
5. Menginstall library Django dan library lain yang diperlukan dengan membuat 'requirements.txt' dan menjalankan 'pip install -r requirements.txt'.
6. Membuat project Django dengan 'django-admin startproject the_eh_toko .' dan mengkonfigurasikan localhost ke dalam allowed host di 'settings.py'.
7. Mengecek apakah project berhasil terbuat dengan 'python manage.py runserver'.
8. Membuat file '.gitignore' untuk membatasi file-file yang akan dipush ke github.
9. Melakukan initial commit dan push project ke github.
10. Membuat aplikasi 'main' dalam project dengan 'python manage.py startapp main' dan menambahkannya ke dalam 'INSTALLED_APPS' di 'settings.py'.
11. Membuat template 'main.html' dan mengisinya dengan teks mengenai e-commerce yang dibikin dan produknya.
12. Membuat model 'Product' dan melakukan migrasi  dengan 'python manage.py makemigrations' dan 'python manage.py migrate'.
13. Menambahkan fungsi pada 'views.py' untuk mengembalikan 'context' yang akan mengisi nilai variabel pada 'main.html'.
14. Mengkonfigurasi routing project sehingga 'main.html' muncul.
15. Melakukan push ke github.
16. Membuat project baru pada website PWS (Pacil Web Service).
17. Menambahkan 'edmond-christian31-ecommerceassignment.pbp.cs.ui.ac.id' ke dalam allowed host project.
18. Menghubungkan project dengan PWS sesuai dengan panduan websitenya. 
19. Melakukan push terhadap branch pws dengan 'git push pws master'.
20. Menunggu proses building project oleh PWS dan setelah selesai project dapat diakses melalui http://edmond-christian31-ecommerceassignment.pbp.cs.ui.ac.id/
(Setiap langkah tersebut tidak saya lakukan sekaligus, melainkan dalam beberapa sesi. Untuk setiap sesi saya mulai dengan 'env\Scripts\activate' dan akhiri dengan 'deactivate')
20. Setelah project dapat terlihat dan benar, saya menambahkan gambar salah satu produk ke dalam 'main.html'
21. Penambahan gambar dilakukan dengan membuat folder baru '/static' pada folder aplikasi 'main', kemudian memasukan gambar ke dalam folder tersebut.
22. Pada 'main.html' saya menambahkan '{% load static %}' di awal dokumen agar gambar di folder '/static' dapat ditemukan
23. Lalu saya juga mengganti beberapa teks dan formatting pada 'main.html'
24. Terakhir saya melakukan push terhadap github dan WPS. (Pada website WPS, project mungkin belum menampilkan tampilan terbaru sebab build yang gagal)

<br></br>
<b>Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara 'urls.py', 'views.py', 'models.py', dan berkas 'html'.</b>

<img src="main/static/DjangoDiagram.png">

<br></br>
<b>Jelaskan fungsi git dalam pengembangan perangkat lunak!</b>
Git merupakan sebuah software version control, yang berarti git berfungsi untuk memanajemen perubahan suatu kode software. Pada pengembangan software tentunya akan terjadi banyak perubahan kode software, dengan git seseorang dapat menyimpan suatu versi dari softwarenya. Jika pengembang software tersebut ingin melakukan perubahan kode tanpa mengganti kode yang sekarang ia dapat membuat berbagai branch baru untuk melakukan testing dll., dan ia juga dapat kembali ke branch utama jika ingin melakukan hal yang berbeda. Dengan branching ini, lebih dari satu orang juga dapat bekerja pada suatu project atau aplikasi yang sama tanpa mengganggu satu sama lain yang di mana jika ingin dilakukan perubahannya perlu dimerge. Fungsi yang terakhir adalah, git dapat berperan sebagai backup jika kode utama memiliki kesalahan ataupun ingin kembali ke kode yang awal. Jadi fungsi git dalam pengembangan software secara singkat adalah meningkatkan efisiensi pengembangan software, memungkinkan kolaborasi dalam pengembangan software, dan sebagai backup versi software.

<br></br>
<b>Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?</b>
Menurut saya, karena Django merupakan framework yang populer (sehingga terdapat banyak resource mengenainya) dan cukup mudah dipahami karena menggunakan Python sebagai bahasa utamanya. Python merupakan bahasa yang telah dipelajari pada DDP1 dan merupakan bahasa pemrograman yang relatif lebih mudah dari bahasa pemrograman lain sehingga akan memudahkan kita dalam mempelajari Django. Selain itu, ada juga alasan lain mengapa Django dipilih yang awalnya saya tidak diketahui, seperti tertulis pada slide materi contohnya Django bersifat open source, cepat, sangat scalable, dan seterusnya.

<br></br>
<b>Mengapa model pada Django disebut sebagai ORM?</b>
Django disebut sebagai ORM (Object Relational Mapping) karena Django menyimpan data sebagai objek di Python, yang kemudian objek-objek tersebut yang berupa data dapat dipetakan terhadap tabel-tabelnya pada sebuah relational database umumnya seperti SQL. Selanjutnya, jika ingin mengolah atau melakukan hal terkait database dapat dilakukan menggunakan prinsip OOP (Object Oriented Programming) pada datanya.