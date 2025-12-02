def pot2(n):
    if n == 0:
        return 1
    if n < 0:
        return 1 
    else:
        return 2 * pot2(n - 1)

n_exemplo = 5
resultado = pot2(n_exemplo)

print(f"Potência de 2^{n_exemplo} (capacidade dobrada 5 vezes): {resultado}") 
print(f"Potência de 2^0: {pot2(0)}")  
print(f"Potência de 2^3: {pot2(3)}")   