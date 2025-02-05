class List:
    def __init__ (self):
        self.dataMhs = []
        self.dataDsn = []
    
    def addToListMhs (self, data):
        self.dataMhs.append(data)
    
    def addToListDsn (self, data):
        self.dataDsn.append(data)
    
    def printOut(self):
        print(f"List Mahasiswa yang hadir")
        print("="*30)
        if len(self.dataMhs) == 0:
            print("Belum ada daftar kehadiran")
        else:
            for i in self.dataMhs:
                print(f"[ Nomor Induk : {i.nomorInduk} ] - [ Nama : {i.nama} ] - [ Jenis Kelamin : {i.jenisKelamin} ] - [ Nomor HP : {i.nomorHp} ] - [ Kelas : {i.kelas} ] - [ Jurusan : {i.jurusan} ]")
        print()
        print(f"List Dosen yang hadir")
        print("="*30)
        if len(self.dataDsn) == 0:
            print("Belum ada daftar kehadiran")
        else:
            for i in self.dataDsn:
                print(f"[ Nomor Induk : {i.nomorInduk} ] - [ Nama : {i.nama} ] - [ Jenis Kelamin : {i.jenisKelamin} ] - [ Nomor HP : {i.nomorHp} ] - [ Jabatan : {i.jabatan} ]")
        print()
    
    def searchMhs(self, nomorInduk):
        for i in self.dataMhs:
            if i.nomorInduk == nomorInduk:
                return True
        return False
    
    def searchDsn(self, nomorInduk):
        for i in self.dataDsn:
            if i.nomorInduk == nomorInduk:
                return True
        return False
    
class Parent:
    def __init__ (self, nomorInduk, nama, jenisKelamin, nomorHp):
        self.nomorInduk = nomorInduk
        self.nama = nama
        self.jenisKelamin = jenisKelamin
        self.nomorHp = nomorHp
    
class Mhs(Parent):
    def __init__ (self, nomorInduk, nama, jenisKelamin, nomorHp, kelas, jurusan):
        super().__init__(nomorInduk, nama, jenisKelamin, nomorHp)
        self.kelas = kelas
        self.jurusan = jurusan
        
    def printOut (self):
        print(f"[ Nomor Induk : {self.nomorInduk} ] - [ Nama : {self.nama} ] - Hadir")

class Dsn(Parent):
    def __init__ (self, nomorInduk, nama, jenisKelamin, nomorHp, jabatan):
        super().__init__(nomorInduk, nama, jenisKelamin, nomorHp)
        self.jabatan = jabatan
    
    def printOut (self):
        print(f"[ Nama : {self.nama} ] - [ Nomor HP : {self.nomorHp} ] - Hadir")

data_list = List()

while True:
    print("Menu")
    print("="*30)
    print("1. Tambah Mahasiswa")
    print("2. Tambah Dosen")
    print("3. Tampilkan Daftar")
    print("4. Keluar")
    print("="*30)
    
    option = input("Pilih opsi ( 1 / 2 / 3 / 4 ) : ")

    if option == '1':
        nomorInduk = input("Nomor Induk: ")
        nama = input("Nama: ")
        jenisKelamin = input("Jenis Kelamin: ")
        nomorHp = input("Nomor HP: ")
        kelas = input("Kelas: ")
        jurusan = input("Jurusan: ")
        mhs = Mhs(nomorInduk, nama, jenisKelamin, nomorHp, kelas, jurusan)
        
        if not data_list.searchMhs(mhs.nomorInduk):
            data_list.addToListMhs(mhs)
            print("Mahasiswa tersebut berhasil ditambahkan!")
            mhs.printOut()
            print()
        else:
            print("Mahasiswa tersebut telah ditambahkan sebelumnya")

    elif option == '2':
        nomorInduk = input("Nomor Induk: ")
        nama = input("Nama: ")
        jenisKelamin = input("Jenis Kelamin: ")
        nomorHp = input("Nomor HP: ")
        jabatan = input("Jabatan: ")
        dsn = Dsn(nomorInduk, nama, jenisKelamin, nomorHp, jabatan)
        
        if not data_list.searchDsn(dsn.nomorInduk):
            data_list.addToListDsn(dsn)
            print("Dosen berhasil ditambahkan!")
            dsn.printOut()
            print()
        else:
            print("Dosen tersebut telah ditambahkan sebelumnya")

    elif option == '3':
        data_list.printOut()

    elif option == '4':
        break
