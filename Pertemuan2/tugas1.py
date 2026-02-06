# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama  : Pratama Fahriel Sanjaya
# NIM   : J0403251053
# Kelas : TPL B2
# ==========================================================


# -------------------------------
# Konstanta nama file
# -------------------------------

nama_file = "Pertemuan2/stok_barang.txt"

# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------

def baca_stok(nama_file):
    """
    Membaca data stok dari file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    Output: - stok_dict (dictionary)
    key   = kode_barang
    value = {"nama": nama_barang, "stok": stok_int}
    """
    stok_dict = {}
    # Buka file dan baca seluruh baris
    with open(nama_file, "r", encoding="utf-8") as f:
        for baris in f:
            baris = baris.strip()  # gunakan strip() untuk menghilangkan \n
            kode, nama, stok = baris.split(",") # pisah berdasarkan koma
            stok_dict[kode] = {
                "nama": nama, "stok": int(stok)
                }
    return stok_dict


# -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------
def tampilkan_semua(stok_dict):
    """
    Menampilkan semua barang di stok_dict.
    """
    # membuat tabel header
    print("==================Daftar Stok Barang=================")
    print(f"{'Kode':<10} | {'Nama':<20} | {'Stok':>5}")
    print("-" * 45)
    for kode in sorted(stok_dict.keys()):
        nama = stok_dict[kode]['nama']
        stok = stok_dict[kode]['stok']
        print(f"{kode:<10} | {nama:<20} | {stok:<5}")


# -------------------------------
# Fungsi: Cari barang berdasarkan kode
# -------------------------------
def cari_barang(stok_dict):
    """
    Mencari barang berdasarkan kode barang.
    """
    kode = input("Masukkan kode barang: ").strip()

    # Cek apakah kode ada di dictionary
    if kode in stok_dict:
        # Jika ada: tampilkan detail barang
        nama = stok_dict[kode]['nama']
        stok = stok_dict[kode]['stok']
        print("\n=======Detail Barang===========")
        print(f"Kode  : {kode}")
        print(f"Nama  : {nama}")
        print(f"Stok  : {stok}")
    else:
        # Jika tidak ada: tampilkan 'Barang tidak ditemukan'
        print("Barang tidak ditemukan.")

# -------------------------------
# Fungsi: Tambah barang baru
# -------------------------------
def tambah_barang(stok_dict):
    """
    Menambah barang baru ke stok_dict.
    """
    kode = input("Masukkan kode barang baru: ").strip()
    nama = input("Masukkan nama barang: ").strip()
    # Validasi kode tidak boleh duplikat
    if kode in stok_dict:
        # Jika sudah ada: tampilkan 'Kode sudah digunakan' dan return
        print("Kode sudah digunakan.")
        return
    # Input stok awal (integer)
    stok_awal = int(input("Masukkan stok awal: "))
    # Simpan ke dictionary
    stok_dict[kode] = {"nama": nama, "stok": stok_awal}
    print("Barang berhasil ditambahkan.")


# -------------------------------
# Fungsi: Update stok barang
# -------------------------------
def update_stok(stok_dict):
    """
    Mengubah stok barang (tambah atau kurangi).
    Stok tidak boleh menjadi negatif.
    """
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip()
    # Cek apakah kode ada di dictionary
    if kode not in stok_dict:
        # Jika tidak ada: tampilkan pesan dan return
        print("Barang tidak ditemukan.")
        return

    print("Pilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")

    pilihan = input("Masukkan pilihan (1/2): ").strip()

    # Input jumlah perubahan stok
    jumlah = int(input("Masukkan jumlah: "))

    # Jika pilihan 1: stok = stok + jumlah
    if pilihan == "1":
        stok_dict[kode]["stok"] += jumlah
    # Jika pilihan 2: stok = stok - jumlah
    elif pilihan == "2":
        if stok_dict[kode]["stok"] - jumlah < 0:
            # Jika hasil < 0: batalkan dan tampilkan error
            print("Stok tidak boleh negatif.")
            return
        stok_dict[kode]["stok"] -= jumlah
    else:
        print("Pilihan tidak valid.")
        return

    print("Stok berhasil diupdate.")



# -------------------------------
# Fungsi: Menyimpan data ke file
# -------------------------------

def simpan_stok(nama_file, stok_dict):
    """
    Menyimpan seluruh data stok ke file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    """
    with open(nama_file, "w", encoding="utf-8") as f:
        for kode in sorted(stok_dict.keys()):
            nama = stok_dict[kode]['nama']
            stok = stok_dict[kode]['stok']
            f.write(f"{kode},{nama},{stok}\n")

# -------------------------------
# Program Utama
# -------------------------------
def main():
    # Membaca data dari file saat program mulai
    stok_barang = baca_stok(nama_file)

    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_semua(stok_barang)

        elif pilihan == "2":
            cari_barang(stok_barang)

        elif pilihan == "3":
            tambah_barang(stok_barang)

        elif pilihan == "4":
            update_stok(stok_barang)

        elif pilihan == "5":
            simpan_stok(nama_file, stok_barang)
            print("Data berhasil disimpan.")

        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
# Menjalankan program utama
if __name__ == "__main__":
    main()
