#==============================================
#Nama  : Pratama Fahriel Sanjaya
#NIM   : J0403251053
#Kelas : TPL B2
#==============================================

# ========================================================== 
# Latihan 5: Rotasi Kiri pada BST Tidak Seimbang 
# ========================================================== 
 
# Class Node untuk menyimpan data BST
class Node:  # Definisi class Node
    def __init__(self, data):  # Constructor untuk inisialisasi node
        self.data = data  # Atribut untuk menyimpan nilai data
        self.left = None  # Atribut untuk pointer child kiri, diinisialisasi None
        self.right = None  # Atribut untuk pointer child kanan, diinisialisasi None 
 
 
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
 
 
# Fungsi rotasi kiri untuk menyeimbangkan BST yang condong ke kanan
def rotate_left(x):  # Fungsi rotasi kiri dengan parameter x sebagai node yang dirotasi
    # x adalah root lama yang akan dirotasi
    y = x.right  # y adalah child kanan x (akan menjadi root baru)
    T2 = y.left  # T2 adalah subtree kiri milik y, disimpan sementara sebelum diputus

    # Proses rotasi dimulai
    y.left = x  # x menjadi child kiri dari y (y naik menjadi parent)
    x.right = T2  # child kanan x diganti dengan T2 (subtree yang disimpan tadi)

    # y menjadi root baru setelah rotasi
    return y  # Return y sebagai root baru 
 
 
# ----------------------------- 
# Program utama 
# ----------------------------- 
# Membuat tree yang tidak seimbang dengan data berurutan naik
# Struktur awal: 10 -> 20 -> 30 (right-skewed tree)

root = Node(10)  # Buat node root dengan nilai 10
root.right = Node(20)  # Buat node child kanan dengan nilai 20
root.right.right = Node(30)  # Buat node child kanan dari 20 dengan nilai 30

print("Preorder sebelum rotasi kiri:")  # Label untuk output sebelum rotasi
preorder(root)  # Tampilkan preorder traversal sebelum rotasi
print("\n\nStruktur sebelum rotasi kiri:")  # Label untuk struktur sebelum rotasi
tampil_struktur(root)  # Tampilkan visual struktur tree sebelum rotasi

# Melakukan rotasi kiri pada root untuk menyeimbangkan tree
root = rotate_left(root)  # Panggil fungsi rotate_left dan jadikan hasilnya sebagai root baru
print("\nPreorder sesudah rotasi kiri:")  # Label untuk output setelah rotasi

preorder(root)  # Tampilkan preorder traversal sesudah rotasi
print("\n\nStruktur sesudah rotasi kiri:")  # Label untuk struktur sesudah rotasi
tampil_struktur(root)  # Tampilkan visual struktur tree sesudah rotasi 