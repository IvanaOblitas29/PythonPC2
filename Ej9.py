def omitir_vocales(cadena):
    vocales="aeiouAEIOU"
    resultado=""
    for letra in cadena:
        if letra not in vocales:
            resultado=resultado+letra
    return resultado
texto= input("Ingrese la palabra o frase: ")
cadena_no_vocales=omitir_vocales(texto)
print(f"Palabra o frase con las vocales omitides: {cadena_no_vocales}")