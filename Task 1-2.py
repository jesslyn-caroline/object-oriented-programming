import os

def cls():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


### ==== Start of Handle Input ==== ###

def checkMajorValidity (major):
    if len(major) == major.count(' '):
        raise ValueError('Jurusan tidak boleh kosong')
    if major not in ['teknik informatika', 'sistem informasi', 'teknologi informasi', 'akuntansi', 'management']:
        raise ValueError('Hanya ada jurusan Teknik Informatika, Sistem Informasi, Teknologi Informasi, Akuntansi, Management')

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


### ==== End of Handle Input ==== ###

### ==== Start of Mhs Class ==== ###

class Mhs:
    def __init__ (self, nim, nama, jenisKelamin, nomorHp, kelas):
        self.nim = nim
        self.nama = nama
        self.jenisKelamin = jenisKelamin
        self.nomorHp = nomorHp

class NewMhs:
  def __init__ (self, nama, jurusan, jenisKelamin, nomorHp, due):
        self.nama = nama
        self.jurusan = jurusan
        self.jenisKelamin = jenisKelamin
        self.nomorHp = nomorHp
        self.due = due

### ==== End of Mhs Class ==== ###

### ==== Start of Mhs List Class ==== ###

class MhsLst:
    def __init__ (self):
        self.lst = []
    
    def addToLst (self, mhs):
        self.lst.append(mhs)
    
    def printLst (self):
        if len(self.lst) == 0:
            print("Tidak ada mahasiswa yang terdaftar")
        else:
            for i in self.lst:
                print(f"NIM: {i.nim} - Nama: {i.nama} - Nomor HP: {i.nomorHp}")


class RolledMhs:
    def __init__ (self):
        self.lst = []
      
    def addToLst (self, mhs):
        self.lst.append(mhs)
    
    def printLst (self):
        if len(self.lst) == 0:
            print("Tidak ada mahasiswa yang terdaftar")
        else:
            for i in self.lst:
                print(f"Nama: {i.nama} - Nomor HP: {i.nomorHp} - Total: {i.due}")
    
    def search (self, nama):
        for i in self.lst:
            if i.nama == nama:
                return i
        
        return False
              
### ==== End of Mhs List Class ==== ###

### ==== Start of Composite Class ==== ###

class Composite:
    def __init__(self, name):
        self.name = name
        self.child = []
        self.total = 0
    
    def addChild(self, leaf):
        self.child.append(leaf)
    
    def detail(self, level = 0):
        print('\t'* level, end="")
        print(f'- {self.name}')
        for i in self.child:
            self.total += i.detail(level + 1)
        
        return self.total


class Leaf:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def detail(self, level):
        print('\t'* level, end="")
        print(f'- {self.name}: {self.price}')
        return self.price

### ==== End of Composite Class ==== ###

def getBill():
    pendaftaran = Leaf("Uang Pendaftaran", 200000)
    kuliahPertama = Leaf("Uang Kuliah Pertama", 1500000)
    
    training = Leaf("Uang Training", 100000)
    penginapan = Leaf("Uang Penginapan", 200000)
    konsumsi = Leaf("Uang Konsumsi", 150000)
    
    uangMpt = Composite("Uang MPT")
    uangMpt.addChild(training)
    uangMpt.addChild(penginapan)
    uangMpt.addChild(konsumsi)
    
    biaya = Composite("Biaya")
    biaya.addChild(pendaftaran)
    biaya.addChild(kuliahPertama)
    biaya.addChild(uangMpt)
    
    total = biaya.detail()
    print(f"Total biaya: {total}")
    return total
    

### ==== Main Program ==== ###

mhsLst = MhsLst()
rolledMhs = RolledMhs()

if __name__ == "__main__":
    while True:
        cls()
        print(f"Menu")
        print(f"="*80)
        print(f"1. Tambah Mahasiswa Baru")
        print(f"2. Daftar Mahasiswa yang mendaftar")
        print(f"3. Daftar Mahasiswa Baru")
        print(f"4. Update biaya pendaftaran Mahasiswa")
        print(f"5. Exit")
        print(f"="*80)
        
        optionValid = False
        while not optionValid:
            try:
                op = input("Pilih menu ( 1 / 2 / 3 / 4 / 5 ): ")
                
                if op.count(" ") == len(op):
                    raise ValueError("Pilihan tidak boleh kosong.")
                if not op.isnumeric():
                    raise ValueError("Pilihan harus berupa angka.")
                if op not in ["1", "2", "3", "4", "5"]:
                    raise ValueError("Pilihan hanya boleh 1 / 2 / 3 / 4 / 5")
                
                optionValid = True
            
            except ValueError as err:
                print(f"Invalid input: {err}")
            
            print()
        
        op = int(op)
        cls()
        
        if op == 1:
            nameValid = False
            while not nameValid:
                try:
                    nama = input('Nama: ').lower()
                    nameValid = checkNameValidity(nama)
                
                except ValueError as err:
                    print(f'Invalid input: {err}')
            
            print()
            
            jurusanValid = False
            while not jurusanValid:
                try:
                    jurusan = input('Jurusan: ').lower()
                    jurusanValid = checkMajorValidity(jurusan)
                
                except ValueError as err:
                    print(f'Invalid input: {err}')
            
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
            print()
            
            print(f"Berikut rincian biaya kuliah")
            total = getBill()
            newMhs = NewMhs(nama, jurusan, jenisKelamin, nomorHp, total)
            rolledMhs.addToLst(newMhs)
        
        elif op == 2:
            print("Daftar Mahasiswa yang Mendaftar")
            rolledMhs.printLst()

        elif op == 3:
            print("Daftar Mahasiswa Baru")
            mhsLst.printLst()

        elif op == 4:
            nameValid = False
            while not nameValid:
                try:
                    nama = input('Nama: ').lower()
                    nameValid = checkNameValidity(nama)
                
                except ValueError as err:
                    print(f'Invalid input: {err}')
            
            print()
            
            found = rolledMhs.search(nama)
            if found:
                found.due = 0
                print(f"Biaya pendaftaran untuk {nama} telah diupdate.")
            else:
                print(f'Mahasiswa tersebut tidak terdaftar.')
        
        elif op == 5:
            print(f"Thank you!")
            break
        
        any = input("[ Press any button to continue ]")
