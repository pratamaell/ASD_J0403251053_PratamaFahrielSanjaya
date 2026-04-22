#==============================================
#Nama  : Pratama Fahriel Sanjaya
#NIM   : J0403251053
#Kelas : TPL B2
#==============================================

# ========================================================== 
# Latihan 6: Rotasi Kanan pada BST Tidak Seimbang 
# ========================================================== 
# DATA: 30, 20, 10 (Membuat left-skewed tree)
# Sebelum Rotasi Kanan:
#     30
#    /
#   20
#  /
# 10
# Sesudah Rotasi Kanan:
#     20
#    /  \
#   10  30
# ========================================================== 

# Class Node untuk menyimpan data BST
class Node:  # Definisi class Node
    def __init__(self, data):  # Constructor untuk inisialisasi node
        self.data = data  # Atribut untuk menyimpan nilai data
        self.left = None  # Atribut untuk pointer child kiri, diinisialisasi None
        self.right = None  # Atribut untuk pointer child kanan, diinisialisasi None


# Fungsi insert untuk menambahkan data ke dalam BST
def insert(root, data):  # Fungsi untuk menyisipkan data ke dalam BST
    # Jika root kosong, buat node baru
    if root is None:  # Cek apakah root kosong
        return Node(data)  # Jika kosong, return node baru
    
    # Jika data lebih kecil, masuk ke subtree kiri
    if data < root.data:  # Cek apakah data lebih kecil dari root
        root.left = insert(root.left, data)  # Masukkan ke subtree kiri
    
    # Jika data lebih besar, masuk ke subtree kanan
    elif data > root.data:  # Cek apakah data lebih besar dari root
        root.right = insert(root.right, data)  # Masukkan ke subtree kanan
    
    return root  # Return node root yang sudah diupdate


# Fungsi preorder untuk melihat isi tree dengan traversal preorder
def preorder(root):  # Fungsi traversal preorder (root, left, right)
    if root is not None:  # Cek apakah node tidak kosong
        print(root.data, end=" ")  # Cetak data node terlebih dahulu
        preorder(root.left)  # Rekursi ke subtree kiri
        preorder(root.right)  # Rekursi ke subtree kanan


# Fungsi untuk menampilkan struktur tree secara visual dengan indentasi
def tampil_struktur(root, level=0, posisi="Root"):  # Fungsi menampilkan tree dengan struktur hirarki
    if root is not None:  # Cek apakah node tidak kosong
        print("   " * level + f"{posisi}: {root.data}")  # Cetak node dengan indentasi sesuai level
        tampil_struktur(root.left, level + 1, "L")  # Rekursi ke child kiri dengan level + 1
        tampil_struktur(root.right, level + 1, "R")  # Rekursi ke child kanan dengan level + 1


# Fungsi rotasi kanan untuk menyeimbangkan BST yang condong ke kiri
def rotate_right(y):  # Fungsi rotasi kanan dengan parameter y sebagai node yang dirotasi
    # y adalah root lama yang akan dirotasi
    x = y.left  # x adalah child kiri y (akan menjadi root baru)
    T2 = x.right  # T2 adalah subtree kanan milik x, disimpan sementara sebelum diputus
    
    # Proses rotasi dimulai
    x.right = y  # y menjadi child kanan dari x (x naik menjadi parent)
    y.left = T2  # child kiri y diganti dengan T2 (subtree yang disimpan tadi)
    
    # x menjadi root baru setelah rotasi
    return x  # Return x sebagai root baru


# ----------------------------- 
# Program utama 
# ----------------------------- 
# Membuat tree yang tidak seimbang dengan data berurutan turun
# Struktur awal: 30 -> 20 -> 10 (left-skewed tree)
root = None  # Inisialisasi root sebagai None
data_list = [30, 20, 10]  # List data yang akan dimasukkan ke BST - DATA BERURUTAN TURUN AKAN MEMBUAT TREE YANG CONDONG KE KIRI!
for data in data_list:  # Loop untuk setiap data dalam list
    root = insert(root, data)  # Insert data ke dalam BST

print("=" * 50)  # Garis pemisah untuk output
print("SEBELUM ROTASI KANAN")  # Label untuk output sebelum rotasi
print("=" * 50)  # Garis pemisah untuk output
print("Preorder sebelum rotasi kanan:")  # Label untuk traversal preorder sebelum rotasi
preorder(root)  # Tampilkan preorder traversal sebelum rotasi
print("\n\nStruktur sebelum rotasi kanan:")  # Label untuk struktur sebelum rotasi
tampil_struktur(root)  # Tampilkan visual struktur tree sebelum rotasi

# Melakukan rotasi kanan pada root untuk menyeimbangkan tree
root = rotate_right(root)  # Panggil fungsi rotate_right dan jadikan hasilnya sebagai root baru

print("\n\n" + "=" * 50)  # Garis pemisah untuk output
print("SESUDAH ROTASI KANAN")  # Label untuk output setelah rotasi
print("=" * 50)  # Garis pemisah untuk output
print("Preorder sesudah rotasi kanan:")  # Label untuk traversal preorder setelah rotasi
preorder(root)  # Tampilkan preorder traversal sesudah rotasi
print("\n\nStruktur sesudah rotasi kanan:")  # Label untuk struktur sesudah rotasi
tampil_struktur(root)  # Tampilkan visual struktur tree sesudah rotasi



