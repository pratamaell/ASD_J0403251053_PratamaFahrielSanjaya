class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Pointer ke node pertama
        self.tail = None  # Pointer ke node terakhir

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:  # Jika list kosong
            self.head = new_node
            self.tail = new_node
        else:  # Jika list tidak kosong
            self.tail.next = new_node  # Hubungkan tail lama ke node baru
            new_node.prev = self.tail  # Hubungkan node baru ke tail lama
            self.tail = new_node  # Update tail ke node baru

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

# Contoh Penggunaan
dll = DoublyLinkedList()
elements_input = input("Masukkan elemen ke dalam Doubly Linked List (pisahkan dengan koma): ")
elements = [int(x.strip()) for x in elements_input.split(',')]
for elem in elements:
    dll.insert_at_end(elem)

print("Masukkan elemen ke dalam Doubly Linked List:", ", ".join(map(str, elements)))
search_key = int(input("Masukkan elemen yang ingin dicari: "))

if dll.search(search_key):
    print(f"Elemen {search_key} ditemukan dalam Doubly Linked List.")
else:
    print(f"Elemen {search_key} tidak ditemukan dalam Doubly Linked List.")
