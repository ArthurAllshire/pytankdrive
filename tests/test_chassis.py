
import pytest
import math

from subsystems.chassis import Chassis

from robot_map import RobotMap

def test_chassis(wpilib, hal_data, robot):
    epsilon = 0.1 # allowed error in speed
    chassis = Chassis(robot)

    for motor in chassis._motors:
        if RobotMap.motor_controllers == "talonsrx":
            assert isinstance(motor, wpilib.CANTalon)
        elif RobotMap.motor_controllers == "victor":
            assert isinstance(motor, wpilib.Victor)
        else:
            print("RobotMap.motor_controllers is not a recognised motorcontroller in the tests")
            assert False

    # test that we stop with all axis 0
    chassis.drive(0.0, 0.0, 0.0, 0.0)
    for motor in chassis._motors:
        if RobotMap.motor_controllers == "talonsrx":
            assert abs(motor.getSetpoint() - 0.0) < epsilon
        elif RobotMap.motor_controllers == "victor":
            assert abs(motor.get() - 0.0) < epsilon

    # test that we stop with 0 throttle
    chassis.drive(1.0, 0.0, 0.0, 0.0)
    for motor in chassis._motors:
        if RobotMap.motor_controllers == "talonsrx":
            assert abs(motor.getSetpoint() - 0.0) < epsilon
        elif RobotMap.motor_controllers == "victor":
            assert abs(motor.get() - 0.0) < epsilon

    # test that throttle works
    chassis.drive(1.0, 0.0, 0.0, 0.5)
    if RobotMap.motor_controllers == "talonsrx":
        assert abs(chassis._motors[0].getSetpoint() - 0.5) < epsilon
        assert abs(chassis._motors[1].getSetpoint() - 0.5) < epsilon
        assert abs(chassis._motors[2].getSetpoint() - -0.5) < epsilon
        assert abs(chassis._motors[3].getSetpoint() - -0.5) < epsilon
    elif RobotMap.motor_controllers == "victor":
        assert abs(chassis._motors[0].get() - 0.5) < epsilon
        assert abs(chassis._motors[1].get() - 0.5) < epsilon
        assert abs(chassis._motors[2].get() - -0.5) < epsilon
        assert abs(chassis._motors[3].get() - -0.5) < epsilon

    # test that vZ works
    chassis.drive(0.0, 0.0, 1.0, 1.0)
    for motor in chassis._motors:
        if RobotMap.motor_controllers == "talonsrx":
            assert abs(motor.getSetpoint() - -1.0) < epsilon
        elif RobotMap.motor_controllers == "victor":
            assert abs(motor.get() - -1.0) < epsilon
