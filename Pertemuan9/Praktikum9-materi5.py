#==============================================
#Nama  : Pratama Fahriel Sanjaya
#NIM   : J0403251053
#Kelas : TPL B2
#==============================================

#==============================================
#latihan 5 : Membuat Traversal Tree Postorder
#==============================================

#class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai pada node
        self.left = None #pointer ke anak kiri
        self.right = None #pointer ke anak kanan

#Fungsi postorder : Left => Right => Root
def postorder(node):
    if node is not None: #jika node tidak kosong
        postorder(node.left)
        postorder(node.right) 
        print(node.data, end=" ")   

#Membuat sebuah node root
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#menjalankan postorder traversal
print("Hasil Postorder Traversal:")
postorder(root)

#Penjelasan :
#1. Postorder traversal adalah metode untuk mengunjungi semua node dalam sebuah pohon dengan urutan Left => Right => Root.
#2. Pada contoh di atas, kita membuat sebuah binary tree dengan root "A", yang memiliki dua anak "B" (kiri) dan "C" (kanan). Node "B" memiliki dua anak yaitu "D" (kiri) dan "E" (kanan), sedangkan node "C" tidak memiliki anak.
#3. Ketika kita menjalankan fungsi postorder, urutan kunjungan akan dimulai dari anak kiri "D", kemudian ke anak kanannya "E", kembali ke parent "B", lalu ke anak kanan root yaitu "C", dan akhirnya ke root "A". Hasilnya adalah D E B C A.   
