#==============================================
# Nama  : Pratama Fahriel Sanjaya
# NIM   : J0403251053
# Kelas : B2
# Praktikum 13 - Graph III: Spanning Tree
#==============================================

# ==========================================================
# Latihan 2 - Implementasi Algoritma Kruskal
# ==========================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_weight = 0

# Menyimpan node yang sudah terhubung
connected = set()

# Proses algoritma Kruskal
for weight, u, v in edges:

    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight

        connected.add(u)
        connected.add(v)

# Menampilkan hasil MST
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

# Menampilkan total bobot
print("Total bobot =", total_weight)

# ==========================================================
# Jawaban Analisis:
# 1. Edge yang dipilih pertama kali adalah C-D dengan bobot 1.
#
# 2. Edge dengan bobot paling kecil dipilih terlebih dahulu agar
#    total bobot MST menjadi minimum.
#
# 3. Total bobot MST yang dihasilkan adalah 6.
#
# 4. Edge tertentu tidak dipilih karena dapat membentuk cycle
#    atau seluruh node sudah terhubung.
# ==========================================================