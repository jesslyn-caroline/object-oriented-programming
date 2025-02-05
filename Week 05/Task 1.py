import pickle

def saveToFile(data):
    with open("Absensi", "wb") as file:
        pickle.dump(data, file)

def loadFromFile():
    try:
        with open("Absensi", "rb") as file:
            return pickle.load(file)
        
    except FileNotFoundError:
        return []

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

def getJurusan(nim):
    if nim == "111":
        return "Teknik Informatika"
    elif nim == "112":
        return "Teknologi Informasi"
    elif nim == "113":
        return "Sistem Informasi"
    elif nim == "211":
        return "Management"
    elif nim == "212":
        return "Akuntansi"

class Absensi:
    def __init__ (self):
        self.absensi = loadFromFile()
        
    def addToList (self, data):
        self.absensi.append(data)
        saveToFile(self.absensi)
    
    def searchByNim(self, nim):
        for i in self.absensi:
            if i.nim == nim:
                return i
        
        return False
    
    def searchByName(self, nama):
        found = []
        for i in self.absensi:
            if i.nama == nama:
                found.append(i)
        
        if len(found) != 0:
            return found

        return False
    
    def printAbsensi(self):
        print("Daftar Hadir")
        print("="*30)
        if len(self.absensi) == 0:
            print("Belum ada mahasiswa yang hadir")
        else:
            for i in self.absensi:
                print(f"[ {i.nim} ] [ {i.nama.title()} ] [ {i.nomorHp} ]  [ {i.jurusan} ]")
            

class Mhs:
    def __init__ (self, nim, nama, nomorHp):
        self.nim = nim
        self.nama = nama
        self.nomorHp = nomorHp
        self.jurusan = getJurusan(self.nim[2:5])
    
absensi = Absensi()    
    
while True:
    print("Menu")
    print("="*30)
    print("1. Lihat absensi")
    print("2. Mencari mahasiswa di daftar absensi")
    print("3. Tambah daftar absensi")
    print("4. Exit")

    op = int(input("Pilihan Menu ( 1 / 2 / 3 / 4 ) : "))
    
    if op == 1:
        absensi.printAbsensi()
    
    elif op == 2:
        searchByValid = False
        while not searchByValid:
            try:
                searchBy = str(input("Cari berdasarkan ( NIM / Nama ) : ")).lower()
                if searchBy.count(" ") == len(searchBy):
                    raise ValueError("Tidak boleh kosong")
                
                if searchBy != "nim" and searchBy != "nama":
                    raise ValueError("Harus berdasarkan NIM / Nama")
                
                searchByValid = True
                
            except ValueError as err:
                print(f"Invalid input : {err}")
        
        found = False
        
        if searchBy == "nim":
            nim = None
            codeValid = False

            while not codeValid:
                try:
                    nim = str(input("NIM yang dicari : "))
                    codeValid = checkCodeValidity(nim)
                
                except ValueError as err:
                    print(f"Invalid input : {err}")
            


            found = absensi.searchByNim(nim)
            if not found:
                print("Mahasiswa tersebut tidak ada di dalam daftar")
            else:
                print("Mahasiswa tersebut ditemukan")
                print(f"[ {found.nim} ] [ {found.nama} ] [ {found.nomorHp} ] [ {found.jurusan} ]")
        
        else:
            nama = str(input("Nama yang dicari : ")).lower()
            
            found = absensi.searchByName(nama)
            if not found:
                print("Mahasiswa tersebut tidak ada di dalam daftar")
            else:
                print("Mahasiswa tersebut ditemukan")
                for i in found:
                    print(f"[ {i.nim} ] [ {i.nama.title()} ] [ {i.nomorHp} ] [ {i.jurusan} ]")
        
    elif op == 3:
        nim = None
        nimValid = False
        while not nimValid:
            try:
                nim = str(input("NIM : "))
                nimValid = checkCodeValidity(nim)
                
            except ValueError as err:
                print(f"Invalid input : {err}")
        
        nama = None
        namaValid = False
        while not namaValid:
            try:
                nama = str(input("Nama : ")).lower()
                namaValid = checkNameValidity(nama)
            
            except ValueError as err:
                print(f"Invalid input : {err}")
        
        nomorHp = False
        nomorHpValid = False
        while not nomorHpValid:
            try:
                nomorHp = str(input("Nomor HP : "))
                nomorHpValid = checkPhoneNumValidity(nomorHp)
            
            except ValueError as err:
                print(f"Invalid input : {err}")
        
        mhs = Mhs(nim, nama, nomorHp)

        found = absensi.searchByNim(nim)
        if found:
            print("Mahasiswa tersebut sudah ada di dalam daftar")    
        else: 
            absensi.addToList(mhs)
            print("Mahasiswa tersebut telah ditambahkan")
    
    elif op == 4:
        print("Thank you!")
        break
