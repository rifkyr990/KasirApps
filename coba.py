total = []
Jumlah = []
def kolbak():
    print('=========== ColtBack ===========')
    print('=== Kopsu 6.000               ==')
    print('=== Rokok 5.000               ==')
    print('================================')
    pilih = int(input('Pilih Menu : '))
    if pilih == 1:
        jml1 = int(input('Jumlah yang dibeli ? '))
        total1 = jml1 * 6000
        Jumlah.append(jml1)
        total.append(total1)
        tanya()

    elif pilih == 2:
        jml2 = int(input('Jumlah yang di beli ? '))
        total2 = jml2 * 5000
        Jumlah.append(jml2)
        total.append(total2)
        tanya()

    else:
        print('Barang tidak tersedia')
    return

def tanya():
    tanya1 = input('apakah ada tambahan lain ? ')
    if tanya1 == 'y':
        kolbak()
    elif tanya1 == 't':
        akhir()
    return

def akhir():
    A = sum(total)
    B = sum(Jumlah)
    print('Total belanja anda ', A)
    bayar = int(input('Bayar : '))
    kembali = bayar - A
    print('Jumlah uang yang dibayar : ', bayar)
    print('Kembali : ', kembali)

kolbak()