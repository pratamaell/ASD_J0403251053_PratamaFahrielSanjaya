#==============================================
#Nama  : Pratama Fahriel Sanjaya
#NIM   : J0403251053
#Kelas : TPL B2
#==============================================

#================================================
#insertion sort dengan tracing
#================================================

def insertion_sort(data):
    # melihat data awal
    print("data awal:", data)
    print("=" * 50)

    # loop mulai dari elemen kedua (index 1) sampai akhir
    for i in range(1, len(data)):
        key = data[i]  # simpan elemen yang akan disisipkan
        j = i - 1  # mulai bandingkan dengan elemen sebelah kiri 

        print("iterasi ke-", i)
        print(" nilai key:", key)
        print("bagian kiri (terurut):", data[:i])
        print("bagian kanan (belum terurut):", data[i:])

        # geser
        while j >= 0 and data[j] > key:  # selama elemen sebelah kiri lebih besar dari key
            data[j + 1] = data[j]  # geser elemen ke kanan
            j -= 1  # geser ke elemen sebelah kiri
        data[j + 1] = key  # sisipkan key di posisi yang benar

        print("data setelah disisipkan:", data)
        print("=" * 50)

    return data

#contoh penggunaan
angka = [7,8,5,2,4,6]
print("hasil insertion sort:", insertion_sort(angka))