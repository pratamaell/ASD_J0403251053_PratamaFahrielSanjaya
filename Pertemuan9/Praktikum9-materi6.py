#==============================================
#Nama  : Pratama Fahriel Sanjaya
#NIM   : J0403251053
#Kelas : TPL B2
#==============================================

#==============================================
#latihan 6 : Struktur Organisasi Perusahaan 
#==============================================

#class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai pada node
        self.left = None #pointer ke anak kiri
        self.right = None #pointer ke anak kanan

#Fungsi preorder : Root => Left => Right
def preorder(node):
    if node is not None: #jika node tidak kosong
        print(node.data, end=" ") 
        preorder(node.left)
        preorder(node.right) 

#membuat tree struktur organisasi perusahaan
root = Node("Direktur")

#child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

#child level 2
root.left.left = Node("Karyawan A1")
root.left.right = Node("Karyawan A2")
root.right.right = Node("Karyawan B1")

#menampilkan struktur organisasi
print("Struktur Organisasi Persusahaan:")
preorder(root)

#Penjelasan :
#1. Pada contoh di atas, kita membuat sebuah tree yang merepresentasikan struktur organisasi perusahaan dengan "Direktur" sebagai root, yang memiliki dua anak yaitu "Manajer A" (kiri) dan "Manajer B" (kanan).    
#2. "Manajer A" memiliki dua anak yaitu "Karyawan A1" (kiri) dan "Karyawan A2" (kanan), sedangkan "Manajer B" hanya memiliki satu anak yaitu "Karyawan B1" (kanan). 
#3. Ketika kita menjalankan fungsi preorder, urutan kunjungan akan dimulai dari root "Direktur", kemudian ke anak kiri "Manajer A", lalu ke anak kiri "Karyawan A1", kembali ke "Manajer A" untuk mengunjungi anak kanannya "Karyawan A2", dan akhirnya ke anak kanan root yaitu "Manajer B", dan terakhir ke anak kanannya "Karyawan B1". Hasilnya adalah Direktur Manajer A Karyawan A1 Karyawan A2 Manajer B Karyawan B1.
