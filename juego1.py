# ==========================================
# JUEGO: AVENTURA EN LA ISLA
# ==========================================

print("==========================================")
print("       AVENTURA EN LA ISLA")
print("==========================================")
print("Objetivo: Encontrar el tesoro escondido.")
print("Debes recolectar 3 llaves y evitar las trampas.")
print("¡Suerte, aventurero!\n")

# Inicializar juego
vidas = 3
llaves = 0
tesoro_encontrado = False

print("Historia inicial:")
print("Llegaste a una isla misteriosa.")
print("Un tesoro está escondido en algún lugar.")
print("Necesitas encontrar 3 llaves para poder buscarlo.\n")

# Mostrar mapa inicial
print("MAPA DE LA ISLA")
print("------------------------------------------")
print("[Norte] [Sur] [Este] [Oeste]")
print("------------------------------------------\n")

# Bucle principal del juego
while vidas > 0 and not tesoro_encontrado:

    # Elegir dirección
    print("Elige una dirección:")
    print("1. Norte")
    print("2. Sur")
    print("3. Este")
    print("4. Oeste")

    opcion = input("Escribe tu opción: ")

    # Validar dirección
    if opcion == "1":
        direccion = "Norte"
    elif opcion == "2":
        direccion = "Sur"
    elif opcion == "3":
        direccion = "Este"
    elif opcion == "4":
        direccion = "Oeste"
    else:
        print("\nOpción no válida. Intenta nuevamente.\n")
        continue

    print(f"\nCaminaste hacia el {direccion}.")

    # Determinar qué hay en la casilla
    # Para que el juego pueda probarse fácilmente,
    # se generan diferentes situaciones.
    import random

    evento = random.choice(["trampa", "llave", "vacio", "tesoro"])

    # ¿Hay una trampa?
    if evento == "trampa":
        vidas -= 1

        print("\n¡Caiste en una trampa!")
        print(f"Vidas restantes: {vidas}")

        # ¿Vidas = 0?
        if vidas == 0:
            print("\n==========================================")
            print("Te quedaste sin vidas.")
            print("FIN DEL JUEGO")
            print("==========================================")
            break

        print("Debes continuar buscando.\n")

    else:
        # Verificar contenido de la casilla
        print("\nVerificando contenido de la casilla...")

        # ¿Hay llave?
        if evento == "llave":
            llaves += 1

            print("¡Encontraste una llave!")
            print(f"Llaves conseguidas: {llaves}")

            # ¿Llaves = 3?
            if llaves == 3:
                print("\n¡Ya tienes las 3 llaves!")
                print("¡Busca el tesoro!")

        else:
            print("No encontraste ninguna llave.")

        # ¿Hay tesoro?
        if evento == "tesoro":

            # Solo puede encontrarse el tesoro
            # cuando se tienen las 3 llaves
            if llaves == 3:
                tesoro_encontrado = True

                print("\n==========================================")
                print("¡FELICIDADES!")
                print("¡Encontraste el tesoro y ganaste!")
                print("==========================================")

            else:
                print("\nEncontraste una zona con un tesoro,")
                print("pero necesitas las 3 llaves para abrirlo.")
                print(f"Actualmente tienes {llaves} llave(s).")

        else:
            print("No hay ningún tesoro en esta casilla.")

    print("\n------------------------------------------")

# Fin del juego
if vidas == 0:
    print("FIN DEL JUEGO")
elif tesoro_encontrado:
    print("FIN DEL JUEGO")
