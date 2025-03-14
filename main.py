# Program Management Contact
from kontak import Kontak

def main():
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
            kontak_kantor.keluar_kontak()
            break
        else:
            print("Pilihan anda Tidak ada pada Menu")

if __name__ =="__main__":
    main()