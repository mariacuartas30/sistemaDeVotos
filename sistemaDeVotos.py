votos ={}

def registrar_voto(votos, persona, candidato):
    if persona in votos:
        print("Esta persona ya realizó su voto.")
        return

    votos[persona] = candidato
    print("Voto registrado correctamente.")

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

    print("\n--- RESULTADOS ---")

    for candidato, cantidad in resultados.items():
        porcentaje = (cantidad / total) * 100

        print(
            f"{candidato}: {cantidad} votos "
            f"({porcentaje:.2f}%)"
        )

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
    