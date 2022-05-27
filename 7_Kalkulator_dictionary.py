nama_barang1 = {
    'nama':'Sepatu Niko',
    'harga':150000,
    'diskon':30000
}
nama_barang2 = {
    'nama':'Baju Uniqlo',
    'harga':80000,
    'diskon':8000
}
nama_barang3 = {
    'nama':'Celana Lepis',
    'harga':200000,
    'diskon':60000
}
daftar_belanja = [nama_barang1,nama_barang2,nama_barang3]
print(daftar_belanja)

harga_nama_barang1 = nama_barang1['harga']-nama_barang1['diskon']
harga_nama_barang2 = nama_barang2['harga']-nama_barang2['diskon']
harga_nama_barang3 = nama_barang3['harga']-nama_barang3['diskon']

harga_total = harga_nama_barang1+harga_nama_barang2+harga_nama_barang3

total_pajak = harga_total * 0.1

print (harga_total+total_pajak)


