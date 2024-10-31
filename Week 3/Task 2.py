from abc import ABC, abstractmethod

class List:
    def __init__(self):
        self.inventory = set()
    
    def addToList(self, student):
        self.inventory.add(student)
    
    def printList(self):
        if len(self.inventory) == 0:
            print("Belum ada siswa terdaftar")
        else:
            for i in self.inventory:
                print(f"[{i.nama}] - Tingkat: {i.tingkat}, Biaya: Rp {i.biaya}")
    
    def search(self, nomorHp, nama, tingkat):
        for i in self.inventory:
            if i.nomorHp == nomorHp and i.nama == nama and i.tingkat == tingkat:
                return True
        return False

class Student(ABC):
    @abstractmethod
    def message(self):
        pass

class Parent:
    def __init__(self, nama, nomorHp, tingkat):
        self.nama = nama
        self.nomorHp = nomorHp
        self.tingkat = tingkat
        self.biaya = "500000" if tingkat == "SD" else "800000" if tingkat == "SMP" else "1200000"


class SD(Parent, Student):
    def __init__(self, nama, nomorHp, tingkat, jenisKelamin):
        super().__init__(nama, nomorHp, tingkat)
        self.jenisKelamin = jenisKelamin

    def message(self):
        print(f"{self.nama} terdaftar sebagai siswa SD. Biaya: Rp {self.biaya}")

class SMP(Parent, Student):
    def __init__(self, nama, nomorHp, tingkat, umur):
        super().__init__(nama, nomorHp, tingkat)
        self.umur = umur

    def message(self):
        print(f"{self.nama} terdaftar sebagai siswa SMP. Biaya: Rp {self.biaya}")

class SMA(Parent, Student):
    def __init__(self, nama, nomorHp, tingkat, jurusan):
        super().__init__(nama, nomorHp, tingkat)
        self.jurusan = jurusan

    def message(self):
        print(f"{self.nama} terdaftar sebagai siswa SMA jurusan {self.jurusan}. Biaya: Rp {self.biaya}")


lst = List()

while True:
    print("Menu")
    print("=" * 30)
    print("1. Daftar Siswa")
    print("2. Tambah Siswa")
    print("3. Exit")
    
    op = int(input("Pilih menu ( 1 / 2 / 3 ) : "))
    
    if op == 1:
        print("Daftar Siswa")
        print("=" * 30)
        lst.printList()
    
    elif op == 2:
        nama = str(input("Nama: "))
        nomorHp = str(input("Nomor HP: "))
        tingkat = str(input("Tingkat ( SD / SMP / SMA ): ")).upper()
        
        if tingkat == "SD":
            jenisKelamin = str(input("Jenis Kelamin: "))
            student = SD(nama, nomorHp, tingkat, jenisKelamin)
            found = lst.search(nomorHp, nama, tingkat)
            if not found:
                lst.addToList(student)
                student.message()
            else:
                print("Murid tersebut sudah pernah terdaftar.")
        
        elif tingkat == "SMP":
            umur = str(input("Umur: "))
            student = SMP(nama, nomorHp, tingkat, umur)
            found = lst.search(nomorHp, nama, tingkat)
            if not found:
                lst.addToList(student)
                student.message()
            else:
                print("Murid tersebut sudah pernah terdaftar.")
        
        elif tingkat == "SMA":
            jurusan = str(input("Jurusan: "))
            student = SMA(nama, nomorHp, tingkat, jurusan)
            found = lst.search(nomorHp, nama, tingkat)
            if not found:
                lst.addToList(student)
                student.message()
            else:
                print("Murid tersebut sudah pernah terdaftar.")

    elif op == 3:
        print("Thank you!")
        break
