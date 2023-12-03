#algoritmo hecho por aquiles millan

#Definiimos las variables necesaariias
tablero: str
TurnodelasO: bool
TurnodelasX: bool
Victoria: bool
Turnos: int
#asignamos un valor vacio a la cadena de tablero, a los booleanos necesarios y a la variable turnos
tablero = "                   "
TurnodelasO = True
Victoria = False
#esta variable nos indicaa cuantos turnos llevan los jugadores, si llega a 9 significa que se llenaron las 9 casillas, por ende es empate
Turnos = 1
#//mostramos el tablero vacio creando un formato
print("-------------")
print("|", tablero[0], "|", tablero[1], "|", tablero[2], "|")
print("-------------")
print("|", tablero[3], "|", tablero[4], "|", tablero[5], "|")
print("-------------")
print("|", tablero[6], "|", tablero[7], "|", tablero[8], "|")
print("-------------")
#//creamos un ciclo que se encargue de registrar los turnos, si llega a empate, se cierra el ciclo
while Turnos < 9:
    #//Cuando uno de los jugadores gane se cerrara este clico y terminara el juego
    while Victoria == False:
        #//los booleanos eran para estblecer cuando sera turno de las O o de las X
        if TurnodelasO == True:
            #//se solicita en que casilla desea hacer el movimiento siguiendo la estructura de columnas,filas. Por ejemplo: 1,1
            print("Turno de las O")
            movimiento = str(input("donde desea colocar la O? columna,fila: "))
            #//si se ingresa una posicion no valida seguira el turno
            if (movimiento != "1,1") and (movimiento != "1,2") and (movimiento != "1,3") and (movimiento != "2,1") and (movimiento != "2,2") and (movimiento != "2,3") and (movimiento != "3,1") and (movimiento != "3,2") and (movimiento != "3,3"):
                print("casilla invalida, intente de nuevo")
            else:
                Turnos = Turnos + 1
                #//dependiendo de que posiciion ingrese el usuario se colocara la O
                if movimiento == "1,1":
                    tablero = "O" + tablero[1:10]
                elif movimiento == "2,1":
                    tablero = tablero[0] + "O" + tablero[2] + tablero[3] + tablero[4] + tablero[5] + tablero[6] + tablero[7] + tablero[8]
                elif movimiento == "3,1":
                    tablero = tablero[0] + tablero[1] + "O" + tablero[3] + tablero[4] + tablero[5] + tablero[6] + tablero[7] + tablero[8]
                elif movimiento == "1,2":
                    tablero = tablero[0] + tablero[1] + tablero[2] + "O" + tablero[4] + tablero[5] + tablero[6] + tablero[7] + tablero[8]
                elif movimiento == "2,2":
                    tablero = tablero[0] + tablero[1] + tablero[2] + tablero[3] + "O" + tablero[5] + tablero[6] + tablero[7] + tablero[8] 
                elif movimiento == "3,2":
                    tablero = tablero[0] + tablero[1] + tablero[2] + tablero[3] + tablero[4] + "O" + tablero[6] + tablero[7] + tablero[8]
                elif movimiento == "1,3":
                    tablero = tablero[0] + tablero[1] + tablero[2] + tablero[3] + tablero[4] + tablero[5] + "O" + tablero[7] + tablero[8]  
                elif movimiento == "2,3":
                    tablero = tablero[0] + tablero[1] + tablero[2] + tablero[3] + tablero[4] + tablero[5] + tablero[6] + "O" + tablero[8] 
                elif movimiento == "3,3":
                    tablero = tablero[0] + tablero[1] + tablero[2] + tablero[3] + tablero[4] + tablero[5] + tablero[6] + tablero[7] + "O"
                         
                print("-------")
                print("|", tablero[0], "|", tablero[1], "|", tablero[2], "|")
                print("-------")
                print("|", tablero[3], "|", tablero[4], "|", tablero[5], "|")
                print("-------")
                print("|", tablero[6], "|", tablero[7], "|", tablero[8], "|")
                print("-------")
            
                if ((tablero[0] == "O") and (tablero[1] == "O") and (tablero[2] == "O")) or (tablero[3] == "O" and tablero[4] == "O" and tablero[5] == "O") or (tablero[6] == "O" and tablero[7] == "O" and tablero[8] == "O") or (tablero[6] == "O" and tablero[4] == "O" and tablero[2] == "O") or (tablero[0] == "O" and tablero[3] == "O" and tablero[6] == "O") or (tablero[1] == "O" and tablero[4] == "O" and tablero[7] == "O") or (tablero[2] == "O" and tablero[5] == "O" and tablero[8] == "O") or (tablero[0] == "O" and tablero[4] == "O" and tablero[8] == "O"):
                    print("Felicidades ganaron las O")
                    Victoria = True
                else:
                    TurnodelasO = False
                    TurnodelasX = True
        
        #se utiliza exactamente el msmo algoritmo con las x

        if TurnodelasX == True:
            print("Turno de las X")
            movimiento = str(input("donde desea colocar la X? columna,fila: "))
            if (movimiento != "1,1") and (movimiento != "1,2") and (movimiento != "1,3") and (movimiento != "2,1") and (movimiento != "2,2") and (movimiento != "2,3") and (movimiento != "3,1") and (movimiento != "3,2") and (movimiento != "3,3"):
                print("casilla invalida, intente de nuevo")
            else:
                Turnos = Turnos + 1

                if movimiento == "1,1":
                    tablero = "X" + tablero[1:10]
                elif movimiento == "2,1":
                    tablero = tablero[0] + "X" + tablero[2] + tablero[3] + tablero[4] + tablero[5] + tablero[6] + tablero[7] + tablero[8]
                elif movimiento == "3,1":
                    tablero = tablero[0] + tablero[1] + "X" + tablero[3] + tablero[4] + tablero[5] + tablero[6] + tablero[7] + tablero[8]
                elif movimiento == "1,2":
                    tablero = tablero[0] + tablero[1] + tablero[2] + "X" + tablero[4] + tablero[5] + tablero[6] + tablero[7] + tablero[8]
                elif movimiento == "2,2":
                    tablero = tablero[0] + tablero[1] + tablero[2] + tablero[3] + "X" + tablero[5] + tablero[6] + tablero[7] + tablero[8] 
                elif movimiento == "3,2":
                    tablero = tablero[0] + tablero[1] + tablero[2] + tablero[3] + tablero[4] + "X" + tablero[6] + tablero[7] + tablero[8]
                elif movimiento == "1,3":
                    tablero = tablero[0] + tablero[1] + tablero[2] + tablero[3] + tablero[4] + tablero[5] + "X" + tablero[7] + tablero[8]  
                elif movimiento == "2,3":
                    tablero = tablero[0] + tablero[1] + tablero[2] + tablero[3] + tablero[4] + tablero[5] + tablero[6] + "X" + tablero[8] 
                elif movimiento == "3,3":
                    tablero = tablero[0] + tablero[1] + tablero[2] + tablero[3] + tablero[4] + tablero[5] + tablero[6] + tablero[7] + "X"
                         
                print("-------")
                print("|", tablero[0], "|", tablero[1], "|", tablero[2], "|")
                print("-------")
                print("|", tablero[3], "|", tablero[4], "|", tablero[5], "|")
                print("-------")
                print("|", tablero[6], "|", tablero[7], "|", tablero[8], "|")
                print("-------")
            
                if ((tablero[0] == "X") and (tablero[1] == "X") and (tablero[2] == "X")) or (tablero[3] == "X" and tablero[4] == "X" and tablero[5] == "X") or (tablero[6] == "X" and tablero[7] == "X" and tablero[8] == "X") or (tablero[6] == "X" and tablero[4] == "X" and tablero[2] == "X") or (tablero[0] == "X" and tablero[3] == "X" and tablero[6] == "X") or (tablero[1] == "X" and tablero[4] == "X" and tablero[7] == "X") or (tablero[2] == "X" and tablero[5] == "X" and tablero[8] == "X") or (tablero[0] == "X" and tablero[4] == "X" and tablero[8] == "X"):
                    print("Felicidades ganaron las X")
                    Victoria = True
                else:
                    TurnodelasO = True
                    TurnodelasX = False
    if Victoria == True:
        Turnos = 12
#empate
if Turnos == 9:
    print("no mas casillas disponibles")
    Victoria = True
#termino el juego
if Victoria == True:
    print("el juego ha terminado")




