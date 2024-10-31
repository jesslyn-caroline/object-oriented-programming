class Store:
    def __init__ (self):
        self.inventory = [HandSanitizer(), BanMobil(), Buah(), BotolMinum()]
    
    def printStorage(self):
        for i in self.inventory:
            print(f"{i.name.title()} : ")
            print(f"History in / out : ", end = "")
            if len(i.history) != 0:
                for j in range (len(i.history)):
                    if j != len(i.history) - 1:
                        print(f"[ {i.history[j]} ]", end = " - ")
                    else:
                        print(f"[ {i.history[j]} ]")
            else:
                print("Belum ada history")
            print(f"Stock : {sum(i.history)}")
    
    def search(self, name):
        for i in self.inventory:
            if i.name == name:
                return i
        return None
        
class Items:
    def __init__ (self, name):
        self.name = name
        self.history = []
        
    def incStock(self, qty):
        self.history.append(qty)
    
    def decStock(self, qty):
        self.history.append(qty * -1)
        
class HandSanitizer (Items):
    def __init__ (self):
        super().__init__("hand sanitizer")

class BanMobil (Items):
    def __init__ (self):
        super().__init__("ban mobil")

class Buah (Items):
    def __init__ (self):
        super().__init__("buah")

class BotolMinum (Items):
    def __init__ (self):
        super().__init__("botol minum")

store = Store()

while True:
    print("Menu")
    print("="*30)
    print("1. Cek laporan stock")
    print("2. Tambah / Kurang stock")
    print("3. Keluar")
    print("="*30)
    
    option = int(input("Pilihan menu ( 1 / 2 / 3 ) : "))
    print()
    
    if option == 1:
        store.printStorage()
    
    elif option == 2:
        op = str(input("Tambah / Kurang Stock : ")).lower()
        
        if op == "tambah":
            name = str(input("Nama barang yang ingin ditambah : ")).lower()
            item = store.search(name)
            if item == None:
                print("\nBarang tersebut tidak ada dalam daftar\n")
                continue
            
            qty = int(input("Jumlah yang ingin ditambah : "))
            item.incStock(qty)
        
        elif op == "kurang":
            name = str(input("Nama barang yang ingin dikurangi : ")).lower()
            item = store.search(name)
            if item == None:
                print("\nBarang tersebut tidak ada dalam daftar\n")
                continue
            
            qty = int(input("Jumlah yang ingin dikurangi : "))
            item.decStock(qty)
        
    elif option == 3:
        print("Terima kasih")
        break
    
    print()