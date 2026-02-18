#==============================================
#Nama  : Pratama Fahriel Sanjaya
#NIM   : J0403251053
#Kelas : TPL B2
#==============================================

#=========================================================
#Impelementasi Dasar: Queue (Antrian) Berbasis Linked List
#=========================================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#queue dengan 2 pointer: front dan rear
class Queue:
    def __init__(self):
        self.front = None #pointer ke elemen depan queue
        self.rear = None #pointer ke elemen belakang queue

    def is_empty(self):
        return self.front is None #queue kosong jika front None

    def enqueue(self, data):
        #menambah data di belakang queue
        NodeBaru = Node(data) 
        if self.is_empty(): #jika queue kosong
            self.front = NodeBaru #front dan rear menunjuk ke node baru
            self.rear = NodeBaru
            return
        
        #jika queue tidak kosong:
        #Rear lama menunjuk ke node baru
        self.rear.next = NodeBaru 
        #rear diupdate ke node baru
        self.rear = NodeBaru

    def dequeue(self):
        #menghapus data dari depan

        #1)lihat data yang paling depan
        data_terhapus = self.front.data 
        #2)geser front ke node berikutnya
        self.front = self.front.next
        #3)Jika setelah geser front menjadi none, maka queue kosonh
        #rear juga harus jadi none
        if self.front is None:
            self.rear = None
            return data_terhapus
        
    def tampilkan(self):
        current = self.front 
        print("Front ", end="->")
        while current is not None:
         print(current.data, end="->")
         current = current.next
         print("None")

#Instantiasi Objek Queue
q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()

q.dequeue()
q.tampilkan()