import os
from prettytable import PrettyTable 

### ==== Start of Other Stuff ==== ###

def cls():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

### ==== End of Other Stuff ==== ###


### ==== Start of Handle Input ==== ###

def checkNimValidity (nim):
    if nim.count(" ") == len(nim):
        raise ValueError("NIM tidak boleh kosong")
    
    if len(nim) != 9:
        raise ValueError("NIM hanya boleh terdiri dari 9 karakter")
    
    num = "123456789"
    for i in range (len(nim)):
        if nim[i] not in num:
            raise ValueError("NIM hanya boleh berupa angka")
            
    year = int(nim[0:2])
    if year > 24:
        raise ValueError("Tahun pada NIM tidak valid")
    
    jurusan = ["111", "112", "113", "211", "212"]
    if nim[2:5] not in jurusan:
        raise ValueError("Kode jurusan di NIM tidak valid")
    
    return True

def checkNameValidity (nama):
    if nama.count(" ") == len(nama):
        raise ValueError("Nama tidak boleh kosong")
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range (len(nama)):
        if nama[i] not in alphabet:
            raise ValueError("Nama hanya boleh berupa huruf")
    
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

def checkGenderValidity (jenisKelamin):
    if jenisKelamin != 'L' and jenisKelamin != 'P':
        raise ValueError("Jenis Kelamin hanya boleh berupa L / P")
    
    return True

def checkClassValidity (kelas):
    if kelas not in ["A", "B", "C"]:
        raise ValueError("Hanya terdapat kelas A / B / C")
    
    return True

### ==== End of Handle Input ==== ###


### ==== Start of Mhs Class ==== ###

class Mhs:
    def __init__ (self, nim, nama, jenisKelamin, nomorHp, kelas):
        self.nim = nim
        self.nama = nama
        self.jenisKelamin = jenisKelamin
        self.nomorHp = nomorHp
        self.kelas = kelas

### ==== End of Mhs Class ==== ###


### ==== Start of Classes Class ==== ###

class Parent:
    def __init__ (self, dsn):
        self.dsn = dsn
        self.mhs = []
    
    def addToList (self, mhs):
        self.mhs.append(mhs)
    
    def getAbsensi (self):
        return self.mhs
    
    def getDsn (self):
        return self.dsn

class ClassA(Parent):
    def __init__ (self):
        super().__init__("Matematika")

class ClassB(Parent):
    def __init__ (self):
        super().__init__("Pemrograman Komputer")

class ClassC(Parent):
    def __init__ (self):
        super().__init__("Inggris")

### ==== Start of Classes Class ==== ###


### ==== Start of Template Pattern ==== ###

class Template:
    def absensiTable(self, absensi, dsn, option):
        print(f"="*80)
        print(f"{'Kelas': >40} {option: <40}")
        print(f"="*80)
        print()
        if len(absensi) == 0:
            print(f"Belum ada mahasiswa yang hadir")
        else:
            table = PrettyTable()
            table.field_names = ["NIM", "Nama", "Nomor HP", "Kelas"]
            for i in absensi:
                table.add_row([i.nim, i.nama, i.nomorHp, i.kelas])
            
            print(table)
            print()
            print(f"="*80)
            
        print()
        print(f"Dosen: {dsn}")
        print()
        print()
    
    def totalMhs (self, size, kelas = None):
        if kelas is None:
            print(f"Total Mahasiswa yang hadir di kelas A, B, C: {size}")
        else:
            print(f"Total Mahasiswa yang hadir di kelas {kelas}: {size}")

### ==== End of Template Pattern ==== ###


### ==== Start of Facade Pattern ==== ###

