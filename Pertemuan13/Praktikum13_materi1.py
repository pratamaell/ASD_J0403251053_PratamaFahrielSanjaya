#==============================================
#Nama  : Pratama Fahriel Sanjaya
#NIM   : J0403251053
#Kelas : TPL B2
#==============================================

# ==========================================================
# Implementasi Kruskal
# ==========================================================
# Daftar edge: (bobot, node1, node2)
# Setiap tuple berisi (bobot, node awal, node akhir)
edges = [
    (1, 'C', 'D'),   # Edge C-D dengan bobot 1
    (2, 'A', 'C'),   # Edge A-C dengan bobot 2
    (3, 'B', 'D'),   # Edge B-D dengan bobot 3
    (4, 'A', 'B'),   # Edge A-B dengan bobot 4
    (5, 'A', 'D')    # Edge A-D dengan bobot 5
    ]

# Mengurutkan edge berdasarkan bobot dari terkecil ke terbesar
edges.sort()

# mst: menyimpan edge-edge yang dipilih untuk Minimum Spanning Tree
mst = []
# total_weight: menyimpan total bobot dari semua edge di MST
total_weight = 0

# Set sederhana untuk menyimpan node yang sudah terhubung
# (catatan: ini adalah implementasi sederhana, bukan Union-Find yang optimal)
connected = set()

# Loop melalui setiap edge yang sudah diurutkan berdasarkan bobot
for weight, u, v in edges:
    # Jika edge tidak membentuk cycle sederhana
    # (cek apakah salah satu dari node u atau v belum ada di set)
    if u not in connected or v not in connected:
        # Tambahkan edge ke MST
        mst.append((u, v, weight))
        # Tambahkan bobot ke total
        total_weight += weight
        # Tambahkan kedua node ke set connected
        connected.add(u)
        connected.add(v)

# Tampilkan hasil Minimum Spanning Tree
print("Minimum Spanning Tree:")
for edge in mst:
    # Tampilkan setiap edge dalam format (node1, node2, bobot)
    print(edge)
    
# Tampilkan total bobot dari MST
print("Total bobot =", total_weight)