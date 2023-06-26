import suwit_jepang

while True:
    try:
        isyarat_pemain = suwit_jepang.get_isyarat_pemain()
    except ValueError:
        print(f"Silahkan masukan angka sesuai ketentuan!")
        continue
    
    isyarat_komputer = suwit_jepang.get_isyarat_komputer()
    suwit_jepang.menentukan_pemenang(isyarat_pemain, isyarat_komputer)
    
    bermain_lagi = input("Ingin bermain lagi? (y/t): ")
    if bermain_lagi.lower() != 'y':
        print("Permainan selesai.")
        break
