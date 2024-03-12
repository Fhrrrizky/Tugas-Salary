def hitung_gaji(gaji_pokok, jam_kerja_per_hari):
    gaji_harian = gaji_pokok / 8
    gaji_mingguan = gaji_pokok / 8 * 6

    return gaji_harian, gaji_mingguan

def main():
    print("Program Salary")
    print("-" * 20)

    nama_karyawan = input("Nama Karyawan: ")
    gaji_pokok = float(input("Masukkan Gaji Pokok: "))
    jam_kerja_per_hari = int(input("Jumlah Jam Kerja per Hari: "))

    print("\nPilih Rician Gaji Mingguan/ Harian [1/2]: ")
    pilihan = int(input("1. Gaji Harian\n2. Gaji Mingguan\nPilihan: "))

    gaji_harian, gaji_mingguan = hitung_gaji(gaji_pokok, jam_kerja_per_hari)

    if pilihan == 1:
        print("\nOutput:")
        print(f"Nama Karyawan: {nama_karyawan}")
        print(f"Gaji Harian: Rp. {gaji_harian}")
        print(f"Jumlah Jam Kerja per Hari: {jam_kerja_per_hari} Jam")

    elif pilihan == 2:
        print("\nOutput:")
        print(f"Nama Karyawan: {nama_karyawan}")
        print(f"Gaji Mingguan: Rp. {gaji_mingguan}")
        print(f"Jumlah Jam Kerja per Hari: {jam_kerja_per_hari} Jam")

    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
