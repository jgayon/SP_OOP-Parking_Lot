class Parqueadero:
    
    def __init__(self) -> None:
        pass

    espaciotot= 150
    espacio_com=50
    espacio_suv=50
    espacio_van=50

    cobro_dia= 30000
    cobro_hora=10000
    cobro_min= 5000

    def cobro_tiempo():
        a_cobrar= input('Escoga el tiempo que se quiere quedar: (min, hora o dia)\n')
        if a_cobrar == 'min':
            cuanto = int(input('Cunatos minutos se va a quedar?\n'))
            costo = Parqueadero.cobro_min*cuanto
        elif a_cobrar =='hora':
            cuanto = int(input('Cunatas horas se va a quedar?\n'))
            costo = Parqueadero.cobro_hora*cuanto
        elif a_cobrar == 'dia':
            costo = Parqueadero.cobro_dia