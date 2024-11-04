def cifrarCesar(texto, desplazamiento):
    resultado = ""
    for char in texto:
        if char.isupper():
            indice = ord(char) - ord('A')
            cifrado = (indice + desplazamiento) % 26
            resultado += chr(cifrado + ord('A'))
        elif char.islower():
            indice = ord(char) - ord('a')
            cifrado = (indice + desplazamiento) % 26
            resultado += chr(cifrado + ord('a'))
        else:
            resultado += char

    return resultado

def descifrarCesar(texto_cifrado, desplazamiento):
    return cifrarCesar(texto_cifrado, -desplazamiento)

def main():
    texto = "¡Hola, Mundo!"
    desplazamiento = 3

    texto_cifrado = cifrarCesar(texto, desplazamiento)
    print(f"Texto Cifrado: {texto_cifrado}")

    texto_descifrado = descifrarCesar(texto_cifrado, desplazamiento)
    print(f"Texto Descifrado: {texto_descifrado}")

if __name__ == "__main__":
    main()
