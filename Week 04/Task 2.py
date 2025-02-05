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
    
def checkLvlValidity(tingkat):
    if len(tingkat) == 0 or tingkat.count(" ") == len(tingkat):
        raise ValueError("Tingkatan tidak boleh kosong")
        
    if tingkat not in ["TK", "SD", "SMP", "SMA"]:
        raise ValueError("Hanya tersedia tingkatan TK, SD, SMP, dan SMA")
    
    return True

class List:
    def __init__ (self):
        self.studentList = []
        
    def addToList(self, data):
        self.studentList.append(data)
    
    def printList(self):
        print("Daftar Murid")
        print("="*30)
        if len(self.studentList) == 0:
            print("Belum ada murid yang terdaftar")
        else:
            for i in self.studentList:
                print(f"[ {i.nama.title()} ] - [ {i.tingkatan} ] - [ {i.jamPengajaran} jam ] - [ {i.biaya} ]")

class Student:
    def __init__(self, nama, tingkatan):
        self.nama = nama
        self.tingkatan = tingkatan
        self.jamPengajaran = 2 if tingkatan == "SD" or tingkatan == "TK" else 1
        self.biaya = 300000 if tingkatan == "TK" else 500000 if tingkatan == "SD" else 700000 if tingkatan == "SMP" else 1000000
    
    def getCard (self):
        print("="*30)
        print("Student Card")
        print("="*30)
        print(f"Nama : {self.nama}")
        print(f"Tingkatan : {self.tingkatan}")
        print(f"Jam Pengajaran : {self.jamPengajaran}")
        print(f"Biaya : {self.biaya}")
        print("="*30)

lst = List()

while True:
    print("Menu")
    print("="*30)
    print("1. Lihat daftar murid")
    print("2. Daftar murid baru")
    print("3. Exit")
    
    op = int(input("Pilih menu ( 1 / 2 / 3 ) : "))
    
    if op == 1:
        lst.printList()
    
    elif op == 2:
        nama = None
        namaValid = False
        while not namaValid:
            try:
                nama = str(input("Nama : ")).lower()
                namaValid = checkNameValidity(nama)
            
            except ValueError as err:
                print(f"*Invalid Input : {err}")
        
        tingkat = None
        tingkatValid = False
        while not tingkatValid:
            try:
                tingkat = str(input("Tingkat : ")).upper()
                tingkatValid = checkLvlValidity(tingkat)
            
            except ValueError as err:
                print(f"*Invalid Input : {err}")
        
        student = Student(nama, tingkat)
        student.getCard()
        lst.addToList(student)
    
    elif op == 3:
        print("Thank you!")
        break
