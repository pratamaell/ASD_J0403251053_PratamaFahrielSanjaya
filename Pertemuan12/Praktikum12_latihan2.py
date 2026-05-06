#==============================================
#Nama  : Pratama Fahriel Sanjaya
#NIM   : J0403251053
#Kelas : TPL B2
# Praktikum 12 - Graph II: Shortest Path
#==============================================

# ==========================================================
# Latihan 2: Implementasi Dijkstra
# ==========================================================

import heapq

# Weighted graph dengan bobot positif
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start ke seluruh node lain
    menggunakan algoritma Dijkstra.
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak dari start ke start adalah 0
    distances[start] = 0
    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat,
        # maka proses dilewati
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

hasil = dijkstra(graph, 'A')
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)


# Jawaban Analisis:

# 1. Berapa jarak terpendek dari A ke B?
#    Jarak terpendek dari A ke B adalah 4.
#    Hanya ada satu jalur langsung: A -> B dengan bobot 4.

# 2. Berapa jarak terpendek dari A ke C?
#    Jarak terpendek dari A ke C adalah 2.
#    Hanya ada satu jalur langsung: A -> C dengan bobot 2.

# 3. Berapa jarak terpendek dari A ke D?
#    Jarak terpendek dari A ke D adalah 3.
#    Diperoleh melalui jalur A -> C -> D: bobot A->C (2) + bobot C->D (1) = 3.

# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
#    Jalur A -> B -> D memiliki total bobot 4 + 5 = 9.
#    Jalur A -> C -> D memiliki total bobot 2 + 1 = 3.
#    Meskipun jumlah edge kedua jalur sama (2 edge), bobot setiap edge
#    di jalur A -> C -> D jauh lebih kecil, sehingga total biayanya lebih rendah.
#    Dijkstra memilih jalur berdasarkan akumulasi bobot terkecil, bukan jumlah edge.

# 5. Apa fungsi priority_queue dalam algoritma Dijkstra?
#    Priority queue (min-heap) berfungsi untuk selalu memproses node dengan
#    jarak terakumulasi paling kecil terlebih dahulu. Setiap elemen disimpan
#    sebagai pasangan (jarak, node), dan heapq.heappop() otomatis mengambil
#    elemen dengan jarak terkecil. Hal ini memastikan bahwa saat suatu node
#    diproses, jarak yang tercatat sudah merupakan jarak terpendek yang mungkin —
#    tanpa perlu memeriksa ulang semua kemungkinan. Tanpa priority queue,
#    algoritma harus melakukan pencarian linear yang jauh lebih lambat (O(V^2)
#    dibanding O((V + E) log V) dengan priority queue).

# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?
#    Dijkstra berasumsi bahwa sekali sebuah node diproses (diambil dari
#    priority queue), jarak ke node tersebut sudah final dan tidak akan
#    berubah menjadi lebih kecil. Asumsi ini hanya berlaku jika semua bobot
#    bernilai positif — karena menambahkan edge positif tidak akan memperkecil
#    jarak yang sudah ditemukan.
#    Jika ada bobot negatif, sebuah jalur yang tampak lebih panjang di awal
#    bisa menjadi lebih pendek setelah melewati edge negatif. Akibatnya,
#    node yang sudah "selesai" diproses bisa saja memiliki jarak yang lebih
#    kecil melalui jalur lain, sehingga hasil Dijkstra menjadi salah.
#    Untuk graph dengan bobot negatif, algoritma Bellman-Ford lebih tepat
#    digunakan karena ia memeriksa seluruh edge sebanyak (V-1) kali.