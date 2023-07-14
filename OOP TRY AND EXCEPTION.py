'''print("Ini adalah program pembagian")

while True:
    try:
        import panda
        penyebut = int(input("Masukkan angka penyebut: "))
        pembilang = int(input("Masukkan angka pembilang: "))
        hasil = penyebut/pembilang
        break
    except ValueError:
        print("yang anda masukkan bukan angka\n")
    except ZeroDivisionError:
        print("Angka pembilang yang anda masukkan adalah nol, pilih yang lain ya bro/sist\n")
    except ImportError:
        print("Gaada modulnya bro")
    except Exception as err:
        print(err)

print("berhasil, hasil pembagian adalah: ",hasil)
'''

class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a +self.b

    def subtraction(self):
        return self.a -self.b

    def multiplication(self):
        return self.a*self.b

    def pembagian(self):
        return self.a//self.b


while True:
    try:
        print("\n1.Penjumlahan")
        print("2.Pengurangan")
        print("3.Perkalian")
        print("4.Pembagian")
        inputt =int(input(("Pilih operasi: ")))
        x = int(input("Angka1   : "))
        y = int(input("Angka2  : "))

        if (inputt == 1):
            kalk = Calculator(x,y)
            print("Hasilnya adalah: ",kalk.addition())
        elif (inputt == 2):
            kalk = Calculator(x,y)
            print("Hasilnya adalah: ",kalk.subtraction())
        elif (inputt ==3):
            kalk = Calculator(x,y)
            print("Hasilnya adalah: ",kalk.multiplication())
        else:
            kalk = Calculator(x,y)
            print("Hasilnya adalah: ",kalk.pembagian())
        break
    except ValueError:
        print("Yang anda masukkan bukan angka\n")
    except ZeroDivisionError:
        print("Angka penyebut yang anda masukkan adalah nol")
    except Exception as err:
        print(err)
