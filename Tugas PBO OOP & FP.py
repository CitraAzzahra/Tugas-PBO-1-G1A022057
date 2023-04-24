# Contoh program FP untuk menghitung nilai faktorial (Functional Programming)

def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)

print(faktorial(5))

print("")

# Contoh program OOP untuk membuat kelas "Mahasiswa"

class Mahasiswa:
    def __init__(self, nama, umur, jurusan):
        self.nama = nama
        self.umur = umur
        self.jurusan = jurusan

    def get_nama(self):
        return self.nama

    def get_umur(self):
        return self.umur

    def get_jurusan(self):
        return self.jurusan

mhs1 = Mahasiswa("Citra", 18, "Informatika")
mhs2 = Mahasiswa("Galuch", 19, "Mesin")

print(mhs1.get_nama())
print(mhs2.get_jurusan())
