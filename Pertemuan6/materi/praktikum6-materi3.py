#==============================================
#Nama  : Pratama Fahriel Sanjaya
#NIM   : J0403251053
#Kelas : TPL B2
#==============================================

#================================================
#Merge sort (Ascending)
#================================================

def merge_sort(data):
    if len(data) <= 1: #jika data hanya terdiri dari satu elemen atau kosong, maka sudah terurut
        return data
    #divide : membagi data menjadi dua bagian sampai menjadi data tunggal
    mid = len(data) // 2 #membagi data menjadi dua bagian
    data_kiri = data[:mid] #data bagian kiri
    data_kanan = data[mid:] #data bagian kanan

    #recursive call
    kiri_sorted = merge_sort(data_kiri) #membagi data bagian kiri
    kanan_sorted = merge_sort(data_kanan) #membagi data bagian kanan

    return merge(kiri_sorted, kanan_sorted)

def merge(data_kiri, data_kanan):

    result = [] #list kosong untuk menyimpan hasil penggabungan
    i = j = 0 #pointer untuk data kiri dan kanan

    #membandingkan elemen kiri dan kanan
    while i < len(data_kiri) and j < len(data_kanan):
         if data_kiri[i] <= data_kanan[j]: #jika elemen kiri lebih kecil atau sama dengan elemen kanan
            result.append(data_kiri[i]) #tambahkan elemen kiri ke hasil
            i += 1 #geser pointer kiri
         else:
            result.append(data_kanan[j]) #tambahkan elemen kanan ke hasil
            j += 1 #geser pointer kanan
    
    #menambahkan sisa elemen yang belum diproses (jika ada)
    result.extend(data_kiri[i:]) #tambahkan sisa elemen kiri ke hasil
    result.extend(data_kanan[j:]) #tambahkan sisa elemen kanan ke hasil

    return result

#contoh penggunaan
angka = [13,7,28,5,19,36,4]
print("hasil merge sort:", merge_sort(angka))