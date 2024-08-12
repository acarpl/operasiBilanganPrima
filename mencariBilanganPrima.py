# Input batas bawah sama atas
batas_bawah = int(input("Masukkan batas bawah: "))
batas_atas = int(input("Masukkan batas atas: "))

# Operasi Mencari Bilangan Prima
angka_sekarang = batas_bawah
while angka_sekarang <= batas_atas:
    if angka_sekarang > 1:
        prima = True
        i = 2
        while i * i <= angka_sekarang:
            if angka_sekarang % i == 0:
                prima = False
                break
            i += 1
        if prima:
            print ("bilangan prima rentang", batas_bawah, "dan", batas_atas, "adalah")
            print( angka_sekarang)
    angka_sekarang += 1