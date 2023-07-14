#LEISHA NOVEA
#205150301111035
import sys
print('Selamat datang di program aritmatika  sederhana!!')
print('1. Penjumlahan')
print('2. Pengurangan')
print('3. Perkalian')
print('4. Pembagian(float)')
print('5. Floor ')
print('6. Modulo')
print('7. Pangkat')
loops = True
while (loops):
    a = int(input('Pilih salah satu: '))

    if a==1:
        b = int(input("Angka 1: "))
        c = int(input('Angka 2: '))
        jml = b + c
        print(int(jml))
        if input('Apakah anda ingin melanjutkan? ') != 'y':
            sys.exit()
      
        
    
    elif a==2:
        b = int(input("Angka 1: "))
        c = int(input('Angka 2: '))
        krg = b -c
        print(int(krg))
        if input('Apakah anda ingin melanjutkan? ') != 'y':
            sys.exit()
        
    
    elif a == 3:
        b = int(input("Angka 1: "))
        c = int(input('Angka 2: '))
        kali = b*c
        print(int(kali))
        if input('Apakah anda ingin melanjutkan? ') != 'y':
            sys.exit()
       
           
    elif a == 4 :
        b = int(input("Angka 1: "))
        c = int(input('Angka 2: '))
        bagi = b/c
        print(float(bagi))
        if input('Apakah anda ingin melanjutkan? ') != 'y':
            sys.exit()
        
            
    
    elif a == 5:
        b = int(input("Angka 1: "))
        c = int(input('Angka 2: '))
        floor = b//c
        print(floor)
        if input('Apakah anda ingin melanjutkan? ') != 'y':
            sys.exit()
        
            
    
    elif a == 6:
        b = int(input("Angka 1: "))
        c = int(input('Angka 2: '))
        print(b%c)
        if input('Apakah anda ingin melanjutkan? ') != 'y':
            sys.exit()
        
    
    elif a == 7: 
        b = int(input("Angka 1: "))
        c = int(input('Angka 2: '))
        print(b**c)
        if input('Apakah anda ingin melanjutkan? ') != 'y':
            sys.exit()
        
        
      
    


    

    
