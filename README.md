nama   : Dikdik Hidayatulloh 
Nim    : 241011450246
matkul : UAS struktur data 
Sistem Manajemen Perpustakaan Digital

Aplikasi Web Perpustakaan berbasis `Streamlit` yang mengimplementasikan 6 Struktur Data + 4 Algoritma Sorting + 2 Algoritma Searching dalam 1 dashboard.

Fitur: `Login, CRUD, Import/Export CSV, Auto Reset Form`

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

1. Fitur Utama

| Menu | Struktur Data | Deskripsi |
| --- | --- | --- |
| **Kelola Buku** | `Single Linked List` + `BST` | CRUD Buku. Tambah, Tampil, Edit, Hapus. Auto validasi ID >= 1. Import/Export CSV. |
| **Peminjaman** | `Queue` + `Circular Single` | Sistem antrian FIFO. Buku yang dipinjam masuk ke `Buku Favorit`. |
| **Pengembalian** | `Double Linked List` | Proses antrian teratas. Riwayat tersimpan 2 arah. |
| **Searching** | `Linear Search`, `Binary Search` | Cari buku by Judul. Binary wajib data sorted dulu. |
| **Sorting** | `Bubble, Selection, Merge, Quick Sort` | Urutkan buku berdasarkan Judul A-Z. |
| **Tree** | `Binary Search Tree by ID` | Cari buku O(log n) by ID. Tampilkan Traversal: Inorder, Preorder, Postorder. |
| **Laporan** | Semua Digabung | Lihat total buku, daftar buku, antrian, riwayat, favorit, rekomendasi. Ada tombol `Reset Data`. |

Fitur UX Tambahan
1.  **Sistem Login**: `admin` / `admin123`. Session aman.
2.  **Form Auto Kosong**: Form `Tambah` auto reset setelah submit pake `form_key`.
3.  **Validasi Ketat**: ID harus angka >= 1. Anti duplikat ID. Anti input kosong.
4.  **Import/Export CSV**: Backup dan restore data buku dengan 1 klik.

2. Struktur Data yang Digunakan

Proyek ini dibuat untuk memenuhi tugas Struktur Data.

1.  `Single Linked List`: Penyimpanan utama semua data buku `inventaris`.
2.  `Double Linked List`: Menyimpan `riwayat pengembalian` biar bisa bolak-balik.
3.  `Queue`: Sistem `antrian peminjaman` FIFO. First In First Out.
4.  `Circular Single Linked List`: Daftar `Buku Favorit` yang melingkar.
5.  `Circular Double Linked List`: Daftar `Rekomendasi Buku` melingkar 2 arah.
6.  `Binary Search Tree`: Index pencarian cepat by `ID Buku`.

3. Algoritma yang Diimplementasikan

1.  **Searching**: `Linear Search O(n)` untuk substring, `Binary Search O(log n)` untuk exact match.
2.  **Sorting**: `Bubble Sort O(n^2)`, `Selection Sort O(n^2)`, `Merge Sort O(n log n)`, `Quick Sort O(n log n)`.

4. Cara Install & Menjalankan

Requirement
```bash
pip install streamlit pandas
Jalankan Lokal
1.  Save code di atas jadi `app.py`
2.  Buka terminal di folder yang sama
streamlit run app.py
3.  Buka `http://localhost:8501`

Login Default
Username: admin
Password: admin123
Deploy ke Streamlit Cloud
1.  Upload `app.py` ke repo Github
2.  Hubungkan ke http://share.streamlit.io
3.  `Main file path`: `app.py`

5. Format File CSV untuk Import

Kolom wajib: `ID`, `Judul`, `Penulis`, `Tahun`
ID,Judul,Penulis,Tahun
1,Dasar Pemrograman Python,Budi Raharjo,2023
2,Struktur Data dan Algoritma,Rinaldi Munir,2024
Note: `ID` yang duplikat akan di-skip saat import.

6. Penjelasan Teknis Penting
Masalah	Solusi di Code
`TypeError` pas Binary Search	`binary_search` return `[]` bukan `None`. Jadi aman di-loop `for b in hasil`.
`KeyError: username`	`st.session_state.get('username', 'Admin')` + set `""` pas logout.
`DeltaGenerator` nongol	Tidak pakai `ternary 1 baris`. Semua pake `if else` blok.
`Form tidak kosong`	`st.form(f"form_{key}", clear_on_submit=True)` + `st.session_state.form_key += 1`
7. Struktur Folder
/
└── app.py          # File utama aplikasi
└── README.md       # File ini
8. Roadmap v22
- [ ] Fitur Edit & Hapus Multi Buku
- [ ] Grafik Jumlah Buku per Tahun 
- [ ] Role Admin & Petugas
- [ ] Simpan ke Database SQLite biar data tidak hilang pas rerun


Dibuat untuk UAS Struktur Data.
