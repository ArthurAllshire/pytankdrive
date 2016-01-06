
from wpilib.command import Subsystem
from wpilib import CANTalon, TalonSRX

from robot_map import RobotMap
from commands.tank_drive import TankDrive

class Chassis(Subsystem):

    def __init__(self):

        self._motors = [TalonSRX(RobotMap.motor_a_talon_id), TalonSRX(RobotMap.motor_b_talon_id), TalonSRX(RobotMap.motor_c_talon_id), TalonSRX(RobotMap.motor_d_talon_id)]#[CANTalon(RobotMap.motor_a_talon_id), CANTalon(RobotMap.motor_b_talon_id), CANTalon(RobotMap.motor_c_talon_id), CANTalon(RobotMap.motor_d_talon_id)]
        #self._motors = []
        #for motor in self._motors:
        #    motor.changeControlMode(RobotMap.drive_motor_mode)

    #Put methods for controlling this subsystem here.
    # Call these from Commands.
    pass

    def initDefaultCommand(self):
        setDefaultCommand(TankDrive())

    def drive(self, vX, vY, vZ, throttle):

        #these mappings assuming that +ve wheel rotation is ccw
        #for a standard tank drive
        mA = vX - vZ
        mB = vX - vZ
        mC = -vX - vZ
        mD = -vX - vZ
        motor_values = [mA, mB, mC, mD]

        # scale between 0 and 1
        max_val = 1.0
        for value in motor_values:
            if abs(value) > max_val:
                max_val = abs(value)

        for motor, value in zip(self._motors, motor_values):
            value /= max_val
            value *= throttle
            #print("vX: ", vX, " Value: ", value)
            motor.set(value)
            #print("Set point: ", motor.setPoint)
