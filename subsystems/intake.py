
from wpilib.command import Subsystem
from wpilib import CANTalon
from wpilib import Victor

from robot_map import RobotMap

from robot_map import RobotMap

class Intake(Subsystem):

    intake_speed = 0.4
    
    def __init__(self, robot):
        super().__init__()

        self.robot = robot
        if RobotMap.motor_controllers == "talonsrx":
            self.motor = CANTalon(RobotMap.motor_intake_talon_id)
            self.motor.changeControlMode(RobotMap.drive_motor_mode)
        elif RobotMap.motor_controllers == "victor":
            self.motor = Victor(RobotMap.motor_intake_pwm_id)
        self._speed = 0.0
        self.motor.set(self._speed)

    def toggle(self):
        if self._speed == Intake.intake_speed:
            self._speed = 0.0
        else:
            self._speed = Intake.intake_speed
        self.motor.set(self._speed)
