import time

class Inventory:
    def __init__(self):
        self.inventory = []
    https://github.com/jesslyn-caroline/object-oriented-programming/tree/main/Week%201
    def addToInventory(self, data):
        self.inventory.append(data)
    
    def printInventoryList(self):
        if len(self.inventory) == 0:
            print("Belum ada barang yang ditambahkan")
            
        else:
            for i in self.inventory:
                print(f"[ ID : {i.id} ] - [ Nama : {i.nama.title()} ] - [ Jenis : {i.jenis.title()} ] - [ Stock : {i.stock} ]")
                print(f"[ History Stock ]")

                for j in range (0, len(i.history)):
                    if j == len(i.history) - 1:
                        print(f"[ {i.history[j][0]} ]")
                    else:
                        print(f"[ {i.history[j][0]} ]" , end = " - ")
                print()
                        
    
    def printHistoryList(self):
        if len(self.inventory) == 0:
            print("Belum ada barang yang ditambahkan")
            
        else:
            for i in self.inventory:
                print(f"[ ID : {i.id} ] - [ Nama : {i.nama.title()} ] - [ Stock : {i.stock} ]")
                print(f"[ History Stock ]")
                for j in range (0, len(i.history)):
                    print(f"[ [ {i.history[j][0]} ] - Waktu : {i.history[j][1]} ]")
                print()
    
    def searchItem(self, nama):
        for item in self.inventory:
            if item.nama == nama:
                return item
                
        return False

class Item:
    def __init__(self, id, nama, jenis, harga):
        self.id = id
        self.nama = nama
        self.jenis = jenis
        self.harga = harga
        self.stock = 0
        self.history = []
    
    def addStock(self, qty):
        self.stock += qty
        self.history.append([qty, time.ctime(time.time())])

    def outStock(self, qty):
        if self.stock - qty < 0:
            return False
            
        self.stock -= qty
        self.history.append([-qty, time.ctime(time.time())])
        
        return True

inventory = Inventory()

while True:
    print()
    print("Menu")
    print("=" * 30)
    print("1. Tambah Barang")
    print("2. Kurangi Barang")
    print("3. Lihat Daftar Inventory")
    print("4. Lihat History Barang")
    print("5. Keluar")
    print("=" * 30)
        
    option = int(input("Pilih menu ( 1 / 2 / 3 / 4 / 5 / 6 ) : "))
        
    if option == 1:
        nama = str(input("Nama Barang : ")).lower()
        found = inventory.searchItem(nama)
        
        if not found:
            id = len(inventory.inventory) + 1
            jenis = str(input("Jenis Barang : ")).lower()
            harga = str(input("Harga Barang : ")).lower() 
            qty = int(input("Stok awal barang: "))
            item = Item(id, nama, jenis, harga)
            inventory.addToInventory(item)
            item.addStock(qty)
            
            print(f"\nBarang [ {nama.title()} ] berhasil ditambahkan ke inventory.\n")
        
        else:
            qty = int(input("Jumlah stock yang ingin ditambahkan : "))
            found.addStock(qty)
            
            print(f"\nStock barang [ {nama.title()} ] berhasil ditambahkan ke inventory.\n")
        
    elif option == 2:
        nama = str(input("Nama Barang : ")).lower()
        item = inventory.searchItem(nama)
        
        if not item:
            print(f"\nBarang dengan nama [ {nama.title()} ] tidak ditemukan di inventory.\n")
            
        else:
            qty = int(input(f"Jumlah stock yang ingin dikurangi : "))
            pos = item.outStock(qty)
            
            if pos:
                print(f"\nStock [ {item.nama.title()} ] berhasil dikurangi.\n")
            else:
                print(f"\nStock [ {item.nama.title()} ] tidak berhasil dikurangi [ Stock akan menjadi minus ].\n")
        
    elif option == 3:
        print()
        print("Daftar Inventory")
        inventory.printInventoryList()
        
    elif option == 4:
        print()
        print("History Barang:")
        inventory.printHistoryList()
        
    elif option == 5:
        print("Thank you!")
        break
