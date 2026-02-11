#Single	Linkedlist	dasar	pada	pyhthon :
class Node:
 def __init__(self, data):
    self.data = data
    self.next = None
class LinkedList:
 def __init__(self):
    self.head = None
    self.tail = None # Tambahkan pointer tail
 def insert_at_end(self, data):
    new_node = Node(data)
    if not self.head: # Jika linked list kosong
        self.head = new_node
        self.tail = new_node # Tail juga menunjuk ke node pertama
        self.tail.next = new_node # Sambungkan tail ke node baru
        self.tail = new_node # Update tail ke node baru
 def display(self):
    temp = self.head
    while temp:
        print(temp.data, end=" -> ")
    temp = temp.next
    print("null")
# Contoh Penggunaan
ll = LinkedList()
ll.insert_at_end(3)
ll.insert_at_end(5)
ll.insert_at_end(13)
ll.insert_at_end(2)
ll.display()
 
 #Double	LinkedList	pada	pyhthon
class Node:
 def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None
class DoublyLinkedList:
 def __init__(self):
    self.head = None
    self.tail = None # Menyimpan node terakhir untuk traversing
#mundur
 def insert_at_end(self, data):
    new_node = Node(data)
    if not self.head:
        self.head = new_node
        self.tail = new_node
    else:
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
 def display_forward(self):
    print("\nTraversing forward:")
    temp = self.head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
        print("null")
 def display_backward(self):
    print("\nTraversing backward:")
    temp = self.tail
    while temp:
        print(temp.data, end=" -> ")
    temp = temp.prev
    print("null")
# Contoh Penggunaan
dll = DoublyLinkedList()
dll.insert_at_end(3)
dll.insert_at_end(5)
dll.insert_at_end(13)
dll.insert_at_end(2)
dll.display_forward()
dll.display_backward()

#Circular singly linked list pada Python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Tambahkan pointer tail

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:  # Jika linked list kosong
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head  # Circular link ke dirinya sendiri
        else:
            self.tail.next = new_node  # Sambungkan tail ke node baru
            self.tail = new_node  # Update tail ke node baru
            self.tail.next = self.head  #

    def display(self):
        if not self.head:
            print("List is empty")
            return
        print("Circular Linked List Traversal:")
        temp = self.head
        print(temp.data, end=" -> ")
        temp = temp.next
        while temp != self.head:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("... (back to head)")
#	Contoh	Penggunaan
cll	=	CircularSinglyLinkedList()
cll.insert_at_end(3)
cll.insert_at_end(5)
cll.insert_at_end(13)
cll.insert_at_end(2)
cll.display()

#Circular doubly linked list in Python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head  # Circular link ke dirinya sendiri
        else:
            tail = self.head.prev  # Node terakhir dalam circular list
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head  # Menghubungkan kembali ke head
            self.head.prev = new_node  # Menghubungkan head ke node baru

    def display_forward(self):
        if not self.head:
            print("List is empty")
            return

        print("\nTraversing forward:")
        temp = self.head
        print(temp.data, end=" -> ")
        temp = temp.next

        while temp != self.head:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("... (back to head)")

    def display_backward(self):
        if not self.head:
            print("List is empty")
            return

        print("\nTraversing backward:")
        tail = self.head.prev  # Node terakhir
        temp = tail
        print(temp.data, end=" -> ")
        temp = temp.prev
        while temp != tail:
            print(temp.data, end=" -> ")
            temp = temp.prev
        print("... (back to tail)")

# Contoh Penggunaan
cdll = CircularDoublyLinkedList()
cdll.insert_at_end(3)
cdll.insert_at_end(5)
cdll.insert_at_end(13)
cdll.insert_at_end(2)
cdll.display_forward()
cdll.display_backward()
