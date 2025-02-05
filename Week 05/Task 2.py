class Stock:
    def __init__(self):
        self.storage = []
    
    def addToStorage(self, item):
        self.storage.append(item)
    
    def showStorage(self, limit = -1):
        print("Daftar Stock")
        print("="*30)
        display = []
        if limit == -1:
            display = self.storage
        else:
            item = iter(self.storage)
            while True:
                try:
                    i = next(item)
                    if i.stok <= limit:
                        display.append(i)
                        
                except StopIteration:
                    break
         
        if len(display) == 0:
            print("Tidak ada barang dalam daftar")
            
        else:
            items = iter(display)
            while True:
                try:
                    i = next(items)
                    print(f"[ {i.id} ] [ {i.nama} ] [ Rp {i.harga} ]")
                    print(f"Jumlah Stock: [ {i.stok} ]")
                    history = iter(i.history)
                    while True:
                        try:
                            print(f"[ {next(history)} ]", end=" ")
                            
                        except StopIteration:
                            break
                    
                    print()
                    print()
                    
                except StopIteration:
                    break
    
    def searchStock(self, nama):
        items = iter(self.storage)
        while True:
            try:
                i = next(items)
                if i.nama == nama:
                    return i
                    
            except StopIteration:
                break
        
        return False


class Item:
    def __init__(self, id, nama, harga):
        self.id = id
        self.nama = nama
        self.harga = harga
        self.stok = 0
        self.history = []
        
    def incStock(self, qty):
        self.stok += qty
        self.history.append(qty)
        
    def decStock(self, qty):
        if qty <= self.stok:
            self.stok -= qty
            self.history.append(-qty)
        else:
            print("Stok tidak mencukupi untuk pengurangan")

stockList = Stock()

while True:
    print("Menu")
    print("=" * 30)
    print("1. Lihat daftar stock")
    print("2. Lihat stock yang hampir kosong")
    print("3. Tambah Barang")
    print("4. Kurangi Barang")
    print("5. Exit")
    
    op = int(input("Pilihan menu ( 1 / 2 / 3 / 4 / 5 ) : "))
    
    if op == 1:
        stockList.showStorage()
    
    elif op == 2:
        while True:
            try:
                limit = int(input("Barang dengan jumlah berapakah yang ingin dilihat? "))
                if limit < 0:
                    raise ValueError("Nilai tidak boeh negatif")
                
                break

            except ValueError as err:
                print(f"Invalid input : {err}")

        stockList.showStorage(limit)
    
    elif op == 3:
        nama = str(input("Nama barang yang ingin ditambahkan : ")).lower()
        found = stockList.searchStock(nama)
        
        if not found:
            harga = int(input("Harga barang : "))
            qty = int(input("Stok awal barang : "))
            item = Item(len(stockList.storage), nama, harga)
            item.incStock(qty)
            stockList.addToStorage(item)
        else:
            qty = int(input("Quantity : "))
            found.incStock(qty)
    
    elif op == 4:
        nama = str(input("Nama barang yang ingin dikurangi : ")).lower()
        found = stockList.searchStock(nama)
        
        if not found:
            print("Barang tidak ditemukan")
        else:
            qty = int(input("Quantity : "))
            found.decStock(qty)
    
    elif op == 5:
        break
