#+++++++++++++++++++++++++++++++++++++++++++++++
#+ Prakatikum 1 : Konsep ADT dan File Handling + 
#+ Latihan Dasar : Mebaca seluruh isi file     +
#+++++++++++++++++++++++++++++++++++++++++++++++


# Program untuk membaca seluruh isi file teks
with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
    isi_file = file.read()
    print(isi_file)

print("=== Selesai Membaca File ===")
print("Tipe data isi_file:", type(isi_file))
print("Jumlah karakter dalam isi_file:", len(isi_file))
print("Jumlah baris dalam isi_file:", isi_file.count('\n') + 1)
print("==================================")

#membaca file baris per baris
print("=== Membaca File per Baris ===")
jumlah_baris=0
with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
    for baris in file:
        jumlah_baris=jumlah_baris+1
        baris=baris.strip()
        print("Baris ke -", jumlah_baris)
        print("Isi baris:", baris)
print("==================================")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+ Prakatikum 1 : Konsep ADT dan File Handling          +
#+ Latihan Dasar 2 : Persing Baris menjadi kolom data   +
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++

with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
    for baris in file:
        baris=baris.strip()
        nim,nama,nilai= baris.split(',')
        print("NIM:", nim , "| Nama:", nama, "| Nilai:", nilai)
print("=================================================")


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+ Prakatikum 1 : Konsep ADT dan File Handling                     +
#+ Latihan Dasar 3 : Membaca File dan Menyimpan File ke dalam List +
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
data_mahasiswa = []
with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
    for baris in file :
        baris= baris.strip()#menghilangkan karakter newline
        nim,nama,nilai= baris.split(',')
        data_mahasiswa.append((nim,nama,int(nilai)))

print("==== Data Mahasiswa dalam List ====")
print(data_mahasiswa)

print("========Jumlah Record dalam List========")
print("Jumlah Record:", len(data_mahasiswa))

print("======Menampilkan Data Record Tertentu======")
print("jumlah Record pertama:", data_mahasiswa[0])

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+ Prakatikum 1 : Konsep ADT dan File Handling                +
#+ Latihan Dasar 4 : Membaca File dan Menyimpan ke Dictionary +
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

data_mahasiswa_dict = {}
with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
    for baris in file :
        nim,nama,nilai= baris.split(',')
        data_mahasiswa_dict[nim] = {
            'nama': nama, 
            'nilai': int(nilai)
            }
print("==== Data Mahasiswa dalam Dictionary ====")
print(data_mahasiswa_dict)

