import pyautogui
import time
import multiprocessing
from datetime import datetime

# Variable para controlar el bucle
process = None

def mostrar_menu():
    print("----------------------------------------")
    print("      Bienvenido al script de actividad")
    print("----------------------------------------")
    print("1. Iniciar el script")
    print("2. Parar el script")
    print("3. Salir")
    print("----------------------------------------")

def simular_movimiento():
    try :
        while True:
            # Mueve el ratón ligeramente
            pyautogui.moveRel(10, 0)  # Mueve el ratón 1 pixel a la derecha
            time.sleep(1)  # Espera 1 segundo
            pyautogui.moveRel(-10, 0)  # Mueve el ratón 1 pixel a la izquierda
            print(f"Simulación de movimiento realizada a las {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            time.sleep(3)
    except Exception as e:
        print(f"Error fatal fatalitico: {e}")

def main():
    global process

    while True:
        if process is not None and process.is_alive():
            print("El proceso está en ejecución en background")
        else:
            print("El proceso está off")

        mostrar_menu()

        opcion = input("Selecciona una opción [1-3]: ").strip()

        if opcion == "1":
            if process is not None and process.is_alive():
                print("----------------------------------------")
                print("El script ya está en ejecución.")
            else:
                print("----------------------------------------")
                print(">>>Para PARAR el script, selecciona la opción 2 del menú.")
                print(">>>Iniciando el script...")
                # Inicia la simulación en un hilo separado
                process = multiprocessing.Process(target=simular_movimiento, args=())
                process.start()

        elif opcion == "2":
            if process is not None and process.is_alive():
                print("----------------------------------------")
                print("Parando el script...")
                print("----------------------------------------")
                process.terminate()
            else:
                print("----------------------------------------")
                print("El script no está en ejecución.")
                print("----------------------------------------")

        elif opcion == "3":
            print("Saliendo...")
            if process is not None and process.is_alive():
                process.terminate()
            break

        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")

if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
