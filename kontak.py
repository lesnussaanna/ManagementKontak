"berisi kelas kontak untuk mengolah kontak"

from module import membuka_kontak
from module import menyimpan_kontak
class Kontak:
    def __init__(self):
        self.kontak= membuka_kontak()

    def melihat_kontak(self):
        # Melihat Semua Kontak
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f"{num}. "+ item)
        else:
            print("Kontak Kosong! Mohon Tambahkan Kontak")
            return 1

    def menambah_kontak(self):
        # Menambahkan Kontak
        nama = input("Masukan nama Kontak: ")
        hp = input("Masukan nomor Handphone: ")
        email = input("Masukan Email: ")
        kontak_baru = f'{nama} ({hp},{email})' + '\n'
        self.kontak.append(kontak_baru)
        print("Kontak baru berhasil ditambahkan!")

    def menghapus_kontak(self):
        # Menghapus Kontak
        if  self.melihat_kontak()== 1:
            return
        else:
            try:
                jumlah_kontak = len(self.kontak)
                kontak_hapus = int(input("Masukan Nomor Kontak yang akan dihapus: "))
                del self.kontak[kontak_hapus - 1]
                print("Kontak berhasil dihapus!\n")
            except:
                print("Inputan anda tidak sesuai")

    def keluar_kontak(self):
        menyimpan_kontak(isi=self.kontak)