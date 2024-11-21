### ==== Start of Other stuff ==== ###
import os 

def cls():
    if os.name == 'nt':  
        os.system('cls')
    else:
        os.system('clear')

### ==== End of Other stuff ==== ###


### ==== Start of Input Handle ==== ###
def checkNipValidity(kode):
    if len(kode) == 0 or kode.count(" ") == len(kode):
        raise ValueError("Kode tidak boleh kosong")

    if len(kode) != 9:
        raise ValueError("Kode harus memiliki 9 angka")

    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    for i in kode:
        if i not in num:
            raise ValueError(f"Kode hanya boleh berupa angka")
            
    return True
    
def checkCodeValidity(kode):
    if len(kode) == 0 or kode.count(" ") == len(kode):
        raise ValueError("Kode tidak boleh kosong")
        
    if len(kode) != 9:
        raise ValueError("Kode harus memiliki 9 angka")
    
    if int(kode[0:2]) > 24:
        raise ValueError("Kode tahun angkatan tidak valid")
    
    if kode[2:5] not in ["111", "112", "113", "211", "212"]:
        raise ValueError(f"Kode jurusan tidak valid")
        
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    for i in kode:
        if i not in num:
            raise ValueError(f"Kode hanya boleh berupa angka")
            
    return True

def checkNameValidity(nama):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
    'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
    if len(nama) == 0 or nama.count(" ") == len(nama):
        raise ValueError("Nama tidak boleh kosong")
        
    for i in nama:
        if i not in letters and i != " ":
            raise ValueError("Nama hanya boleh berupa huruf dan spasi")
            
    return True

def checkGenderValidity (jenisKelamin):
    if len(jenisKelamin) == 0 or jenisKelamin.count(" ") == len(jenisKelamin):
        raise ValueError("Jenis Kelamin tidak boleh kosong")

    if jenisKelamin != 'L' and jenisKelamin != 'P':
        raise ValueError("Jenis kelamin hanya boleh berupa P atau L")

    return True

def checkPhoneNumValidity (nomorHp):
    if len(nomorHp) == 0 or nomorHp.count(" ") == len(nomorHp):
        raise ValueError("Nomor HP tidak boleh kosong")
    
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    if nomorHp[0] != '+':
        raise ValueError("Nomor HP harus berawal dengan tanda '+'")
                
    nomorHpLength = len(nomorHp)
    if nomorHpLength < 8 or nomorHpLength > 15:
        raise ValueError("Nomor HP hanya boleh terdiri dari 8 - 12 karakter")
        
    for i in range (1, nomorHpLength):
        if nomorHp[i] not in num and nomorHp[i] != " ":
            raise ValueError("Nomor HP hanya boleh terdiri dari nomor dan spasi")
            
    return True

def checkClassValidity(kelas):
    if len(kelas) == 0 or kelas.count(" ") == len(kelas):
        raise ValueError("Kelas tidak boleh kosong")

    if kelas != "A" and kelas != "B" and kelas != "C":
        raise ValueError("Kelas hanya ada A / B / C")

    return True

def checkTimeValidity(jam):
    if len(jam) == 0 or jam.count(" ") == len(jam):
        raise ValueError("Jam tidak boleh kosong")

    if jam != "sore" and jam != "pagi":
        raise ValueError("Hanya tersedia opsi Pagi dan Sore")

    return True

### ==== End of Input Handle ==== ###


### ==== Start of Mhs and Dsn Class ==== ###

class Mhs:
    def __init__ (self, nim, nama, jenisKelamin, nomorHp, kelas, jam):
        self.nim = nim
        self.nama = nama
        self.jenisKelamin = jenisKelamin
        self.nomorHp = nomorHp
        self.kelas = kelas
        self.jam = jam
        self.jurusan = "IF" if nim[2:5] == "111" else "TI" if nim[2:5] == "112" else "SI" if nim[2:5] == "113" else "MN" if nim[2:5] == "211" else "AK"
        self.As = "mhs"
        
class Dsn:
    def __init__ (self, nip, nama, jenisKelamin, nomorHp, jabatan):
        self.nip = nip
        self.nama = nama
        self.jenisKelamin = jenisKelamin
        self.nomorHp = nomorHp
        self.jabatan = jabatan
        self.As = "dsn"

### ==== End of Mhs and Dsn Class ==== ###       


