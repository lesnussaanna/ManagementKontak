# Program Management Contact
kontak1 ={'nama':"Anna", 'hp':"083469292",'email':"anna@python.com"}
kontak2 ={'nama':"Elsa", 'hp':"083494567",'email':"elsa@python.com"}
kontak = [kontak1,kontak2]

while True:
    print("\n------Menu Kontak-------")
    print("1. Melihat Semua Kontak")
    print("2. Menambahkan Kontak Baru")
    print("3. Menghapus Kontak")
    print("4. Keluar dari Kontak")
    print("--------------------------\n")

    pilihan = input("Masukan Pilihan Menu Kontak: ")


    if pilihan == '1':
        #Melihat Semua Kontak
        if kontak:
            for num,item in enumerate(kontak,start=1):
                print(f"{num}. {item['nama']}  ({item['hp']},{item['email']})\n")
        else:
            print("Kontak Kosong! Mohon Tambahkan Kontak")
            continue
    elif pilihan == '2':
        # Menambahkan Kontak
        nama = input("Masukan nama Kontak: ")
        hp = input("Masukan nomor Handphone: ")
        email = input("Masukan Email: ")
        kontak_baru ={'nama': nama, 'hp': hp, 'email':email}
        kontak.append(kontak_baru)
        print("Kontak baru berhasil ditambahkan!")
    elif pilihan == '3':
        # Menghapus Kontak
        if kontak:
            for num,item in enumerate(kontak,start=1):
                print(f"{num}. {item['nama']}  ({item['hp']},{item['email']})\n")
            kontak_hapus = int(input("Masukan Nomor Kontak yang akan dihapus: "))
            del kontak[kontak_hapus-1]
            print("Kontak berhasil dihapus!\n")
        else:
            print("Kontak Kosong! Mohon Tambahkan Kontak")
            continue
    elif pilihan == '4':
        print("Terimakasih telah menggunakan Management Contact")
        print("-------------------------------------------------\n")
        break
    else:
        print("Pilihan anda Tidak ada pada Menu")