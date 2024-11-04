def atbash(texto):
    resultado = ""
    for char in texto:
        if char.isupper():
            cifrado = chr(ord('Z') - (ord(char) - ord('A')))
            resultado += cifrado
        elif char.islower():
            cifrado = chr(ord('z') - (ord(char) - ord('a')))
            resultado += cifrado
        else:
            resultado += char

    return resultado

def main():
    texto = "¡Hola, Mundo!"  
    tCifrado = atbash(texto)
    print(f"Texto Cifrado: {tCifrado}")
    tDescifrado = atbash(tCifrado)
    print(f"Texto Descifrado: {tDescifrado}")

if __name__ == "__main__":
    main()
