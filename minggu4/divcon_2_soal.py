# Data mahasiswa dan 5 nilai UG
mahasiswa = [
    {"nama": "Andi", "nilai": [80, 75, 90, 70, 85]},
    {"nama": "Budi", "nilai": [60, 65, 70, 55, 60]},
    {"nama": "Citra", "nilai": [90, 85, 95, 88, 92]},
    {"nama": "Deni", "nilai": [70, 75, 65, 72, 68]},
    {"nama": "Eka", "nilai": [85, 80, 78, 90, 87]},
    {"nama": "Fajar", "nilai": [65, 70, 68, 60, 72]},
    {"nama": "Gina", "nilai": [88, 92, 85, 90, 87]},
    {"nama": "Hadi", "nilai": [75, 80, 70, 78, 72]},
    {"nama": "Intan", "nilai": [55, 60, 65, 58, 62]},
    {"nama": "Joko", "nilai": [78, 82, 75, 80, 85]}
]


# Menghitung rata-rata nilai setiap mahasiswa
rata2 = []
for k in mahasiswa:
    k["avg"] = sum(k["nilai"]) / len(k["nilai"])
    rata2.append(k)

print(rata2)

# Divide and Conquer - Merge Sort
def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2 
    kiri = data[:mid]  
    kanan = data[mid:]

    kiri = merge_sort(kiri)  
    kanan = merge_sort(kanan) 
    return merge(kiri, kanan)


def merge(kiri, kanan):
    result = []  
    i = 0
    j = 0  
    while i < len(kiri) and j < len(kanan):  
        if kiri[i]["avg"] > kanan[j]["avg"]:  
            result.append(kiri[i])  
            i += 1  
        else:  
            result.append(kanan[j])  
            j += 1  
    result.extend(kiri[i:])
    result.extend(kanan[j:])
    return result 


# Menghitung rata-rata keseluruhan
rata2all = sum(k["avg"]for k in mahasiswa) / len(mahasiswa)
# print(rata2all)

# Mengurutkan mahasiswa menggunakan Merge Sort
mahasiswa_urut = merge_sort(mahasiswa)


# Menampilkan hasil rata-rata keseluruhan
print("Rata-rata keseluruhan: ", rata2all)


print("\n=== DI ATAS / SAMA DENGAN RATA-RATA ===")
hasil = merge_sort(mahasiswa)

for i in hasil:
    # for j in 
    if i["avg"] >= rata2all:
        print(i)

    # print(i["avg"])
# if hasil["avg"] > rata2all:
# print(type(hasil["avg"]))
    
# print(hasil)
# Tampilkan List di atas / sama dengan rata-rata


print("\n=== DI BAWAH RATA-RATA ===")

for i in hasil:
    # for j in 
    if i["avg"] < rata2all:
        print(i)
# Tampilkan List di bawah rata-rata

