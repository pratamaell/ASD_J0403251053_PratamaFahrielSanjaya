#=============================================
# Nama  : Pratama Fahriel Sanjaya
# NIM   : J0403251053
# Kelas : B2
# Praktikum 13 - Graph III: Spanning Tree
#==============================================

# ==========================================================
# Latihan 1 - Memahami Konsep Spanning Tree
# ==========================================================

# Daftar edge graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

# Menampilkan edge graph
print("Edge pada graph:")
for edge in edges:
    print(edge)

# Menampilkan spanning tree
print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

# Menampilkan jumlah edge
print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# ==========================================================
# Jawaban Analisis:
# 1. Graph awal memiliki lebih banyak edge dan dapat memiliki cycle,
#    sedangkan spanning tree hanya mengambil edge yang diperlukan
#    untuk menghubungkan semua node tanpa cycle.
#
# 2. Spanning tree tidak boleh memiliki cycle karena cycle membuat
#    penggunaan edge menjadi berlebih dan tidak efisien.
#
# 3. Jumlah edge spanning tree lebih sedikit karena spanning tree
#    hanya membutuhkan jumlah edge sebanyak jumlah node - 1.
# ==========================================================