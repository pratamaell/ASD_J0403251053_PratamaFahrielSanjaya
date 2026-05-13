#==============================================
#Nama  : Pratama Fahriel Sanjaya
#NIM   : J0403251053
#Kelas : TPL B2
#==============================================

import heapq
graph = {
 'A': {'B': 4, 'C': 2, 'D': 5},
 'B': {'A': 4, 'D': 3},
 'C': {'A': 2, 'D': 1},
 'D': {'A': 5, 'B': 3, 'C': 1}
}
def prim(graph, start):
    """Algoritma Prim untuk mencari Minimum Spanning Tree (MST).

    Parameters:
        graph (dict): Representasi graf berbobot. Format:
            {node: {tetangga: bobot, ...}, ...}
        start: Node awal untuk membangun MST.

    Returns:
        mst (list): Daftar edge MST dalam bentuk (u, v, bobot).
        total_weight (int/float): Total bobot semua edge MST.
    """

    # Kumpulan node yang sudah masuk ke MST
    visited = set([start])

    # Min-heap untuk memilih edge berbobot terkecil
    # Elemen heap: (bobot, u, v)
    edges = []

    # Masukkan semua edge dari node awal ke heap
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    # Selama masih ada edge kandidat
    while edges:
        # Ambil edge dengan bobot terkecil
        weight, u, v = heapq.heappop(edges)

        # Jika node tujuan belum dikunjungi, berarti edge ini bisa dipakai
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight

            # Masukkan edge dari node v ke heap (untuk kandidat selanjutnya)
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight


# Jalankan Prim mulai dari node 'A'
mst, total = prim(graph, 'A')

# Tampilkan hasil MST
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

# Tampilkan total bobot MST
print("Total bobot =", total)

