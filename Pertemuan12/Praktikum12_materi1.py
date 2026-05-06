#==============================================
#Nama  : Pratama Fahriel Sanjaya
#NIM   : J0403251053
#Kelas : TPL B2
#==============================================

# Import library heapq untuk priority queue (antrian berdasarkan prioritas)
import heapq 

# Membuat graf/jaringan dengan node dan bobot (jarak antar node)
# Format: node -> {tetangga: jarak}
graph = { 
            'A': {'B': 4, 'C': 2},      # Dari A ke B jauhnya 4, ke C jauhnya 2
            'B': {'D': 5},              # Dari B ke D jauhnya 5
            'C': {'D': 1},              # Dari C ke D jauhnya 1
            'D': {}                     # D tidak punya tetangga
        } 
 
 
def dijkstra(graph, start): 
    #untuk nyimpan jarak minimum dari node awal ke setiap node
    # Awalnya semua jaraknya infinity (belum ketemu jalan terpendek)
    distances = {node: float('inf') for node in graph} 
    # Jarak dari nodeawal ke dirinya sendiri adalah 0 (tidak perlu jalan)
    distances[start] = 0 
    # Priority queue (antrian) yang nyimpan (jarak, node)
    # Dijkstra selalu ambil jarak terkecil dulu buat dievaluasi
    pq = [(0, start)] 
 
    # Terus loop selama masih ada node yang perlu diproses
    while pq: 
        # Ambil node dengan jarak terkecil dari priority queue
        current_distance, current_node = heapq.heappop(pq) 
        # Loop untuk setiap tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items(): 
            # Hitung jarak baru = jarak ke node saat ini + jarak ke tetangganya
            distance = current_distance + weight 
            # Kalo jarak baru lebih kecil daripada jarak yang tersimpan sebelumnya
            if distance < distances[neighbor]: 
                # Update jarak ke tetangga dengan jarak yang lebih kecil
                distances[neighbor] = distance 
                # Masukin tetangga dengan jarak barunya ke priority queue
                heapq.heappush(pq, (distance, neighbor)) 
 
    return distances 
 
hasil = dijkstra(graph, 'A') 
print(hasil) 