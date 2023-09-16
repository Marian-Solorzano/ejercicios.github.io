rango = int(input("Rango para calcular números primos 0 a :"))

for i in range(2,rango+1):
    for j in range(1,i+1):
        prim_eval = i%j
        es_primo = True

        if  j != 1 and prim_eval == 0 and j != i:
            es_primo = False
            break

    if es_primo == True:
        print(i)