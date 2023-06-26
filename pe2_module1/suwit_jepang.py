from enum import IntEnum
import random

class Isyarat(IntEnum):
    BATU = 1
    GUNTING = 2
    KERTAS = 3

def get_isyarat_pemain():
    pilihan = [f"{isyarat.value}. {isyarat.name}" for isyarat in Isyarat]
    print("\nMasukkan angka sesuai pilihan dibawah:")
    for pilihan_user in pilihan:
        print(pilihan_user.title())
    isyarat_pemain = Isyarat(int(input(f"> ")))
    return isyarat_pemain

def get_isyarat_komputer():
    isyarat_komputer = Isyarat(random.randint(1, len(Isyarat)))
    return isyarat_komputer

def menentukan_pemenang(isyarat_pemain, isyarat_komputer):
    kondisi_menang = {
        Isyarat.BATU : Isyarat.GUNTING,
        Isyarat.GUNTING : Isyarat.KERTAS,
        Isyarat.KERTAS: Isyarat.BATU
    }
    kondisi_kalah = kondisi_menang[isyarat_pemain]
    if isyarat_pemain == isyarat_komputer:
        print(f"Kedua peserta memilih {isyarat_pemain.name.lower()}. Permainan seri!")
    elif isyarat_komputer == kondisi_kalah:
        print(f"{isyarat_pemain.name.capitalize()} mengalahkan {isyarat_komputer.name.lower()}. Pemain menang!")
    else:
        print(f"{isyarat_komputer.name.capitalize()} mengalahkan {isyarat_pemain.name.lower()}. Pemain kalah.")
