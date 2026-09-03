def pola_sakit_kepala(panjang, lebar):
    panjang = abs(panjang)
    lebar = abs(lebar)

    if panjang != lebar:
        print("Panjang dan lebar harus sama!!")
        return

    if panjang % 2 == 0 or lebar % 2 == 0:
        print("Panjang dan lebar harus bilangan ganjil!!")
        return

    tengah = panjang // 2

    for i in range(panjang):
        for j in range(lebar):
            angka = abs(i - tengah) + abs(j - tengah) + 1

            # Ambil digit paling kiri
            angka = int(str(angka)[0])

            if j == lebar - 1:
                print(angka)
            else:
                print(angka, end=" ")


pola_sakit_kepala(7, 7)