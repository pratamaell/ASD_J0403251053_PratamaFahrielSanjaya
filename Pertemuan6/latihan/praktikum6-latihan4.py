#==============================================
#Nama  : Pratama Fahriel Sanjaya
#NIM   : J0403251053
#Kelas : TPL B2
#==============================================

#==================================================
#Latihan 4 . Memahami Kode Program (Merge Sort)
#==================================================
from heapq import merge

def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge (left_sorted, right_sorted)

'''
Soal:
1. Apa yang dimaksud dengan base case?
Jawab : Base case adalah kondisi berhenti untuk rekursi, yaitu if len(data) <= 1: return data.
        Kalau array sudah punya 1 elemen atau kosong, dianggap sudah terurut, jadi langsung
        dikembalikan tanpa diproses lebih lanjut. Tanpa base case, fungsi bakalan memanggil
        dirinya sendiri terus-terusan sampai error.

2. Mengapa fungsi memanggil dirinya sendiri?
Jawab : Karena merge sort pake strategi divide and conquer. Fungsi merge_sort memisah array
        jadi 2 bagian (left dan right), terus masing-masing bagian diurutkan dengan cara
        memanggil merge_sort pada bagian tersebut. Ini dilakukan terus sampai array tinggal
        1 elemen (base case terpenuhi).

3. Apa tujuan fungsi merge()?
Jawab : Fungsi merge() buat menggabungkan 2 array yang sudah terurut (left_sorted dan
        right_sorted) jadi 1 array yang juga terurut. Ini adalah bagian terakhir dari
        divide and conquer, hasil dari merge ini yang dijadikan return value.
'''
