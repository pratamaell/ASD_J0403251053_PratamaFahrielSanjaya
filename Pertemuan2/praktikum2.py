#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+ Prakatikum 2 : Konsep ADT dan File Handling                +
#+ Latihan  1 : Membuat Fungsi Load Data dari File            +
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

nama_file = 'data_mahasiswa.txt'

#membuat fungsi membaca data mahasiswa dari file
def baca_data_mahasiswa(nama_file):
    data_mahasiswa_dict = {} #inisialisasi dictionary kosong
    with open(nama_file, 'r', encoding='utf-8') as file:
        for baris in file :
            baris= baris.strip()#menghilangkan karakter newline
            nim,nama,nilai= baris.split(',')#pecah menjadi data satuan
            data_mahasiswa_dict[nim] = {
                'nama': nama, 
                'nilai': int(nilai)
                }
    return data_mahasiswa_dict

#memanggil fungsi baca_data_mahasiswa
#buka_data = baca_data_mahasiswa(nama_file)
#print("jumlah data terbaca:", len(buka_data))

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+ Prakatikum 2 : Konsep ADT dan File Handling                +
#+ Latihan  2 : Membuat Fungsi Menampilkan data               +
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def tampilkan_data_mahasiswa(data_mahasiswa_dict):

    #membuat tabel header
    print("==================Daftar Mahasiswa=================")
    print(f"{'NIM':<12} | {'Nama':<20} | {'Nilai':>5}")
    print("-" * 45) 
    '''
    untuk tampilan yang rapi, gunakan f-string dengan format spesifikasi lebar kolom
    {'NIM':<12}  : rata kiri dengan lebar 12 karakter
    {'Nama':<20} : rata kiri dengan lebar 20 karakter
    {'Nilai':>5} : rata kanan dengan lebar 5 karakter
    '''

    for nim in sorted(data_mahasiswa_dict.keys()):
        nama = data_mahasiswa_dict[nim]['nama']
        nilai = data_mahasiswa_dict[nim]['nilai']
        print(f"{nim:<12} | {nama:<20} | {nilai:<5}")

#memanggil fungsi tampilkan_data_mahasiswa
#tampilkan_data_mahasiswa(buka_data)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+ Prakatikum 2 : Konsep ADT dan File Handling                +
#+ Latihan  3 : Membuat Fungsi Mencari data                   +
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def cari_data_mahasiswa(data_mahasiswa_dict,):
    #mencari data mahaisswa berdasarkan NIM
    nim_cari= input("Masukkan NIM yang ingin dicari: ").strip()

    if nim_cari in data_mahasiswa_dict:
        nama = data_mahasiswa_dict[nim_cari]['nama']
        nilai = data_mahasiswa_dict[nim_cari]['nilai']
        print("\n=======Data ditemukan:===========")
        print(f"NIM    :     {nim_cari}")
        print(f"Nama   :     {nama}")
        print(f"Nilai  :     {nilai} ")
    else:
        print("\n Data NIM tidak ditemukan")

#memanggil fungsi cari_data_mahasiswa
#cari_data_mahasiswa(buka_data)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+ Prakatikum 2 : Konsep ADT dan File Handling                +
#+ Latihan  4 : Membuat Fungsi Update nilai                   +
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def update_nilai_mahasiswa(data_mahasiswa_dict):
    #mengupdate nilai mahasiswa berdasarkan NIM
    nim= input("Masukkan NIM yang ingin diupdate nilainya: ").strip()

    if nim not in data_mahasiswa_dict:
        print("Data NIM tidak ditemukan")
        return
    try:
        nilai_baru= int(input("Masukkan nilai baru: ").strip())
    except ValueError:
        print("Input nilai tidak valid, harus berupa angka")
        return
    
    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0 sampai 100")
       
    nilai_lama= data_mahasiswa_dict[nim]['nilai']
    data_mahasiswa_dict[nim]['nilai'] = nilai_baru
    print(f"\n=======Update Berhasil: Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}===========")

#memanggil fungsi update_nilai_mahasiswa
#update_nilai_mahasiswa(buka_data)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+ Prakatikum 2 : Konsep ADT dan File Handling                +
#+ Latihan  5 : Membuat Fungsi Menyimpan nilai                +
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def simpan_data_mahasiswa(nama_file, data_mahasiswa_dict):
    with open(nama_file, 'w', encoding='utf-8') as file:
        for nim in sorted(data_mahasiswa_dict.keys()):
            nama= data_mahasiswa_dict[nim]['nama']
            nilai= data_mahasiswa_dict[nim]['nilai']
            file.write(f"{nim},{nama},{nilai}\n")

#simpan_data_mahasiswa(nama_file, buka_data)
#print(f"\nData mahasiswa telah disimpan kembali ke file {nama_file}")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+ Prakatikum 2 : Konsep ADT dan File Handling                +
#+ Latihan  4 : Membuat Fungsi Utama                          +
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def main():
    #mwnjalankan fungsi 1 load data
    buka_data= baca_data_mahasiswa(nama_file)

    while True:
        print("\n=== Menu Data Mahasiswa ===")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Mahasiswa")
        print("3. Update Nilai Mahasiswa")
        print("4. Simpan Data Mahasiswa")
        print("0. Keluar")

        pilihan = input("Masukkan pilihan Anda: ").strip()
        if pilihan == '1':
            tampilkan_data_mahasiswa(buka_data)
        elif pilihan == '2':
            cari_data_mahasiswa(buka_data)
        elif pilihan == '3':
            update_nilai_mahasiswa(buka_data)
        elif pilihan == '4':
            simpan_data_mahasiswa(nama_file, buka_data)
            print(f"Data mahasiswa telah disimpan kembali ke file {nama_file}")
        elif pilihan == '0':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()