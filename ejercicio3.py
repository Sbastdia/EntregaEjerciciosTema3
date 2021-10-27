def respuestas(numCoorectas, numIncorrectas, numEnBlanco):
    correcta=3
    incorrecta=-1
    enBlanco=0
    puntuaje= numCoorectas*correcta + numIncorrectas*incorrecta + numEnBlanco*enBlanco
    return puntuaje