def checkSortOptionValidity(sortOption):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
    'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
    if len(sortOption) == 0 or sortOption.count(" ") == len(sortOption):
        raise ValueError("Opsi tidak boleh kosong")
        
    for i in sortOption:
        if i not in letters:
            raise ValueError("Opsi hanya boleh berupa huruf")
    
    if sortOption not in ["id", "nama", "jenis", "harga"]:
        raise ValueError("Hanya tersedia opsi pengurutan berdasarkan Nama, NIM, dan jurusan")
    
    return True

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
    def __init__(self, id, nama, harga, jenis):
        self.id = id
        self.nama = nama
        self.harga = harga
        self.jenis = jenis
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
    print("5. Pengurutan data")
    print("6. Exit")
    
    op = int(input("Pilihan menu ( 1 / 2 / 3 / 4 / 5 / 6) : "))
    
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
            jenis = str(input("Jenis barang : "))
            item = Item(len(stockList.storage), nama, harga, jenis)
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
        sortOption = None
        sortOptionValid = False
        while not sortOptionValid:
            try:
                sortOption = str(input("Pengurutan berdasarkan : ")).lower()
                sortOptionValid = checkSortOptionValidity(sortOption)
            
            except ValueError as err:
                print(f"Invalid input : {err}")
        
        stockList.sortedBy(sortOption)
        stockList.showStorage()
    
    elif op == 6:
        break
