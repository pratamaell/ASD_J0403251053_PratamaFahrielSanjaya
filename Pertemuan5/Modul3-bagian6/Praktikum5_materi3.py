#==============================================
#Nama  : Pratama Fahriel Sanjaya
#NIM   : J0403251053
#Kelas : TPL B2
#==============================================

#==============================================
#Materi rekursif : Menjumlahkan elemen list
#==============================================

def jumlah_list(data, index=0):
    #base case
    if index == len(data):
        return 0
    #rekursive case
    return data[index] + jumlah_list(data, index+1)

print("====== Program Jumlah List ======")
print("Hasil Jumlah List : ", jumlah_list([2,4,6,8,10]))