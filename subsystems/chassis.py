
from wpilib.command import Subsystem
from wpilib import CANTalon
from wpilib import Victor

from robot_map import RobotMap
from commands.tank_drive import TankDrive

class Chassis(Subsystem):

    def __init__(self, robot):

        super().__init__()

        self.robot = robot

        if RobotMap.motor_controllers == "talonsrx":
            self._motors = [CANTalon(RobotMap.motor_a_talon_id),
                    CANTalon(RobotMap.motor_b_talon_id),
                    CANTalon(RobotMap.motor_c_talon_id),
                    CANTalon(RobotMap.motor_d_talon_id)]
            for motor in self._motors:
                motor.changeControlMode(RobotMap.drive_motor_mode)
        elif RobotMap.motor_controllers == "victor":
            self._motors = [Victor(RobotMap.motor_a_pwm_id),
                    Victor(RobotMap.motor_b_pwm_id),
                    Victor(RobotMap.motor_c_pwm_id),
                    Victor(RobotMap.motor_d_pwm_id)]

    def initDefaultCommand(self):
        self.setDefaultCommand(TankDrive(self.robot))

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
