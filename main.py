# Program Management Contact

class Kontak:
    def __init__(self):
        self.kontak= []

    def melihat_kontak(self):
        # Melihat Semua Kontak
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f"{num}. {item['nama']}  ({item['hp']},{item['email']})\n")
        else:
            print("Kontak Kosong! Mohon Tambahkan Kontak")
            return 1

    def menambah_kontak(self):
        # Menambahkan Kontak
        nama = input("Masukan nama Kontak: ")
        hp = input("Masukan nomor Handphone: ")
        email = input("Masukan Email: ")
        kontak_baru = {'nama': nama, 'hp': hp, 'email': email}
        self.kontak.append(kontak_baru)
        print("Kontak baru berhasil ditambahkan!")

    def menghapus_kontak(self):
        # Menghapus Kontak
        if  self.melihat_kontak()== 1:
            return
        else:
            jumlah_kontak = len(self.kontak)
            kontak_hapus = int(input("Masukan Nomor Kontak yang akan dihapus: "))
            if kontak_hapus > 0:
                if kontak_hapus <= jumlah_kontak:
                    del self.kontak[kontak_hapus - 1]
                    print("Kontak berhasil dihapus!\n")
                else:
                    print("Angka yang anda masukan salah")
            else:
                print("masukan angka diatas 0")

kontak_kantor = Kontak()
kontak_keluarga = Kontak()
while True:
    print("\n------Menu Kontak-------")
    print("1. Melihat Semua Kontak")
    print("2. Menambahkan Kontak Baru")
    print("3. Menghapus Kontak")
    print("4. Keluar dari Kontak")
    print("--------------------------\n")

    pilihan = input("Masukan Pilihan Menu Kontak: ")


    if pilihan == '1':
        kontak_kantor.melihat_kontak()
    elif pilihan == '2':
        kontak_kantor.menambah_kontak()
    elif pilihan == '3':
        kontak_kantor.menghapus_kontak()
    elif pilihan == '4':
        print("Terimakasih telah menggunakan Management Contact")
        print("-------------------------------------------------\n")
        break
    else:
        print("Pilihan anda Tidak ada pada Menu")