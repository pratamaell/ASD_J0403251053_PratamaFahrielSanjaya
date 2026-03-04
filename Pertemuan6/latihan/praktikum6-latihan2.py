#==============================================
#Nama  : Pratama Fahriel Sanjaya
#NIM   : J0403251053
#Kelas : TPL B2
#==============================================

#==================================================
#Latihan 2 . Melengkapi Potongan Kode
#==================================================

# No 1. ASCENDING SORT
def insertion_sort_asc(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data

# No 2. DESCENDING SORT 
def insertion_sort_desc(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] < key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data

'''
Soal:
1. Lengkapi kondisi agar menjadi sorting ascending.
Jawab : data[j] > key
        Elemen yang lebih besar dari key digeser ke kanan, terus j bergerak mundur.
        Setelah while loop selesai, data[j + 1] = key menempatkan key di posisi yang benar
        dalam array yang sudah terurut.

2. Ubah agar menjadi descending.
Jawab : data[j] < key
        Kondisi dibalik: elemen yang lebih kecil dari key digeser ke kanan, sehingga elemen
        yang lebih besar berada di depan. Setelah while loop selesai, data[j + 1] = key
        menempatkan key di posisi yang benar untuk descending.
'''
