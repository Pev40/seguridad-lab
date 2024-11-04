import string

def crearTabla(clave):
    clave = clave.replace(" ", "").upper()
    clave = clave.replace("J", "I")
    tabla = []
    letras_usadas = set()
    for char in clave:
        if char in string.ascii_uppercase and char not in letras_usadas:
            tabla.append(char)
            letras_usadas.add(char)
    for char in string.ascii_uppercase:
        if char == "J":
            continue  # Se omite 'J'
        if char not in letras_usadas:
            tabla.append(char)
            letras_usadas.add(char)
    tabla_playfair = [tabla[i:i+5] for i in range(0, 25, 5)]
    return tabla_playfair

def imprimir(tabla):
    print("Tabla de Playfair:")
    for fila in tabla:
        print(" ".join(fila))
    print()

def prepararTexto(texto):
    texto = ''.join([char for char in texto if char.isalpha()]).upper()
    texto = texto.replace("J", "I")
    
    digrafos = []
    i = 0
    while i < len(texto):
        letra1 = texto[i]
        if i + 1 < len(texto):
            letra2 = texto[i + 1]
            if letra1 != letra2:
                digrafos.append(letra1 + letra2)
                i += 2
            else:
                digrafos.append(letra1 + 'X')
                i += 1
        else:
            digrafos.append(letra1 + 'X')
            i += 1
    return digrafos

def cambiarposicion(tabla, letra):
    for fila_idx, fila in enumerate(tabla):
        if letra in fila:
            return (fila_idx, fila.index(letra))
    return None

def cifrar_playfair(texto, clave):
    tabla = crearTabla(clave)
    digrafos = prepararTexto(texto)
    texto_cifrado = ""
    for par in digrafos:
        pos1 = cambiarposicion(tabla, par[0])
        pos2 = cambiarposicion(tabla, par[1])

        if pos1[0] == pos2[0]:
            texto_cifrado += tabla[pos1[0]][(pos1[1] + 1) % 5]
            texto_cifrado += tabla[pos2[0]][(pos2[1] + 1) % 5]
        elif pos1[1] == pos2[1]:
            texto_cifrado += tabla[(pos1[0] + 1) % 5][pos1[1]]
            texto_cifrado += tabla[(pos2[0] + 1) % 5][pos2[1]]
        else:
            texto_cifrado += tabla[pos1[0]][pos2[1]]
            texto_cifrado += tabla[pos2[0]][pos1[1]]    
    return texto_cifrado

def descifrarPlayfair(texto_cifrado, clave):
    tabla = crearTabla(clave)
    digrafos = [texto_cifrado[i:i+2] for i in range(0, len(texto_cifrado), 2)]
    texto_descifrado = ""

    for par in digrafos:
        pos1 = cambiarposicion(tabla, par[0])
        pos2 = cambiarposicion(tabla, par[1])

        if pos1[0] == pos2[0]:
            texto_descifrado += tabla[pos1[0]][(pos1[1] - 1) % 5]
            texto_descifrado += tabla[pos2[0]][(pos2[1] - 1) % 5]
        elif pos1[1] == pos2[1]:
            texto_descifrado += tabla[(pos1[0] - 1) % 5][pos1[1]]
            texto_descifrado += tabla[(pos2[0] - 1) % 5][pos2[1]]
        else:
            texto_descifrado += tabla[pos1[0]][pos2[1]]
            texto_descifrado += tabla[pos2[0]][pos1[1]] 
    return texto_descifrado

def main():
    print("=== Cifrado Playfair ===")
    modo = input("¿Deseas (C)ifrar o (D)escifrar? ").strip().upper()
    
    if modo not in ['C', 'D']:
        print("Modo inválido. Por favor, elige 'C' para cifrar o 'D' para descifrar.")
        return
    
    texto = input("Introduce el texto: ")
    clave = input("Introduce la clave: ")
    
    if modo == 'C':
        texto_cifrado = cifrar_playfair(texto, clave)
        print(f"\nTexto Cifrado: {texto_cifrado}")
    else:
        texto = ''.join([char for char in texto if char.isalpha()]).upper()
        if len(texto) % 2 != 0:
            print("El texto cifrado debe tener un número par de caracteres.")
            return
        texto_descifrado = descifrarPlayfair(texto, clave)
        print(f"\nTexto Descifrado: {texto_descifrado}")


if __name__ == "__main__":
    main()
