# Pacmann-Cashier-Project
Project Cashier dengan menggunakan Python

## A. Background Project
![Screenshot 2023-02-05 131628](https://user-images.githubusercontent.com/110279502/216803035-bff0c707-8946-45d0-9c8f-67fa4ec3427d.jpg)

## B. Feature Requirements
1. Customer membuat ID transaksi customer berikut
  a. Dengan membuat objek dari class: trnsct_123 = Transaction()
2. Kemudian, Customer memasukkan nama item, jumlah item, dan harga barang.
  a. Memasukkan item yang ingin dibeli.
     add-item ([<nama_item>, <jumlah item>, <harga per item>])
3. Jika ternyata ada kesalahan dalam memaukkan nama item atau jumlah item atau harga item tetapi  tidak ingin menghapus itemnya, Customer bisa melakukan
  a. Update nama item dengan method:
     update_item_nama(<nama item>, <jumlah item>, <harga per item>)
  b. Update jumlah item dengan method:
     update_item_qty(<nama_item>, <update jumlah item>)
  c. Update harga item menggunakan method:
     update_item_price(<nama_item>, <update harga item>
 4. Jika batal membeli item belanjaan, Customer bida melakukan
  a. Menghapus salah satu item dari nama item dengan method
      delete_item(<nama item>)
      ![Uploading Screenshot 2023-02-05 133045.jpg…]()
      Ketika menghapus salah satu nama item, maka jumlah item dan harga per item pada baris/list       tersebut akan ikut terhapus
  b. Langsung menghapus semua transaksi atau reset transaksi dengan method
     reset_transaction()
5. Customer sudah selesai dengan berbelanja online nya, tetapi Customer masih ragu apakah harga barang dan nama barang yang diinput sudah benar. Bisa ssaja Customer melakukan kesalahan dalam melakukan input, semisal sudah melakukan input harga barang tetapi lupa untuk input nama barangnya. Andi bisa menggunakan method check_order(). Terdapat ketentuan:
  a. Akan mengeluarkan pesan "Pemesanan sudah benar" (bebas bisa dengan messege yang lain)          jika tidak ada kesalahan input
  b. Akan mengeluarkan pesan "Terdapat kesalahan input data" jika terjadi kesalahan input
  c. keluarkan output transaksi atau pemesanan apa saja yang sudah dibeli.
    Contoh Output:
    ![Uploading Screenshot 2023-02-05 134223.jpg…]()
6. Setelah melakukan pengecekan, Customer bisa menghitung total belanja yang sudah dibeli, Andi bisa menggunakan method total_price(). Pada supermarket ini ternyata terdapat ketentuan:
   a. Jika total belanja Andi diatas Rp 200_000 maka akan mendaptkan diskon 5%
   b. Jika total belanja Andi diatas Rp 200_000 maka akan mendaptkan diskon 8%
   c. Jika total belanja Andi diatas Rp 200_000 maka akan mendaptkan diskon 10%
  
## C. Tools
  
  Languages:
  
    - Python
  
  Libraries:
  
    - Pandas
  
 ## D. Hasil Test Case
  
  
  1. Membuat modul cashier.py
  
  ![Screenshot 2023-02-05 210202](https://user-images.githubusercontent.com/110279502/216820921-8e93465d-b59c-4ccc-99d2-b19cf99adc3a.jpg)

  
  2. Inisiasi 
  
  ![Screenshot 2023-02-05 210448](https://user-images.githubusercontent.com/110279502/216821019-2dcd86b4-e973-42d0-b09c-177d6f5f828f.jpg)

  
  -- Menambahkan Item
  ![Screenshot 2023-02-05 142326](https://user-images.githubusercontent.com/110279502/216805002-06616c6e-b645-4713-9bee-dff158781d95.jpg)
  
  -- Mengubah Nama Item
  ![Screenshot 2023-02-05 142737](https://user-images.githubusercontent.com/110279502/216805116-29dfa49e-f32b-41b3-9c3a-a8072763738c.jpg)
  
  -- Mengubah Jumlah Item
  ![Screenshot 2023-02-05 142923](https://user-images.githubusercontent.com/110279502/216805163-383c0d96-5f67-4f6e-bcf6-197103561594.jpg)

  -- Mengubah Harga Item
  ![Screenshot 2023-02-05 143102](https://user-images.githubusercontent.com/110279502/216805195-74865b0e-7e52-4612-8559-0867e783a367.jpg)
  
  -- Menghapus Item yang tidak diinginkan
  ![Screenshot 2023-02-05 143245](https://user-images.githubusercontent.com/110279502/216805266-4f34acb9-2c4e-4d30-8ccc-9114d7838d86.jpg)
  
  -- Menghapus Semua Item yang tidak diinginkan
  ![Screenshot 2023-02-05 143459](https://user-images.githubusercontent.com/110279502/216805305-d85b63d7-85d2-498c-bf45-9ba87714ed93.jpg)

  -- Menghitung Harga seluruh Item yang akan dibeli
  ![Screenshot 2023-02-05 143803](https://user-images.githubusercontent.com/110279502/216805394-fe29c561-28e7-44fb-9bde-6f6b1099f747.jpg)

## E. Saran Perbaikan
  - Sebaiknya 

  




  
  
  

      
