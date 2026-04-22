#==============================================
#Nama  : Pratama Fahriel Sanjaya
#NIM   : J0403251053
#Kelas : TPL B2
#==============================================

# ========================================================== 
# Latihan 4: Membuat BST yang Tidak Seimbang 
# ========================================================== 
 
# Class Node untuk menyimpan data BST 
class Node:  # Definisi class Node
    def __init__(self, data):  # Constructor untuk inisialisasi node 
        self.data = data      # nilai pada node 
        self.left = None      # child kiri 
        self.right = None     # child kanan 
 
 
# Fungsi insert untuk BST 
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
 
 
# Fungsi preorder untuk melihat bentuk tree 
def preorder(root):  # Fungsi untuk traversal preorder
    if root is not None:  # Cek apakah node tidak kosong
        print(root.data, end=" ")  # Cetak data node
        preorder(root.left)  # Rekursi ke subtree kiri
        preorder(root.right)  # Rekursi ke subtree kanan 
 
 
# Fungsi sederhana untuk menampilkan struktur tree 
def tampil_struktur(root, level=0, posisi="Root"):  # Fungsi untuk menampilkan struktur tree secara visual
    if root is not None:  # Cek apakah node tidak kosong
        print("   " * level + f"{posisi}: {root.data}")  # Cetak node dengan indentasi
        tampil_struktur(root.left, level + 1, "L")  # Rekursi untuk child kiri
        tampil_struktur(root.right, level + 1, "R")  # Rekursi untuk child kanan 
# ----------------------------- 
# Program utama 
# ----------------------------- 
root = None  # Inisialisasi root sebagai None
# Data dimasukkan berurutan naik 
data_list = [10, 20, 30]  # List data yang akan dimasukkan ke BST
for data in data_list:  # Loop untuk setiap data dalam list
    root = insert(root, data)  # Insert data ke dalam BST
print("Preorder BST:")  # Cetak label preorder
preorder(root)  # Panggil fungsi preorder
print("\n\nStruktur BST:")  # Cetak label struktur tree
tampil_struktur(root)  # Panggil fungsi tampil_struktur 