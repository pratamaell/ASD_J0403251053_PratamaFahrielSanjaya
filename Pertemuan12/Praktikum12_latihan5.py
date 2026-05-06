#==============================================
#Nama  : Pratama Fahriel Sanjaya
#NIM   : J0403251053
#Kelas : TPL B2
# Praktikum 12 - Graph II: Shortest Path
#==============================================

# ==========================================================
# Latihan 5: Studi Kasus Shortest Path Antar Kota
# Algoritma: Dijkstra
# ==========================================================

import heapq

# 1. Representasi graph berbobot menggunakan dictionary
#    Setiap key adalah nama kota, dan value-nya adalah dictionary
#    berisi kota tetangga beserta bobot (jarak) edge-nya.
graph = {
    'Bogor'   : {'Jakarta': 5, 'Depok': 2},
    'Depok'   : {'Jakarta': 2, 'Bandung': 6},
    'Jakarta' : {'Bandung': 7},
    'Bandung' : {}
}

# 2. Fungsi Dijkstra
def dijkstra(graph, start):
    """
    Mencari jarak terpendek dari node 'start' ke semua node lain
    dalam graph berbobot menggunakan algoritma Dijkstra.

    Parameter:
        graph (dict) : representasi graph berbobot (adjacency dict)
        start (str)  : nama node awal

    Return:
        distances (dict) : jarak terpendek dari start ke tiap node
    """
    # Inisialisasi semua jarak dengan nilai tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari node awal ke dirinya sendiri adalah 0
    distances[start] = 0

    # Priority queue: menyimpan pasangan (jarak_kumulatif, nama_node)
    # heapq selalu mengambil elemen dengan jarak terkecil terlebih dahulu
    priority_queue = [(0, start)]

    while priority_queue:
        # Ambil node dengan jarak terkecil dari priority queue
        current_distance, current_node = heapq.heappop(priority_queue)

        # Lewati jika jarak ini sudah tidak relevan (sudah ada yang lebih kecil)
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            # Hitung jarak ke tetangga melalui node saat ini
            distance = current_distance + weight

            # Relaksasi: perbarui jarak jika ditemukan jalur yang lebih pendek
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# 3. Penentuan node awal
node_awal = 'Bogor'

# 4. Jalankan Dijkstra dan tampilkan output jarak terpendek
hasil = dijkstra(graph, node_awal)

print(f"Jarak terpendek dari {node_awal}:")
for kota, jarak in hasil.items():
    print(f"  {node_awal} -> {kota} = {jarak}")



# Jawaban Analisis:

# 1. Node awal yang digunakan apa?
#    Node awal yang digunakan adalah Bogor.
#    Ditentukan melalui variabel: node_awal = 'Bogor'

# 2. Node mana yang memiliki jarak paling kecil dari node awal?
#    Node dengan jarak paling kecil (selain Bogor sendiri) adalah Depok = 2.
#    Depok terhubung langsung ke Bogor dengan bobot edge terkecil, yaitu 2.

# 3. Node mana yang memiliki jarak paling besar dari node awal?
#    Node dengan jarak paling besar adalah Bandung = 8.
#    Jalur terpendek ke Bandung: Bogor -> Depok -> Bandung = 2 + 6 = 8.
#    Jalur alternatif Bogor -> Jakarta -> Bandung = 5 + 7 = 12, lebih jauh.
#    Jalur alternatif Bogor -> Depok -> Jakarta -> Bandung = 2 + 2 + 7 = 11, juga lebih jauh.

# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus ini.
#
#    Langkah awal:
#    - Semua jarak diinisialisasi tak hingga, kecuali Bogor = 0.
#    - Priority queue dimulai dengan: [(0, 'Bogor')]
#
#    Iterasi 1 — proses Bogor (jarak 0):
#    - Periksa tetangga: Jakarta (0+5=5) dan Depok (0+2=2).
#    - Perbarui distances: Jakarta=5, Depok=2.
#    - Priority queue: [(2, 'Depok'), (5, 'Jakarta')]
#
#    Iterasi 2 — proses Depok (jarak 2, terkecil di queue):
#    - Periksa tetangga: Jakarta (2+2=4) dan Bandung (2+6=8).
#    - Jakarta diperbarui dari 5 menjadi 4 karena 4 < 5.
#    - Bandung diperbarui dari inf menjadi 8.
#    - Priority queue: [(4, 'Jakarta'), (5, 'Jakarta'), (8, 'Bandung')]
#
#    Iterasi 3 — proses Jakarta (jarak 4, terkecil di queue):
#    - Periksa tetangga: Bandung (4+7=11).
#    - 11 > 8 (jarak Bandung saat ini), maka tidak diperbarui.
#    - Priority queue: [(5, 'Jakarta'), (8, 'Bandung')]
#
#    Iterasi 4 — proses Jakarta (jarak 5, dilewati):
#    - 5 > distances['Jakarta'] yang sudah 4, maka dilewati (skip).
#
#    Iterasi 5 — proses Bandung (jarak 8):
#    - Bandung tidak memiliki tetangga, tidak ada yang diproses.
#    - Priority queue kosong, algoritma selesai.
#
#    