### ==== Start of Absensi Class ==== ###
class Absensi:
    def __init__ (self, strategyMhs = False, strategyDsn = False):
        self.mhs = []
        self.dsn = []
        self.strategyMhs = strategyMhs
        self.strategyDsn = strategyDsn

    def addToMhs (self, data):
        self.mhs.append(data)

    def addToDsn (self, data):
        self.dsn.append(data)
    
    def printAbsensi(self):
        print("Daftar Mahasiswa yang hadir")
        print("="*40)
        if len(self.mhs) == 0:
            print("Belum ada mahasiswa yang hadir")
        else:
            for i in self.mhs:
                print(f"[ {i.nim} ] - [ {i.nama.title()} ] - [ {i.jenisKelamin.title()} ] - [ {i.nomorHp} ] - [ {i.jurusan}-{i.kelas.title()} {i.jam.title()} ]")
        print()
        self.strategyMhs = GetSum()
        totalMhs = self.strategyMhs.getSum(self.mhs)
        print(f"Jumlah mahasiswa yang hadir: {totalMhs}")
        self.strategyMhs = False
        print()
        print()
        
        print("Daftar Dosen yang hadir")
        print("="*40)
        if len(self.dsn) == 0:
            print("Belum ada dosen yang hadir")
        else:
            for i in self.dsn:
                print(f"[ {i.nip} ] - [ {i.nama.title()} ] - [ {i.jenisKelamin.title()} ] - [ {i.nomorHp} ] - [ {i.jabatan.title()} ]")
        print()
        self.strategyDsn = GetSum()
        totalDsn = self.strategyDsn.getSum(self.dsn)
        print(f"Jumlah dosen yang hadir: {totalDsn}")
        self.strategyDsn = False
        print()
        print()

        print(f"Total Kehadiran: {totalDsn + totalMhs}")
        
    def searchByNimMhs (self, nim):
        for i in self.mhs:
            if i.nim == nim:
                return i

        return False
    
    def searchByNameMhs (self, nama):
        found = []
        for i in self.mhs:
            if i.nama == nama:
                found.append(i)
        
        return found

    def searchByNipDsn (self, nip):
        for i in self.dsn:
            if i.nip == nip:
                return i

        return False
    
    def searchByNameDsn (self, nama):
        found = []
        for i in self.dsn:
            if i.nama == nama:
                found.append(i)
        
        return found

    def sortedByMhs (self, num):
        if num == 1:
            self.strategyMhs = SortedByNim()
        elif num == 2:
            self.strategyMhs = SortedByNama()
        elif num == 3:
            self.strategyMhs = SortedByJurusan()
        
        self.mhs = self.strategyMhs.sorting(self.mhs)
    
    def sortedByDsn (self, num): 
        if num == 1:
            self.strategyDsn = SortedByNip()
        elif num == 2:
            self.strategyDsn = SortedByNama()
        
        self.dsn = self.strategyDsn.sorting(self.dsn)

### ==== End of Absensi Class ==== ###


### ==== Start of Strategy Class ==== ###

class SortedByNim:
    def sorting (self, data):
        return sorted(data, key=lambda x: x.nim)
        
class SortedByNama:
    def sorting (self, data):
        return sorted(data, key=lambda x: x.nama)

class SortedByJurusan:
    def sorting (self, data):
        return sorted(data, key=lambda x: x.jurusan)

class SortedByNip:
    def sorting (self, data):
        return sorted(data, key=lambda x: x.nip)

class GetSum:
    def getSum(self, data):
        return len(data)

### ==== Start of Strategy Class ==== ###


### ==== Main Program === ###
absensi = Absensi()

