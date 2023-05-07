import random

def estrategiaJuan():
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    resultado = 0

    #print(f'Juan tiro los dados con valores ({dado1},{dado2})')

    if(dado1 == 4):
        resultado = dado2
        if(dado2 <= 3):
            resultado = random.randint(1,6)
            #print(f'Se volvio a tirar dado con valor {dado2}')
            #print(f'Valor final ({dado1},{resultado})')
    elif(dado2 == 4):
        resultado = dado1
        if(dado1 <= 3):
            resultado = random.randint(1,6)
            #print(f'Se volvio a tirar dado con valor {dado1}')
            #print(f'Valor final ({resultado},{dado2})')
    
    #print(f'El resutado es {resultado}')


    if(resultado == 0):
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)

        #print(f'Juan tiro los dos dados nuevamente con valores ({dado1},{dado2})')

        if(dado1 == 4):
            resultado = dado2
        elif(dado2 == 4):
            resultado = dado1

        #print(f'El resutado es {resultado}')
    
    return resultado
    

def estrategiaMaria(puntos):
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    resultado = 0

    #print(f'Maria tiro los dados con valores ({dado1},{dado2})')

    if(dado1 == 4):
        if(dado2 == puntos):
            if(dado2 <= 3):
                resultado = random.randint(1,6)
                #print(f'Ya que el resultado igual a los puntos de Juan y es menor o igual a 3 se vuelve a lanzar el dado con valor {dado2}')
            elif(dado2 > 3):
                resultado = dado2
                #print(f'Ya que el resultado es igual a los puntos de Juan y es mayor a 3 se me quedo con este resultado')
        elif(dado2 <= puntos):
            resultado = random.randint(1,6)
            #print(f'Ya que el resultado es menor al de Juan vuelvo a lanzar el dado con valor {dado2}')
        elif(dado2 > puntos):
            resultado = dado2
            #print(f'Ya que el resultado es mayor al de Juan, no vuelvo a jugar el dado')
        #print(f'Valor final ({dado1},{resultado})')
    elif(dado2 == 4):
        if(dado1 == puntos):
            if(dado1 <= 3):
                resultado = random.randint(1,6)
                #print(f'Ya que el resultado igual a los puntos de Juan y es menor o igual a 3 se vuelve a lanzar el dado con valor {dado1}')
            elif(dado1 > 3):
                resultado = dado1
                #print(f'Ya que el resultado es igual a los puntos de Juan y es mayor a 3 se me quedo con este resultado')
        elif(dado1 <= puntos):
            resultado = random.randint(1,6)
            #print(f'Ya que el resultado es menor al de Juan vuelvo a lanzar el dado con valor {dado1}')
        elif(dado1 > puntos):
            resultado = dado1
            #print(f'Ya que el resultado es mayor al de Juan, no vuelvo a jugar el dado')
        #print(f'Valor final ({resultado},{dado2})')

    #print(f'El resutado es {resultado}')

    if(resultado == 0):
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)

        #print(f'Maria tiro los dos dados nuevamente con valores ({dado1},{dado2})')
    
        if(dado1 == 4):
            resultado = dado2
        elif(dado2 == 4):
            resultado = dado1
    
        #print(f'El resutado es {resultado}')

    return resultado

def jugar(cantidadJuegos):
    empates = 0
    ganadosJuan = 0
    ganadosMaria = 0

    for x in range(cantidadJuegos):
        puntosJuan = estrategiaJuan()
        puntosMaria = estrategiaMaria(puntosJuan)

        #print(f'Puntos Juan: {puntosJuan}')
        #print(f'Puntos Maria: {puntosMaria}')

        if(puntosJuan == puntosMaria):
            empates = empates+1
        elif(puntosJuan > puntosMaria):
            ganadosJuan = ganadosJuan+1
        elif(puntosJuan < puntosMaria):
            ganadosMaria = ganadosMaria+1

    print(f'Se jugaron un total de {cantidadJuegos} veces')
    print(f'Veces que empataron: {empates}')
    print(f'Veces que gano Juan: {ganadosJuan}')
    print(f'Veces que gano Maria: {ganadosMaria}')




if __name__ == "__main__":
    jugar(100000)
