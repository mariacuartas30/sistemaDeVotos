votos ={}
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
    