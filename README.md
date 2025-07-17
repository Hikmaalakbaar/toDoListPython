📝 To-Do List CLI Python
Program sederhana berbasis terminal (CLI) untuk mencatat, menandai, dan menghapus daftar tugas. Data disimpan ke dalam file todo.txt.

🔧 Fitur
✅ Menambahkan tugas baru

📋 Melihat seluruh daftar tugas

✔️ Menandai tugas sebagai selesai

🗑 Menghapus tugas dari daftar

🕒 Menyimpan waktu saat tugas ditambahkan

🎨 Menampilkan teks berwarna di terminal dengan colorama

💾 Penyimpanan data otomatis ke file todo.txt

🚀 Cara Menjalankan
Clone atau buat file Python baru:

Simpan sebagai todo_cli.py.

Install library yang dibutuhkan:

bash
Salin
Edit
pip install colorama
Jalankan program:

bash
Salin
Edit
python todo_cli.py
🧠 Struktur Kode
Fungsi	Deskripsi
load_todos()	Membaca isi file todo.txt dan mengembalikannya sebagai list.
save_todos(todos)	Menyimpan list tugas ke dalam todo.txt.
show_menu()	Menampilkan menu utama pilihan pengguna.
main()	Fungsi utama yang menangani logika input dan eksekusi fitur.

📁 Format Penyimpanan
Tugas disimpan dalam file todo.txt dengan format seperti berikut:

scss
Salin
Edit
[ ] Belajar Python (ditambahkan 2025-07-16 19:30:20)
[x] Cuci motor (ditambahkan 2025-07-15 16:00:12)
[ ] menandakan tugas belum selesai

[x] menandakan tugas sudah selesai

Timestamp menunjukkan kapan tugas ditambahkan

🧪 Contoh Output Program
markdown
Salin
Edit
=== TO-DO LIST ===
1. Tambah Tugas
2. Lihat Semua Tugas
3. Tandai Tugas Selesai
4. Hapus Tugas
5. Keluar
Pilih menu:
💡 Tambahan Opsional (Pengembangan Selanjutnya)
Filter hanya tugas yang belum selesai

Fitur pencarian tugas

Export ke format .csv atau .json

Tampilan GUI (Tkinter / PyQt)

Sinkronisasi ke cloud (Firebase atau Google Sheets)

👨‍💻 Dibuat oleh
Hikmal Akbar
Mahasiswa Teknik Informatika – STIKOM Poltek Cirebon
