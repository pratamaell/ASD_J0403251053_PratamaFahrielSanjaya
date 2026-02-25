#==============================================
#Nama  : Pratama Fahriel Sanjaya
#NIM   : J0403251053
#Kelas : TPL B2
#==============================================

#==============================================
#Materi rekursif : Faktorial
#rekursif case => 3! = 3 x 2 x 1 
#base case => 0 berhenti
#==============================================

def faktorial(n):
   #base case
   if n == 0:
      return 1
   #rekursive case
   return n*faktorial(n-1)
print("====== Program Faktorial ======")
print("Hasil Faktorial : ", faktorial(5))