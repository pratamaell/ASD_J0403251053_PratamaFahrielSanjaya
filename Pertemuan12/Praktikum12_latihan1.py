#==============================================
#Nama  : Pratama Fahriel Sanjaya
#NIM   : J0403251053
#Kelas : TPL B2
# Praktikum 12 - Graph II: Shortest Path
#==============================================


# ==========================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# ==========================================================

# Representasi weighted graph menggunakan dictionary bersarang
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Menghitung dua kemungkinan jalur dari A ke D
jalur_1 = graph['A']['B'] + graph['B']['D']
jalur_2 = graph['A']['C'] + graph['C']['D']

print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

# A -> B -> D
# A -> C -> D

if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")


# Jawaban Analisis:

# 1. Berapa total bobot jalur A -> B -> D?
#    Total bobot jalur A -> B -> D adalah 9.
#    Diperoleh dari: bobot edge A->B (4) + bobot edge B->D (5) = 9.

# 2. Berapa total bobot jalur A -> C -> D?
#    Total bobot jalur A -> C -> D adalah 3.
#    Diperoleh dari: bobot edge A->C (2) + bobot edge C->D (1) = 3.

# 3. Jalur mana yang dipilih sebagai jalur terpendek?
#    Jalur terpendek yang dipilih adalah A -> C -> D dengan total bobot 3.
#    Karena 3 < 9, kondisi (jalur_1 < jalur_2) bernilai False,
#    sehingga program mencetak "Jalur terpendek adalah A -> C -> D".

# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?
#    Karena dalam weighted graph, setiap edge memiliki bobot (cost/jarak) yang berbeda-beda.
#    Jumlah edge hanya menghitung banyaknya langkah, bukan beban totalnya.
#    Contoh pada program ini: kedua jalur sama-sama memiliki 2 edge,
#    namun jalur A->B->D memiliki total bobot 9, jauh lebih besar dari
#    jalur A->C->D yang hanya 3. Dalam konteks nyata (seperti peta jalan
#    atau jaringan komputer), bobot merepresentasikan jarak, waktu, atau biaya —
#    sehingga jalur dengan edge lebih banyak bisa saja lebih "murah" atau
#    lebih efisien daripada jalur dengan edge lebih sedikit namun bobot besar.
