import random

piedra = 'piedra'
papel = 'papel'
tijera = 'tijera'
lagarto = 'lagarto'
opciones = [piedra, papel, tijera]
partidas = [[papel, piedra], [tijera, papel], [piedra, tijera],
            [lagarto, papel], [piedra, lagarto], [tijera, lagarto]]
no_partidas = [[piedra, papel], [papel, tijera], [tijera, piedra],
               [lagarto, piedra], [lagarto, tijera], [papel, lagarto]]


def generar_movimientos():
    movimiento = random.choice(opciones)
    return movimiento


def verificar_movimientos(usuario_movimento, ordenador_movimiento):
    if [usuario_movimento, ordenador_movimiento] in partidas:
        return 1
    elif [usuario_movimento, ordenador_movimiento] in no_partidas:
        return -1
    return 0


print("JUEGO : Piedra, papel y tijera")


nombre = input("Introduce tu nombre: ")
num_intentos = int(input("Introduce el numero de intentos: "))
cont = 1
ganadas_usuario = 0
ganadas_ordenador = 0

while cont <= num_intentos:
    print(f"Intento número: {cont}")
    ordenador_mov = generar_movimientos()

    usuario_mov = ""
    movimiento_car = input("Selecciona un movimiento ('p' para piedra / 'a' para papel "
                           "/ 't' para tijeras / 'l' para lagarto): ").lower()

    if movimiento_car in ['p', 'a', 't', 'l']:
        if movimiento_car == 'p':
            usuario_mov = piedra
        elif movimiento_car == 'a':
            usuario_mov = papel
        elif movimiento_car == 't':
            usuario_mov = tijera
        elif movimiento_car == 'l':
            usuario_mov = lagarto

        print(f"Elección del ordenador: {ordenador_mov}")
        print(f"Elección del usuario: {usuario_mov}")

        resultado = verificar_movimientos(usuario_mov, ordenador_mov)

        if resultado == 1:
            print(f"Has ganado la ronda, {nombre} !!!")
            ganadas_usuario += 1
        elif resultado == -1:
            print("Gana el ordenador !!!")
            ganadas_ordenador += 1
        elif resultado == 0:
            print("Empate !!!")
        cont += 1
    else:
        print("Entrada incorrecta. Vuelve a intentar.")

print("\nRESULTADOS FINALES:")
if ganadas_usuario > ganadas_ordenador:
    print(f"Ha ganado la partida, {nombre}")
    print("-------------------")
    print(f"|{nombre} : {ganadas_usuario} | Ordenador: {ganadas_ordenador}")
elif ganadas_ordenador > ganadas_usuario:
    print("Ha ganado el ordenador.")
    print("-------------------")
    print(f"|{nombre} : {ganadas_usuario} | Ordenador: {ganadas_ordenador}")
else:
    print("Hubo un empate.")
    print("-------------------")
    print(f"|{nombre} : {ganadas_usuario} | Ordenador: {ganadas_ordenador}")
