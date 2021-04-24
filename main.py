from calculadora import somar, subtrair, multiplicar, dividir, calc_all, rad, pot

a = int(input("Insira o número a:"))
b = int(input("Insira o número b:"))

"""print(f'Soma {a} e {b}: {somar(a, b)}')
print(f'Subtração {a} e {b}: {subtrair(a, b)}')
print(f'Multiplicação {a} e {b}: {multiplicar(a, b)}')
print(f'Divisão {a} e {b}: {dividir(a, b):.3f}') 

calc_all(a,b)"""

print(rad(a,b))
print(pot(a,b))
print(pot(a,b)*rad(a,b))
