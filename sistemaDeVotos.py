votos = {}


# --------------------------------------------------
# REGISTRAR VOTO
# --------------------------------------------------

def registrar_voto(votos, persona, candidato):
    if persona in votos:
        print("Esta persona ya realizó su voto.")
        return

    votos[persona] = candidato
    print("Voto registrado correctamente.")


# --------------------------------------------------
# VER RESULTADOS
# --------------------------------------------------

def ver_resultados(votos):
    if not votos:
        print("No hay votos registrados.")
        return

    resultados = {}

    for candidato in votos.values():
        if candidato not in resultados:
            resultados[candidato] = 0

        resultados[candidato] += 1

    total = len(votos)

    print("\n================================")
    print("         RESULTADOS")
    print("================================")

    for candidato, cantidad in resultados.items():
        porcentaje = (cantidad / total) * 100
        print(f"{candidato}: {cantidad} votos ({porcentaje:.2f}%)")


# --------------------------------------------------
# MOSTRAR GANADOR
# --------------------------------------------------

def mostrar_ganador(votos):
    if not votos:
        print("No hay votos registrados.")
        return

    resultados = {}

    for candidato in votos.values():
        if candidato not in resultados:
            resultados[candidato] = 0

        resultados[candidato] += 1

    mayor = max(resultados.values())

    ganadores = [
        candidato
        for candidato, cantidad in resultados.items()
        if cantidad == mayor
    ]

    print("\n================================")
    print("          GANADOR")
    print("================================")

    if len(ganadores) == 1:
        print(f"Ganador: {ganadores[0]}")
        print(f"Votos: {mayor}")
    else:
        print("Hay un empate entre:")
        for ganador in ganadores:
            print(f"- {ganador}")
        print(f"Votos obtenidos: {mayor}")


# --------------------------------------------------
# REINICIAR VOTACIÓN
# --------------------------------------------------

def reiniciar_votacion(votos):
    if not votos:
        print("No hay votos para reiniciar.")
        return {}

    with open("historial_votaciones.txt", "a", encoding="utf-8") as archivo:
        archivo.write("=== HISTORIAL DE VOTACIÓN ===\n")

        for persona, candidato in votos.items():
            archivo.write(f"{persona} -> {candidato}\n")

        archivo.write("\n")

    print("Votación reiniciada correctamente.")
    print("El historial fue guardado.")

    return {}


# --------------------------------------------------
# MENÚ PRINCIPAL
# --------------------------------------------------

def menu():
    votos = {}

    while True:
        print("\n================================")
        print("       SISTEMA DE VOTACIÓN")
        print("================================")
        print("1. Registrar voto")
        print("2. Ver resultados")
        print("3. Mostrar ganador")
        print("4. Reiniciar votación")
        print("5. Salir")
        print("================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            persona = input("Ingrese el nombre de la persona: ")
            candidato = input("Ingrese el candidato: ")

            registrar_voto(votos, persona, candidato)

        elif opcion == "2":
            ver_resultados(votos)

        elif opcion == "3":
            mostrar_ganador(votos)

        elif opcion == "4":
            votos = reiniciar_votacion(votos)

        elif opcion == "5":
            print("Gracias por utilizar el sistema de votación.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


# --------------------------------------------------
# INICIAR PROGRAMA
# --------------------------------------------------

menu()