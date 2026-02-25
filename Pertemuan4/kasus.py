#==============================================
#Nama  : Pratama Fahriel Sanjaya
#NIM   : J0403251053
#Kelas : TPL B2
#==============================================

#=========================================================
#Kasus: Sistem Antrian Layanan Akadmik
#Implemetasi Queue =>
#Enqueue : Memindahkan pointer ke rear (nambah data baru di belakang)
#Dequeue : Memindahkan pointer ke front (hapus data di depan)
#Front ->  ->Rear
#=========================================================

#1) Mendefinisikan kelas Node (unit dasar linked list)
class Node:
    def __init__(self, nim, nama):
        self.nim = nim #menyimpan data nim mahasiswa
        self.nama = nama #menyimpan data nama mahasiswa
        self.next = None #pointer ke node berikutnya
    
#2) Mendefinisikan queue, terdiri dari pointer front dan rear    
class queueAkademik:
    def __init__(self):
        self.front = None #pointer ke elemen depan queue
        self.rear = None #pointer ke elemen belakang queue

    def is_empty(self):
        #ketika queue kosong maka front = rear = None
        return self.front is None #queue kosong jika front None
    
    #menambahkan data baru ke bagian belakang (rear)
    def enqueue(self, nim, nama):
        nodebaru = Node(nim, nama)
        #jika data baru masuk dari queue yang kosong maka data baru = front = rear
        if self.is_empty(): 
            self.front = nodebaru
            self.rear = nodebaru
            return
        #jika queue tidak kosong, maka data baru diletakkan setelah rear kemudian dijadikan sebagai rear
        self.rear.next = nodebaru #rear lama menunjuk ke node baru
        self.rear = nodebaru #rear diupdate ke node baru

    #menghapus data dari bagian depan (front)
    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong, tidak ada data yang bisa dilayani")
            return None
        #lihat data bagian front, simpan di variabel data yang akan dihapus(dilayani)
        node_dilayani = self.front

        #geser pointer ke next front
        self.front = self.front.next

        #jika front menjadi none (data antrian terakhir yang dilayani), maka front = rear = None
        if self.front is None:
            self.rear = None

        return node_dilayani
    
    #menampilkan isi antrian
    def tampilkan(self):
        print("Daftar Antrian Layanan Akademik Mahasiswa (Front -> Rear): ")
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. NIM: {current.nim}, Nama: {current.nama}")
            current = current.next
            no += 1 

#Program utama
def main():
    q = queueAkademik()

    while True:
        print("========= Sistem Antrian Akademik =========")
        print ("1. Tambah Antrian")
        print ("2. Layani Antrian")
        print ("3. Tampilkan Antrian")
        print ("4. Keluar")

        pilihan = input("Pilih menu (1-4): ").strip()

        if pilihan == "1":
            nim = input("Masukkan NIM mahasiswa: ").strip()
            nama = input("Masukkan nama mahasiswa: ").strip()
            q.enqueue(nim, nama)
            print("Antrian berhasil ditambahkan.\n")

        elif pilihan == "2":
            mahasiswa_dilayani = q.dequeue()
            if mahasiswa_dilayani is not None:
                print(f"Mahasiswa dengan NIM {mahasiswa_dilayani.nim} dan nama {mahasiswa_dilayani.nama} telah dilayani.\n")

        elif pilihan == "3":
            q.tampilkan()
    
        elif pilihan == "4":
            print("Terima kasih telah menggunakan sistem antrian akademik. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu 1-4.\n")
        
if __name__ == "__main__":
     main()