# Rama Timer
# se crea branch Timer para adicion de funcion timer

from datetime import datetime
import winsound


def activar_alarma():
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 500  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)
    frequency = 5000  # Set Frequency To 2500 Hertz
    duration = 500  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 500  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)
    frequency = 5000  # Set Frequency To 2500 Hertz
    duration = 500  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)





ejecutar = True

print("Programa tiempo")
tiempo = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(tiempo)
tiempo = tiempo.split()
print("Split ->", tiempo)




while ejecutar:
    hora = input("Ingrese hora de alarma hh:mm:ss, q (salir) ->")
    if hora != "q":
        print("Tiempo ingresado: ", hora)
        while tiempo[1] != hora:
            tiempo = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            tiempo = tiempo.split()
                
        print("Alarma !")
        activar_alarma()
    elif hora == "q":
        ejecutar = False
        print("Saliendo del programa...nos vemos la proxima!")
    else:
        print("Opcion no valida!")


             