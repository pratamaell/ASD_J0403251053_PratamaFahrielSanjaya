#==============================================
#Nama  : Pratama Fahriel Sanjaya
#NIM   : J0403251053
#Kelas : TPL B2
#==============================================

#==================================================
#Latihan 3 . Tracing Insertion Sort
#==================================================

#Buat program dengan menggunakan algoritma insertion sort
#Tracing dengan data = [5, 2, 4, 6, 1, 3]

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        
        data[j + 1] = key
    
    return data

data = [5, 2, 4, 6, 1, 3]
result = insertion_sort(data)
print(f"Hasil akhir: {result}")

'''
Soal:
1. Tuliskan isi list setelah iterasi i = 1.
Jawab : [2, 5, 4, 6, 1, 3]
        Penjelasan: key = 2, dibandingkan dengan 5, lebih kecil jadi 5 digeser ke kanan
                   dan 2 ditempatkan di depan.

2. Tuliskan isi list setelah iterasi i = 3.
Jawab : [2, 4, 5, 6, 1, 3]
        Penjelasan: key = 6, sudah lebih besar dari 5, jadi 6 tidak perlu digeser.
                   Semua elemen sebelumnya sudah terurut.

3. Berapa kali pergeseran terjadi pada iterasi i = 4?
Jawab : 4 kali pergeseran
        Penjelasan: key = 1, harus bergeser melewati 6, 5, 4, dan 2 sebelum ditempatkan
                   di posisi paling depan. Setiap elemen lebih besar dari 1 digeser ke kanan.
'''
