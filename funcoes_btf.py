# Funções para a FLL
# Criadores: Deivid e Jean
# Versão: 1.1
# Funções: Andar Reto, Andar Reto com Rampa, Curva


from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Direction, Port, Axis, Color, Stop
from pybricks.tools import wait
from pybricks.robotics import DriveBase
hub = PrimeHub(top_side=Axis.Z,front_side=Axis.X)
left_motor = Motor(Port.E,Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D)
a_motor = Motor(Port.A)
b_motor = Motor(Port.B)
drive_base = DriveBase(left_motor,right_motor,60,115)
VEL_RETA = 400
VEL_CURVA = 400
ACEL_RETA = 1000
FREIO_RETA = 1500
ACEL_SUAVE = 650
FREIO_SUAVE = 950
ACEL_CURVA = 250
FREIO_CURVA = 550
PID_PADRAO = drive_base.heading_control.pid()
def configurar_base():
    drive_base.settings(straight_speed=VEL_RETA,straight_acceleration=(ACEL_RETA,FREIO_RETA),turn_rate=VEL_CURVA,turn_acceleration=(ACEL_CURVA,FREIO_CURVA))
def configurar_pid(fator_kp=1.0,fator_ki=1.0,fator_kd=1.0):
    kp,ki,kd,zona,taxa = PID_PADRAO
    kp = round(kp*fator_kp)
    ki = round(ki*fator_ki)
    kd = round(kd*fator_kd)
    drive_base.heading_control.pid(kp,ki,kd,zona,taxa)
    print("Kp:",kp)
    print("Ki:",ki)
    print("Kd:",kd)
def reset():
    drive_base.reset()
def parar():
    drive_base.brake()
def liberar_motores():
    drive_base.stop()
    left_motor.stop()
    right_motor.stop()
def andar_reto(cms,pot=400,wa=True,wait=None):
    if wait is not None:
        wa = wait
    drive_base.settings(straight_speed=min(abs(pot),VEL_RETA),straight_acceleration=(ACEL_RETA,FREIO_RETA))
    drive_base.use_gyro(True)
    drive_base.straight(cms*10,wait=wa)
def andar_reto_pid(cms,pot=400,wa=True,wait=None):
    andar_reto(cms,pot,wa,wait)
def andar_reto_suave(cm,pot=400,wa=True,wait=None):
    if wait is not None:
        wa = wait
    drive_base.settings(straight_speed=min(abs(pot),VEL_RETA),straight_acceleration=(ACEL_SUAVE,FREIO_SUAVE))
    drive_base.use_gyro(True)
    drive_base.straight(cm*10,wait=wa)
def turn(graus,potencia=400,liberar=False,wa=True,wait=None):
    if wait is not None:
        wa = wait
    drive_base.settings(turn_rate=min(abs(potencia),VEL_CURVA),turn_acceleration=(ACEL_CURVA,FREIO_CURVA))
    drive_base.use_gyro(True)
    drive_base.turn(graus,then=Stop.COAST if liberar else Stop.HOLD,wait=wa)
def turn2(graus,potencia=400,liberar=False,wa=True,wait=None):
    turn(graus,potencia,liberar,wa,wait)
def curva(raio,angulo,wa=True,wait=None):
    if wait is not None:
        wa = wait
    drive_base.settings(straight_speed=VEL_RETA,straight_acceleration=(ACEL_RETA,FREIO_RETA),turn_rate=VEL_CURVA,turn_acceleration=(ACEL_CURVA,FREIO_CURVA))
    drive_base.use_gyro(True)
    drive_base.curve(raio,angulo,wait=wa)
configurar_base()
drive_base.use_gyro(True)
configurar_pid()


