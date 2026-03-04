#==============================================
#Nama  : Pratama Fahriel Sanjaya
#NIM   : J0403251053
#Kelas : TPL B2
#==============================================

#==================================================
#Latihan 1 . Memahami Kode Program (Insertion Sort)
#==================================================

def insertion_sort(data):
 for i in range(1, len(data)):
    key = data[i]
    j = i - 1

    while j >= 0 and data[j] > key:
        data[j + 1] = data[j]
        j -= 1

    data[j + 1] = key

    return data
 
'''
Soal:
1. Mengapa perulangan dimulai dari indeks 1?
Jawab : Karena elemen pertama di indeks 0 dianggap sudah berada di posisi yang benar.
        Jadi mulai dari indeks 1 lah kita mulai ngecek dan ngurut elemen-elemennya.

2. Apa fungsi variabel key?
Jawab : Key itu variabel buat nyimpan elemen yang sedang kita proses, yaitu data[i].
        Nanti key ini yang akan kita bandingkan dan cari posisi yang tepat.

3. Mengapa digunakan while, bukan for?
Jawab : Karena kita nggak tahu harus bergeser berapa kali. While bisa terus bergerak mundur
        sampai nemuin posisi yang tepat untuk elemen tersebut.

4. Operasi apa yang terjadi di dalam while?
Jawab : Elemen-elemen yang lebih besar dari key digeser ke kanan satu posisi,
        terus j dikurangi 1 untuk cek elemen sebelumnya sampai ketemu posisi yang pas.
'''