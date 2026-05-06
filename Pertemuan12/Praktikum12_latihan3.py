#==============================================
#Nama  : Pratama Fahriel Sanjaya
#NIM   : J0403251053
#Kelas : TPL B2
# Praktikum 12 - Graph II: Shortest Path
#==============================================

# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start ke seluruh node lain
    menggunakan algoritma Bellman-Ford.
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):
        # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():
                # Jika jarak ke node saat ini sudah diketahui,
                # dan ditemukan jarak yang lebih kecil ke neighbor,
                # maka lakukan update jarak
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    return distances

hasil = bellman_ford(graph, 'A')
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)


# Jawaban Analisis:

# 1. Berapa bobot langsung dari A ke B?
#    Bobot langsung dari A ke B adalah 5.
#    Terlihat dari definisi graph: 'A': {'B': 5, 'C': 4},
#    artinya edge A -> B memiliki bobot 5.

# 2. Berapa total bobot jalur A -> C -> B?
#    Total bobot jalur A -> C -> B adalah 2.
#    Diperoleh dari: bobot A->C (4) + bobot C->B (-2) = 2.
#    Bobot negatif pada edge C->B membuat jalur ini lebih murah
#    dibandingkan jalur langsung A->B.

# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
#    Jalur A -> C -> B menghasilkan jarak lebih kecil, yaitu 2.
#    Jalur langsung A -> B memiliki bobot 5, sedangkan
#    jalur A -> C -> B hanya 4 + (-2) = 2.
#    Karena 2 < 5, algoritma memilih A -> C -> B sebagai jalur terpendek.
#    Hal ini juga dikonfirmasi oleh output: B = 2.

# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
#    Bellman-Ford tidak berasumsi bahwa jarak sebuah node langsung final
#    setelah pertama kali diproses. Sebaliknya, algoritma ini melakukan
#    relaksasi pada SEMUA edge secara berulang sebanyak (V-1) kali,
#    di mana V adalah jumlah node. Pengulangan ini memberi kesempatan
#    pada setiap node untuk terus memperbarui jaraknya jika ditemukan
#    jalur yang lebih pendek — termasuk jalur yang melewati edge negatif.
#    Berbeda dengan Dijkstra yang langsung "mengunci" jarak suatu node,
#    Bellman-Ford bersedia merevisi jarak yang sudah ada selama iterasi
#    masih berjalan.

# 5. Apa yang dimaksud dengan proses relaksasi edge?
#    Relaksasi edge adalah proses memeriksa apakah jarak ke suatu node
#    tetangga (neighbor) dapat diperbarui menjadi lebih kecil melalui
#    node saat ini. Formulanya:
#        if distances[node] + weight < distances[neighbor]:
#            distances[neighbor] = distances[node] + weight
#    Artinya: "Jika jarak ke node saat ini ditambah bobot edge lebih kecil
#    dari jarak terbaik yang sudah diketahui ke neighbor, maka perbarui
#    jarak neighbor tersebut." Proses ini diulangi untuk semua edge di
#    setiap iterasi, sehingga jarak terpendek dapat menyebar secara
#    bertahap ke seluruh node dalam graph.

# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
#
#    - Bobot negatif:
#      Dijkstra tidak mendukung bobot negatif.
#      Bellman-Ford mendukung bobot negatif.
#
#    - Strategi proses:
#      Dijkstra selalu memproses node dengan jarak terkecil terlebih dahulu.
#      Bellman-Ford merelaksasi semua edge secara berulang sebanyak (V-1) kali.
#
#    - Struktur data utama:
#      Dijkstra menggunakan priority queue (min-heap).
#      Bellman-Ford menggunakan nested loop biasa.
#
#    - Kompleksitas waktu:
#      Dijkstra: O((V + E) log V) — lebih cepat.
#      Bellman-Ford: O(V * E) — lebih lambat.
#
#    - Deteksi negative cycle:
#      Dijkstra tidak dapat mendeteksi siklus negatif.
#      Bellman-Ford dapat mendeteksinya pada iterasi ke-V.
#
#    Kesimpulan: Gunakan Dijkstra jika semua bobot positif dan performa
#    penting. Gunakan Bellman-Ford jika graph memiliki bobot negatif
#    atau perlu mendeteksi negative cycle.