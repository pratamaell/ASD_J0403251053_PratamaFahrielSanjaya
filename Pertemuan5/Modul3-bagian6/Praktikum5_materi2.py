#==============================================
#Nama  : Pratama Fahriel Sanjaya
#NIM   : J0403251053
#Kelas : TPL B2
#==============================================

#==============================================
#Materi rekursif : Call Stack
#Tracing Bilangan (masuk - keluar)
#inputan : 3
#Masuk : 1-2-3
#Keluar : 3-2-1
#==============================================

def hitung(n):
    #base case
    if n == 0:
        return
    print("Masuk : ", n) 
    hitung(n-1)
    print("Keluar : ", n) 

print("====== Program Call Stack ======")
hitung(3)