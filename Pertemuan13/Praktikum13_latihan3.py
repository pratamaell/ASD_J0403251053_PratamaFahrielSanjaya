#===========================================
# Nama  : Pratama Fahriel Sanjaya
# NIM   : J0403251053
# Kelas : B2
# Praktikum 13 - Graph III: Spanning Tree
#==============================================

# ==========================================================
# Latihan 3 - Implementasi Algoritma Prim
# ==========================================================

import heapq

# Representasi graph berbobot
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

# Fungsi algoritma Prim
def prim(graph, start):

    visited = set([start])
    edges = []

    # Memasukkan edge dari node awal
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    # Proses pemilihan edge
    while edges:

        weight, u, v = heapq.heappop(edges)

        if v not in visited:

            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight

            # Menambahkan edge baru
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight

# Menjalankan algoritma Prim
mst, total = prim(graph, 'A')

# Menampilkan hasil MST
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

# Menampilkan total bobot
print("Total bobot =", total)

# ==========================================================
# Jawaban Analisis:
# 1. Node awal yang digunakan adalah node A.
#
# 2. Edge yang dipilih pertama kali adalah A-C dengan bobot 2.
#
# 3. Prim menentukan edge berikutnya berdasarkan edge dengan
#    bobot terkecil dari node yang sudah dikunjungi.
#
# 4. Total bobot MST yang dihasilkan adalah 6.
#
# 5. Perbedaan Prim dan Kruskal:
#    - Prim membangun tree dari satu node awal.
#    - Kruskal memilih edge terkecil secara global.
# ==========================================================