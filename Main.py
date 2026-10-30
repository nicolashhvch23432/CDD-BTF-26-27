
from pybricks.tools import wait,StopWatch,hub_menu
from funcoes_btf import hub,andar_reto_suave,reset,drive_base,a_motor,b_motor,andar_reto,turn,left_motor,right_motor,turn2,liberar_motores,configurar_base,configurar_pid,curva
timer = StopWatch()
def saida_1():
    drive_base.reset()
    drive_base.straight(-3)
    andar_reto(20,400)
    turn(-13,400)
    andar_reto(16,400)
    turn(13,400)
    andar_reto(20,400)
    andar_reto(-25,400)
def saida_2():
    curva(440,50)
    andar_reto(9,400)
    a_motor.run_target(1000,300)
    andar_reto_suave(-45,400)
def saida_3():
    b_motor.run_target(500,-50,wait=False)
    a_motor.run_time(-800,800,wait=False)
    andar_reto(70,400)
    left_motor.run_angle(400,48)
    andar_reto(10, 300)
    turn(-15, 450)
    andar_reto_suave(-7,450)
    b_motor.run_target(500,-10)
    andar_reto(14, 450)
    andar_reto(-19,400)
    a_motor.run_time(730,730,wait=False)
    right_motor.run_angle(137,137)
    andar_reto(14.5,400)
    a_motor.run_time(-800,800)
    andar_reto(-7,400)
    curva(-10,-130)
    andar_reto(-50,400)
    turn(-99,400,liberar=True)
    liberar_motores()
    
    '''andar_reto(10)
    turn(-17)''


    turn(10,200)
    wait(700)
    andar_reto(11,400)
    turn(-17,200)
    andar_reto(-5,400)
    b_motor.run_target(500,-10)
    andar_reto(3,400)
    b_motor.run_target(1000,20,wait=False)
    andar_reto(5,400)
    b_motor.run_target(1000,-10)
    andar_reto(-15,400)
    a_motor.run_time(730,730,wait=False)
    right_motor.run_angle(130,130)
    andar_reto(16,400)
    a_motor.run_time(-800,800)
    andar_reto(-7,400)
    curva(-10,-130)
    andar_reto(-50,400)
    turn(-99,400,liberar=True)
    liberar_motores()'''
def saida_4():
    andar_reto(58,300)
    right_motor.run_angle(3000,300)
    andar_reto(-5,400)
    turn(50,400)
    andar_reto(-70,900)

def saida_5():
    andar_reto(30,900)
    

def saida_6():
    drive_base.use_gyro(True)
    a_motor.run_time(-180,800)
    turn(-2,200)
    andar_reto_suave(29,300)
    a_motor.run_time(-500,900)
    andar_reto_suave(-20,400)
    andar_reto(4,500)
    a_motor.run_time(680,800)
    andar_reto(-40,900)


def saida_7():
    drive_base.use_gyro(True)
    andar_reto_suave(30,450)
    turn(-10,450)
    andar_reto_suave(37,450)
    left_motor.run_angle(172,172)
    andar_reto_suave(30,450)
    a_motor.run_time(9000,1000)
    andar_reto(-15,450)
    turn(-65,450)
    andar_reto(-70,900)



def saida_8():
    b_motor.run_target(500,-35, wait=False)
    andar_reto(49,300)
    turn(-20,450)
    b_motor.run_target(500,0)
    andar_reto_suave(-28,300)
    turn(11,500)
    b_motor.run_target(100,-50)
    andar_reto_suave(-20, 450)

    

saidas = [saida_1,saida_2,saida_3,saida_4,saida_5,saida_6,saida_7,saida_8]
proxima_saida = 1
print("PID reta:",drive_base.distance_control.pid())
print("PID curva:",drive_base.heading_control.pid())
while True:
    liberar_motores()
    opcoes = [str(i) for i in range(proxima_saida,9)]+[str(i) for i in range(1,proxima_saida)]
    selected = hub_menu(*opcoes)
    drive_base.use_gyro(True)
    drive_base.reset()
    configurar_base()
    timer.reset()
    numero_saida = int(selected)
    print("Iniciando saida:",numero_saida)
    saidas[numero_saida-1]()
    wait(150)
    print("Saida finalizada:",numero_saida)
    print("Tempo(ms):",timer.time())
    print("Distancia(mm):",drive_base.distance())
    print("Angulo(graus):",drive_base.angle())
    liberar_motores()
    proxima_saida = numero_saida%8+1
    wait(500)

