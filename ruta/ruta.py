import math

def crearCudaricula(texto, filas, columnas):
    texto = texto.upper().replace(" ", "")  # Convertir a mayúsculas y eliminar espacios
    total = filas * columnas
    texto += 'X' * (total - len(texto))  # Rellenar con 'X' si es necesario
    cuadricula = []
    indice = 0
    for _ in range(filas):
        fila = []
        for _ in range(columnas):
            fila.append(texto[indice])
            indice += 1
        cuadricula.append(fila)
    return cuadricula

def leer(cuadricula):
    filas = len(cuadricula)
    columnas = len(cuadricula[0]) if filas > 0 else 0
    resultado = []
    if filas == 0 or columnas == 0:
        return ""
    arriba, abajo = 0, filas - 1
    izquierda, derecha = 0, columnas - 1
    
    while arriba <= abajo and izquierda <= derecha:
        for col in range(izquierda, derecha + 1):
            resultado.append(cuadricula[arriba][col])
        arriba += 1
        for row in range(arriba, abajo + 1):
            resultado.append(cuadricula[row][derecha])
        derecha -= 1
        if arriba <= abajo:
            for col in range(derecha, izquierda - 1, -1):
                resultado.append(cuadricula[abajo][col])
            abajo -= 1
        if izquierda <= derecha:
            for row in range(abajo, arriba - 1, -1):
                resultado.append(cuadricula[row][izquierda])
            izquierda += 1
    
    return ''.join(resultado)

def cifrar_ruta(texto):
    longitud = len(texto)
    columnas = math.ceil(math.sqrt(longitud))
    filas = math.ceil(longitud / columnas)
    cuadricula = crearCudaricula(texto, filas, columnas)
    texto_cifrado = leer(cuadricula)
    return texto_cifrado

def rellenar(texto_cifrado, filas, columnas):
    cuadricula = [['' for _ in range(columnas)] for _ in range(filas)]
    indice = 0
    arriba, abajo = 0, filas - 1
    izquierda, derecha = 0, columnas - 1
    
    while arriba <= abajo and izquierda <= derecha:
        for col in range(izquierda, derecha + 1):
            if indice < len(texto_cifrado):
                cuadricula[arriba][col] = texto_cifrado[indice]
                indice += 1
        arriba += 1
        for row in range(arriba, abajo + 1):
            if indice < len(texto_cifrado):
                cuadricula[row][derecha] = texto_cifrado[indice]
                indice += 1
        derecha -= 1
        if arriba <= abajo:
            for col in range(derecha, izquierda - 1, -1):
                if indice < len(texto_cifrado):
                    cuadricula[abajo][col] = texto_cifrado[indice]
                    indice += 1
            abajo -= 1
        if izquierda <= derecha:
            for row in range(abajo, arriba - 1, -1):
                if indice < len(texto_cifrado):
                    cuadricula[row][izquierda] = texto_cifrado[indice]
                    indice += 1
            izquierda += 1
    return cuadricula

def leerPorFilas(cuadricula):
    resultado = []
    for fila in cuadricula:
        for char in fila:
            if char != '':
                resultado.append(char)
    return ''.join(resultado)

def descifrarRuta(texto_cifrado):
    longitud = len(texto_cifrado)
    columnas = math.ceil(math.sqrt(longitud))
    filas = math.ceil(longitud / columnas)
    cuadricula = rellenar(texto_cifrado, filas, columnas)
    texto_descifrado = leerPorFilas(cuadricula)
    texto_descifrado = texto_descifrado.rstrip('X')
    return texto_descifrado

def main():
    print("=== Cifrado por Ruta ===")
    modo = input("¿Deseas (C)ifrar o (D)escifrar? ").strip().upper()
    
    if modo not in ['C', 'D']:
        print("Modo inválido. Por favor, elige 'C' para cifrar o 'D' para descifrar.")
        return
    
    texto = input("Introduce el texto: ")
    
    if modo == 'C':
        texto_cifrado = cifrar_ruta(texto)
        print(f"\nTexto Cifrado: {texto_cifrado}")
    else:
        texto_descifrado = descifrarRuta(texto)
        print(f"\nTexto Descifrado: {texto_descifrado}")

if __name__ == "__main__":
    main()
