#==============================================
#Nama  : Pratama Fahriel Sanjaya
#NIM   : J0403251053
#Kelas : TPL B2
#==============================================

#==============================================
#Impelementasi Dasar: Node Pada Linked List
#==============================================

class Node:
    def __init__(self,data): #kosntruktor untuk inisialisasi node
        self.data = data #menyimpan data/nilai
        self.next = None #pointer ke note berikutnya

# 1) Membuat node satu per satu
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

# 2) Menghubungkan node-node tersebut
nodeA.next = nodeB #nodeA menunjuk ke nodeB
nodeB.next = nodeC #nodeB menunjuk ke nodeC

# 3) Menentukan head linked list
head = nodeA #head linked list menunjuk ke nodeA

# 4) Traversal : menelusuri dari head sampai none
current = head #mulai dari head
while current is not None: #selama current tidak None
    print(current.data) #cetak data node saat ini
    current = current.next #pindah ke node berikutnya

#=================================================
#Impelementasi Dasar: Linked list + Insert Awal
#=================================================

class Linkedlist:
    def __init__(self):
        self.head = None #inisialisasi head linked list


    def insert_awal (self, data):
       #1) Buat node baru
       nodeBaru = Node(data) #panggil class node
       #2) Hubungkan node baru dengan head
       nodeBaru.next = self.head #node baru menunjuk ke head
       #3) Update head ke node baru
       self.head = nodeBaru #update head ke node baru

    def hapus_awal(self):
        data_terhapus = self.head.data #simpan data yang akan dihapus
        self.head = self.head.next #update head ke node berikutnya
        print("Node yang dihapus adalah : ", data_terhapus)
    def tampilkan(self):
        current = self.head 
        while current is not None:
            print(current.data) 
            current = current.next 

print("--------------------------------")
ll = Linkedlist() #instantiasi linked list
ll.insert_awal("X")
ll.insert_awal("Y")
ll.insert_awal("Z") 
ll.tampilkan()
ll.hapus_awal()
ll.tampilkan()