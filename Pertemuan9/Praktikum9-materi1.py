#==============================================
#Nama  : Pratama Fahriel Sanjaya
#NIM   : J0403251053
#Kelas : TPL B2
#==============================================

#==============================================
#latihan 1  Membuat Node
#==============================================

#class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai pada node
        self.left = None #pointer ke anak kiri
        self.right = None #pointer ke anak kanan

# membuat root
root = Node("A")

# menampilkan isi node 
print("Isi node root:", root.data)
print("Anak kiri root:", root.left)
print("Anak kanan root:", root.right)
    
#pembahasan :
#1. Node adalah struktur data dasar dalam pohon yang menyimpan nilai dan referensi ke anak-anaknya.
#2. Pada contoh di atas, kita membuat sebuah node dengan nilai "A" dan kedua anaknya (left dan right) diinisialisasi sebagai None, yang berarti node tersebut belum memiliki anak.      