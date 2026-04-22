#==============================================
#Nama  : Pratama Fahriel Sanjaya
#NIM   : J0403251053
#Kelas : TPL B2
#==============================================

#=============================================
# latihan Binary Search Tree (BST)
# BST itu pohon dimana anak kiri lebih kecil dari induk, anak kanan lebih besar
# Fungsi utama: insert data, traversal inorder (urut), search data
#=============================================

# Class Node: buat bikin satu simpul/nod di pohon BST
class Node:
    # Fungsi __init__: constructor buat inisialisasi node baru
    def __init__(self,data):
        self.data = data          # # simpan data di node ini
        self.left = None          # # pointer ke anak kiri, awalnya kosong
        self.right = None         # # pointer ke anak kanan, awalnya kosong

# Fungsi insert: buat masukin data baru ke pohon BST supaya tetap terurut
# Cara kerja: rekursi, bandingin data dengan root, kiri jika kecil, kanan jika besar
# Buat apa: bangun pohon BST dari list data
def insert(root,data):
    # # cek apakah posisi sekarang kosong (root None)
    if root is None :
        # # ya kosong, bikin node baru dan return sebagai root baru
        return Node(data)

    # # data lebih kecil dari root sekarang, masukin ke cabang kiri
    if data < root.data:
        # # rekursi ke cabang kiri
        root.left = insert(root.left, data)
    # # data lebih besar dari root sekarang, masukin ke cabang kanan
    elif data > root.data:
        # # rekursi ke cabang kanan
        root.right = insert(root.right, data)

    # # kembalikan root yang udah diupdate (struktur pohon berubah)
    return root 

# # inisialisasi root pohon BST kosong dulu
root = None
# # list data yang mau dimasukin ke BST
data_list = [50,30,70,20,40,60,80]

# # loop untuk masukin setiap data dari list ke BST
for data in data_list:
    # # panggil insert untuk setiap data, update root
    root = insert(root,data)

# # cetak pesan sukses, tampilin list data asli
print("BST berhasil dibuat dengan data:", data_list)

#=============================================
# Fungsi inorder: traversal pohon BST secara inorder (kiri-root-kanan)
# Buat apa: cetak data secara urut ascending karena sifat BST
#=============================================

def inoorder(root):
    # # cek root tidak kosong
    if root is not None:
        # # rekursi ke kiri dulu
        inoorder(root.left)
        # # cetak data root sekarang (tanpa enter)
        print(root.data, end=' ')
        # # rekursi ke kanan
        inoorder(root.right)

# # cetak judul traversal
print("Traversal Inorder dari BST:")
# # jalankan inorder traversal
inoorder(root)
# # print enter otomatis di akhir print sebelumnya

#=============================================
# Fungsi search: cari apakah key ada di pohon BST
# Buat apa: cek keberadaan data dengan rekursi (kiri jika kecil, kanan jika besar)
# Return True jika ketemu, False jika tidak
#=============================================

def search(root, key):
    # # jika root kosong, tidak ketemu
    if root is None:
        return False
    
    # # data root sama dengan yang dicari, ketemu
    if root.data == key:
        return True
    # # key lebih kecil, cari di kiri
    if key < root.data:
        return search(root.left, key)
    # # key lebih besar, cari di kanan
    else:
        return search(root.right, key)
    
# # tentukan key yang mau dicari (contoh 40)
key = 40
# # cek hasil search
if search(root, key):
    # # ketemu, cetak pesan
    print(f"\nNilai {key} ditemukan dalam BST.")
else:
    # # tidak ketemu, cetak pesan
    print(f"\nNilai {key} tidak ditemukan dalam BST.")