class Facade(Template):
    def __init__ (self):
        super().__init__()
        self.A = ClassA()
        self.B = ClassB()
        self.C = ClassC()
    
    def processA (self):
        absensi = self.A.getAbsensi()
        dsn = self.A.getDsn()
        self.absensiTable(absensi, dsn, "A")
        self.totalMhs(len(absensi), "A")
    
    def processB (self):
        absensi = self.B.getAbsensi()
        dsn = self.B.getDsn()
        self.absensiTable(absensi, dsn, "B")
        self.totalMhs(len(absensi), "B")
    
    def processC (self):
        absensi = self.C.getAbsensi()
        dsn = self.C.getDsn()
        self.absensiTable(absensi, dsn, "C")
        self.totalMhs(len(absensi), "C")
    
    def processAll (self):
        absensiA = self.A.getAbsensi()
        dsn = self.A.getDsn()
        self.absensiTable(absensiA, dsn, "A")

        absensiB = self.B.getAbsensi()
        dsn = self.B.getDsn()
        self.absensiTable(absensiB, dsn, "B")

        absensiC = self.C.getAbsensi()
        dsn = self.C.getDsn()
        self.absensiTable(absensiC, dsn, "C")
        
        a, b, c = len(absensiA), len(absensiB), len(absensiC)
        total = a + b + c
        
        self.totalMhs(a, "A")
        self.totalMhs(b, "B")
        self.totalMhs(c, "C")
        self.totalMhs(total)
    
    def getAll (self):
        absensiA = self.A.getAbsensi()
        absensiB = self.B.getAbsensi()
        absensiC = self.C.getAbsensi()

        return absensiA + absensiB + absensiC

### ==== End of Facade Class ==== ###


### ==== Main Program ==== ###

facade = Facade()
a = ClassA()
b = ClassB()
c = ClassC()

while True:
    cls()
    print(f"Menu")
    print(f"="*80)
    print(f"1. Lihat Absensi")
    print(f"2. Input Absensi")
    print(f"3. Exit")
    print(f"="*80)
    
    optionValid = False
    while not optionValid:
        try:
            op = input("Pilih menu ( 1 / 2 / 3 ): ")
            
            if op.count(" ") == len(op):
                raise ValueError("Pilihan tidak boleh kosong.")
            if not op.isnumeric():
                raise ValueError("Pilihan harus berupa angka.")
            if op not in ["1", "2", "3"]:
                raise ValueError("Pilihan hanya boleh 1 / 2 / 3")
            
            optionValid = True
        
        except ValueError as err:
            print(f"Invalid input: {err}")
        
        print()
    
    op = int(op)
    cls()
    if op == 1:
        kelasValid = False
        while not kelasValid:
            try:
                kelas = input(f"Absensi kelas mana yang mau dilihat ( A / B / C / ALL): ").upper()
                if kelas not in ["A", "B", "C", "ALL"]:
                    raise ValueError("Hanya ada opsi A / B / C / ALL")
                
                kelasValid = True
            
            except ValueError as err:
                print(f"Invalid input: {err}")
        
        print()
        
        if kelas == "A": facade.processA()
        if kelas == "B": facade.processB()
        if kelas == "C": facade.processC()
        if kelas == "ALL": facade.processAll()
    
    elif op == 2:
        nimValid = False
        while not nimValid:
            try:
                nim = input("NIM: ")
                nimValid = checkNimValidity(nim)
            
            except ValueError as err:
                print(f"Invalid input: {err}")
        
        print()
        
        nameValid = False
        while not nameValid:
            try:
                nama = input("Nama: ").lower()
                nameValid = checkNameValidity(nama)
            
            except ValueError as err:
                print(f"Invalid input: {err}")
        
        print()
        
        phoneNumValid = False
        while not phoneNumValid:
            try:
                nomorHp = input("Nomor HP: ")
                phoneNumValid = checkPhoneNumValidity(nomorHp)
            
            except ValueError as err:
                print(f"Invalid input: {err}")
        
        print()
        
        genderValid = False
        while not genderValid:
            try:
                jenisKelamin = input("Jenis Kelamin: ").upper()
                genderValid = checkGenderValidity(jenisKelamin)
            
            except ValueError as err:
                print(f"Invalid input: {err}")
        
        print()
        
        kelasValid = False
        while not kelasValid:
            try:
                kelas = input("Kelas ( A / B / C ): ").upper()
                kelasValid = checkClassValidity(kelas)
                
            except ValueError as err:
                print(f"ValueError: {err}")
                
        print()
        
        found = False

        absensi = facade.getAll()
        for i in absensi:
            if i.nim == nim:
                found = True

        if found:
            print(f"Mahasiswa tersebut sudah pernah ada")
        else:
            mhs = Mhs(nim, nama, jenisKelamin, nomorHp, kelas)
            if kelas == 'A':
                a.addToList(mhs)
                facade.A = a
            
            if kelas == 'B':
                b.addToList(mhs)
                facade.B = b
            
            if kelas == 'C':
                c.addToList(mhs)
                facade.C = c
        
    elif op == 3:
        print(f"Thank you!")
        break
    
    any = input("[ Press any button to continue ]")
