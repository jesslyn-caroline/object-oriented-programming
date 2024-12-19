import os
from prettytable import PrettyTable

def cls():
    if os.name == 'nt': _ = os.system('cls')
    else: _ = os.system('clear')

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


### ==== Start of Mhs Dsn Class ==== ###

class Parent:
    def __init__ (self, nama, nomorHp, jenisKelamin, As):
        self.nama = nama
        self.nomorHp = nomorHp
        self.jenisKelamin = jenisKelamin
        self.As = As

class Mhs (Parent):
    def __init__ (self, nim, nama, kelas, jam, nomorHp, jenisKelamin):
        super().__init__ (nama, nomorHp, jenisKelamin, 'mhs')
        self.nim = nim
        self.kelas = kelas
        self.jam = jam
        self.jurusan = 'IF' if nim[2:5] == '111' else 'TI' if nim[2:5] == '112' else 'SI' if nim[2:5] == '113' else 'MN' if nim[2:5] == '211' else 'AK'

class Dsn (Parent):
    def __init__ (self, nip, nama, jabatan, nomorHp, jenisKelamin):
        super().__init__ (nama, nomorHp, jenisKelamin, 'dsn')
        self.nip = nip
        self.jabatan = jabatan

### ==== End of Mhs Dsn Class ==== ###


### ==== Start of Mhs Dsn List Class ==== ###

class Lst:
    def __init__ (self):
        self.mhs = []
        self.dsn = []
    
    def searchByNim (self, nim):
        for i in self.mhs:
            if i.nim == nim:
                return i
        
        return False
    
    def searchByNip (self, nip):
        for i in self.dsn:
            if i.nip == nip:
                return i
        
        return False
    
    def searchByNameMhs (self, nama):
        found = []
        for i in self.mhs:
            if i.nama == nama:
                found.append(i)
                
        if (len(found) > 0): return found
        else: return False
    
    def searchByNameDsn (self, nama):
        found = []
        
        for i in self.dsn:
            if i.nama == nama:
                found.append(i)
        
        if (len(found) > 0): return found
        else: return False
    
    def addMhs (self, mhs):
        if not self.searchByNim(mhs.nim):
            self.mhs.append(mhs)
            return True
            
        return False
    
    def addDsn (self, dsn):
        if not self.searchByNip(dsn.nip):
            self.dsn.append(dsn)
            return True
        
        return False
    
    def getList (self):
        tableMhs = PrettyTable()
        tableMhs.field_names = ["NIM", "Nama", "Kelas", "Jam", "Nomor HP", "Jenis Kelamin", "Jurusan"]
        for i in self.mhs:
            tableMhs.add_row([i.nim, i.nama, i.kelas, i.jam, i.nomorHp, i.jenisKelamin, i.jurusan])
        
        tableDsn = PrettyTable()
        tableDsn.field_names = ["NIP", "Nama", "Jabatan", "Nomor HP", "Jenis Kelamin"]
        for i in self.dsn:
            tableDsn.add_row([i.nip, i.nama, i.kelas, i.nomorHp, i.jenisKelamin])
        
        print(f'Daftar Mahasiswa yang hadir')
        print(tableMhs)
        print()
        print()
        print(f'Daftar Dosen yang hadir')
        print(tableDsn)
        print()
        print()
        print(f'Total Mahasiswa yang hadir: {len(self.mhs)}')
        print(f'Total Dosen yang hadir: {len(self.dsn)}')
        print(f'Total kehadiran: {len(self.mhs) + len(self.dsn)}')

### ==== End of Mhs Dsn List Class ==== ###


### ==== Main Program ==== ###

