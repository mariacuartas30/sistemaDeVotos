votos ={}
def registrar_voto(votos, persona, candidato):
    if persona in votos:
        print("Esta persona ya realizó su voto.")
        return

    votos[persona] = candidato
    print("Voto registrado correctamente.")