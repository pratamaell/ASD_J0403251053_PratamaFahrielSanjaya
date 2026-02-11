class Node:
    def __init__(self, data):
        self.data = data  # Data yang disimpan dalam node
        self.next = None  # Pointer ke node berikutnya

class LinkedList:
    def __init__(self):
        self.head = None  # Pointer ke node pertama

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:  # Jika list kosong
            self.head = new_node
        else:  # Jika list tidak kosong
            temp = self.head
            while temp.next:  # Traverse hingga node terakhir
                temp = temp.next
            temp.next = new_node  # Tambahkan node baru di akhir

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Simpan node berikutnya
            current.next = prev      # Balik pointer next ke prev
            prev = current           # Geser prev ke current
            current = next_node      # Geser current ke next_node
        self.head = prev             # Update head ke node yang sebelumnya terakhir

# Input User
ll = LinkedList()

# Input jumlah elemen
n = int(input("Masukkan jumlah elemen yang ingin ditambahkan: "))

# Input elemen satu per satu
for i in range(n):
    data = int(input(f"Masukkan elemen ke-{i+1}: "))
    ll.insert_at_end(data)

print("Linked List sebelum dibalik:", end=" ")
ll.display()

ll.reverse()

print("Linked List setelah dibalik:", end=" ")
ll.display()
