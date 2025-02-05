class List:
    def __init__ (self):
        self.storage = []
    
    def addToList(self, data):
        print("Telah berhasil terdaftar. Berikut kartu murid.")
        self.storage.append(data)
    
    def checkList(self):
        if len(self.storage) == 0:
            print("Belum ada murid yang terdaftar")
        else:
            print("Daftar Murid")
            print("="*30)
            for i in self.storage:
                print(f"[ Nama : {i.nama} ] - [ Tingkat : {i.tingkat} ] - [ Jam Pengajaran : {i.jamPengajaran} ] - [ Biaya Les : {i.biayaLes} ]")
            print("="*30)

class Student:
    def __init__ (self, nama, tingkat):
        self.nama = nama
        self.tingkat = tingkat
        self.jamPengajaran = 2 if tingkat == "SD" or tingkat == "TK" else 1 if tingkat == "SMP" or tingkat == "SMA" else ""
        self.biayaLes = 300000 if tingkat == "TK" else 500000 if tingkat == "SD" else 700000 if tingkat == "SMP" else 1000000
    
    def printCard(self):
        print("="*30)
        print("Student Card")
        print(f"Nama : {self.nama}")
        print(f"Tingkat : {self.tingkat}")
        print(f"Jam Pengajaran : {self.jamPengajaran}")
        print(f"Biaya Les : Rp {self.biayaLes},-")
        print("="*30)

_List = List()
while True:
    print("Menu")
    print("1. Lihat daftar murid")
    print("2. Daftar murid")
    print("3. Exit")
    print("="*30)
    option = int(input("Pilihan menu ( 1 / 2 / 3 ) : "))
    print()
    if option == 1:
        _List.checkList()
        print()
        
    elif option == 2:
        print("Silahkan mengisi data sebagai berikut")
        nama = str(input("Nama : "))
        tingkat = str(input("Tingkat : "))
        print()
        _List.addToList(Student(nama, tingkat))
        Student.printCard(Student(nama, tingkat))
        print()
        
    elif option == 3:
        break
