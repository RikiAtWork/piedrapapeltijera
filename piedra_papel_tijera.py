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
while True:
    opcion = input("Quieres jugar? (s/n): ")
    if 's' in opcion.lower():
        ordenador_mov = generar_movimientos()
        while True:
            usuario_mov = ""
            movimiento_car = input("Selecciona un movimiento ('p' para piedra / 'a' para papel "
                                   "/ 't' para tijeras, 'l' lagarto): ").lower()
            if movimiento_car.upper() == "TERMINAR":
                print("Tienes miedo?")
                break
            else:
                print(f"Elección del ordenador: {ordenador_mov}")
                if movimiento_car in ['p', 'a', 't', 'l']:
                    if 'p' in movimiento_car:
                        usuario_mov = piedra
                    elif 'a' in movimiento_car:
                        usuario_mov = papel
                    elif 't' in movimiento_car:
                        usuario_mov = tijera
                    elif 'l' in movimiento_car:
                        usuario_mov = lagarto
                    print(f"Elección del usuario: {usuario_mov}")
                    if verificar_movimientos(usuario_mov, ordenador_mov) == 1:
                        print("Gana el usuario !!!")
                    elif verificar_movimientos(usuario_mov, ordenador_mov) == -1:
                        print("Gana el ordenador !!!")
                    elif verificar_movimientos(usuario_mov, ordenador_mov) == 0:
                        print("Empate !!!")
                    break
                else:
                    print("Entrada incorrecta. Vuelve a intentar.")
    elif 'n' in opcion.lower():
        break
    else:
        print('Entrada incorrecta. Vuelve a intentar.')
    print()
