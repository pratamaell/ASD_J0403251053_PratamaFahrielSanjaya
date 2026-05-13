#============================================
# Nama  : Pratama Fahriel Sanjaya
# NIM   : J0403251053
# Kelas : B2
# Praktikum 13 - Graph III: Spanning Tree
#==============================================

# ==========================================================
# Latihan 4 - Studi Kasus Jaringan Kabel Antar Gedung
# Menggunakan Algoritma Kruskal
# ==========================================================

# Daftar edge graph
edges = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
]

# Mengurutkan edge
edges.sort()

mst = []
total_cost = 0
connected = set()

# Proses Kruskal
for weight, u, v in edges:

    if u not in connected or v not in connected:

        mst.append((u, v, weight))
        total_cost += weight

        connected.add(u)
        connected.add(v)

# Menampilkan hasil
print("Jaringan Kabel Minimum:")
for edge in mst:
    print(edge)

print("Total biaya minimum =", total_cost)

# ==========================================================
# Jawaban Analisis:
# 1. Algoritma yang digunakan adalah Kruskal.
#
# 2. Edge yang dipilih:
#    - GedungC - GedungD = 1
#    - GedungA - GedungC = 2
#    - GedungB - GedungD = 3
#
# 3. Total biaya minimum adalah 6.
#
# 4. MST cocok digunakan karena dapat menghubungkan seluruh
#    gedung dengan biaya pemasangan kabel paling minimum.
# ==========================================================