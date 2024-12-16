import os
from prettytable import PrettyTable 


def cls():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


### ==== Start of Handle Input ==== ###

def checkNimValidity (nim):
    if nim.count(" ") == len(nim):
        raise ValueError("NIM tidak boleh kosong")
    
    if len(nim) != 9:
        raise ValueError("NIM hanya boleh terdiri dari 9 karakter")
    
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
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
    def __init__ (self, nim, nama, jenisKelamin, nomorHp):
        self.nim = nim
        self.nama = nama
        self.jenisKelamin = jenisKelamin
        self.nomorHp = nomorHp

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
            table = PrettyTable()
            table.field_names = ["NIM", "Nama", "Jenis Kelamin", "Nomor HP"]
            for i in self.lst:
                table.add_row([i.nim, i.nama.title(), i.jenisKelamin, i.nomorHp])
            print(table)
    
    def getLength (self):
        return len(self.lst)

class PaymentHistory:
    def __init__ (self):
        self.history = []
    
    def addToHistory (self, mhs):
        self.history.append(mhs)

    def checkHistory (self):
        if len(self.history) == 0:
            print("Tidak ada mahasiswa yang telah membayar")
        else:
            table = PrettyTable()
            table.field_names = ["NIM", "Nama", "Nominal"]
            for i in self.history:
                table.add_row([i[0].nim, i[0].nama, i[1]])

            print(table)
    
    def search (self, nim):
        for i in self.history:
            if i[0].nim == nim:
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
        print('  '* level, end="")
        print(f'- {self.name}')
        for i in self.child:
            self.total += i.detail(level + 1)
        
        return self.total


class Leaf:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def detail(self, level):
        print(' '* level, end="")
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
    
def getNim (year, jurusan):
    year = str(year % 2000)
    kodeJurusan = None

    if jurusan == 'teknik informatika':
        kodeJurusan = '111'
    elif jurusan == 'sistem informasi':
        kodeJurusan = '112'
    elif jurusan == 'teknologi informasi':
        kodeJurusan = '113'
    elif jurusan == 'akuntansi':
        kodeJurusan = '211'
    else:
        kodeJurusan = '212'
    
    id = mhsLst.getLength() + 1
    if id < 10:
        id = f'000{id}'
    elif id < 100:
        id = f'00{id}'
    elif id < 1000:
        id = f'0{id}'
    else:
        id = f'{id}'

    return f'{year}{kodeJurusan}{id}'


### ==== Main Program ==== ###

mhsLst = MhsLst()
paymentHistory = PaymentHistory()
total = getBill()
if __name__ == "__main__":
    while True:
        cls()
        print(f"Menu")
        print(f"="*80)
        print(f"1. Tambah Mahasiswa Baru")
        print(f"2. History pembayaran Mahasiswa")
        print(f"3. Daftar Mahasiswa Baru")
        print(f"4. Bayar cicilan uang kuliah")
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
            
            total = getBill()

            valid = False
            while not valid:
                try:
                    full = input("Apakah anda ingin membayar penuh? (Y/N): ").upper()
                    if len(full) == full.count(' '):
                        raise ValueError("Tidak boleh kosong")
                    if full not in ['Y', 'N']:
                        raise ValueError("Hanya ada Y / N")
                    
                    valid = True

                except ValueError as err:
                    print(f'Invalid input: {err}')
            
            if full == 'Y':
                total = total - (total * 0.1)
                print("Biaya pendaftaran telah dibayar penuh dengan potongan diskon 10%")
            else:
                print("Mahasiswa tersebut telah didaftarkan")

            nim = getNim(2023, jurusan)
            mhs = Mhs(nim, nama, jenisKelamin, nomorHp)

            mhsLst.addToLst(mhs)
            if full == 'Y':
                paymentHistory.addToHistory([mhs, int(total)])
            else:
                paymentHistory.addToHistory([mhs, int(total / 4)])
            
            print(f"Mahasiswa tersebut telah terdaftar dengan NIM: {nim}")
        
        elif op == 2:
            print("History pembayaran Mahasiswa")
            paymentHistory.checkHistory()

        elif op == 3:
            print("Daftar Mahasiswa Baru")
            mhsLst.printLst()

        elif op == 4:
            nimValid = False
            while not nimValid:
                try:
                    nim = input("NIM: ")
                    nimValid = checkNimValidity(nim)
                
                except ValueError as err:
                    print(f"Invalid input: {err}")
            
            print()
            
            found = paymentHistory.search(nim)
            if found:
                paymentHistory.addToHistory([mhs, int(total / 4)])
                print("Terima kasih telah membayar")
            else:
                print("Mahasiswa belum terdaftar")
        
        elif op == 5:
            print(f"Thank you!")
            break
        
        print()
        any = input("[ Press any button to continue ]")
