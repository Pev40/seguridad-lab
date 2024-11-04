import math

def ordenar_clave(clave):
    clave = clave.upper()
    letras = list(clave)
    orden = sorted(list(set(letras)))
    asignaciones = {}
    contador = 1
    for letra in orden:
        asignaciones[letra] = contador
        contador += 1
    
    orden_columnas = []
    for letra in letras:
        orden_columnas.append(asignaciones[letra])
    
    return orden_columnas

def cifrar_amsco(texto, clave):
    texto = ''.join([char.upper() for char in texto if char.isalnum()])
    num_columnas = len(clave)
    num_filas = math.ceil(len(texto) / num_columnas)
    texto += 'X' * (num_filas * num_columnas - len(texto))
    matriz = []
    indice = 0
    for _ in range(num_filas):
        fila = []
        for _ in range(num_columnas):
            fila.append(texto[indice])
            indice += 1
        matriz.append(fila)
    orden_columnas = ordenar_clave(clave)
    columnas = list(zip(orden_columnas, range(num_columnas)))
    columnas_sorted = sorted(columnas, key=lambda x: x[0])
    texto_cifrado = ""
    for _, idx in columnas_sorted:
        for fila in matriz:
            texto_cifrado += fila[idx]
    
    return texto_cifrado

def descifrar_amsco(texto_cifrado, clave):
    texto_cifrado = ''.join([char.upper() for char in texto_cifrado if char.isalnum()])  
    num_columnas = len(clave)
    num_filas = math.ceil(len(texto_cifrado) / num_columnas)
    orden_columnas = ordenar_clave(clave)    
    columnas = list(zip(orden_columnas, range(num_columnas)))
    columnas_sorted = sorted(columnas, key=lambda x: x[0])
    num_letras = len(texto_cifrado)
    letras_por_columna = num_filas
    columnas_asignadas = {}
    indice = 0
    for _, idx in columnas_sorted:
        columnas_asignadas[idx] = texto_cifrado[indice:indice + letras_por_columna]
        indice += letras_por_columna
    matriz = []
    for _ in range(num_filas):
        fila = []
        for i in range(num_columnas):
            fila.append(columnas_asignadas[i][0] if len(columnas_asignadas[i]) > 0 else 'X')
            columnas_asignadas[i] = columnas_asignadas[i][1:]
        matriz.append(fila)
    texto_descifrado = ""
    for fila in matriz:
        texto_descifrado += ''.join(fila)
    texto_descifrado = texto_descifrado.rstrip('X')
    
    return texto_descifrado

def main():
    print("=== Cifrado AMSCO ===")
    modo = input("¿Deseas (C)ifrar o (D)escifrar? ").strip().upper()
    
    if modo not in ['C', 'D']:
        print("Modo inválido. Por favor, elige 'C' para cifrar o 'D' para descifrar.")
        return
    
    texto = input("Introduce el texto: ")
    clave = input("Introduce la clave: ")
    
    if modo == 'C':
        texto_cifrado = cifrar_amsco(texto, clave)
        print(f"\nTexto Cifrado: {texto_cifrado}")
    else:
        texto_descifrado = descifrar_amsco(texto, clave)
        print(f"\nTexto Descifrado: {texto_descifrado}")

if __name__ == "__main__":
    main()
