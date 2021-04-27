total = []
bbm = []
nama = []
liter = []
lt1 = []
def bensin():
    print('=====================================================')
    print('====             SPBU DJOKO KENDIL               ====')
    print('====                 KUNINGAN                    ====')
    print('=====================================================')
    print('====         1.      Premium             8.500   ====')
    print('====         2.      Solar               7.500   ====')
    print('====         3.      Bio Solar           7.500   ====')
    print('====         4.      Pertamax           10.300   ====')
    print('=====================================================')
    print('====            PT. Maju Mundur Cantik           ====')
    print('=====================================================')
    pilih = int(input('Masukan pilihan : '))
    if pilih == 1:
        print('Jenis BBM Premium Rp 8.500 /liter')
        beli = int(input('Beli berapa ? '))
        jenis = 'Premium'
        lt = 8500
        liter1 = beli / 8500
        lt1.append(lt)
        liter.append(liter1)
        nama.append(jenis)
        total.append(beli)
        bayar()

    elif pilih == 2:
        print('Jenis BBM Solar Rp 7.500.00 /liter')
        beli = int(input('Beli berapa ? '))
        jenis = 'Solar'
        lt = 7500
        liter1 = beli / 7500
        lt1.append(lt)
        liter.append(liter1)
        nama.append(jenis)
        total.append(beli)
        bayar()

    elif pilih == 3:
        print('Jenis BBM Bio Solar Rp 7.500.00 /liter')
        beli = int(input('Beli berapa ? '))
        jenis = 'Bio Solar'
        liter1 = beli / 7500
        lt = 7500
        lt1.append(lt)
        liter.append(liter1)
        nama.append(jenis)
        total.append(beli)
        bayar()

    elif pilih == 4:
        print('Jenis BBM Pertamax Rp 10.300.00 /liter')
        beli = int(input('Beli berapa ? '))
        jenis = 'Pertamax'
        lt = 10300
        liter1 = beli / 10300
        lt1.append(lt)
        liter.append(liter1)
        nama.append(jenis)
        total.append(beli)
        bayar()
    else:
        print('Gagal')
    return
def bayar():
    D = sum(lt1)
    C = sum(liter)
    B = str(nama)[1:-1]
    A = sum(total)
    Plat = input('Plat : ')
    bayar = int(input('Bayar : '))
    kembali = bayar - A
    print('=====================================================')
    print('====               STRUK PEMBAYARAN              ====')
    print('====               SPBU DJOKO KENDIL             ====')
    print('=====================================================')
    print('Total : ', A)
    print('Jenis BBM :'+ B)
    print('Harga per liter : ', D)
    print('Nomor Plat : ', Plat)
    print('Liter : ', C)
    print(f'Jumlah yang di bayar : {bayar}')
    print(f'Kembali : {kembali}')
    print('=====================================================')
    print('====                 Terima Kasih                ====')
    print('=====================================================')
bensin()
