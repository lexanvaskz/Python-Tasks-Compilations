# Defisig Fungsi
def f(x):
    return x**3-5*x-9

# Implementasi metode reguler falsi
def falsePosition(x0,x1,e):
    step = 1
    print('\n\n*** Implementasi Metode Regulas Falsi ***')
    condition = True
    while condition:
        x2 = x0 - (x1-x0) * f(x0)/( f(x1) - f(x0) )
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        step = step + 1
        condition = abs(f(x2)) > e

    print('\nRequired root is: %0.8f' % x2)


# Input Section
x0 = input('Nilai X0: ')
x1 = input('Nilai X1: ')
e = input('Nilai  Error toleransi : ')

# Converting input to float
x0 = float(x0)
x1 = float(x1)
e = float(e)




# Check nilai F(x)
if f(x0) * f(x1) > 0.0:
    print('Di antara kedua titik tidak diketemukan akar.')
    print('Masukan nilai baru.')
else:
    falsePosition(x0,x1,e)
