#==============================================
#Nama  : Pratama Fahriel Sanjaya
#NIM   : J0403251053
#Kelas : TPL B2
#==============================================

# Latihan 1: Studi Kasus BFS (Jalur Terdekat Lokasi)

from collections import deque

# Definisi Graph
graph = {
    'Rumah': ['Sekolah', 'Toko'],
    'Sekolah': ['Perpustakaan'],
    'Toko': ['Pasar'],
    'Perpustakaan': [],
    'Pasar': []
}

# Fungsi BFS (Breadth-First Search)
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Menjalankan BFS dari Rumah
print("BFS dari Rumah:")
bfs(graph, 'Rumah')
print()

#.....................................................................
# PERTANYAAN ANALISIS
#.....................................................................

# 1. Node mana yang dikunjungi pertama?
# JAWAB: Node yang dikunjungi pertama adalah 'Rumah' karena merupakan
#        starting point/node awal dari algoritma BFS. BFS selalu 
#        mengunjungi node awal terlebih dahulu sebelum menjelajahi
#        neighbor-neighbor nya.

# 2. Mengapa BFS cocok untuk mencari jalur terdekat?
# JAWAB: BFS cocok untuk mencari jalur terdekat (shortest path) karena:
#        a) BFS menggunakan prinsip FIFO (First In First Out) dengan queue
#        b) BFS menjelajahi graph level per level, dimulai dari node awal
#        c) Node yang ditemukan lebih dulu dijamin memiliki jumlah edge
#           (langkah) yang paling minimal untuk mencapai node tersebut
#        d) BFS menjamin menemukan path dengan edge terkecil, sebelum
#           mengeksplorasi path yang lebih panjang
#        Contoh: Jalur ke 'Pasar' adalah Rumah->Toko->Pasar (2 langkah),
#        lebih dekat daripada kemungkinan rute lain jika ada.

# 3. Apa perbedaan urutan BFS jika struktur graph diubah?
# JAWAB: Urutan BFS akan berbeda tergantung perubahan struktur graph:
#        a) Jika urutan neighbor berubah: Urutan kunjungan bisa berbeda
#           Contoh: Jika 'Rumah': ['Toko', 'Sekolah'], maka urutan 
#           kunjungan menjadi: Rumah Toko Sekolah Pasar Perpustakaan
#           (berbeda dari sebelumnya: Rumah Sekolah Toko Perpustakaan Pasar)
#        b) Jika ada node baru/edge baru ditambahkan: Akan ada node
#           baru dalam urutan kunjungan BFS
#        c) Jika ada node/edge dihapus: Beberapa node mungkin tidak
#           dapat dikunjungi (tidak terhubung dari starting node)
#        d) Perubahan struktur hanya mempengaruhi URUTAN kunjungan,
#           bukan mekanisme BFS-nya itu sendiri
