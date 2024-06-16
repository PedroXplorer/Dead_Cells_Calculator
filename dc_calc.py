dano = float(input("Dano inicial: "))
dano2 = float(input("Dano secundário: "))
per_a = float(input("Porcentagem de dano adicional: "))
dano_s = dano + dano2
dano_t = dano_s + (dano_s *(per_a/100))
print(f"Dano total da armas: {dano_t}")