#=============================================
#Nama  : Pratama Fahriel Sanjaya
#NIM   : J0403251053
#Kelas : TPL B2
#==============================================

#==================================================
#Latihan 5 . Melengkapi Fungsi Merge
#==================================================

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

'''
Soal:
1. Lengkapi kondisi agar menjadi ascending.
Jawab : left[i] < right[j]
        Kondisi ini membandingkan elemen dari left dan right. Kalau left lebih kecil,
        elemen left diambil dulu (ditambahkan ke result), sebaliknya right diambil.
    
2. Jelaskan fungsi result.extend()
Jawab : extend() buat menambahkan semua elemen dari list lain ke dalam result.
        left[i:] atau right[j:] adalah sisa elemen yang belum diproses.
        Karena salah satu list sudah habis (while sudah selesai), sisa elemen dari
        list yang lain langsung ditambahkan ke result. Sisa elemen ini sudah terurut,
        jadi bisa langsung ditambahkan tanpa perlu dibandingkan lagi.
'''