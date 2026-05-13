# Nama  : Pratama Fahriel Sanjaya
# NIM   : 
# Kelas : 
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Latihan 5 - Tugas Mandiri
# Kasus: Jaringan Komputer
# Menggunakan Algoritma Prim
# ==========================================================

import heapq

# Representasi weighted graph
graph = {
    'RouterA': {'RouterB': 3, 'RouterC': 2},
    'RouterB': {'RouterA': 3, 'RouterD': 5, 'RouterC': 4},
    'RouterC': {'RouterA': 2, 'RouterD': 1, 'RouterB': 4},
    'RouterD': {'RouterB': 5, 'RouterC': 1}
}

# Fungsi Prim
def prim(graph, start):

    visited = set([start])
    edges = []

    # Memasukkan edge awal
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    while edges:

        weight, u, v = heapq.heappop(edges)

        if v not in visited:

            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight

            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight

# Menjalankan program
mst, total = prim(graph, 'RouterA')

# Menampilkan hasil
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot minimum =", total)

# ==========================================================
# Jawaban Analisis:
# 1. Kasus yang dipilih adalah Jaringan Komputer.
#
# 2. Algoritma yang digunakan adalah Prim.
#
# 3. Edge yang dipilih dalam MST:
#    - RouterA - RouterC = 2
#    - RouterC - RouterD = 1
#    - RouterA - RouterB = 3
#
# 4. Total bobot MST adalah 6.
#
# 5. Edge tertentu tidak dipilih karena dapat membentuk cycle
#    dan membuat total bobot menjadi lebih besar.
# ==========================================================