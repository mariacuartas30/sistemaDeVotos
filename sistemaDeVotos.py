votos ={}
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