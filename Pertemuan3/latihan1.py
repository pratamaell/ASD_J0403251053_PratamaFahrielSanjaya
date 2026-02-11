class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def delete_node(self, key):
        # Mulai dari head linked list
        temp = self.head
        # Jika head adalah node yang akan dihapus
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        # Inisialisasi prev sebagai None untuk melacak node sebelumnya
        prev = None
        # Traverse linked list untuk mencari node dengan data == key
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        # Jika node tidak ditemukan, keluar dari fungsi
        if temp is None:
            return
        # Hapus node dengan menghubungkan prev.next ke temp.next
        prev.next = temp.next
        # Set temp ke None untuk membersihkan referensi
        temp = None

# Contoh Penggunaan 
ll = LinkedList()

# Input jumlah elemen
n = int(input("Masukkan jumlah elemen yang ingin ditambahkan: "))

# Input elemen satu per satu
for i in range(n):
    data = int(input(f"Masukkan elemen ke-{i+1}: "))
    ll.insert_at_end(data)

print("Linked List sebelum penghapusan:")
ll.display()

# Input node yang ingin dihapus
key = int(input("Masukkan nilai node yang ingin dihapus: "))
ll.delete_node(key)

print(f"Linked List setelah penghapusan node dengan nilai {key}:")
ll.display()
