nama = input("Masukan Nama Karyawan: ")
jam = int(input("Masukan jam karyawan: "))
lembur = 0
total = 0

if jam > 48:
    lembur = jam - 48

    total = (2000 * (jam-lembur)) + (3000 * lembur)
    print("Karyawan atas nama: ", nama)
    print("Upah mingguan karyawan Rp. ", total)
else:
    total = (3000 * jam)
    print("Karyawan atas nama: ", nama)
    print("Upah mingguan karyawan Rp. ", total)