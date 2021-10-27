def respuestas(numCorrectas, numIncorrectas, numEnBlanco):
    correcta=3
    incorrecta=-1
    enBlanco=0
    puntuaje= numCorrectas*correcta + numIncorrectas*incorrecta + numEnBlanco*enBlanco
    print ('El puntuaje es: ', puntuaje)