print ("CREATE BY : NOPAL")
def kalkulator():
#MENU APLIKASI
    print ("I--------------------------------I")
    print ("I      APLIKASI KALKULATOR       I")
    print ("I--------------------------------I")
    print ("I Pilih Operasi:                 I")
    print ("I--------------------------------I")
    print ("I  1. Pengurangan                I")
    print ("I  2. Penjumlahan                I")
    print ("I  3. Perkalian                  I")
    print ("I  4. Pembagian                  I")
    print ("I  5. Pemangkat                  I")
    print ("I  6. CV Desimal Ke Biner        I")
    print ("I  7. CV Biner Ke Desimal        I")
    print ("I                                I")
    print ("I  0. EXIT                       I")
    print ("I--------------------------------I")
    while True:
        pilih = input("Masukan Operasi (1,2,3,4,5,6,7,0) : ")
        if pilih.lower() == '0':
            break

#SISTEM OPERASI
        if pilih in ['1', '2', '3', '4', '5', '6', '7']:
            try:
                if pilih == '1':
                    x = int(input("Masukan Angka Pertama : "))
                    y = int(input("Masukan Angka kedua : "))
                    hasil = x - y
                    print (f"Hasil Dari {x} dikurang {y} adalah : {hasil}")

                if pilih == '2':
                    x = int(input("Masukan Angka Pertama : "))
                    y = int(input("Masukan Angka kedua : "))
                    hasil = x + y
                    print (f"Hasil Dari {x} ditambah {y} adalah : {hasil}")

                if pilih == '3':
                    x = int(input("Masukan Angka Pertama : "))
                    y = int(input("Masukan Angka kedua : "))
                    hasil = x * y
                    print (f"Hasil Dari {x} dikali {y} adalah : {hasil}")

                if pilih == '4':
                    x = int(input("Masukan Angka Pertama : "))
                    y = int(input("Masukan Angka Pembagi : "))
                    hasil = x / y
                    if y != 0:
                        print (f"Hasil Dari {x} dibagi {y} adalah : {hasil}")
                    else:
                        print ("Tidak bisa dibagi dengan angka 0 !")

                if pilih == '5':
                    x = int(input("Masukan Angka Pertama : "))
                    y = int(input("Masukan Angka Pemangkat : "))
                    hasil = x ** y
                    print (f"Hasil Dari {x} pangkat {y} adalah : {hasil}")

                if pilih == '6':
                    def desimal_ke_biner(desimal):
                        return bin(desimal) [2:]
                    desimal = int(input("Masukkan bilangan desimal : "))
                    biner = desimal_ke_biner(desimal)
                    print (f"bilangan desimal ({desimal}) dalam biner adalah : {biner}")

                if pilih == '7':
                    def biner_ke_desimal(biner):
                        desimal = 0
                        for digit in biner:
                            desimal = desimal * 2 + int(digit)
                        return desimal
                    biner = input("Masukkan bilangan biner : ")
                    desimal = biner_ke_desimal(biner)
                    print (f"bilangan biner ({biner}) dalam desimal adalah : {desimal}")
            except ValueError:
                print ("Input tidak valid !")
        else:
            print ("Pilihan tidak valid silahkan coba lagi !")

kalkulator()
