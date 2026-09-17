import random
from dataMahasiswa import data
from fungsiMahasiswa import show_data, presensi_dummy, acak_data

data = data.copy()
presensi_dummy(data)
acak_data(data)



def sort_by(data: list=data, index: str="presensi",rev = True):
    maps = {
        "nim":0,
        "nama":1,
        "presensi":2,
    }
    
    # Kerjakan disini
    kolom = maps[index]
    for i in range(1, len(data) - 1):
        for j in range(1, len(data) - i):
            if rev == False:
                if data[j][kolom] > data[j + 1][kolom]:
                    data[j], data[j + 1] = data[j + 1], data[j]
            else:
                if data[j][kolom] < data[j + 1][kolom]:
                    data[j], data[j + 1] = data[j + 1], data[j]

    
    # Jangan Dihapus
    show_data(data)

sort_by(data)


    
