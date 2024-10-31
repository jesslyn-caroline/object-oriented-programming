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
    if len(jenisKelamin) == 0 or jenisKelamin.count(" ") == len(jenisKelamin):
        raise ValueError("Jenis kelamin tidak boleh kosong")
        
    if jenisKelamin != "L" and jenisKelamin != 'P':
        raise ValueError("Jenis Kelamin tidak valid")
    
    return True

def checkClassValidity (kelas):
    if len(kelas) == 0 or kelas.count(" ") == len(kelas):
        raise ValueError("Kelas tidak boleh kosong")
        
    if kelas not in ["A", "B", "C"]:
        raise ValueError("Kelas tidak valid")
    
    return True

def checkTimeValidity (waktu):
    if len(waktu) == 0 or waktu.count(" ") == len(waktu):
        raise ValueError("Waktu tidak boleh kosong")
    
    if waktu != "sore" and waktu != "pagi":
        raise ValueError("Waktu kuliah hanya ada pagi dan sore")
    
    return True

class List:
    def __init__ (self):
        self.mhs = []
        self.dsn = []
    
    def addToMhsList(self, data):
        self.mhs.append(data)
    
    def addToDsnList(self, data):
        self.dsn.append(data)
    
    def searchInMhs (self, nim):
        for i in self.mhs:
            if i.kode == nim:
                return True
                
        return False
    
    def searchInDsn (self, nip):
        for i in self.dsn:
            if i.kode == nip:
                return True
                
        return False
        
        
    def printList(self):
        print(f"Daftar Mahasiswa")
        print("="*30)
        if len(self.mhs) == 0:
            print("Masih belum ada mahasiswa yang terdaftar")
        else:
            for i in self.mhs:
                print(f"[ {i.kode} ] [ {i.nama} ] [ {i.jurusan} ] [ {i.kelas} {i.waktu} ] [ {'Perempuan' if i.jenisKelamin == 'P' else 'Laki-laki'} ] [ {i.nomorHp} ]")
        
        print()
        
        print(f"Daftar Dosen")
        print("="*30)
        if len(self.dsn) == 0:
            print("Masih belum ada dosen yang terdaftar")
        else:
            for i in self.dsn:
                print(f"[ {i.kode} ] [ {i.nama} ] [ {i.jurusan} ] [ {'Perempuan' if i.jenisKelamin == 'P' else 'Laki-laki'} ] [ {i.jabatan} ] [ {i.nomorHp} ]")
        
class Parent:
    def __init__ (self, kode, nama, nomorHp, jenisKelamin):
        self.kode = kode
        self.nama = nama
        self.nomorHp = nomorHp
        self.jenisKelamin = jenisKelamin
        self.jurusan = "Teknik Informatika" if kode[2:5] == "111" else "Sistem Informasi" if kode[2:5] == "112" else "Teknologi Informasi" if kode[2:5] == "113" else "Management" if kode[2:5] == "211" else "Akuntansi"
        self.tahun = int(kode[0:2])

class Mhs(Parent):
    def __init__ (self, kode, nama, nomorHp, jenisKelamin, kelas, waktu):
        super().__init__(kode, nama, nomorHp, jenisKelamin)
        self.kelas = kelas
        self.waktu = waktu
    
    def printOut (self):
        print("="*30)
        print(f"NIM : {self.kode}")
        print(f"Nama : {self.nama.title()}")
        print(f"Jenis Kelamin : {'Perempuan' if self.jenisKelamin == 'P' else 'Laki-laki'}")
        print(f"Jurusan : {self.jurusan}")
        print(f"Kelas : {self.kelas}")
        print(f"Waktu : {self.waktu}")
        print(f"Angkatan : Tahun {self.tahun}")
        print(f"Nomor HP : {self.nomorHp}")
        print("="*30)

class Dsn(Parent):
    def __init__(self, kode, nama, nomorHp, jenisKelamin, jabatan):
        super().__init__(kode, nama, nomorHp, jenisKelamin)
        self.jabatan = jabatan
    
    def printOut(self):
        print("="*30)
        print(f"NIP : {self.kode}")
        print(f"Nama : {self.nama.title()}")
        print(f"Jenis Kelamin : {'Perempuan' if self.jenisKelamin == 'P' else 'Laki-laki'}")
        print(f"Jurusan : {self.jurusan}")
        print(f"Jabatan : {self.jabatan.title()}")
        print(f"Tahun : {self.tahun}")
        print(f"Nomor HP : {self.nomorHp}")
        print("="*30)

