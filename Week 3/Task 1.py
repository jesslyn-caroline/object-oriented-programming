from abc import ABC, abstractmethod

class List:
    def __init__ (self):
        self.inventory = set()
    
    def addToList(self, data):
        self.inventory.add(data)
    
    def printList(self):
        if len(self.inventory) == 0:
            print("Belum ada yang hadir")
        else:
            for i in self.inventory:
                print(f"[i.num] - {i.nama}")

class Person (ABC):
    
    @abstractmethod
    def message(self):
        pass

class Parent:
    def __init__ (self, num, nama):
        self.num = num
        self.nama = nama
    
class Mhs (Parent, Person):
    def __init__ (self, num, nama):
        super().__init__ (num, nama)
        
    def message(self):
        print(f"Terima kasih sudah hadir.")

class Dsn (Parent, Person):
    def __init__ (self, num, nama):
        super().__init__ (num, nama)
    
    def message(self):
        print(f"Silahkan memulai pelajaran")

lst = List()

while True:
    print("Menu")
    print("="*30)
    print("1. Daftar hadir")
    print("2. Absensi Mahasiswa")
    print("3. Absensi Mahasiswa")
    print("4. Exit")
    
    op = int(input("Pilih menu ( 1 / 2 / 3 / 4 ) : "))
    
    if op == 1:
        print("Daftar Hadir")
        print("="*30)
        lst.printList()
    
    elif op == 2 or op == 3:
        num = str(input("Id : "))
        nama = str(input("Nama : "))
        
        if op == 2:
            mhs = Mhs(num, nama)
            mhs.message()
            lst.addToList(mhs)
        
        if op == 3:
            dsn = Dsn(num, nama)
            dsn.message()
            lst.addToList(dsn)
    
    elif op == 4:
        print("Thank you!")
        break