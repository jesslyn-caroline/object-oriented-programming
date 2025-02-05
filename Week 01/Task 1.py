class Mahasiswa:
    def __init__(self, nim, nama, kelas, waktu, gender, nomorHp):
        self.nim = nim
        self.nama = nama
        self.kelas = kelas
        self.waktu = waktu
        self.gender = gender
        self.nomorHp = nomorHp

class Dosen:
    def __init__(self, nip, nama, jabatan, gender, nomorHp):
        self.nip = nip
        self.nama = nama
        self.jabatan = jabatan
        self.gender = gender
        self.nomorHp = nomorHp

class VisitorList:
    def __init__(self):
        self.visitorMhs = []
        self.visitorDsn = []
    
    def addToVisitorMhs(self, data):
        self.visitorMhs.append(data)
    
    def addToVisitorDsn(self, data):
        self.visitorDsn.append(data)
    
    def printList(self):
        print("Daftar hadir mahasiswa")
        print("="*30)
        if len(self.visitorMhs) == 0:
            print("Belum ada mahasiswa yang hadir")
        else:
            for i in self.visitorMhs:
                print(f"[ NIM : {i.nim} ] - [ Nama : {i.nama} ] - [ Kelas : {i.kelas} ] - [ Waktu: {i.waktu} ] - [ Gender: {i.gender} ] - [ Nomor Telepon: {i.nomorHp} ]")
        
        print()
        print("Daftar hadir dosen")
        print("="*30)
        if len(self.visitorDsn) == 0:
            print("Belum ada dosen yang hadir")
        else:
            for i in self.visitorDsn:
                print(f"[ NIP : {i.nip} ] - [ Nama : {i.nama} ] - [ Jabatan : {i.jabatan} ] - [ Gender : {i.gender} ] - [ Nomor Telepon : {i.nomorHp} ]")

        totalMhs = len(self.visitorMhs)
        totalDsn = len(self.visitorDsn)
        print()
        print("Total Mahasiswa: ", totalMhs)
        print("Total Dosen: ", totalDsn)
        print("Total: ", totalMhs + totalDsn)

visitorList = VisitorList()

while True:
    print("=" * 30)
    print("1. Cek daftar pengunjung")
    print("2. Tambah daftar pengunjung")
    print("3. Keluar")
    print("=" * 30)
    opsi = int(input("Pilih Menu ( 1 / 2 / 3 ) : "))
    print()
    
    if opsi == 1:
        visitorList.printList()
    
    elif opsi == 2:
        op = str(input("Siapa yang ingin ditambahkan (Dosen / Mahasiswa) ? "))
        if op.lower() == 'dosen':
            print("Silakan masukkan informasi berikut")
            nip = str(input("NIP : "))
            nama = str(input("Nama : "))
            jabatan = str(input("Jabatan : "))
            gender = str(input("Gender : "))
            nomorHp = str(input("Nomor Telepon : "))
            data = Dosen(nip, nama, jabatan, gender, nomorHp)
            visitorList.addToVisitorDsn(data)
        
        elif op.lower() == "mahasiswa":
            print("Silakan masukkan informasi berikut")
            nim = str(input("NIM : "))
            nama = str(input("Nama : "))
            kelas = str(input("Kelas : "))
            waktu = str(input("Waktu : "))
            gender = str(input("Gender : "))
            nomorHp = str(input("Nomor Telepon: "))
            data = Mahasiswa(nim, nama, kelas, waktu, gender, nomorHp)
            visitorList.addToVisitorMhs(data)
        
    elif opsi == 3:
        print("Terima kasih!")
        break
    
    print()
