import string
    
def crear_tabla_polybius():
    alfabeto = "ABCDEFGHIKLMNOPQRSTUVWXYZ" 
    
    tabla = {}
    tabla_inversa = {}
    fila = 1
    columna = 1
    
    for letra in alfabeto:
        tabla[letra] = f"{fila}{columna}"
        tabla_inversa[f"{fila}{columna}"] = letra
        columna += 1
        if columna > 5:
            columna = 1
            fila += 1
    
    return tabla, tabla_inversa

def cifrar_polybius(texto):
    tabla, _ = crear_tabla_polybius()
    texto_cifrado = ""
    
    for caracter in texto.upper():
        if caracter == 'J':
            caracter = 'I' 
        if caracter in tabla:
            texto_cifrado += tabla[caracter] + " "
        else:
            texto_cifrado += caracter + " " 
    
    return texto_cifrado.strip()

def descifrar_polybius(texto_cifrado):
    _, tabla_inversa = crear_tabla_polybius()
    texto_descifrado = ""
    pares = texto_cifrado.split()
    
    for par in pares:
        if par.isdigit() and len(par) == 2:
            letra = tabla_inversa.get(par, '')
            texto_descifrado += letra
        else:
            texto_descifrado += par 
    return texto_descifrado

def main():
    print("=== Cifrado de Polybius ===")
    modo = input("¿Deseas (C)ifrar o (D)escifrar? ").strip().upper()
    
    if modo not in ['C', 'D']:
        print("Modo inválido. Por favor, elige 'C' para cifrar o 'D' para descifrar.")
        return
    
    texto = input("Introduce el texto: ")
    
    if modo == 'C':
        texto_cifrado = cifrar_polybius(texto)
        print(f"\nTexto Cifrado: {texto_cifrado}")
    else:
        texto_descifrado = descifrar_polybius(texto)
        print(f"\nTexto Descifrado: {texto_descifrado}")

if __name__ == "__main__":
    main()