if __name__ == '__main__':
    lst = Lst()
    
    while True:
        cls()
        
        print('Menu')
        print('-' * 50)
        print('1. Lihat daftar kehadiran')
        print('2. Tambah pengunjung')
        print('3. Mencari pengunjung')
        print('4. Exit')
        print('-' * 50)
        
        
        optionValid = False
        while not optionValid:
            try:
                op = input("Pilihan menu ( 1 / 2 / 3 / 4 ): ")
                if len(op) == op.count(" "): raise ValueError('Opsi tidak boleh kosong')
                if not op.isnumeric(): raise ValueError('Opsi harus berupa angka')
                if op not in ['1', '2', '3', '4']: raise ValueError('Opsi yang tersedia hanya 1 / 2 / 3 / 4')
                
                optionValid = True
            
            except ValueError as err:
                print(f'Invalid Input: {err}')
        
        cls()
        
        if op == '1':
            lst.getList()
        
        elif op == '2':
            print('Tambah pengunjung')
            print('-' * 50)
            print('1. Mahasiswa')
            print('2. Dosen')
            print('-' * 50)
            
            optionValid = False
            while not optionValid:
                op = input('Pilihan opsi ( 1 / 2 ): ')
                
                if len(op) == op.count(" "): raise ValueError('Opsi tidak boleh kosong')
                if not op.isnumeric(): raise ValueError('Opsi harus berupa angka')
                if op not in ['1', '2']: raise ValueError('Opsi yang tersedia hanya 1 / 2')
                
                optionValid = True
            
            except ValueError as err:
                print(f'Invalid Input: {err}')
            
            
            if op == '1':
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
        
                mhs = Mhs(nim, nama, kelas, jam, nomorHp, jenisKelamin)
                pos = lst.addMhs(mhs)
                
                if pos: print('Mahasiswa tersebut berhasil ditambahkan')
                else print('Mahasiswa sudah terdaftar sebelumnya')
            
            elif op == '2':
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
        
                dsn = Dsn(nip, nama, jabatan, nomorHp, jenisKelamin)
        
        elif op == '3':
            print('Mencari pengunjung')
            print('-' * 50)
            print('1. Mahasiswa')
            print('2. Dosen')
            print('-' * 50)
            
            optionValid = False
            while not optionValid:
                op = input('Pilihan opsi ( 1 / 2 ): ')
                
                if len(op) == op.count(" "): raise ValueError('Opsi tidak boleh kosong')
                if not op.isnumeric(): raise ValueError('Opsi harus berupa angka')
                if op not in ['1', '2']: raise ValueError('Opsi yang tersedia hanya 1 / 2')
                
                optionValid = True
            
            except ValueError as err:
                print(f'Invalid Input: {err}')
            
            print()
            print('-' * 50)
            print('1. NIM / NIP')
            print('2. Nama')
            print('-' * 50)
            print()
            
            if op == '1':
                searchBy = input('Pencarian berdasarkan ( 1 / 2 ): ')
                
                if searchBy == '1':
                    nim = None
                    nimValid = False
                    while not nimValid:
                        try:
                            nim = str(input("NIM: "))
                            nimValid = checkCodeValidity(nim)
            
                        except ValueError as err:
                            print(f"Error: {err}")
                    
                    found = lst.searchByNim(nim)
                    if found: print('Mahasiswa tersebut ditemukan di dalam daftar')
                    else: print('Mahasiswa tersebut tidak terdaftar')
                
                elif searchBy == '2':
                    nama = None
                    nameValid = False
                    while not nameValid:
                        try:
                            nama = str(input("Nama: ")).lower()
                            nameValid = checkNameValidity(nama)
            
                        except ValueError as err:
                            print(f"Error: {err}")
                    
                    found = lst.searchByNamaMhs(nama)
                    if found: 
                        table = PrettyTable()
                        table.field_names = ["NIM", "Nama", "Kelas", "Jam", "Nomor HP", "Jenis Kelamin", "Jurusan"]
                        for i in found:
                            table.add_row([i.nim, i.nama, i.kelas, i.jam, i.nomorHp, i.jenisKelamin, i.jurusan])
                        
                        print(table)
                        
                    else: print('Mahasiswa tersebut tidak terdaftar')
            
            elif op == '2':
                searchBy = input('Pencarian berdasarkan ( 1 / 2 ): ')
                
                if searchBy == '1':
                    nim = None
                    nimValid = False
                    while not nimValid:
                        try:
                            nim = str(input("NIM: "))
                            nimValid = checkCodeValidity(nim)
            
                        except ValueError as err:
                            print(f"Error: {err}")
                    
                    found = lst.searchByNim(nim)
                    if found: print('Mahasiswa tersebut ditemukan di dalam daftar')
                    else: print('Mahasiswa tersebut tidak terdaftar')
                
                elif searchBy == '2':
                    nama = None
                    nameValid = False
                    while not nameValid:
                        try:
                            nama = str(input("Nama: ")).lower()
                            nameValid = checkNameValidity(nama)
            
                        except ValueError as err:
                            print(f"Error: {err}")
                    
                    found = lst.searchByNamaDsn(nama)
                    if found: 
                        table = PrettyTable()
                        table.field_names = ["NIP", "Nama", "Jabatan", "Nomor HP", "Jenis Kelamin"]
                        for i in self.dsn:
                            table.add_row([i.nip, i.nama, i.kelas, i.nomorHp, i.jenisKelamin])
                        
                        print(table)
                        
                    else: print('Dosen tersebut tidak terdaftar')
        
        elif op == '4':
            print("Thank you")
            break
        
        input("Any button to continue")