while True:
    cls()
    print("Menu")
    print("="*30)
    print("1. Lihat Absensi")
    print("2. Mencari data")
    print("3. Mengurutkan data")
    print("4. Tambah data mahasiswa")
    print("5. Tambah data dosen")
    print("6. Exit")
    
    op = int(input("Pilihan menu ( 1 / 2 / 3 / 4 / 5 / 6 ):"))

    cls()
    if op == 1:
        absensi.printAbsensi()
    
    elif op == 2:
        option = str(input("Data apa yang ingin dicari ( Mahasiswa / Dosen )? ")).lower()
        
        if option == "mahasiswa":
            searchBy = str(input("Pencarian berdasarkan ( nim / nama )? ")).lower()
            if searchBy == "nim":
                nim = str(input("NIM data yang dicari: "))
                found = absensi.searchByNimMhs(nim)

                if found:
                    print("Data ditemukan")
                    print(f"NIM: {found.nim}")
                    print(f"Nama: {found.nama}")
                    print(f"Nomor HP: {found.nomorHp}")
                    print(f"Jenis Kelamin: {found.jenisKelamin}")
                    print(f"Kelas: {found.jurusan}-{found.kelas} {found.jam}")
                else:
                    print("Data tidak ditemukan")
                    
            elif searchBy == "nama":
                nama = str(input("Nama data yang dicari: ")).lower()
                found = absensi.searchByNameMhs(nama)

                if found:
                    for i in found:
                        print(f"Nama: {i.nama}")
                        print(f"NIM: {i.nim}")
                        print(f"Nomor HP: {i.nomorHp}")
                        print(f"Jenis Kelamin: {i.jenisKelamin}")
                        print(f"Kelas: {i.jurusan}-{i.kelas} {i.jam}")
                else:
                    print("Data tidak ditemukan")

        elif option == "dosen":
            searchBy = str(input("Pencarian berdasarkan ( nip / nama )? ")).lower()
            if searchBy == "nip":
                nip = str(input("NIP data yang dicari: "))
                found = absensi.searchByNipDsn(nip)

                if found:
                    print("Data ditemukan")
                    print("="*40)
                    print(f"NIP: {found.nip}")
                    print(f"Nama: {found.nama}")
                    print(f"Nomor HP: {found.nomorHp}")
                    print(f"Jenis Kelamin: {found.jenisKelamin}")
                    print(f"Jabatan: {found.jabatan}")
                    print("="*40)
                else:
                    print("Data tidak ditemukan")
                    
            elif searchBy == "nama":
                nama = str(input("Nama data yang dicari: ")).lower()
                found = absensi.searchByNameDsn(nama)

                if found:
                    for i in found:
                        print("Data ditemukan")
                        print("="*40)
                        print(f"Nama: {i.nama}")
                        print(f"NIP: {i.nip}")
                        print(f"Nomor HP: {i.nomorHp}")
                        print(f"Jenis Kelamin: {i.jenisKelamin}")
                        print(f"Jabatan: {i.jabatan}")
                        print("="*40)
                else:
                    print("Data tidak ditemukan")
    
    elif op == 3:
        print("Pilih data yang ingin diurutkan:")
        print("1. Mahasiswa")
        print("2. Dosen")
        dataOption = int(input("Pilihan ( 1 / 2 ): "))
        
        if dataOption == 1:
            print("Cara pengurutan mahasiswa:")
            print("1. NIM")
            print("2. Nama")
            print("3. Jurusan")
            sortOption = int(input("Pilihan ( 1 / 2 / 3 ): "))
            absensi.sortedByMhs(sortOption)
            print("Data mahasiswa berhasil diurutkan.")

        elif dataOption == 2:
            print("Cara pengurutan dosen:")
            print("1. NIP")
            print("2. Nama")
            sortOption = int(input("Pilihan ( 1 / 2 ): "))
            absensi.sortedByDsn(sortOption)
            print("Data dosen berhasil diurutkan.")
    
    elif op == 4:
        nim = None
        nimValid = False
        while not nimValid:
            try:
                nim = str(input("NIM: "))
                nimValid = checkCodeValidity(nim)

            except ValueError as err:
                print(f"Error: {err}")

        nama = None
        nameValid = False
        while not nameValid:
            try:
                nama = str(input("Nama: ")).lower()
                nameValid = checkNameValidity(nama)

            except ValueError as err:
                print(f"Error: {err}")

        jenisKelamin = None
        genderValid = False
        while not genderValid:
            try:
                jenisKelamin = str(input("Jenis Kelamin ( L / P ): ")).upper()
                genderValid = checkGenderValidity(jenisKelamin)

            except ValueError as err:
                print(f"Error: {err}")

        nomorHp = None
        phoneNumValid = False
        while not phoneNumValid:
            try:
                nomorHp = str(input("Nomor HP: "))
                phoneNumValid = checkPhoneNumValidity(nomorHp)

            except ValueError as err:
                print(f"Error: {err}")

        kelas = None
        classValid = False
        while not classValid:
            try:
                kelas = str(input("Kelas: ")).upper()
                classValid = checkClassValidity(kelas)

            except ValueError as err:
                print(f"Error: {err}")

        jam = None
        timeValid = False
        while not timeValid:
            try:
                jam = str(input("Jam: ")).lower()
                timeValid = checkTimeValidity(jam) 

            except ValueError as err:
                print(f"Error: {err}")

        mhs = Mhs(nim, nama, jenisKelamin, nomorHp, kelas, jam)
        
        found = absensi.searchByNimMhs(nim)
        if found:
            print("Mahasiswa tersebut sudah pernah ditambahkan")
        else:
            absensi.addToMhs(mhs)
            print(f"Mahasiswa {nama.title()} berhasil ditambahkan!")
    
    elif op == 5:
        nip = None
        nipValid = False
        while not nipValid:
            try:
                nip = str(input("NIP: "))
                nipValid = checkNipValidity(nip)

            except ValueError as err:
                print(f"Error: {err}")

        
        nama = None
        nameValid = False
        while not nameValid:
            try:
                nama = str(input("Nama: ")).lower()
                nameValid = checkNameValidity(nama)

            except ValueError as err:
                print(f"Error: {err}")

        jenisKelamin = None
        genderValid = False
        while not genderValid:
            try:
                jenisKelamin = str(input("Jenis Kelamin ( L / P ): ")).upper()
                genderValid = checkGenderValidity(jenisKelamin)

            except ValueError as err:
                print(f"Error: {err}")

        nomorHp = None
        phoneNumValid = False
        while not phoneNumValid:
            try:
                nomorHp = str(input("Nomor HP: "))
                phoneNumValid = checkPhoneNumValidity(nomorHp)

            except ValueError as err:
                print(f"Error: {err}")

        jabatan = str(input("Jabatan: "))

        dsn = Dsn(nip, nama, jenisKelamin, nomorHp, jabatan)

        found = absensi.searchByNipDsn(nip)
        if found:
            print("Dosen tersebut sudah pernah ditambahkan")
        else:
            absensi.addToDsn(dsn)
            print(f"Dosen {nama.title()} berhasil ditambahkan!")
    
    elif op == 6:
        print("Thank you.")
        break

    test = str(input("[ENTER] to continue"))