lst = List()

while True:
    print("Menu")
    print("="*30)
    print("1. Lihat daftar")
    print("2. Tambah daftar mahasiswa")
    print("3. Tambah daftar dosen")
    print("4. Exit")
    
    op = int(input("Pilih menu ( 1 / 2 / 3 / 4 ) : "))
    
    if op == 1:
        lst.printList()
    
    elif op == 2:
        nim = None
        kodeValid = False
        while not kodeValid:
            try:
                nim = str(input("NIM : "))
                kodeValid = checkCodeValidity(nim)
                
            except ValueError as err:
                print(f"*Invalid input : {err}")
                
        nama = None
        namaValid = False
        while not namaValid:
            try:
                nama = str(input("Nama : ")).lower()
                namaValid = checkNameValidity(nama)
                
            except ValueError as err:
                print(f"*Invalid input : {err}")
                
        nomorHp = None
        nomorHpValid = False
        while not nomorHpValid:
            try:
                nomorHp = str(input("Nomor HP : "))
                nomorHpValid = checkPhoneNumValidity(nomorHp)
                
            except ValueError as err:
                print(f"*Invalid input : {err}")
                
        jenisKelamin = None
        jenisKelaminValid = False
        while not jenisKelaminValid:
            try:
                jenisKelamin = str(input("Jenis Kelamin ( L / P ) : ")).upper()
                jenisKelaminValid = checkGenderValidity(jenisKelamin)
            
            except ValueError as err:
                print(f"*Invalid input : {err}")
        
        kelas = None
        kelasValid = False
        while not kelasValid:
            try:
                kelas = str(input("Kelas ( A / B / C ) : ")).upper()
                kelasValid = checkClassValidity(kelas)
            
            except ValueError as err:
                print(f"*Invalid input : {err}")
                
        waktu = None
        waktuValid = False
        while not waktuValid:
            try:
                waktu = str(input("Waktu ( Pagi / Sore ) : ")).lower()
                waktuValid = checkTimeValidity(waktu)
            
            except ValueError as err:
                print(f"*Invalid input : {err}")
        
        mhs = Mhs(nim, nama, nomorHp, jenisKelamin, kelas, waktu)
        
        found = lst.searchInMhs(nim)
        if found:
            print("Mahasiswa tersebut sudah pernah ada")
        else:
            lst.addToMhsList(mhs)
            mhs.printOut()
        
    elif op == 3:
        nip = None
        kodeValid = False
        while not kodeValid:
            try:
                nip = str(input("NIP : "))
                kodeValid = checkCodeValidity(nip)
            
            except ValueError as err:
                print(f"*Invalid input : {err}")
        
        nama = None
        namaValid = False
        while not namaValid:
            try:
                nama = str(input("Nama : ")).lower()
                namaValid = checkNameValidity(nama)
            
            except ValueError as err:
                print(f"*Invalid input : {err}")
        
        nomorHp = None
        nomorHpValid = False
        while not nomorHpValid:
            try:
                nomorHp = str(input("Nomor HP : "))
                nomorHpValid = checkPhoneNumValidity(nomorHp)
                
            except ValueError as err:
                print(f"*Invalid input : {err}")
                
        jenisKelamin = None
        jenisKelaminValid = False
        while not jenisKelaminValid:
            try:
                jenisKelamin = str(input("Jenis Kelamin ( L / P ) : ")).upper()
                jenisKelaminValid = checkGenderValidity(jenisKelamin)
            
            except ValueError as err:
                print(f"*Invalid input : {err}")
        
        jabatan = str(input("Jabatan : "))
        
        dsn = Dsn(nip, nama, nomorHp, jenisKelamin, jabatan)
        
        found = lst.searchInDsn(nip)
        if found:
            print("Dosen tersebut sudah pernah ada")
        else:
            lst.addToDsnList(dsn)
            dsn.printOut()
    
    elif op == 4:
        print("Thank you!")
        break