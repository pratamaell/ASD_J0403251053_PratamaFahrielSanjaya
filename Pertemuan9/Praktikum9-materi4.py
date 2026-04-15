#==============================================
#Nama  : Pratama Fahriel Sanjaya
#NIM   : J0403251053
#Kelas : TPL B2
#==============================================

#==============================================
#latihan 4 : Membuat Traversal Tree Inorder
#==============================================

#class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai pada node
        self.left = None #pointer ke anak kiri
        self.right = None #pointer ke anak kanan


#membuat fugsi inorder : Left => Root => Right
def inorder(node):
    if node is not None: #jika node tidak kosong
        inorder(node.left) 
        print(node.data, end=" ")
        inorder(node.right) 


#Membuat sebuah node root
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#menjalankan inorder traversal
print("Hasil Inorder Traversal:")
inorder(root)

#Penjelasan :
#1. Inorder traversal adalah metode untuk mengunjungi semua node dalam sebuah pohon dengan urutan Left => Root => Right.
#2. Pada contoh di atas, kita membuat sebuah binary tree dengan root "A", yang memiliki dua anak "B" (kiri) dan "C" (kanan). Node "B" memiliki dua anak yaitu "D" (kiri) dan "E" (kanan), sedangkan node "C" tidak memiliki anak.
#3. Ketika kita menjalankan fungsi inorder, urutan kunjungan akan dimulai dari anak kiri "D", kemudian ke parent "B", lalu ke anak kanannya "E", kembali ke root "A", dan akhirnya ke anak kanan root yaitu "C". Hasilnya adalah D B E A C.