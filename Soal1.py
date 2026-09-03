def piramida_angka(angka):
    for i in range(1, angka+1):
        print (" " * (angka - 1), end = " ")

    for j in range(1, i + 1):
        if j == i and i == 1:
            print(j, end = " ")
        else:
            print(j, end = " ")

    for j in range(i -1, 0, -1):
        if j == 1:
            print (j, end = " ")
        else:
            print(j, end = " ")
        
n = int(input("masukkan angka piramida: "))
piramida_angka(n)