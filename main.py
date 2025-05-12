def lista_numeros(numeros):
    
    media = sum(numeros)/len(numeros)
    
    maior_numero = max(numeros)
    menor_numero = min(numeros)

    numeros_pares = sum(1 for n in numeros if n % 2==0)
    
    
    print(f"Lista de numeros:{numeros}")
    print(f"Media:{media:.2f}")
    print(f"Maior numero:{maior_numero}")
    print(f"Menor numero:{menor_numero}")
    print(f"Quantidade de numero pares dentro da lista:{numeros_pares}")