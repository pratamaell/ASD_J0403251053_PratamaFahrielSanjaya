#==============================================
#Nama  : Pratama Fahriel Sanjaya
#NIM   : J0403251053
#Kelas : TPL B2
#==============================================

# Fungsi Bellman-Ford untuk mencari jarak terpendek dari node awal ke semua node
# Parameter: graph = graf/jaringan yang dipakai, start = node mula-mula
def bellman_ford(graph, start): 
 
    # untuk nyimpan jarak ke setiap node
    # Awalnya semua jaraknya infinity (belum ketemu jalan)
    distances = {node: float('inf') for node in graph} 
    # Jarak dari node awal ke dirinya sendiri adalah 0
    distances[start] = 0 
    # Loop relaksasi berulang sebanyak (jumlah node - 1) kali
    # Dijamin bakal ketemu jarak terpendek setelah loop ini
    for _ in range(len(graph) - 1): 
        # Untuk setiap node yang ada di graf
        for node in graph: 
            # Untuk setiap tetangga dari node saat ini
            for neighbor, weight in graph[node].items(): 
                # Kalo jarak lewat node sekarang lebih pendek daripada yang tersimpan
                if distances[node] + weight < distances[neighbor]: 
                    # Update jarak ke tetangga dengan jarak yang lebih pendek
                    distances[neighbor] = distances[node] + weight 
 
    return distances 

