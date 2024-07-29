import itertools

# Palabras a combinar
palabras = ["ipms", "costarica", "cr", "oficial"]

# Lista de combinaciones que ya existen
combinaciones_existentes = ["ipmscostaricaoficial", "ipmscostarica", "ipmscr", "ipms.costarica", "ipmscr.oficial", "ipms.cr"]

# Función para generar combinaciones
def generarCombinaciones(palabras):
    todas_combinaciones = set()
    for i in range(1, len(palabras) + 1):
        for combo in itertools.permutations(palabras, i):
            combinacion = "".join(combo)
            if "cr" in combo and "costarica" in combo:
                continue
            todas_combinaciones.add(combinacion)
            todas_combinaciones.add(".".join(combo))
    return todas_combinaciones

# Generar todas las combinaciones
todas_combinaciones = generarCombinaciones(palabras)

# Filtrar las combinaciones existentes
nuevas_combinaciones = [combo for combo in todas_combinaciones if combo not in combinaciones_existentes]

# Imprimir las nuevas combinaciones
for combinacion in nuevas_combinaciones:
    print(combinacion)
