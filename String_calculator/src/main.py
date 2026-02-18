def suma_string_numeros(cadena):
    cadena = cadena.replace("\n", ",")
    numeros = cadena.split(",")
    return sum(int(n.strip()) for n in numeros if n.strip() != "")


if __name__ == "__main__":
    entrada = input("Introduce números separados por comas: ")
    resultado = suma_string_numeros(entrada)
    print("La suma es:", resultado)
