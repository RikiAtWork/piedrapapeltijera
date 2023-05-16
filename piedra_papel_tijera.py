import random

piedra = 'piedra'
papel = 'papel'
tijera = 'tijera'
opciones = [piedra, papel, tijera]
partidas = [[papel, piedra], [tijera, papel], [piedra, tijera]]
no_partidas = [[piedra, papel], [papel, tijera], [tijera, piedra]]


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
                                   "/ 't' para tijeras): ").lower()
            print(f"Elección del ordenador: {ordenador_mov}")
            if 'p' in movimiento_car or 'a' in movimiento_car or 't' in movimiento_car:
                if 'p' in movimiento_car:
                    usuario_mov = piedra
                elif 'a' in movimiento_car:
                    usuario_mov = papel
                elif 't' in movimiento_car:
                    usuario_mov = tijera
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
