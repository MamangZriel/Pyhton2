# Meminta input total pembelian dari pengguna
total_pembelian = float(input("Masukkan total pembelian: "))

# Menentukan diskon berdasarkan total pembelian
if total_pembelian > 100000:
    diskon = 20
elif 50000 <= total_pembelian <= 100000:
    diskon = 15
elif 10000 <= total_pembelian < 50000:
    diskon = 10
else:
    diskon = 0

# Menampilkan persentase diskon
print(f"Diskon yang diperoleh: {diskon}%")
