#==============================================
#Nama  : Pratama Fahriel Sanjaya
#NIM   : J0403251053
#Kelas : TPL B2
# Praktikum 12 - Graph II: Shortest Path
#==============================================

# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================

import heapq

# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

hasil = dijkstra(graph, 'Gerbang')
print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")



# Jawaban Analisis:

# 1. Lokasi mana yang paling dekat dari Gerbang?
#    Lokasi paling dekat dari Gerbang adalah Kantin, dengan waktu tempuh 2 menit.
#    Kantin terhubung langsung ke Gerbang melalui edge berbobot 2,
#    yang merupakan nilai terkecil di antara semua lokasi lain.

# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
#    Waktu tempuh terpendek dari Gerbang ke Aula adalah 7 menit.
#    Jalur yang ditempuh: Gerbang -> Kantin -> Lab -> Aula
#    Rincian: Gerbang->Kantin (2) + Kantin->Lab (4) + Lab->Aula (1) = 7 menit.
#    Jalur alternatif Gerbang -> Kantin -> Aula membutuhkan 2 + 7 = 9 menit,
#    dan Gerbang -> Perpustakaan -> Lab -> Aula membutuhkan 6 + 3 + 1 = 10 menit.
#    Jadi jalur lewat Kantin -> Lab adalah yang paling efisien.

# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
#    Tidak selalu. Contohnya pada kasus ini:
#    - Gerbang ke Lab: tidak ada edge langsung, sehingga harus melewati
#      node perantara. Jalur terpendeknya adalah Gerbang->Kantin->Lab = 2+4 = 6 menit.
#    - Gerbang ke Aula: jalur langsung Gerbang->Kantin->Aula = 2+7 = 9 menit,
#      namun jalur tidak langsung Gerbang->Kantin->Lab->Aula = 2+4+1 = 7 menit
#      ternyata lebih singkat meski melewati lebih banyak node.
#    Ini membuktikan bahwa jalur dengan lebih banyak langkah bisa lebih cepat
#    jika bobot tiap edge-nya kecil. Dijkstra dirancang untuk menemukan
#    jalur semacam ini secara otomatis.

# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
#    Ada beberapa alasan Dijkstra tepat digunakan di sini:
#
#    - Semua bobot bernilai positif: waktu tempuh antar lokasi tidak mungkin
#      negatif, sehingga syarat utama Dijkstra terpenuhi.
#
#    - Graph berukuran kecil dan statis: jumlah lokasi kampus terbatas dan
#      tidak berubah-ubah, sehingga efisiensi Dijkstra dapat dimanfaatkan
#      secara optimal.
#
#    - Butuh jarak terpendek dari satu sumber: kita hanya perlu menghitung
#      dari satu titik awal (Gerbang) ke semua lokasi lain, yang merupakan
#      persis masalah yang diselesaikan Dijkstra (Single Source Shortest Path).
#
#    - Performa lebih baik dari Bellman-Ford: karena tidak ada bobot negatif,
#      tidak perlu menggunakan Bellman-Ford yang lebih lambat. Dijkstra
#      menyelesaikan masalah ini lebih cepat dengan priority queue.