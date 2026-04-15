#==============================================
#Nama  : Pratama Fahriel Sanjaya
#NIM   : J0403251053
#Kelas : TPL B2
#==============================================

#==============================================
#latihan 3 : Membuat Traversal Tree Preorder
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

#Membuat sebuah node root
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#menjalankan preorder traversal
print("Hasil Preorder Traversal:")
preorder(root)

#Penjelasan :
#1. Preorder traversal adalah metode untuk mengunjungi semua node dalam sebuah pohon dengan urutan Root => Left => Right.
#2. Pada contoh di atas, kita membuat sebuah binary tree dengan root "A", yang memiliki dua anak "B" (kiri) dan "C" (kanan). Node "B" memiliki dua anak yaitu "D" (kiri) dan "E" (kanan), sedangkan node "C" tidak memiliki anak.
#3. Ketika kita menjalankan fungsi preorder, urutan kunjungan akan dimulai dari root "A", kemudian ke anak kiri "B", lalu ke anak kiri "D", kembali ke "B" untuk mengunjungi anak kanannya "E", dan akhirnya ke anak kanan root yaitu "C". Hasilnya adalah A B D E C.
