#this modul to make dictionary as DataFrame
import pandas as pd

#this class to warp all methods requirement in Casier Project
class Transaction():
    
    def __init__(self):
        
        """ Function From This Method is to wrap 
        the nama_item,jumlah_item,harga_item in Dictionary """
        
        self.transaction = dict()
        
    def add_item(self,nama_item,jumlah_item,harga_item):
        
        """ Function From This Method to add the nama_item[key], jumlah_item[values], harga_item[values] to self.transaction
            
            Parameter:
                nama_item   : name of groceries in store
                jumlah_item : quantity of the item
                harga_item  : Price each item """
        
        self.transaction.update({nama_item: [jumlah_item,harga_item,jumlah_item*harga_item]})
    
    
    def update_item_name(self,nama_item,nama_item_baru):
        
        """ Function From This Method is to update or change the nama_item 
            
            Parameter : 
                nama_item      : The name of item to change
                nama_item_baru : The updated name of the nama_item"""
        
        self.nama_item = nama_item
        self.nama_item_baru = nama_item_baru
        nama_baru = self.transaction[self.nama_item]
        self.transaction.pop(self.nama_item) 
        self.transaction.update({nama_item_baru: nama_baru})     
        
        print(f"Nama Item {nama_item} telah diganti menjadi {nama_item_baru}")
     
    def update_item_qty(self,nama_item,jumlah_item_baru):
        
        """ Function From This Method to update specific quantity from nama_item
            
           Parameter:
               nama_item        : name of groceries in store
               jumlah_item_baru : updated quantity of the item """
        
        self.nama_item = nama_item
        self.jumlah_item_baru = jumlah_item_baru
        self.transaction[nama_item][0]= self.jumlah_item_baru
        
        print(f"Jumlah Pesanan terhadap barang {nama_item} telah diubah menjadi {jumlah_item_baru} ")
    
    def update_item_price(self, nama_item, harga_item_baru):
        
        """ Function From This Method to update specific price from nama_item
        
           Parameter:
               nama_item       : name of groceries in store
               harga_item_baru : updated price of the nama_item"""
        
        self.nama_item = nama_item
        self.harga_item_baru = harga_item_baru
        self.transaction[nama_item][1] = harga_item_baru
        
        print(f"Harga Pesanan terhadap barang {nama_item} telah diubah menjadi {harga_item_baru} ")
    
    def delete_item(self, nama_item):
        
        """ Function From This Method to Delete nama_item include jumlah_item and harga_item
        
           Parameter:
               nama_item : name of groceries in store"""
        
        self.nama_item = nama_item
        self.transaction.pop(nama_item)
        
        print(f"Transaksi untuk Pesananan {nama_item} telah dihapus")
        
    def reset_transaction(self):
        
        """ Function From This Method to clear all Item in self.transaction"""
        
        self.transaction.clear()
        print("Anda Telah Menghapus semua item belanjaan Anda")
        
    def check_order(self):
        
        """ Function From This Method to check type of the value in self.transaction if there is wrong inputation in 
        nama_item(str), jumlah_item(int), harga_item(int) """
        
        
        for key, values in self.transaction.items():
                                 
            nama_item = key
            jumlah_item = values[0]
            harga_item = values[1]
        
        if type(key) != str and values[0] != int and values[1] != int:
            print("Terdapat Kesalahan input data \n"
                  "Masukkan Nama Barang dengan huruf misal; Motor, Ayam,..\n"
                  "Masukkan Jumlah dari barang menggunakan angka misal; 1, 2,.." )
        else:
            print("Pemesanan Sudah Benar")
            print("")
         
        df = pd.DataFrame(self.transaction)
        # create the index 
        index_ = ['Jumlah Item', 'Harga/Item', 'Total Harga']   
        # Set the index   
        df.index = index_           
        # return the transpose 
        df2_transposed = df.T # or df2.transpose()
        print(df2_transposed)
        
        
    def total_price(self):
        
        """Function From This Method to display the total transaction before and after discount """
        
        #const variable for discount rate 
        DISKON1 = 5/100
        DISKON2 = 8/100
        DISKON3 = 10/100
        
        # to sum of values[2](harga_total) in self.transaction
        transaksi = self.transaction
        total = sum(transaksi[item][2] for item in transaksi)
        
        print("")
        
        #branching to determine the discount rate and therefore calculate the total transaction after discount 
        if total > 200_000 and total < 300_000:
            harga_diskon = DISKON1 * total
            harga_setelah_diskon = total - harga_diskon
            print(f"Harga Total dari Pesanan Anda sebesar  : Rp. {total}\n\nSelamat pesanan melebihi Rp. 200.000 dan anda mendapatkan DISKON 5%\n\nAnda Cukup Membayar sebesar      : Rp. {harga_setelah_diskon}")
        elif total > 300_000 and total < 500_000:
            harga_diskon = DISKON2 * total
            harga_setelah_diskon = total - harga_diskon
            print(f"Harga Total dari Pesanan Anda sebesar  : Rp. {total}\n\nSelamat pesanan melebihi Rp. 300.000 dan anda mendapatkan DISKON 8%\n\nAnda Cukup Membayar sebesar      : Rp. {harga_setelah_diskon}")
        elif total > 500_000:
            harga_diskon = DISKON3 * total
            harga_setelah_diskon = total - harga_diskon
            print(f" Harga Total dari Pesanan Anda sebesar : Rp. {total}\n\nSelamat pesanan melebihi Rp. 500.000 dan anda mendapatkan DISKON 10%\n\nAnda Cukup Membayar sebesar       : Rp. {harga_setelah_diskon}")
        else:
            print(f" Total Harga Yang Harus Anda Bayarkan : Rp. {total}\nAyok Tambah Lagi Pesananmu Supaya Anda Dapat Diskon\nSemakin Banyak Belanja Semakin Banyak Diskonnya")
        
        
            
           
            
        
        
        
        