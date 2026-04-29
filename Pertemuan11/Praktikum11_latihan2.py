#==============================================
#Nama  : Pratama Fahriel Sanjaya
#NIM   : J0403251053
#Kelas : TPL B2
#==============================================

# Latihan 2: Studi Kasus DFS (Eksplorasi Jalur)

# Definisi Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Fungsi DFS (Depth-First Search) - Recursive
def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Menjalankan DFS dari A
visited = set()
print("DFS dari A:")
dfs(graph, 'A', visited)
print()

#.....................................................................
# PERTANYAAN ANALISIS
#.....................................................................

# 1. Mengapa DFS masuk ke node terdalam terlebih dahulu?
# JAWAB: DFS menggunakan prinsip LIFO (Last In First Out) dan rekursi:
#        a) DFS mengeksplorasi graph dengan cara "menggali ke dalam"
#           (go deep first) sebelum kembali (backtrack)
#        b) Menggunakan stack (implicit stack dari rekursi) sehingga
#           node yang terakhir ditambahkan ke stack akan diproses terlebih
#           dahulu (LIFO principle)
#        c) Algoritma DFS terus menelusuri neighbor sampai mencapai node
#           leaf (node tanpa neighbor) sebelum backtrack
#        d) Prinsip ini membuat DFS cocok untuk eksplorasi mendalam dan
#           pencarian solusi di kedalaman graph
#        Contoh: Dari A, maka A->B->D (terdalam)->backtrack->E->backtrack->C->F

# 2. Apa yang terjadi jika urutan neighbor diubah?
# JAWAB: Urutan neighbor mempengaruhi urutan kunjungan dalam DFS:
#        a) Algoritma DFS menelusuri neighbor sesuai urutan dalam adjacency
#           list
#        b) Jika 'A': ['B', 'C'] diubah menjadi 'A': ['C', 'B'], maka:
#           - Urutan lama: A B D E C F
#           - Urutan baru: A C F B D E
#        c) DFS akan tetap mencapai semua node yang terhubung, tetapi
#           URUTAN KUNJUNGAN akan berbeda
#        d) Perubahan urutan tidak mempengaruhi sifat DFS (tetap deep-first),
#           hanya mengubah path mana yang dijelajahi lebih dulu

# 3. Bandingkan hasil DFS dengan BFS pada graph yang sama
# JAWAB: Perbedaan DFS vs BFS pada graph yang sama:
#        DFS dari A:  A B D E C F  (depth-first, go deep)
#        BFS dari A:  A B C D E F  (breadth-first, level by level)
#        
#        Perbedaan Detail:
#        a) CARA EKSPLORASI:
#           - DFS: Mengikuti satu path hingga ke leaf node (menggunakan stack)
#           - BFS: Menjelajahi level per level (menggunakan queue)
#        
#        b) STRUKTUR DATA:
#           - DFS: Menggunakan stack (rekursi atau explicit stack)
#           - BFS: Menggunakan queue (FIFO)
#        
#        c) URUTAN KUNJUNGAN:
#           - DFS: A->B->D, kembali->E, kembali->C->F
#           - BFS: A, lalu level 1 (B,C), lalu level 2 (D,E,F)
#        
#        d) KEGUNAAN:
#           - DFS: Cocok untuk topological sorting, cycle detection,
#             path finding (deep exploration)
#           - BFS: Cocok untuk shortest path, level-order traversal
#        
#        e) KOMPLEKSITAS:
#           - Keduanya sama: O(V + E) dimana V=vertices, E=edges
#           - Perbedaan hanya pada URUTAN dan STRATEGI eksplorasi