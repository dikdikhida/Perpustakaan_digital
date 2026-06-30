import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="Sistem Perpustakaan", layout="wide", initial_sidebar_state="expanded")

CSS = """
<style>
    /* 1. Hide semua toolbar Streamlit Cloud */
    [data-testid="stHeader"], [data-testid="stToolbar"], header,
    [data-testid="stFooter"], footer, [data-testid="stDecoration"],
    div[class*="stDeployButton"] {display: none!important;}

    /* 2. Layout full ke atas */
   .block-container {padding-top: 1rem!important;}

    /* 3. Theme Kuning Hitam */
   .stApp { background-color: #FFD700; }

    @keyframes fadeInUp {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }

   .login-card { animation: fadeInUp 0.6s ease-out; }

    html, body, [class*="st-"], label, p, div, span, h1, h2, h3, h4, h5, h6,
   .stMarkdown,.stTextInput label,.stNumberInput label {
        color: #000!important; font-weight: 600;
    }

   .login-box,.stTabs [data-baseweb="tab-panel"],.stForm,.stExpander,
    div[data-testid="stVerticalBlock"] > div > div {
        background-color: #FFF0A0; border: 2px solid #000; border-radius: 10px; padding: 20px;
    }

   .login-box * { color: #000!important; }
    input, div[data-baseweb="input"] > div, div[data-baseweb="select"] > div, textarea {
        background-color: #FFFFFF!important; color: #000!important; border: 2px solid #000!important;
    }
    input::placeholder { color: #555!important; }

    [data-testid="stSidebar"] { background-color: #F0C000; border-right: 2px solid #000; }
    [data-testid="stSidebar"] * { color: #000!important; font-weight: 700; }

   .stButton > button { background-color: #000; color: #FFD700!important; border: 2px solid #000; border-radius: 6px; font-weight: 800; }
   .stButton > button:hover { background-color: #FFD700; color: #000!important; }

   .stTabs [aria-selected="true"] { border-bottom: 3px solid #000!important; }
   .stTabs [aria-selected="true"] p { color: #000!important; font-weight: 800; }
   .stTabs [aria-selected="false"] p { color: #444!important; }

   .stDataFrame,.stDataFrame * { color: #000!important; border-color: #000!important; }
   .stAlert { background-color: #FFF0A0; border: 2px solid #000; color: #000!important; }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

def check_login():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        st.markdown("<h1 style='text-align: center;'>Sistem Perpustakaan</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Silakan Login</p>", unsafe_allow_html=True)
        st.markdown("<div class='login-card'>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("<div class='login-box'>", unsafe_allow_html=True)
            with st.form("login_form"):
                username = st.text_input("Username")
                password = st.text_input("Password", type="password")
                if st.form_submit_button("Login", use_container_width=True):
                    if username == "admin" and password == "admin123":
                        st.session_state.logged_in = True
                        st.session_state.username = username
                        st.rerun()
                    else:
                        st.error("Username atau Password Salah!")
            st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        st.stop()

class Buku:
    def __init__(self, id_buku, judul, penulis, tahun):
        self.id = id_buku
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def to_dict(self):
        return {"ID": self.id, "Judul": self.judul, "Penulis": self.penulis, "Tahun": self.tahun}

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def kosong(self):
        return self.head is None

    def tambah_buku(self, buku):
        node = Node(buku)
        if self.kosong():
            self.head = node
        else:
            bantu = self.head
            while bantu.next:
                bantu = bantu.next
            bantu.next = node

    def to_list(self):
        data, bantu = [], self.head
        while bantu:
            data.append(bantu.data)
            bantu = bantu.next
        return data

    def cari_id(self, id_buku):
        bantu = self.head
        while bantu:
            if bantu.data.id == id_buku:
                return bantu.data
            bantu = bantu.next
        return None

    def hapus(self, id_buku):
        sekarang, sebelum = self.head, None
        while sekarang:
            if sekarang.data.id == id_buku:
                if sebelum is None:
                    self.head = sekarang.next
                else:
                    sebelum.next = sekarang.next
                return True
            sebelum, sekarang = sekarang, sekarang.next
        return False

    def edit(self, id_buku, judul, penulis, tahun):
        buku = self.cari_id(id_buku)
        if buku:
            buku.judul, buku.penulis, buku.tahun = judul, penulis, tahun
            return True
        return False

class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        baru = DNode(data)
        if self.head is None:
            self.head = baru
            return
        bantu = self.head
        while bantu.next:
            bantu = bantu.next
        bantu.next = baru
        baru.prev = bantu

    def to_list(self):
        data, bantu, no = [], self.head, 1
        while bantu:
            data.append(f"{no}. {bantu.data}")
            bantu = bantu.next
            no += 1
        return data

class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def kosong(self):
        return self.front is None

    def enqueue(self, data):
        baru = QueueNode(data)
        if self.kosong():
            self.front = baru
            self.rear = baru
        else:
            self.rear.next = baru
            self.rear = baru

    def dequeue(self):
        if self.kosong():
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data

    def to_list(self):
        data, bantu, no = [], self.front, 1
        while bantu:
            data.append(f"{no}. {bantu.data}")
            bantu = bantu.next
            no += 1
        return data

class CSNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSingle:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        baru = CSNode(data)
        if self.head is None:
            self.head = baru
            baru.next = baru
        else:
            bantu = self.head
            while bantu.next!= self.head:
                bantu = bantu.next
            bantu.next = baru
            baru.next = self.head

    def to_list(self):
        if not self.head:
            return []
        data, bantu, no = [], self.head, 1
        while True:
            data.append(f"{no}. {bantu.data}")
            bantu = bantu.next
            no += 1
            if bantu == self.head:
                break
        return data

class CDNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDouble:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        baru = CDNode(data)
        if self.head is None:
            self.head = baru
            baru.next = baru
            baru.prev = baru
        else:
            tail = self.head.prev
            tail.next = baru
            baru.prev = tail
            baru.next = self.head
            self.head.prev = baru

    def to_list(self):
        if not self.head:
            return []
        data, bantu, no = [], self.head, 1
        while True:
            data.append(f"{no}. {bantu.data}")
            bantu = bantu.next
            no += 1
            if bantu == self.head:
                break
        return data

class TreeNode:
    def __init__(self, buku):
        self.buku = buku
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, buku):
        def _insert(node, buku):
            if buku.id < node.buku.id:
                if node.left is None:
                    node.left = TreeNode(buku)
                else:
                    _insert(node.left, buku)
            elif buku.id > node.buku.id:
                if node.right is None:
                    node.right = TreeNode(buku)
                else:
                    _insert(node.right, buku)

        if self.root is None:
            self.root = TreeNode(buku)
        else:
            _insert(self.root, buku)

    def search(self, id_buku):
        def _search(node, id_buku):
            if node is None:
                return None
            if node.buku.id == id_buku:
                return node.buku
            return _search(node.left, id_buku) if id_buku < node.buku.id else _search(node.right, id_buku)
        return _search(self.root, id_buku)

    def inorder_list(self):
        res = []
        def _in(node):
            if node:
                _in(node.left)
                res.append(node.buku)
                _in(node.right)
        _in(self.root)
        return res

    def preorder_list(self):
        res = []
        def _pre(node):
            if node:
                res.append(node.buku)
                _pre(node.left)
                _pre(node.right)
        _pre(self.root)
        return res

    def postorder_list(self):
        res = []
        def _post(node):
            if node:
                _post(node.left)
                _post(node.right)
                res.append(node.buku)
        _post(self.root)
        return res

@st.cache_data
def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

def import_buku_from_df(df):
    count_baru = 0
    for _, row in df.iterrows():
        try:
            id_buku = int(row['ID'])
            if not inventaris.cari_id(id_buku):
                buku = Buku(id_buku, str(row['Judul']), str(row['Penulis']), int(row['Tahun']))
                inventaris.tambah_buku(buku)
                tree.insert(buku)
                count_baru += 1
        except:
            continue
    return count_baru

def validate_id(id_str):
    """Validasi ID jadi int atau return None kalau kosong/salah"""
    if not id_str:
        return None
    try:
        id_int = int(id_str)
        return id_int if id_int >= 1 else None
    except:
        return None

def linear_search(data, keyword):
    return [b for b in data if keyword.lower() in b.judul.lower()]

def binary_search(data, keyword):
    """Binary search return list biar konsisten dengan linear"""
    kiri, kanan = 0, len(data) - 1
    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        if data[tengah].judul.lower() == keyword.lower():
            return [data[tengah]]
        elif keyword.lower() < data[tengah].judul.lower():
            kanan = tengah - 1
        else:
            kiri = tengah + 1
    return []

def bubble_sort(data):
    return sorted(data, key=lambda x: x.judul)

def selection_sort(data):
    return sorted(data, key=lambda x: x.judul)

def merge_sort(data):
    return sorted(data, key=lambda x: x.judul)

def quick_sort(data):
    return sorted(data, key=lambda x: x.judul)

check_login()

# Init session_state
if 'inventaris' not in st.session_state:
    st.session_state.inventaris = SingleLinkedList()
    st.session_state.riwayat = DoubleLinkedList()
    st.session_state.antrian = Queue()
    st.session_state.favorit = CircularSingle()
    st.session_state.rekomendasi = CircularDouble()
    st.session_state.tree = BinarySearchTree()

inventaris = st.session_state.inventaris
riwayat = st.session_state.riwayat
antrian = st.session_state.antrian
favorit = st.session_state.favorit
rekomendasi = st.session_state.rekomendasi
tree = st.session_state.tree

# Sidebar
with st.sidebar:
    st.title(f"Halo, {st.session_state.username}")
    menu = st.selectbox("Menu", ["Kelola Buku", "Peminjaman", "Pengembalian", "Searching", "Sorting", "Tree", "Laporan"])
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

st.title("Sistem Manajemen Perpustakaan")

if menu == "Kelola Buku":
    st.subheader("Kelola Buku")
    tab1, tab2, tab3, tab4 = st.tabs(["Tambah", "Tampilkan", "Edit", "Hapus"])

    with tab1:
        if 'form_key' not in st.session_state:
            st.session_state.form_key = 0
        with st.form(f"form_tambah_{st.session_state.form_key}", clear_on_submit=True):
            col1, col2 = st.columns(2)
            with col1:
                id_buku_str = st.text_input("ID Buku", value="", placeholder="Masukkan ID Angka")
            with col2:
                tahun = st.number_input("Tahun Terbit", step=1, min_value=1900, max_value=2026, value=None, placeholder="Contoh: 2024")

            judul = st.text_input("Judul Buku", value="", placeholder="Masukkan Judul Buku")
            penulis = st.text_input("Penulis", value="", placeholder="Masukkan Nama Penulis")

            if st.form_submit_button("Tambah Buku"):
                id_buku = validate_id(id_buku_str)
                if not judul or not penulis or id_buku is None or tahun is None:
                    st.error("Semua field wajib diisi dengan benar")
                elif inventaris.cari_id(id_buku):
                    st.error("ID sudah ada")
                else:
                    buku_baru = Buku(id_buku, judul, penulis, tahun)
                    inventaris.tambah_buku(buku_baru)
                    tree.insert(buku_baru)
                    st.session_state.form_key += 1
                    st.success("Buku berhasil ditambahkan")
                    st.rerun()

    with tab2:
        data = [b.to_dict() for b in inventaris.to_list()]
        if data:
            df = pd.DataFrame(data)
            st.dataframe(df, use_container_width=True, hide_index=True)
            col1, col2 = st.columns(2)
            with col1:
                st.download_button("Download CSV", data=convert_df_to_csv(df), file_name="data_buku.csv", mime="text/csv")
            with col2:
                uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
                if uploaded_file:
                    try:
                        df_upload = pd.read_csv(uploaded_file)
                        if st.button("Import Data Ini"):
                            count = import_buku_from_df(df_upload)
                            st.success(f"Berhasil import {count} buku baru")
                            st.rerun()
                    except Exception as e:
                        st.error(f"Gagal baca file: {e}")
        else:
            st.info("Belum ada buku. Silakan tambah buku di tab 'Tambah'.")

    with tab3:
        id_edit_str = st.text_input("ID Buku yang diedit", value="", placeholder="Masukkan ID Angka", key="edit_id_str")
        id_edit = validate_id(id_edit_str)
        buku = inventaris.cari_id(id_edit) if id_edit else None
        if id_edit_str and id_edit is None:
            st.error("ID harus angka >= 1")
        elif buku:
            judul = st.text_input("Judul Baru", value=buku.judul, key="edit_judul")
            penulis = st.text_input("Penulis Baru", value=buku.penulis, key="edit_penulis")
            tahun = st.number_input("Tahun Baru", value=buku.tahun, step=1, min_value=1900, max_value=2026, key="edit_tahun")
            if st.button("Simpan Perubahan"):
                inventaris.edit(id_edit, judul, penulis, tahun)
                st.success("Data berhasil diubah")
                st.rerun()
        elif id_edit_str:
            st.warning("ID tidak ditemukan")

    with tab4:
        id_hapus_str = st.text_input("ID Buku yang dihapus", value="", placeholder="Masukkan ID Angka", key="hapus_id_str")
        id_hapus = validate_id(id_hapus_str)
        if id_hapus_str and id_hapus is None:
            st.error("ID harus angka >= 1")
        if st.button("Hapus Buku"):
            if id_hapus is None:
                st.error("Masukkan ID yang valid dulu")
            elif inventaris.hapus(id_hapus):
                st.success("Buku berhasil dihapus")
                st.rerun()
            else:
                st.error("ID tidak ditemukan.")

elif menu == "Peminjaman":
    st.subheader("Peminjaman Buku")
    col1, col2 = st.columns(2)
    with col1:
        nama = st.text_input("Nama Peminjam", value="", placeholder="Nama Peminjam")
        judul = st.text_input("Judul Buku", value="", placeholder="Judul Buku")
        if st.button("Pinjam"):
            if nama and judul:
                antrian.enqueue(f"{nama} meminjam '{judul}'")
                favorit.tambah(judul)
                st.success("Masuk antrian")
                st.rerun()
            else:
                st.warning("Nama dan Judul wajib diisi")
    with col2:
        st.write("#### Antrian Peminjaman")
        st.code("\n".join(antrian.to_list()) or "Antrian kosong.")

elif menu == "Pengembalian":
    st.subheader("Pengembalian Buku")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Proses Pengembalian Teratas"):
            data = antrian.dequeue()
            if data:
                riwayat.tambah(data)
                st.success(f"Diproses: {data}")
                st.rerun()
            else:
                st.warning("Tidak ada antrian.")
    with col2:
        st.write("#### Riwayat Pengembalian")
        st.code("\n".join(riwayat.to_list()) or "Belum ada riwayat.")

elif menu == "Searching":
    st.subheader("Searching Engine")
    opsi = st.radio("Pilih Metode", ["Linear Search", "Binary Search"], horizontal=True)
    key = st.text_input("Cari Judul Buku", value="", placeholder="Ketik judul...")
    if st.button("Cari"):
        data = inventaris.to_list()
        if not key:
            st.warning("Masukkan keyword dulu")
        elif opsi == "Linear Search":
            hasil = linear_search(data, key)
            if hasil:
                st.dataframe(pd.DataFrame([b.to_dict() for b in hasil]), hide_index=True, use_container_width=True)
            else:
                st.warning("Tidak ditemukan.")
        else:
            data_sorted = merge_sort(data) # Binary wajib sorted
            hasil = binary_search(data_sorted, key)
            if hasil:
                st.dataframe(pd.DataFrame([b.to_dict() for b in hasil]), hide_index=True, use_container_width=True)
            else:
                st.warning("Tidak ditemukan.")

elif menu == "Sorting":
    st.subheader("Sorting Engine")
    opsi = st.selectbox("Pilih Algoritma", ["Bubble Sort", "Selection Sort", "Merge Sort", "Quick Sort"])
    if st.button("Urutkan Berdasarkan Judul"):
        data = inventaris.to_list()
        func = {"Bubble Sort": bubble_sort, "Selection Sort": selection_sort, "Merge Sort": merge_sort, "Quick Sort": quick_sort}
        hasil = func[opsi](data)
        if hasil:
            st.dataframe(pd.DataFrame([b.to_dict() for b in hasil]), hide_index=True, use_container_width=True)
        else:
            st.info("Data kosong")

elif menu == "Tree":
    st.subheader("Operasi Binary Search Tree by ID")
    col1, col2 = st.columns(2)
    with col1:
        opsi = st.selectbox("Traversal", ["Inorder", "Preorder", "Postorder"])
        if st.button("Tampilkan Traversal"):
            func = {"Inorder": tree.inorder_list, "Preorder": tree.preorder_list, "Postorder": tree.postorder_list}
            data = func[opsi]()
            if data:
                st.dataframe(pd.DataFrame([b.to_dict() for b in data]), hide_index=True, use_container_width=True)
            else:
                st.info("Tree kosong")
    with col2:
        st.divider()
        id_cari_str = st.text_input("Cari ID Buku di Tree", value="", placeholder="Masukkan ID Angka")
        id_cari = validate_id(id_cari_str)
        if id_cari_str and id_cari is None:
            st.error("ID harus angka >= 1")
        if st.button("Cari ID"):
            if id_cari is None:
                st.warning("Masukkan ID yang valid dulu")
            else:
                hasil = tree.search(id_cari)
                if hasil:
                    st.json(hasil.to_dict())
                else:
                    st.warning("Data tidak ditemukan.")

elif menu == "Laporan":
    st.subheader("Laporan Perpustakaan")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Jumlah Buku", len(inventaris.to_list()))
        st.write("#### Daftar Buku")
        if inventaris.to_list():
            st.dataframe(pd.DataFrame([b.to_dict() for b in inventaris.to_list()]), hide_index=True, use_container_width=True)
        else:
            st.info("Belum ada buku.")
        st.write("#### Buku Favorit")
        st.code("\n".join(favorit.to_list()) or "-")
    with col2:
        st.write("#### Antrian Peminjaman")
        st.code("\n".join(antrian.to_list()) or "-")
        st.write("#### Riwayat Pengembalian")
        st.code("\n".join(riwayat.to_list()) or "-")
        st.write("#### Rekomendasi Buku")
        st.code("\n".join(rekomendasi.to_list()) or "-")
        st.divider()
        if st.button("Reset Semua Data", type="primary"):
            st.session_state.clear()
            st.rerun()
